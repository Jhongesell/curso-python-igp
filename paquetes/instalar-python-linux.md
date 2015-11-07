Instalar Python en Ubuntu Linux
===============================

1. Instalar interprete de Python

Ya debería venir instalado, pero en todo caso se instala con:

```
sudo apt-get install python
```

2. Herramientas de desarrollo para Python


```
sudo apt-get install python-dev
```

3. Gestores de paquetes Python (setuptools, pip)

```
sudo apt-get install python-setuptools python-pip
```

4. Ejemplo de instalación de MySQL-python

```
sudo apt-get install libmysqlclient-dev
sudo pip install MySQL-python
```

5. Trabajar con virtualenv

```
sudo apt-get install python-virtualenv
```

Activar el entorno virtual en Bash

```
source env/bin/activate
```

Activar el entorno virtual desde un script de Python:

```python
activate_this = '/ruta/completa/a/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
```
