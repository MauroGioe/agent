from google.adk.tools.mcp_tool import MCPToolset
from google.adk.tools.mcp_tool.mcp_toolset import StreamableHTTPConnectionParams
from mcp import StdioServerParameters



def return_http_mcp_tools_search():
    print("Attempting to connect to MCP server for math functions...")
    server_params = StreamableHTTPConnectionParams(
        url="http://localhost:7001/mcp",
    )
    tools = MCPToolset(connection_params=server_params)
    print("MCP Toolset created successfully.")
    return [tools]
