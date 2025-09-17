from fastapi import Request
from src.shared.application.profanity_service import ProfanityService


def get_profanity_service(request: Request) -> ProfanityService:
    if request.app.state.profanity_service is None:
        raise RuntimeError("ProfanityService not initialized")
    return request.app.state.profanity_service