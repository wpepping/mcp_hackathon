from fastapi import APIRouter, Depends, Request, status
from schemas import DataIn

main_router = APIRouter()

@main_router.post("/", status_code=status.HTTP_202_ACCEPTED, description="mcp_hackathon")
async def post_analysis_task(request: Request, data: DataIn) -> str:

    return "Request succesful"
