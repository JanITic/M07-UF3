from typing import List
from fastapi import FastAPI, HTTPException, File, UploadFile
from pydantic import BaseModel
from db import productDB
from model.product import Product
from model.csv import CSVData
from schema.producte import product_schema, products_schema
from typing import Annotated

app = FastAPI()

# Retorna un hello world
@app.get("/")  
def read_root():
    return {"Hello": "World"}

# Llegeix tots els productes i retorna les dades en format JSON
@app.get("/product/")  
def read_products():
    return product_schema(productDB.consulta())

# Llegeix un producte específic per la seva ID i retorna les seves dades en format JSON
@app.get("/product/{product_id}")  
def read_product(product_id: int):
    data = productDB.get_product_by_id(product_id)
    if not data:
        raise HTTPException(status_code=404, detail="Product not found")
    return product_schema(data)

# Afegeix un nou producte a la base de dades
@app.post("/product/")  
def create_product(prod: Product):
    success = productDB.insert(prod)
    if success:
        return {"message": "Product added successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to add product to database")

# Actualitza les dades d'un producte existent
@app.put("/product/{product_id}")  
def update_product(product_id: int, prod: Product):
    success = productDB.update_product(product_id, prod)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product updated successfully"}

# Esborra un producte de la base de dades
@app.delete("/product/{product_id}")  
def delete_product(product_id: int):
    success = productDB.delete_product(product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}

# Llegeix tots els productes i les seves dades relacionades i retorna la informació en format JSON
@app.get("/productAll/")  
def read_products_all():
    return products_schema(productDB.get_all_products())

# Carrega massiva de productes, categories i subcategories des d'un fitxer CSV
@app.post("/loadProducts/")  
async def create_upload_file(file: UploadFile):
    productDB.load(file)
    return {"filename": file.filename, "message": "cargado con éxito"}

