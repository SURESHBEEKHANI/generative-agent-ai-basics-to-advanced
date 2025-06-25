# Import the FastMCP server framework for creating MCP (Machine Conversation Protocol) servers
from mcp.server.fastmcp import FastMCP

# Initialize the FastMCP server with the name "math server"
mcp = FastMCP("math server")

# Define a tool for addition
@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two integers together.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: The sum of a and b
    """
    return a + b

# Define a tool for subtraction
@mcp.tool()
def subtract(a: int, b: int) -> int:
    """
    Subtract the second integer from the first.
    
    Args:
        a (int): First number (minuend)
        b (int): Second number (subtrahend)
        
    Returns:
        int: The difference between a and b
    """
    return a - b

# Define a tool for multiplication
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """
    Multiply two integers.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: The product of a and b
    """
    return a * b

# Define a tool for division
@mcp.tool()
def divide(a: int, b: int) -> float:
    """
    Divide the first integer by the second.
    
    Args:
        a (int): First number (dividend)
        b (int): Second number (divisor)
        
    Returns:
        float: The quotient of a divided by b
        
    Raises:
        ValueError: If attempting to divide by zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

# Run the MCP server with stdio transport if the script is executed directly
#The transport="stdio" argument tells the server to:
#Use standard input/output (stdin and stdout) to receive and respond to tool function calls.

if __name__=="__main__":
    # Start the MCP server using standard input/output for communication
    # This allows the server to receive requests and send responses through stdin/stdout
    mcp.run(transport="stdio")