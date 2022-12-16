from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from db import get_db
import crud
import models as mod
from returns import Returns

class_router = APIRouter()


@class_router.post('/api/create-class')
async def create_class(req: mod.ClassSchema, header_param: Request, db: Session = Depends(get_db)):
    result = await crud.create_class(req, header_param, db)
    if result:
        return Returns.object(result)
    else:
        return Returns.NOT_INSERTED


@class_router.get('/api/get-admin-classes')
async def get_admin_classes(header_param: Request, db: Session = Depends(get_db)):
    result = await crud.read_admin_classes(header_param, db)
    if result:
        return Returns.object(result)
    else:
        return Returns.NULL
