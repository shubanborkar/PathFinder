from agent import CareerPathwayAgent

def main():
    print("Welcome to the Student Career Pathway Recommender!")
    print("Please describe your interests, hobbies, and academic strengths. Type 'quit' to exit.\n")
    agent = CareerPathwayAgent()
    conversation = ""
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        conversation += f"Student: {user_input}\n"
        response = agent.recommend_paths(conversation)
        print(f"\nAgent: {response}\n")
        # Show explanations for clusters if available
        explanations = agent.get_cluster_explanations(conversation)
        if explanations:
            print("Career Path Explanations:")
            for cluster, expl in explanations.items():
                print(f"- {cluster}: {expl}")
            print()

if __name__ == "__main__":
    main() 