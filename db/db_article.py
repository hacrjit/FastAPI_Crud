from sqlalchemy.orm.session import Session

from schemas import ArticleBase
from db.models import DbArticle

def create_article(db: Session, request: ArticleBase):
    new_article = DbArticle(
        title = request.title,
        content = request.content,
        published = request.published,
        user_id = request.creator_id

    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)

    return new_article

def get_all_articles(db: Session): 
    return db.query(DbArticle).all()

def get_article(db: Session, id: int):
    article = db.query(DbArticle).filter(DbArticle.id == id).first()
    # handle errors

    return article

def update_article(db: Session, id: int, request: ArticleBase):
    article = db.query(DbArticle).filter(DbArticle.id == id)
    article.update({
        DbArticle.title: request.title,
        DbArticle.content: request.content,
        DbArticle.published: request.published
    })
    db.commit()
    return db.query(DbArticle).filter(DbArticle.id == id).first()

def delete_article(db: Session, id: int):
    article = db.query(DbArticle).filter(DbArticle.id == id)
    title = article.first().title
    article.delete(synchronize_session=False)
    db.commit()
    return f'{title} Removed Successfully...'

