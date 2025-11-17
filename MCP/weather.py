from mcp.server.fastmcp import FastMCP

mcp = FastMCP('Weather')

@mcp.tool()
async def get_weather(location:str)-> str:
    """Get the weather location."""
    return "It's a always raining in California"


if __name__ == '__main__':
    mcp.run(transport='streamable-http')


# streammable-http will work as an api and it will run in the port number ex: http://127.0.0.1:8000/