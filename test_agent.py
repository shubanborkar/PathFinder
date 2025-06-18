from agent import CareerPathwayAgent

class MockLLM:
    def __init__(self, responses):
        self.responses = responses
        self.calls = 0
    def __call__(self, *args, **kwargs):
        resp = self.responses[self.calls]
        self.calls += 1
        return resp
    def generate(self, *args, **kwargs):
        class Result:
            def __init__(self, text):
                self.generations = [[type('Gen', (), {'text': text})()]]
        return Result(self.responses[self.calls-1])

    def __getattr__(self, name):
        return self

# Test extraction and recommendation

def test_agent():
    # Mock responses for extraction and mapping
    extract_response = "Interests: math, computers\nHobbies: chess, coding\nAcademic Strengths: science, math\n"
    map_response = "1. STEM: Your interest in math, computers, and science suggests a strong fit for STEM careers.\n2. Business: Your analytical skills and interest in chess could also suit business roles."
    mock_llm = MockLLM([extract_response, map_response])
    agent = CareerPathwayAgent(llm=mock_llm)
    conversation = "I love math and computers. I enjoy playing chess and coding. My best subjects are science and math."
    result = agent.recommend_paths(conversation)
    assert "STEM" in result and "Business" in result
    print("Test passed!\nRecommendation:\n", result)

if __name__ == "__main__":
    test_agent() 