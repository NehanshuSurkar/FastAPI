from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

products = {}

class Product(BaseModel):

    product_name: str
    price: int

@app.post("/products/{product_id}")
def create_product(product_id: int, product: Product):

    products[product_id] = product

    return {
        "message": "Product created"
    }

@app.get("/products/{product_id}")
def get_product(product_id: int):

    return products.get(product_id)

@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):

    products[product_id] = product

    return {
        "message": "Product updated"
    }

@app.delete("/products/{product_id}")
def delete_product(product_id: int):

    products.pop(product_id)

    return {
        "message": "Product deleted"
    }
