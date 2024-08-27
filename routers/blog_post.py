from typing import List, Optional
from fastapi import APIRouter, Body, Query, Path
from pydantic import BaseModel

router = APIRouter(
    prefix="/blog",
    tags=["blog"],
)

class Image(BaseModel):
    url: str
    name: str

class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    Contact_Number: Optional[int]
    tags : List[str] = []
    metadata : dict[str,str] = {'author':'Author Name'} 
    image: Optional[Image] = None

@router.post('/new/{id}')
def create_blog(blog: BlogModel,id: int,version: int = 1):
    return {
        "id": id,
        "version": version,
        "data": blog
        }

@router.post('/new/{id}/comments/{comment_id}')
def create_comment(blog:BlogModel,id:int,
                comment_title: int= Query(None,
                title="Comment Title",
                description="This is the ID of the comment",
                alias="comment Title",
                deprecated=True,
                ),
                content : str = Body(...,
                                    max_length=100,
                                    min_length=10,
                                    regex="^[\\s]+$",
                                     ),
                # content : str = Body(Ellipsis),
                version: Optional[List[str]]  = Query([1,2,3]),
                comment_id: int = Path(...,gt=5,le=10)


            ):
    return {"id":id,
            "comment_Title":comment_title,
            "data":blog,
            "content":content,
            "version":version,
            "comment_id":comment_id
            }
 
def required_functionality():
    return "This is the required functionality"