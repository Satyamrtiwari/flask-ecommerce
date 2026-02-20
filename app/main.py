from fastapi import FastAPI, HTTPException ,Query,Path
from service.product import get_all_products
from schema.product import Product

app = FastAPI()

@app.get("/")
def get():
    return "Welcome to fastapi"


# using Query parameters to filter and sort products --> Filtering, sorting, pagination
@app.get("/products")         # Query is a helper in FastAPI used to define and validate data that comes from the URL query string.
def list_products(
    name:str = Query(
            default= None , min_length=1, max_length=50, description="Search product by name(Case sensetive)",example="Samsung"
            ),
    sort_by_price:bool = Query(default=None,description="Sort product by price"),
    order : str = Query(default='asc',description="Sort order when sort_by_price=True (asc,desc)",),
    limit : int = Query(default=5, ge=1, le =100, description="Limit the number of products"),
    offset : int = Query(default=0, ge=0,description="Offset for pagination")
     ):
    
    products = get_all_products()
    if name :
        needle = name.strip().lower()
        products = [p for p in products if needle in p.get("name", "").lower()]

    if not products:
        raise HTTPException(status_code=404, detail=f"No products found with the given name={name}")
        
    if sort_by_price:
        reverse = order=="desc"
        products = sorted(products , key = lambda x: x.get("price", 0), reverse=reverse)

    total = len(products)
    products = products[offset:offset+limit]
    return {
        "total": total,
        "limit": limit,
        "items": products
        }


# using path ---> to put the rules or protocol in the parameter ,Identifying a specific resource,
@app.get("/products/{product_id}")
def get_product(product_id:str = Path(
    ...,min_length=36,max_length=36,description="UUID of the product"),example="0005a8bf-ce3f-4dd7-bee0-fvvv70fea6a"
    ):
    products = get_all_products()
    for product in products:
        if product["id"]==product_id:
            return product
    raise HTTPException(status_code=404,details=f"Product with id={product_id} not found")



@app.post("/products")
def create_product(product:Product):
    return product