from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi_mcp import FastApiMCP
from typing import Any, List, Tuple, Optional
from dotenv import load_dotenv
import uvicorn
import os
load_dotenv(override=True)

# DEBUG: Confirm .env is working

# assaigin routet file
from app.routes.text_to_image_route import TextToImage_router as text_to_image_router
from app.routes.enhanced_prompt_route import enhance_router as enhanced_prompt_router
app = FastAPI()

# ✅ Apply CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route include
app.include_router(text_to_image_router,prefix="/text-image",tags=["text-to-image"])
app.include_router(enhanced_prompt_router,prefix="/enhanced-prompt",tags=["enhanced-prompt"])


mcp = FastApiMCP(app)
mcp.mount(app, mount_path="/mcp")

@app.get("/")
def read_root():
    return {"message": "HermoniAI MCP API is live"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
