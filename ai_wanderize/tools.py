"""Centralized tool configurations for AI Wanderize travel system."""

import os
from dotenv import load_dotenv
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters, StdioConnectionParams

load_dotenv()

# ============================================================================
# MCP TOOLSET CONFIGURATION
# ============================================================================


web_scraping_toolset = MCPToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command='npx',
            args=["-y", "@brightdata/mcp"],
            env={
                "API_TOKEN": os.getenv("API_TOKEN"),
                "WEB_UNLOCKER_ZONE": os.getenv("WEB_UNLOCKER_ZONE"),
                "BROWSER_AUTH": os.getenv("BROWSER_AUTH")
            }
        ),
        timeout=600.0
    )
)

# Alias for backward compatibility and clarity
toolset = web_scraping_toolset
