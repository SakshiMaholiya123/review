# from itertools import product
from typing import Optional
from fastapi import APIRouter
from schema import Product
from crud import(create,get_specific_product,get_all,delete,get_product,update_product)

router=APIRouter()

@router.post('/products')
def create_prod(prod:Product):
    return create(prod)



@router.get('/products/{id}')
def specific_product(id:int):
    return get_specific_product(id)


@router.put('/products/{id}')
def update(id:int,update_prod:Product):
    return update_product(id,update_prod)


@router.get('/products')
def get_all_prod():
    return get_all()



@router.delete('/products/{id}')
def delete_prod(id:int):
    return delete(id)



# get product using filter
@router.get('/products')
def get_product_filter(category:str=None,price:Optional[float]=None):
    return get_product(category,price)

