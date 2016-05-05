# cesmaccloud
## Requirements
  * Install the project dependencies using `pip`:

```
pip install -r requirements.txt
```

## Endpoints
#### Adding todos
**Method: POST**

**URL:**
```
  localhost:8000/todos/
```

**Body:**
```
{
    "descricao": "",
    "data": null
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
