from agent.graph import graph

def main():
    print("AI Agent: Ask your question in any language and get a summarized answer.")
    try:
        query = input("Your question: ")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
        return
    
    if not query.strip():
        print("Please enter a valid question.")
        return
    
    result = graph.invoke({"query": query})
    print("\nFinal Response: \n")
    print(result.get("final_answer", "No response was obtained"))


if __name__ == "__main__":
    main()

