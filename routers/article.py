from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import ArticleBase, ArticleDisplay
from db.database import get_db
from db import db_article

router = APIRouter(
    prefix="/article",
    tags=["article"],
)

# Create a new article
@router.post("/",response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(db, request)

# Get all articles
@router.get("/",response_model=List[ArticleDisplay])
def get_all_articles(db: Session = Depends(get_db)):
    return db_article.get_all_articles(db)

# Get article by id
@router.get("/{id}",response_model=ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db)):
    return db_article.get_article(db, id)

# Update article
@router.post("/{id}/update")
def update_article(id: int, request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.update_article(db, id, request)

# Delete article
@router.delete("/{id}/delete")
def delete_article(id: int, db: Session = Depends(get_db)):
    return db_article.delete_article(db, id)
 