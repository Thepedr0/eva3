Evaluación EVA3 – API REST con Django REST Framework

Descripción general
Este proyecto consiste en el desarrollo de una **API REST** utilizando **Django REST Framework (DRF)**.  
El objetivo es demostrar la comprensión de los principios RESTful y su aplicación práctica en la gestión del recurso **Tarea**, implementando las operaciones CRUD y respetando los códigos y convenciones HTTP.

Configuración de URLs
	Proyecto – `tareas_api/urls.py`
	```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('tareas.urls')),  # Versionado en la ruta
]
-----------------------------------------------------------------------------------------------------------
Aplicación – tareas/urls.py

from rest_framework.routers import DefaultRouter
from .views import TareaViewSet

router = DefaultRouter()
router.register(r'tareas', TareaViewSet, basename='tarea')

urlpatterns = router.urls
Resultado:

Colección: /api/v1/tareas/ → (GET, POST)

Detalle: /api/v1/tareas/{id}/ → (GET, PATCH, DELETE)

------------------------------------------------------


Recurso principal
**Tarea** con los siguientes campos:

| Campo | Tipo | Descripción |
|--------|------|-------------|
| id | Auto | Identificador único |
| titulo | String | Título o nombre de la tarea |
| hecho | Boolean | Indica si la tarea está completada |
| created_at | Datetime | Fecha y hora de creación |
Ejemplo de respuesta JSON:

{
  "id": 1,
  "titulo": "Comprar leche para Serafín",
  "hecho": false,
  "created_at": "2025-10-14T04:00:35.20297Z"
}

--------------------------------------------------------------------

Endpoints y URIs
- **Colección:** `/api/v1/tareas/`  
- **Elemento:** `/api/v1/tareas/{id}/`

---------------------------------------------------------------------

Verbos y códigos HTTP esperados

| Método | Endpoint | Descripción | Código |
|---------|-----------|--------------|---------|
| GET | `/api/v1/tareas/` | Lista todas las tareas | **200 OK** |
| POST | `/api/v1/tareas/` | Crea una nueva tarea | **201 Created** |
| GET | `/api/v1/tareas/{id}/` | Muestra el detalle de una tarea específica | **200 OK** |
| PATCH | `/api/v1/tareas/{id}/` | Actualiza parcialmente el campo `hecho` o `titulo` | **200 OK** |
| DELETE | `/api/v1/tareas/{id}/` | Elimina una tarea del sistema | **204 No Content** |

----------------------------------------------------------------------------------------------

Reglas REST aplicadas

- **Stateless:**  
  Cada petición contiene toda la información necesaria.  
  No se usan sesiones ni almacenamiento de estado entre peticiones.

- **Formato JSON:**  
  Las solicitudes y respuestas se realizan en formato `application/json`.

- **Versionado en la ruta:**  
  Se utiliza `/api/v1/` para permitir futuras versiones sin romper compatibilidad.

- **Idempotencia:**  
  - `GET` no cambia el estado del recurso.  
  - `PATCH` repetido deja el mismo estado.  
  - `DELETE` repetido devuelve 404 porque el recurso ya no existe.

--------------------------------------------------------

 Diagrama de arquitectura


          
  	[Cliente (Postman / curl)]
          │
					
       HTTP / JSON
          │
					
	[API /api/v1 (DRF ViewSets)]
          │
					
	[Serializers (validación y conversión)]
          │
       
	[Modelos Django (ORM)]
          │
          
	[Base de datos SQLite (local)]


Descripción de cada capa

Cliente (Postman / curl / SPA):
Representa al usuario o la aplicación que realiza las solicitudes HTTP hacia la API.
Envía peticiones (GET, POST, PATCH, DELETE) y recibe las respuestas en formato JSON.

HTTP / JSON:
Es el medio de comunicación entre el cliente y el servidor.
HTTP define los verbos (métodos) utilizados y JSON es el formato estándar para transmitir los datos.

API /api/v1 (DRF ViewSets / URLs):
Es la capa que gestiona las rutas y los métodos disponibles.
Django REST Framework (DRF) define los endpoints, interpreta los verbos HTTP y coordina la lógica de negocio.

Lógica / Serializers (validación):
Se encarga de validar, transformar y serializar los datos entre los modelos de Django y el formato JSON.
Garantiza que la información enviada o recibida cumpla con las reglas del modelo.

Modelo Django (ORM):
Define la estructura de los datos (por ejemplo, la clase Tarea) y cómo se almacenan en la base de datos.
Django ORM permite manipular la información mediante objetos Python sin escribir SQL manualmente.

Base de datos SQLite (local):
Es el sistema de almacenamiento utilizado por la API.
Guarda de manera persistente los registros creados, modificados o eliminados desde los endpoints.

Ejemplos con curl

Antes de probar los comandos, inicia el servidor:

python manage.py runserver

🔹 Listar tareas
curl -i http://127.0.0.1:8000/api/v1/tareas/

🔹 Crear tarea
curl -i -X POST http://127.0.0.1:8000/api/v1/tareas/ \
  -H "Content-Type: application/json" \
  -d '{"titulo":"Comprar leche para Serafín"}'

🔹 Detalle de una tarea
curl -i http://127.0.0.1:8000/api/v1/tareas/1/

🔹 Actualizar parcialmente una tarea
curl -i -X PATCH http://127.0.0.1:8000/api/v1/tareas/1/ \
  -H "Content-Type: application/json" \
  -d '{"hecho": true}'

🔹 Eliminar tarea
curl -i -X DELETE http://127.0.0.1:8000/api/v1/tareas/1/
