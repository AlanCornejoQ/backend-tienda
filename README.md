# Proyecto final de modulo 5

# Instrucciones para instalar y ejecutar el proyecto

Este proyecto está hecho con Python 3.11 y Django 5.2. Usé Miniconda para manejar el entorno virtual porque me pareció la forma más práctica y compatible con cualquier sistema.

## 1. Clonar el repositorio

```bash
git clone https://github.com/AlanCornejoQ/backend-tienda.git
cd backend-tienda
```
## 2. Crear el entorno con Conda
Ya dejé preparado un archivo environment.yml, así que con estos comandos se puede crear el entorno fácilmente:
```bash
conda env create -f environment.yml
conda activate tienda-backend
```

## 3. Aplicar migraciones
Esto es necesario para que Django cree las tablas iniciales en la base de datos:
```bash
python manage.py migrate
```

## 4. Probar que todo funciona
Se pueden ejecutar los siguientes archivos para verificar los módulos desarrollados:
```bash
python tests/test_productos.py
python tests/test_inventario.py
python tests/test_ordenes.py
python tests/test_notificaciones.py
```