if __name__ == "__main__":
    # Step 1: Fetch data from MongoDB
    messages = fetch_data()
    
    # Step 2: Process data into entities and relationships
    entities, relationships = process_data(messages)
    
    # Step 3: Integrate with LangGraph for visualization
    integrate_with_langgraph(entities, relationships)

    print("Demo completed!")
