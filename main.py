from fastapi import Depends,FastAPI
from models import product
from database import sessionlocal,engine
import db_models 
from sqlalchemy.orm import Session 

app = FastAPI()

db_models.base.metadata.create_all(bind= engine)


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

def get_db():

    db = sessionlocal()
    try :
        yield db
    finally:
        db.close()

def init_db():
    db=sessionlocal()
    count=db.query(db_models.product).count
    if count==0:

        for i in products:
            db.add(db_models.product(**i.model_dump()))

        db.commit()
init_db()


@app.post("/product")
def add_product(productss:product,db: Session = Depends(get_db)):
    db.add(db_models.product(**productss.model_dump()))
    db.commit()
    return productss



@app.get("/product")
def get_all_product(db :Session = Depends(get_db)):
    db_product= db.query(db_models.product).all()

    return db_product

#this method is used when we ar not dealing with db and directly using any data structure 
# @app.get("/product/{id}")
# def get_by_id(id:int):
#     for p in products:
#         if p.id==id:

    #         return products[id-1]
    # return 'Product not found'

@app.get("/product/{id}")
def get_by_id(id:int, db: Session = Depends(get_db)):
    db_product=db.query(db_models.product).filter(db_models.product.id==id).first()

    if db_product:
        return db_product
    
    return "Product not found "
    



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


