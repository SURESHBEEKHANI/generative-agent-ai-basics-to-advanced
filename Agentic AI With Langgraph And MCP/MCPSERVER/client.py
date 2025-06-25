# Import required libraries for MCP client, agent creation, and LLM integration
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    # Initialize the MultiServerMCPClient with configurations for math and weather servers
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["mathserver.py"],  # Path to the math server script
                "transport": "stdio",       # Use standard I/O for communication
            },
            "weather": {
                "url": "http://localhost:8000/mcp",  # Weather server endpoint
                "transport": "stdio",      # Use HTTP with streaming support
            }
        }
    )

    # Set up Groq API key from environment variables
    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    # Get available tools from the MCP servers
    tools = await client.get_tools()
    
    # Initialize the Groq language model
    model = ChatGroq(model="qwen-qwq-32b")
    
    # Create a ReAct agent with the model and tools
    agent = create_react_agent(
        model, tools
    )

    # Example: Query the math server
    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
    )
    print("Math response:", math_response['messages'][-1].content)

    # Example: Query the weather server
    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what is the weather in California?"}]}
    )
    print("Weather response:", weather_response['messages'][-1].content)

# Run the main async function
asyncio.run(main())