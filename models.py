#this file is used when we use pydantic to make classes and use its node to store data typically in lists or such data structure.

from pydantic import BaseModel

class product(BaseModel):
    id: int
    name: str
    quantity:int
    price: float
    description: str

    # def __init__(self,id:int,name: str, quantity:int,price:float,description:str):
    #     self.id=id
    #     self.name=name
    #     self.quantity=quantity
    #     self.price=price
    #     self.description=description
