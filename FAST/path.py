from fastapi import FastAPI

app = FastAPI()

@app.get("/products/{product_id}")
def product(product_id:int):
    return {
        "product": product_id
    }
