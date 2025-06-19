from typing import List, Dict, Any
from mcp.types import Tool, TextContent, CallToolRequest, ServerResult, CallToolResult, ImageContent
from fastapi_mcp.server import LowlevelMCPServer,Server
from app.schemas.Enhannced_Prompt import EnhanceRequest
from app.schemas.TextToImage import TextToImageRequest
from app.agents.text_to_image_agents import text_to_generate_image
from app.services.enhanced_prompt import enhance_prompt


class HarmoniMCPServer:
    def __init__(self):
        self.server = Server("harmoni-ai")
        self.tools = [
            Tool(
                name="enhance-prompt",
                description="Enhance a base prompt for better image generation",
                inputSchema=EnhanceRequest.schema()
            ),
            Tool(
                name="text-to-image",
                description="Generate images using a text prompt",
                inputSchema=TextToImageRequest.schema()
            )
        ]

        # Initialize the low-level MCP server
        self.server = LowlevelMCPServer(name="harmoni-ai", description="HermoniAI MCP Server")

        # Register tools
        self.register_tools()

    def register_tools(self):
        @self.server.list_tools()
        async def list_tools() -> List[Tool]:
            return self.tools

        @self.server.call_tool()
        async def call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent | ImageContent]:
            if name == "enhance-prompt":
                req = EnhanceRequest(**arguments)
                result = await enhance_prompt(req)
                return [TextContent(type="text", text=result.enhanced_prompt)]

            elif name == "text-to-image":
                req = TextToImageRequest(**arguments)
                result = await text_to_generate_image(req)
                return [TextContent(type="text", text=result.get("image_url", "❌ Image generation failed"))]

            else:
                return [TextContent(type="text", text="❌ Unknown tool name")]
