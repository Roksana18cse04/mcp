from fastapi import APIRouter, Depends, HTTPException
from app.schemas.TextToImage import TextToImageRequest
from app.agents.text_to_image_agents import text_to_generate_image

import os
TextToImage_router = APIRouter()

@TextToImage_router.post("/text-image-generate")
async def image_generate(data: TextToImageRequest):
    """
    Classify the given prompt into one of the predefined categories.
    """
    print("EACHLABS_API_KEY:", os.getenv("EACHLABS_API_KEY"))
    result = text_to_generate_image(data)
    print(result)
    return result