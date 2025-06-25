# Import the FastMCP server framework for creating MCP (Machine Conversation Protocol) servers
from mcp.server.fastmcp import FastMCP

# Initialize the FastMCP server with the name "Weather"
mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """
    Get the weather for a specified location.
    
    Args:
        location (str): The location to get weather information for
        
    Returns:
        str: A string containing the weather information
    """
    return "It's always raining in California"

# If this script is run directly (not imported as a module)
if __name__ == "__main__":
    # Start the MCP server using HTTP transport that supports streaming responses
    mcp.run(transport="stdio")