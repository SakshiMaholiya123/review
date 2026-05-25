
from typing import Optional
from fastapi import HTTPException
from schema import Product
import json

#to create a product

def load_data():
    with open('products.json','r') as file:
        try:
            product=json.load(file)
            return product
        except:
            []

def save_data(data):
    with open('products', "w") as file:
        json.dump(data,file)



def create(prod:Product):
    product=load_data()
    for p in product:
        if p['id']==id:
            return {'error':'product already exist'}
        
        product.append(prod.dict())
        save_data(product)
        return prod


# to get  product by id
def get_specific_product(id:int):
    product=load_data()
    for p in product:
        if p['id']==id:
            return p
        
        else:
            raise HTTPException(status_code=404,detail='product not found')
        
# to update the product

def update_product(id:int,update_prod:Product):
    product=load_data()
    for i,prod in enumerate(product):
        if prod['id']==id:
            product[i]=update_prod.dict()
            return save_data(product)
        raise HTTPException(status_code=404,detail='product not found')


# to get all products
def get_all():
    product=load_data()
    return product

# to delete product
def delete(id:int):
    product=load_data()
    for i,prod in enumerate(product):
        if prod['id']==id:
            product.pop(i)
            save_data(product)
            return{'message':'product deleted'}
        raise HTTPException(status_code=404,detail='product not found')



# get product using filter
def get_product(category:str=None,price:Optional[float]=None):
    product=load_data()
    filter=product
    if category:
        filter=[product for product in filter
                    if product['category']==category
                ]
        
    if price is not None:
        filter=[product for product in filter
                    if product['price']<=price
                ]
        
    
    return filter  
    

