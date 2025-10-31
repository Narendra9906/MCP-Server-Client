from mcp.server.fastmcp import FastMCP   # Here we are installing mcp.

mcp=FastMCP("Weather") # Creating an instance of FastMCP with the name "Weather". So here "Weather" is the name of the server.

async def fetch_weather(location: str)-> str:
    """Fetching the weather of a specific location"""
    return f"It's raining in {location} today."

if __name__=="__main__":
    mcp.run(transport="streamable-http")