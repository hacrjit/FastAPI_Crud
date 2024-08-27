from enum import Enum
from typing import Optional
from fastapi import APIRouter, Depends, Response, status
from routers.blog_post import required_functionality

router = APIRouter(
    prefix="/blog",
    tags=["blog"],
)

@router.get(
        '/{id}/all',
        summary="Get all blogs",
        description="Get all blogs In detail",
        response_description="List of all blogs"
        )
def get_blog(id,page=1,pagesize: Optional[int]=None,req_parameter:str=Depends(required_functionality)):
    return {"id": id ,"page": page, "pagesize": pagesize, "req_parameter":req_parameter}

# @router.get('/all')
# def get_blog(page=1,pagesize: Optional[int]=None):
#     return {"page": page, "pagesize": pagesize}

@router.get("/{id}",status_code=status.HTTP_200_OK)
def show_blog(id: int,response: Response):
    if id > 10:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error':f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {"data": f'Blog id is {id}'}
    
@router.get('/{id}/comments/{comment_id}',tags=["comments"])
def get_comment(id:int,comment_id:int):
    return {"blog_id":id,"comment_id":comment_id}

# @router.get("/all")
# def show_blog():
#     return {"data": "All Blogs"}

# @router.get("/{id}")
# def show_blog(id: int):
#     return {"data": f'Blog id is {id}'}

class BlogType(str,Enum):
    short = 'short'
    medium = 'medium'
    large = 'large'

@router.get('/type/{type}')
def blog_type(type: BlogType):
    return {"message" : f"Blog type : {type}"}

@router.get('/all',response_description="Get all blogs")
def get_blog(page,pagesize):
    return {"page": page, "pagesize": pagesize}
