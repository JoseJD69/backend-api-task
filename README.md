# Backend-Task - API REST

Bancked para la aplicación de visualizacion de commits de github.

## Instalación

Para instalar los requerimentos se debe ejecutar el siguiente comando:

```bash
pip install requeriments.txt -r
```

## Variables de entorno

Para el correcto funcionamiento del proyecto se debe crear un archivo .env con las siguientes variables de entorno:

:warning: El token es valido durante 7 días y solo de acceso para repositorios publicos

```bash 
GITHUB_TOKEN=XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
ENVIROMENT=development
```


## Ejecución
Para ejecutar el proyecto se debe ejecutar el siguiente comando:

```bash
python main.py
```
una vez ejecutado verificar que el proyecto se encuentre corriendo en el puerto 4000, haciendo una petición GET a la siguiente url:

```bash 
http://localhost:4000/health
```
## Test
Para ejecutar los test se debe ejecutar el siguiente comando:

```bash
pytest
```