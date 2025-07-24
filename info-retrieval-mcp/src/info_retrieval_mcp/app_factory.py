# app_factory.py
# -*- coding: utf-8 -*-
"""
App factory for the Information Retrieval MCP Server.
"""

from mcp.server.fastmcp import FastMCP

# Importing the module *creates* the FastMCP instance (`mcp`) and wires
# up its lifespan, tools, resources, … exactly once.
import info_retrieval_mcp.server as _server  # noqa: F401  (import for side-effects)


def create_app() -> FastMCP:
    """
    Return the singleton FastMCP application.

    Gunicorn/Uvicorn will call this function (because we'll reference it
    in `asgi.py`) to get an ASGI app object.
    """
    return _server.mcp 