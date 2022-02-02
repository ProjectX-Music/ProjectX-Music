from fastapi import APIRouter, Depends

from pxm_commons.enums import ApiVersionEnum
from pxm_security.security import verify_user_authorization
from pxm_resources.album_resource import router as album_router
from pxm_resources.artist_resource import router as artist_router
from pxm_resources.track_resource import router as track_router
from pxm_resources.user_resource import router as user_router


async def _common_parameters(
        version: ApiVersionEnum = ApiVersionEnum.V1,
) -> dict:
    """Helper function to get all the common parameters for all REST endpoints."""
    return {'version': version}


# API Router Definition
router = APIRouter(
    prefix='/api/{version}',
    dependencies=[
        Depends(_common_parameters),
        Depends(verify_user_authorization)
    ]
)

# Attach Artist API Router
router.include_router(artist_router)

# Attach Album API Router
router.include_router(album_router)

# Attach Track API Router
router.include_router(track_router)

# Attach User API Router
router.include_router(user_router)
