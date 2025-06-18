# Pre-defined career clusters and mapping logic
CAREER_CLUSTERS = {
    "STEM": ["math", "science", "technology", "engineering", "computers", "medicine"],
    "Arts": ["art", "music", "painting", "writing", "theater", "literature", "dance"],
    "Sports": ["sports", "athletics", "football", "basketball", "coaching", "fitness"],
    "Business": ["business", "management", "marketing", "finance", "entrepreneurship"],
    "Social Sciences": ["psychology", "sociology", "law", "history", "politics"]
}

CAREER_EXPLANATIONS = {
    "STEM": "STEM careers involve science, technology, engineering, and math. They suit analytical and problem-solving minds.",
    "Arts": "Arts careers are for creative individuals who enjoy expressing themselves through various mediums.",
    "Sports": "Sports careers are ideal for those passionate about athletics, fitness, and teamwork.",
    "Business": "Business careers suit those interested in management, entrepreneurship, and working with people.",
    "Social Sciences": "Social Sciences careers are for those curious about society, human behavior, and helping others."
}

def map_to_career_clusters(interests, hobbies, strengths):
    """
    Map extracted interests, hobbies, and strengths to career clusters.
    Returns a list of recommended clusters.
    """
    from collections import Counter
    all_inputs = (interests or []) + (hobbies or []) + (strengths or [])
    all_inputs = [x.lower() for x in all_inputs]
    scores = Counter()
    for cluster, keywords in CAREER_CLUSTERS.items():
        for keyword in keywords:
            for item in all_inputs:
                if keyword in item:
                    scores[cluster] += 1
    # Return top 2-3 clusters
    return [c for c, _ in scores.most_common(3)]

def get_career_explanation(cluster):
    """
    Return a short explanation for a given career cluster.
    """
    return CAREER_EXPLANATIONS.get(cluster, "No explanation available.") 