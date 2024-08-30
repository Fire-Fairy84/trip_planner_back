# Travel Planner :airplane:

## Índice

- [Proyecto 📝](#proyecto-)
    - [Requisitos previos](#requisitos-previos-)
- [Diagramas](#diagramas-)
    - [Diagrama de flujo](#diagrama-de-flujo-)
    - [Diagrama de datos](#diagrama-de-datos-)
- [Instalación 🛠️](#instalación-)
    - [Requerimientos](#requerimientos-)
- [Estructura del proyecto](#estructura-del-proyecto-)
- [Tecnologías](#tecnologías-)
- [Uso](#uso-)
- [Contribución 🤝](#contribución-)
- [Desarrolladores 👩‍💻](#desarrolladores-)
- [Demo](#demo-)

## Proyecto 

Desarrollo de una aplicación de viajes en la que los usuarios pueden registrarse, seleccionar un destino y los días que quieren estar (de 1 a 3), y recibir un itinerario personalizado con opciones de alojamiento y actividades.

El backend está desarrollado en Python utilizando Django y Django REST Framework, con una base de datos PostgreSQL, mientras que el frontend está planeado para desarrollarse con tecnologías web como React.

### Requisitos previos

**Funcionalidades**
- Registro de usuarios y autenticación.
- Selección de destino y días de estancia (1 a 3 días).
- Generación automática de un itinerario con actividades y alojamiento.
- Visualización del itinerario detallado y organizado por día.
- Guardado de itinerarios favoritos en el perfil del usuario.

## Diagramas

### Workflow

[Ver workflow](#) *(https://drive.google.com/file/d/1mTCRFqmTulP77HtNCvABib0hpjCstS6j/view)*

### Diagrama de datos

La base de datos ha sido diseñada para soportar la funcionalidad de la app, con tablas normalizadas para usuarios, destinos, itinerarios, alojamientos y actividades.

<img width="864" alt="uml_diagram" src="/utils/img/uml_diagram_viajes.png">

## Instalación 🛠️

### Requerimientos

- [Python 3.x](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)
- [Git](https://git-scm.com/)

1. Clona el repositorio del backend:

    ```bash
    git clone https://github.com/tu-usuario/trip_planner_back
    ```

2. Crea y activa un entorno virtual:

    ```bash
    cd trip_planner_back
    python -m venv env
    source env/bin/activate  # En Windows usa: env\Scripts\activate
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Configura tu base de datos PostgreSQL y añade las credenciales en el archivo `settings.py` de Django.

5. Realiza las migraciones y corre el servidor:

    ```bash
   python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```

## Estructura del proyecto

El proyecto sigue una estructura común para aplicaciones Django, con la API organizada en diferentes módulos para una gestión eficiente.

```plaintext
/
├── trip_planner_back
├── trip_planner_back/
│   │    ├── __init__.py
│   │    ├── asgi.py
│   │    ├── settings.py
│   │    ├── urls.py
│   │    ├── wsgi.py
│   ├── accommodation_app/
│   │    ├── migrations/
│   │    ├── models.py
│   │    ├── serializers.py
│   │    ├── urls.py
│   │    ├── views.py
│   │    └── ...
│   ├── activity_app/
│   │    └── ...
│   ├── destination_app/
│   │    └── ...
│   ├── itinerary_app/
│   │    └── ...
│   ├── user_app/
│   │    └── ...
│   ├── utils/
│   │    └── img/
│   │       ├── accommodations
│   │       ├── activities
│   │       ├── destinations
│   ├── manage.py
│   ├── requirements.txt
│   ├── README.md
│   └── ...
├── 
```
## Tecnologías


**Backend**
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Pillow](https://python-pillow.org/) para manejo de imágenes.
- [psycopg2](https://pypi.org/project/psycopg2/) para la conexión con la base de datos PostgreSQL.

**Frontend** *(https://github.com/GabyRosas/trip_planner_front)*
- [React.js](https://reactjs.org/)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Axios](https://axios-http.com/es/docs/intro)

## Uso

Para iniciar la aplicación, primero asegúrate de que el servidor de backend esté corriendo:

```bash
python manage.py runserver
```

## Contribución 🤝

1. Haz un fork del repositorio.
2. Crea una nueva rama: 

   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Realiza tus cambios y haz commit:
    ```bash
   git commit -m 'Agrega nueva funcionalidad'
   ```
4. Haz push de tu rama:  
    ```bash
   git push origin feature/nueva-funcionalidad
    ```
5. Crea un pull request.

## Desarrolladoras 👩‍💻

El equipo de desarrollo de este proyecto está compuesto por:

- **Esther**(https://github.com/Fire-Fairy84)
- **Gabriela**(https://github.com/GabyRosas)
- **Lara**(https://github.com/laradrb)
- **Noemí**(https://github.com/noemipeteilh)
- **Angelica**(https://github.com/Angelica2013)
   

