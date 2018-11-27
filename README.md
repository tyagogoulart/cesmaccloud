# TODO Application with Python and Django Rest Framework

TODO's Application developed to train git use and team development in Software Engineer Especialization of CESMAC/AL. It returns a API in JSON format with HTTP methods GET, POST, PUT and DELETE documented below:

## Requirements
  * Install the project dependencies using `pip`:

```
pip install -r requirements.txt
```

## Endpoints
#### Adding todos
Method: **POST**

**URL:**
```
  localhost:8000/todos/
```

**Body:**
```
{
    "descrição": "Teste",
    "data": "04/04/2016"
}
```

**Response:**
```
{
    "id": 1,
    "descricao": "Teste",
    "data": "04/04/2016"
}
```

#### Todo List (all todos)
Method: **GET**

**URL:**
```
  localhost:8000/todos/
```

**Response:**
```
[
   {
       "id": 1,
       "descricao": "Teste 1",
       "data": "01/01/2016"
   },
   {
       "id": 2,
       "descricao": "Teste 2",
       "data": "02/02/2016"
   },
   {
       "id": 3,
       "descricao": "Teste 3",
       "data": "03/03/2016"
   }
 ]
```

#### Getting a specific todo
Method: **GET**

**URL:**
```
  localhost:8000/todos/1
```

**Response:**
```
{
       "id": 1,
       "descricao": "Teste 1",
       "data": "01/01/2016"
}
```

#### Updating a specific todo
Method: **PUT**

**URL:**
```
  localhost:8000/todos/1
```

**Body:**
```
{
       "descricao": "Teste 1 MODIFICADO",
       "data": "01/01/2016"
}
```

**Response:**
```
{
       "id": 1,
       "descricao": "Teste 1 MODIFICADO",
       "data": "01/01/2016"
}
```

#### Deleting a specific todo
Method: **DELETE**

**URL:**
```
  localhost:8000/todos/1
```

**Response:**
``` 
 
```

##Test
To run the test you have to enter the line below on your project directory:
```
python manage.py test todos
```
