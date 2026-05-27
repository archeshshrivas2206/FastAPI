from fastapi import FastAPI
from models import product

app = FastAPI()

@app.get("/")
def greet():
    return "First time properly running a backend server "

@app.get("/second")
def second_page():
    return "You are on the second page"

products=[
    product(id=1,name='Phone',quantity=1,price=150000.0,description='Foldable Phone'),
    product(id=2,name='Laptop',quantity=2,price=550000.0,description='Macbook'),   
]

@app.get("/product")
def get_all_product():
    return products

@app.get("/product/{id}")
def get_by_id(id:int):
    for p in products:
        if p.id==id:

            return products[id-1]
    return 'Product not found '

@app.post("/product")
def add_product(productss:product):
    products.append(productss)
    return productss

@app.put("/product")
def edit_product(id:int, product3: product):
    for i in range(len(products)):
        if products[i].id==id:
            products[i]=product3
            return "product updated ssuccessfully "
    return "Product not found "

@app.delete("/product")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id==id:
            del products[i]
            return "Product Deleted "
    return "Product not found"


