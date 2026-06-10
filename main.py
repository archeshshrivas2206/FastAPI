from fastapi import Depends,FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import product
from database import sessionlocal,engine
import db_models 
from sqlalchemy.orm import Session 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)

db_models.base.metadata.create_all(bind= engine)


@app.get("/")
def greet():
    return "First time properly running a backend server "

# @app.get("/second")
# def second_page():
#     return "You are on the second page"

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


@app.post("/products")
def add_product(productss:product,db: Session = Depends(get_db)):
    db.add(db_models.product(**productss.model_dump()))
    db.commit()
    return productss



@app.get("/products")
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

@app.get("/products/{id}")
def get_by_id(id:int, db: Session = Depends(get_db)):
    db_product=db.query(db_models.product).filter(db_models.product.id==id).first()

    if db_product:
        return db_product
    
    return "Product not found "
    

#this is the way to do put without db
# @app.put("/product")
# def edit_product(id:int, product3: product):
#     for i in range(len(products)):
#         if products[i].id==id:
#             products[i]=product3
#             return "product updated ssuccessfully "
#     return "Product not found "

@app.put("/products/{id}")
def edit_product(id:int, product3: product, db: Session=Depends(get_db)):
    db_product = db.query(db_models.product).filter(db_models.product.id==id).first()
    if db_product:
        db_product.description=product3.description
        db_product.name=product3.name
        db_product.quantity=product3.quantity
        db_product.price=product3.price
        db.commit()
        return "product updated"
    else:
        return "Product not found "
  

# @app.delete("/product")
# def delete_product(id:int):
#     for i in range(len(products)):
#         if products[i].id==id:
#             del products[i]
#             return "Product Deleted "
#     return "Product not found"


@app.delete("/products")
def delete_product(id:int, db: Session= Depends(get_db)):
    db_product=db.query(db_models.product).filter(db_models.product.id==id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "product deleted successfully "
    return "Product not found"