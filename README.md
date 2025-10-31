# MCP-Server-Client
The project is about a Multi-Client Protocol (MCP) system built using the MCP framework, Langchain MCP adapters, and Langgraph. It involves creating separate servers named "Math" and "Weather" that provide tools via MCP. The client interacts with these servers through agents created with Langgraph and Langchain, enabling commands like math.


# build-mcp-from-scratch-using-langgraph

This project demonstrates building a Multi-Client Protocol (MCP) system with custom servers and clients using Langgraph and Langchain MCP adapters.

## Features

- Math server: Provides addition and multiplication tools.
- Weather server: Provides weather information tools.
- MCP client: Utilizes Langchain and Langgraph to interact with multiple servers, get their tools, and run commands with an intelligent React agent.

## Requirements

- langchain-groq
- langchain-mcp-adapters
- mcp
- langgraph

## Usage

Run the mathserver.py or weatherserver.py to start the respective servers. Use client.py to start the client which connects and interacts with these servers using Langgraph agents.

## Main Components

- mathserver.py: MCP Math server with add and multiply tools.
- weatherserver.py: MCP Weather server with location weather fetching tool.
- client.py: MCP client with Langgraph React agent managing commands to servers.
- main.py: Entry script printing a hello message for project validation.


