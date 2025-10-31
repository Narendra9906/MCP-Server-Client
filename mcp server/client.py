from langchain_mcp_adapters.client import MultiServerMCPClient #here by using the langchain we are installing mcp client which interact with the multiple servers.
# when we call any client we need to create an agent to interact with the server. so here we are using langgraph to create an agent. because it has prebuilt agents.
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    print("🚀 Starting MCP Client...")

    client = MultiServerMCPClient(
        {
            "math":{
                "command": "python",
                "args": ["mathserver.py"], ## here it should be absolute correct path
                "transport": "stdio"
            }
            # Weather server can be added when needed
            # "weather":{
            #     ## here it should be absolute correct path
            #     "url": "http://127.0.0.1:8000/mcp",
            #     "transport": "streamable_http"
            # }
        }
    )

    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    print("🔑 Loaded GROQ API key:", bool(os.environ["GROQ_API_KEY"]))

    # 1. MCP Client gets the tools from the servers
    print("🧠 Getting tools from MCP servers...")
    tools = await client.get_tools()  # Returns: [add_tool, multiply_tool, weather_tool]
    print("🔧 Tools loaded:", tools)

    # 2. Without an agent, you'd have to manually:
    # - Parse "what's (3+5)*12"
    # - Realize you need to add 3+5 first
    # - Call add_tool(3, 5) 
    # - Take result (8) and call multiply_tool(8, 12)
    # - Format the final answer

    # 3. With an agent, it automatically:
    model = ChatGroq(model="llama-3.1-8b-instant")
    agent = create_react_agent(model, tools)

    print("🔍Invoking agent for math task...")
    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "Calculate (5+3)*2 step by step. First use the add tool to calculate 5+3, then use the multiply tool to multiply the result by 2."}]}
    )

    print("🛠️ Raw Response:", math_response)
    print("☑️ Math Response:", math_response["messages"][-1].content)

asyncio.run(main())
