from typing import Any, Optional
from pydantic import BaseModel
from scripts.api.constants import STATUS


class DefaultResponse(BaseModel):
    status: str = STATUS.SUCCESS
    message: Optional[str]
    data: Optional[Any]


class DefaultFailureResponse(DefaultResponse):
    status: str = STATUS.FAILED
    error: Any