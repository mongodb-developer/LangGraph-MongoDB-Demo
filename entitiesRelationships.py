# Process messages to create entities and relationships for LangGraph
def process_data(messages):
    entities = {}
    relationships = []

    for message in messages:
        customer_id = message.get("customer_id")
        agent_id = message.get("agent_id")
        content = message.get("message")
        
        # Create entities for customer and agent if they don't exist
        if customer_id not in entities:
            entities[customer_id] = {"type": "Customer", "id": customer_id}
        if agent_id not in entities:
            entities[agent_id] = {"type": "Agent", "id": agent_id}

        # Define relationships based on message content
        relationships.append({
            "source": customer_id,
            "target": agent_id,
            "relationship": "discussed",
            "content": content
        })

    return entities, relationships
