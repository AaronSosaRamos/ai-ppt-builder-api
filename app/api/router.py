from fastapi import APIRouter, Depends
from app.api.features.full_workflow import full_workflow
from app.api.features.schemas.schemas import RequestSchemaWithFiles
from app.api.logger import setup_logger
from app.api.auth.auth import key_check

logger = setup_logger(__name__)
router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.post("/generate-ppt")
async def submit_tool( data: RequestSchemaWithFiles, _ = Depends(key_check)):

    logger.info(f"File type uploaded successfully: {data.file_type}")
    
    ppt_content = full_workflow(data)

    return ppt_content