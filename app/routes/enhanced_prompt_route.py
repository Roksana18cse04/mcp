# routes.py
from fastapi import APIRouter, Form
from app.schemas.Enhannced_Prompt import EnhanceRequest
from app.services.enhanced_prompt import enhance_prompt

enhance_router = APIRouter()
@enhance_router.post("/enhance-prompt/")
async def get_enhanced_prompt(request: EnhanceRequest):
    response = await enhance_prompt(
        base_prompt=request.base_prompt,
        target_model=request.target_model,
        platform=request.platform,
        intend=request.intend
    )
    return response
