Evaluación EVA3 – API REST con Django REST Framework

Descripción general
Este proyecto consiste en el desarrollo de una **API REST** utilizando **Django REST Framework (DRF)**.  
El objetivo es demostrar la comprensión de los principios RESTful y su aplicación práctica en la gestión del recurso **Tarea**, implementando las operaciones CRUD y respetando los códigos y convenciones HTTP.

-----------------------------------------------------------------------------------------------------------

Recurso principal
**Tarea** con los siguientes campos:

| Campo | Tipo | Descripción |
|--------|------|-------------|
| id | Auto | Identificador único |
| titulo | String | Título o nombre de la tarea |
| hecho | Boolean | Indica si la tarea está completada |
| created_at | Datetime | Fecha y hora de creación |

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
          ▼
      HTTP / JSON
          │
          ▼
[API /api/v1 (DRF ViewSets)]
          │
          ▼
[Serializers (validación y conversión)]
          │
          ▼
[Modelos Django (ORM)]
          │
          ▼
[Base de datos SQLite (local)]



