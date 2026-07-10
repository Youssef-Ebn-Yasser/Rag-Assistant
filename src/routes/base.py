from fastapi import FastAPI ,APIRouter
import os




base_router = APIRouter(
    prefix= '/api/v1',
    tags=['api-v1']
)



@base_router.get('/')
async def welcome():
    app_name = os.getenv('App_NAEM')
    app_version = os.getenv('App_VERSION')

    return {
        'msg' : f'app name {app_name} and app version {app_version}'
    }