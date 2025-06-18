from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from prompts import EXTRACT_PREFERENCES_PROMPT, MAP_TO_CAREER_PATHS_PROMPT, FALLBACK_PROMPT
from career_paths import map_to_career_clusters, get_career_explanation
import os

# Optional imports for advanced features
try:
    from langchain.embeddings import OpenAIEmbeddings
    from langchain.vectorstores import FAISS
    from langchain.memory import ConversationBufferMemory
except ImportError:
    OpenAIEmbeddings = None
    FAISS = None
    ConversationBufferMemory = None

class CareerPathwayAgent:
    def __init__(self, llm=None, use_embeddings=False, use_memory=False):
        if llm is None:
            raise ValueError("You must provide an LLM instance, e.g., ChatMistralAI")
        self.llm = llm
        self.use_embeddings = use_embeddings and OpenAIEmbeddings is not None and FAISS is not None
        self.use_memory = use_memory and ConversationBufferMemory is not None
        self.extract_chain = LLMChain(
            llm=self.llm,
            prompt=PromptTemplate.from_template(EXTRACT_PREFERENCES_PROMPT)
        )
        self.map_chain = LLMChain(
            llm=self.llm,
            prompt=PromptTemplate.from_template(MAP_TO_CAREER_PATHS_PROMPT)
        )
        if self.use_memory:
            self.memory = ConversationBufferMemory()
        else:
            self.memory = None
        if self.use_embeddings:
            # Prepare embeddings for career clusters
            self.embeddings = OpenAIEmbeddings()
            self.vectorstore = FAISS.from_texts(list(get_career_explanation(c) for c in map_to_career_clusters([], [], [])), self.embeddings)
            self.cluster_names = list(map_to_career_clusters([], [], []))

    def extract_preferences(self, conversation):
        if self.use_memory and self.memory:
            self.memory.save_context({"input": conversation}, {})
        result = self.extract_chain.run({"conversation": conversation})
        interests = self._parse_list(result, "Interests:")
        hobbies = self._parse_list(result, "Hobbies:")
        strengths = self._parse_list(result, "Academic Strengths:")
        return interests, hobbies, strengths

    def _parse_list(self, text, header):
        import re
        match = re.search(f"{header}(.*?)(\n|$)", text, re.DOTALL)
        if match:
            items = match.group(1).strip().split(",")
            return [i.strip() for i in items if i.strip()]
        return []

    def recommend_paths(self, conversation):
        interests, hobbies, strengths = self.extract_preferences(conversation)
        if not (interests or hobbies or strengths):
            return FALLBACK_PROMPT
        if self.use_embeddings and self.embeddings and self.vectorstore:
            # Use embeddings to find the closest career cluster explanations
            query = ", ".join(interests + hobbies + strengths)
            docs_and_scores = self.vectorstore.similarity_search_with_score(query, k=3)
            clusters = [self.cluster_names[i] for i, _ in enumerate(docs_and_scores)]
        else:
            clusters = map_to_career_clusters(interests, hobbies, strengths)
        if not clusters:
            return FALLBACK_PROMPT
        prompt_vars = {
            "interests": ", ".join(interests),
            "hobbies": ", ".join(hobbies),
            "strengths": ", ".join(strengths)
        }
        return self.map_chain.run(prompt_vars)

    def get_cluster_explanations(self, conversation):
        interests, hobbies, strengths = self.extract_preferences(conversation)
        if self.use_embeddings and self.embeddings and self.vectorstore:
            query = ", ".join(interests + hobbies + strengths)
            docs_and_scores = self.vectorstore.similarity_search_with_score(query, k=3)
            clusters = [self.cluster_names[i] for i, _ in enumerate(docs_and_scores)]
        else:
            clusters = map_to_career_clusters(interests, hobbies, strengths)
        return {c: get_career_explanation(c) for c in clusters} 