from fastapi import FastAPI, HTTPException ,Query
from service.product import get_all_products


app = FastAPI()

@app.get("/")
def get():
    return "Welcome to fastapi"


@app.get("/products")
def list_products(name:str = Query(default= None , min_length=1, max_length=50, description="Search product by name(Case sensetive)") ):
    products = get_all_products()
    if name :
        needle = name.strip().lower()
        products = [p for p in products if needle in p.get("name", "").lower()]
        if not products:
            raise HTTPException(status_code=404, detail=f"No products found with the given name={name}")
        
        total = len(products)
        return {
            "total": total,
            "items": products
        }