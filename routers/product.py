from typing import List, Optional
from fastapi import APIRouter, Header, Response
from fastapi.responses import HTMLResponse

router = APIRouter(
    prefix="/product",
    tags=["product"],
)

products = ['tea','coffee','milk','sugar','salt']

@router.get("/all")
def get_all_products():
    data = ", ".join(products)
    return Response(content=data, media_type="text/plain")

@router.get("/withheader")
def get_products(
    response: Response,
    custom_header: Optional[List[str]] = Header(None)
):
    return products

@router.get("/{id}",responses={
    200: {
        "content": {
            'text/html': {
                "example": "<html><body><h1>Product</h1><p>Product: tea</p></body></html>"
            }
        },
        "description": "Returns the html content of the product"
    },
    404: {
        "content": {
            'text/plain': {
                "example": "Product not found"
            }
        },
        "description": "A clear text error message if the product is not found"
    }
},)
def get_product(id: int):
    if id >= len(products):
        return Response(status_code=404, content="Product not found", media_type="text/plain")
    product = products[id]
    out = f"""
    <h1>Product</h1>

    <p>Product: {product}</p>
    """
    return HTMLResponse(content=out, media_type="text/html")