from mcp.types import Tool, TextContent
from app.schemas.TextToImage import TextToImageRequest
from app.agents.text_to_image_agents import text_to_generate_image

class TextToImageTool(Tool):
    name = "text_to_image"
    description = "Generate image from a text prompt and model"

    def run(self, input: TextContent) -> TextContent:
        request = TextToImageRequest(
            model_name="flux-dev-realism",  # or pull from prompt
            prompt=input.text,
            intend="image generation"
        )
        result = text_to_generate_image(request)
        return TextContent(text=str(result))
