from fastapi import APIRouter, Depends, Request, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer
from db import get_db
import crud
import models as mod

family_router = APIRouter(tags=['Family'], dependencies=[Depends(HTTPBearer())])

@family_router.post('/api/create-family')
async def create_family(header_param: Request, req: mod.FamilySchema, db: Session = Depends(get_db)):
    result = await crud.create_family(header_param=header_param, req=req, db=db)
    if result == -1:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if result:
        result['msg'] = 'Создано!'
        result = jsonable_encoder(result)
        return JSONResponse(content=result, status_code=status.HTTP_201_CREATED)
    else:
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT)
    


@family_router.put('/api/update-family/{id}')
async def update_family(id: int, header_param: Request, req: mod.FamilySchema, db: Session = Depends(get_db)):
    result = await crud.update_family(id, header_param, req, db)
    if result == -1:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if result:
        result['msg'] = 'Обновлено!'
        result = jsonable_encoder(result)
        return JSONResponse(content=result, status_code=status.HTTP_200_OK)
    else:
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT)
    
    
@family_router.get('/api/get-admin-families')
async def get_admin_families(header_param: Request, db: Session = Depends(get_db)):
    result = await crud.read_admin_family(header_param, db)
    if result == -1:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if result:
        result = jsonable_encoder(result)
        return JSONResponse(content=result, status_code=status.HTTP_200_OK)
    else:
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT)