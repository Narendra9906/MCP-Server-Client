from mcp.server.fastmcp import FastMCP   # Here we are installing mcp.

mcp=FastMCP("Math") # Creating an instance of FastMCP with the name "Math". So here "Math" is the name of the server.

#defining a tool for addition
@mcp.tool()
def add(a:int, b:int)->int:
    """Add two numbers"""
    return a+b

#defining a tool for multiplication
@mcp.tool()
def multiply(a:int, b:int)->int:
    """Multiply two numbers"""
    return a*b

#The transport="stdio" argument tells the server to:
#Use standard input/output (stdin and stdout) to receive and respond to tool function calls.
if __name__=="__main__":
    mcp.run(transport="stdio")