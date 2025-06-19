import uvicorn
from app.main import app
from app.mcp_server.hermoniAI_server import mount_tools

if __name__ == "__main__":
    mount_tools(app)
    uvicorn.run(app, host="0.0.0.0", port=8000)
