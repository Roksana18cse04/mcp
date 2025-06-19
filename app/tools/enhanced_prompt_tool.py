from mcp.types import TextContent,Tool
from app.services.enhanced_prompt import enhance_prompt
from app.schemas.Enhannced_Prompt import EnhanceRequest

class EnhancedPromptTool(Tool):
    name = "enhance_prompt"
    description = "Enhances user prompt using a language model"

    async def call(self, request: EnhanceRequest) -> TextContent:
        data = EnhanceRequest(**request.args)
        result = await enhance_prompt(data)
        return TextContent(text=result)
