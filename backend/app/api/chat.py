from fastapi import APIRouter, Depends
from pydantic import BaseModel
import httpx, uuid, asyncio
from app.core.settings import get_settings


router = APIRouter()


class ChatRequest(BaseModel):
message: str
conv_id: str | None = None


class ChatResponse(BaseModel):
conv_id: str
reply: str


@router.post("/", response_model=ChatResponse)
async def chat(req: ChatRequest, settings = Depends(get_settings)):
conv_id = req.conv_id or str(uuid.uuid4())
async with httpx.AsyncClient() as client:
resp = await client.post(
f"https://api-inference.huggingface.co/models/deepseek-ai/deepseek-llm-7b-instruct",
headers={"Authorization": f"Bearer {settings.deepseek_token}"},
json={"inputs": req.message, "parameters": {"temperature": 0.7}},
timeout=90,
)
data = resp.json()
reply_text = data[0]["generated_text"] if isinstance(data, list) else data.get("generated_text", "…")
return ChatResponse(conv_id=conv_id, reply=reply_text)