from google.adk.tools.mcp_tool import MCPToolset
from mcp import StdioServerParameters
from google.adk.tools.mcp_tool.mcp_toolset import StreamableHTTPConnectionParams



def return_http_mcp_tools_search():
    print("Attempting to connect to MCP server for math functions...")
    server_params = StreamableHTTPConnectionParams(
        url="http://localhost:8001/mcp",
    )
    tools = MCPToolset(connection_params=server_params)
    print("MCP Toolset created successfully.")
    return [tools]