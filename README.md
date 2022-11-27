# UserValidator

### Requerimientos del proyecto

- python 3.8.10
- ffmpeg 4.2.4-1ubuntu0.1
- redis 5.0.7

### Instrucciones para construir el proyecto

Para construir el proyecto es necesario utilizar un ambiente virtual de python, para realizarlo se debe instalar **venv** y crearlo con el siguiente comando:

```bash
  $ python3 -m venv env
```

Luego se activa el ambiente con el siguiente comando:

```bash
  $ source env/bin/activate
```

Instalar dependencias del proyecto:

```bash
  $ cd validateUser
  $ pip install -r ./requirements.txt
```

### Ejecutar servidor

#### Con flask directamente

```bash
  $ cd validateUser
  $ FLASK_APP=app/app.py flask run
```