# # from fastapi import FastAPI, HTTPException
# # from pydantic import BaseModel
# # from typing import List

# # app = FastAPI()

# # class Item(BaseModel):
# #     id: int
# #     name: str
# #     description: str

# # items = []

# # @app.get("/items", response_model=List[Item])
# # def get_items():
# #     return items

# # @app.post("/items", response_model=Item)
# # def add_item(item: Item):
# #     items.append(item)
# #     return item

# # @app.put("/items/{item_id}", response_model=Item)
# # def update_item(item_id: int, item: Item):
# #     for i in range(len(items)):
# #         if items[i].id == item_id:
# #             items[i] = item
# #             return item
# #     raise HTTPException(status_code=404, detail="Item not found")







# from enum import Enum
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def test():
#     return {'Message':"Test Successfull"}

# @app.get("/{name}")
# def test(name: str):
#     return {'Message':f"{name} Successfull"}

# @app.get("/square/{num}")
# def square(num: int):
#     return {f'Square of {num}': num*num}


# class roompartners(str,Enum):
#     room1 = "Room 1"
#     room2 = "Room 2"
#     room3 = "Room 3"

# @app.get("/room/{room_name}")
# def room(room_name: roompartners):
#     return {"Room":room_name}

# from typing import Optional

# @app.get("/{name}/{email}/{mobile}")
# def test(name: str, email: str,mobile: int, PIN: Optional[int] = None):
#     """
#     This is a test function
#     **hii**
#     """

#     return {'Name':name, 'Mobile':mobile, 'Email':email, 'PIN':PIN}






















from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from db import models
from exceptions import StoryException
from routers import blog_get, blog_post,user,article,product
from db.database import engine

app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get("/")
def home():
    return {"Hello": "World",
            "Message": "Welcome to the FastAPI CRUD Application",
            "Developed By": "Dummy Developer",
            "docs": "https://fastapi-crud-2upi.onrender.com/docs"
            } 

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Error: {exc.name}"}
    )

# @app.exception_handler(HTTPException)
# def http_exception_handler(request: Request, exc: HTTPException):
#     return JSONResponse(
#         status_code=exc.status_code,
#         content={"message": f"Error: {exc.detail}"}
#     )

# models.Base.metadata.create_all(engine)
models.Base.metadata.create_all(bind=engine)


