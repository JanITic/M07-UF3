# M07-UF3

#### 1.  Crear un entorn amb FastAPI
    

Utilitzar el framework fastapi per crear una api rest

[https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)

  

#### 2.  Crear una bases de dades amb PostgreSQL per una botiga online de productes tecnològics.
    

  

CREATE TABLE category (

category_id SERIAL PRIMARY KEY,

name VARCHAR(100) NOT NULL,

created_at TIMESTAMP,

updated_at TIMESTAMP

);

  

CREATE TABLE subcategory (

subcategory_id SERIAL PRIMARY KEY,

name VARCHAR(100) NOT NULL,

category_id INT NOT NULL,

created_at TIMESTAMP,

updated_at TIMESTAMP,

FOREIGN KEY (category_id) REFERENCES category(category_id)

);

  

CREATE TABLE product (

product_id SERIAL PRIMARY KEY,

name VARCHAR(100) NOT NULL,

description TEXT,

company VARCHAR(255) NOT NULL,

price DECIMAL(10,2) NOT NULL,

units NUMERIC,

subcategory_id INT NOT NULL,

created_at TIMESTAMP,

updated_at TIMESTAMP,

FOREIGN KEY (subcategory_id) REFERENCES subcategory(subcategory_id)

);

  

#### 3.  Les funcionalitats que ens demanen el client:
    


####  a. CRUD Productes: (4 punts)
    

  

-   Ruta:  **/product/**
    

Tipus de petició: Get

Funcionament: Retorna una llista json amb tota la informació dels productes de la taula products

  

-   Ruta:  **/product/{id}**
    

	Tipus de petició: Get

	Funcionament: Retorna un objecte json amb la informació del producte que la id de la bases de dades coincideix amb la id que ens arribar per paràmetre.

  

-   Ruta:  **/product/**
    

	Tipus de petició: Post

	Funcionament: Permet afegir un nou producte a la BBDD

	Retorna un objecte  json amb el missatge “S’ha afegit correctement”

  

-   Ruta:  **/product/**
    

	**/produt/{id}**

	Tipus de petició: Put

	Funcionament: Permet modificar el camp d’un producte de la BBDD definit per la id que arribar per paràmetre.

	Retorna un objecte json amb el missatge “S’ha modificat correctement”

  

-   Ruta:  **/product/{id}**
    

	Tipus de petició: Delete

	Funcionament: Permet eliminar un producte de la BBDD

	Retorna un objecte  json amb el missatge “S’ha borrat correctement”

  

-   Ruta:  **/productAll/**
    

	Tipus de petició: Get

	Funcionament: Retorna una llista json amb la següent informació: nom de la categoria, nom de la subcategoria, nom del producte, marca del producte i el preu.

  

#### b.  Càrrega massiva de productes (5 punts)
    

Ruta:  **/loadProducts**

Tipus de petició: Post

Funcionament: Servirà per fer una càrrega massiva de categories, subcategories i productes a les bases de dades a través d’un fitxer csv.

Per cada registre del csv:

1.  Per la **categoria**:
    

	a.  Si no existeix a les BBDD farà un insert a les bases de dades i modificarà el camps create_at i updated_at a la data i hora actual
    
	b.  Si existeix farà un update del name i actualiztarà updated_at a la data i hora actual.
    

2.  Per la **subcategoria**:
    

a.  Si no existeix a les BBDD farà un insert a les bases de dades i modificarà el camps create_at i updated_at a la data i hora actual
    
b.  Si existeix farà un update del name i actualiztarà updated_at a la data i hora actual.
    

3.  Pel **producte** :
    

a.  Si no existeix a les BBDD farà un insert a les bases de dades i modificarà el camps create_at i updated_at a la data i hora actual
    
b.  Si existeix farà un update del name i actualiztarà updated_at a la data i hora actual.
    

Retorna

Un objecte json indicant si el procés s’ha realitzat correctament o hi ha hagut un error.

-   El fitxer que s’ha de carregar el podeu descarregar [aquí](https://drive.google.com/file/d/1pGX8MQj6-wj22o3PSOa9PdfS8LVYb74j/view?usp=sharing).
    
-   Us podeu ajudar de la documentació: [https://fastapi.tiangolo.com/tutorial/request-files/](https://fastapi.tiangolo.com/tutorial/request-files/)
    

  

#### c.  Consultes avançades (1 punt)
    

Fer servir query parameters per fer les següents consultes:

Us podeu ajudar de la documentació: [https://fastapi.tiangolo.com/tutorial/query-params/](https://fastapi.tiangolo.com/tutorial/query-params/)

-   **?orderby= (str)**
    

	   Valor: “asc” | “desc”
    
	 Retorna una llista json ordenada ascendent o descendent (segons el valor de la querystring) pel nom del productes. Els valors que retorna son: nom de la categoria, nom de la subcategoria, nom del producte, marca del producte i el preu.
    
	   Exemple ruta amb query parameters: ?orderby=asc
    
	  Us podeu ajudar de:
    

	[https://www.w3schools.com/postgresql/postgresql_orderby.php](https://www.w3schools.com/postgresql/postgresql_orderby.php)

-   **?contain=(str)**
    

	   Valor: “text”
    
	   Retorna una llista json amb els noms dels productes que continguin el valor que arriba per la querystring. Els valors que retorna son:: nom de la categoria, nom de la subcategoria, nom del producte, marca del producte i el preu.
    
	  Exemple ruta amb query parameters: ?contain=portat
    
	   Us podeu ajudar de: 	[https://www.w3schools.com/postgresql/postgresql_like.php](https://www.w3schools.com/postgresql/postgresql_like.php)
    

-   **?skip= (int)&limit=(int)**
    

	   Valor: 1 - 100
    
	   Retorna una llista json amb el numero de registres segons el valor de limit i començarà segons el valor de skip. Els valors que retorna son: nom de la categoria, nom de la subcategoria, nom del producte, marca del producte i el preu.
    
	   Exemple ruta amb query parameters: ?skip=2&limit=10
    
	   Us podeu ajudar de:
    

	[https://www.w3schools.com/postgresql/postgresql_limit.php](https://www.w3schools.com/postgresql/postgresql_limit.php)