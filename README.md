# cesmaccloud
## Requirements
  * Install the project dependencies using `pip`:

```
pip install -r requirements.txt
```

## Endpoints
#### Adding todos
**URL:**
```
 localhost:8000/add/
 localhost:8000/api/todos/
```

**Boddy:**
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
