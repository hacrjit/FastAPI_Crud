from typing import List
from pydantic import BaseModel

# Article in UserDisplay is a list of Article objects
class Article(BaseModel):
    title: str
    content: str
    published: bool
    class config():
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article] = []
    class config():
        orm_mode = True
# user inside ArticleDisplay is an object of User
class User(UserBase):
    id: int
    username: str
    class config():
        orm_mode = True
        
class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int

class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user : User
    class config():
        orm_mode = True