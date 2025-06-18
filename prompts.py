# Prompt templates for the Student Career Pathway Recommender

EXTRACT_PREFERENCES_PROMPT = '''
You are a career advisor. Given the following conversation, extract the student's interests, hobbies, and academic strengths.

Conversation:
{conversation}

Extracted Information:
Interests:
Hobbies:
Academic Strengths:
'''

MAP_TO_CAREER_PATHS_PROMPT = '''
Based on these interests, hobbies, and academic strengths:
Interests: {interests}
Hobbies: {hobbies}
Academic Strengths: {strengths}

Recommend 2-3 suitable career paths from the following list: [STEM, Arts, Sports, Business, Social Sciences]. For each, provide a short explanation tailored to the student.
'''

FALLBACK_PROMPT = '''
I need more information to recommend a career path. Could you tell me about your favorite subjects, hobbies, or what you enjoy doing in your free time?
''' 