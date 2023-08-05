from fastapi import APIRouter
import moligeek.__version__ as info
import app.__version__ as api_info
router = APIRouter()

@router.get("/")
async def show_info():
    return {"core":{
                "name": info.__name__,
                "version": info.__version__,
                "author": info.__author__,
                "author_email": info.__author_email__,
                "url": info.__url__,
                "description": info.__description__,
                "license": info.__license__,
                "copyright": info.__copyright__,
                },
            "api":{
                "name": api_info.__name__,
                "version": api_info.__version__,
                "author": api_info.__author__,
                "author_email": api_info.__author_email__,
                "url": api_info.__url__,
                "description": api_info.__description__,
                "license": api_info.__license__,
                "copyright": api_info.__copyright__,
                }
            }