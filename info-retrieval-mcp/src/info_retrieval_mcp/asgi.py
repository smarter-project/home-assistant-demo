# asgi.py
# -*- coding: utf-8 -*-
"""
ASGI entry point for the Information Retrieval MCP Server.
"""

from .app_factory import create_app

# Build the FastMCP server once
mcp_server = create_app()

# Turn it into a plain ASGI application (FastAPI instance)
# For stateful sessions (default):
app = mcp_server.streamable_http_app() 