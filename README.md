# LangGraph-MongoDB-Demo 🦜
This MongoDB / LangGraph demo will allow you to:  Use real, structured data to build an interactive, visual representation of relationships.  * Assumes you have LangGraph Studio installed https://studio.langchain.com/ Uses the Sample_Mflix movie data base to make it easy

Here’s a step-by-step guide to set up a new project directory for your MongoDB and LangGraph integration:

1. Create a New Project Directory
Navigate to the LangGraph home directory, and create a new project directory:

```
cd /path/to/langgraph-home
mkdir mongodb_integration_demo
cd mongodb_integration_demo
```

2. Set Up Project Structure
Within this directory, create a structure for your project. Here’s a simple structure to start:
```
mongodb_integration_demo/
├── .env                   # MongoDB connection string
├── main.py                # Main script
├── data/                  # Static data or samples
├── config/                # Config files
├── utils/                 # Utility scripts
│   ├── movie_processor.py # NEW: Processes movie data
│   └── graph_builder.py   # NEW: Builds graphs for visualization
```
3. Create the .env File
Create a .env file in the project directory to store your MongoDB connection string:
```
MONGODB_URI=mongodb+srv://<username>:<password>@<cluster-url>/<database>
```

4. Install Dependencies
Ensure you have all required dependencies, including pymongo and python-dotenv, to connect and interact with MongoDB:

```
pip install pymongo python-dotenv
```

5. Write the Main Script (main.py)
In main.py, add code to load environment variables, connect to MongoDB, and interact with LangGraph Studio.
Here's a sample outline for main.py:
```
from pymongo import MongoClient
from dotenv import load_dotenv
import os
```
# Load environment variables
```
load_dotenv()
mongo_uri = os.getenv("MONGODB_URI")
```

# Connect to MongoDB
```
client = MongoClient(mongo_uri)
db = client['Langchain_Demo']  # Update with your database name
collection = db['payload']     # Update with your collection name
```
# Fetch data from MongoDB
```
messages = list(collection.find())
```
```
# Sample function to process and visualize data
def process_data(messages):
    for message in messages:
        customer_id = message.get("customer_id")
        agent_id = message.get("agent_id")
        content = message.get("message")
        print(f"Customer: {customer_id}, Agent: {agent_id}, Message: {content}")
        # Here you could add LangGraph logic to create nodes/relationships
```
# Run the demo
```
if __name__ == "__main__":
    process_data(messages)
```

6. Add Utility Functions (Optional)
If you need functions to handle specific tasks (e.g., entity extraction, topic categorization), create these as separate Python files in the utils/ directory. For example, utils/entity_extractor.py might contain functions for processing message content.

7. Integrate with LangGraph Studio
In main.py or another dedicated script, add the code to connect to LangGraph Studio’s APIs or directly use its functions if available. This will allow you to visualize the MongoDB data within the LangGraph Studio interface.

8. Run and Test the Project
With everything set up, you can test your MongoDB integration by running:

```
python main.py
```
9. Adjust and Expand as Needed
Testing: Make sure that the MongoDB data is loaded and processed correctly. You should see the customer_id, agent_id, and message details printed out.
Expanding: As you test, consider adding more advanced data processing and integrating LangGraph’s graph visualization functions.
