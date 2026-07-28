# ARD Suite Knowledge Center v1.2

Centro de conocimiento privado para visualizar claramente el proyecto ARD Suite.

## Ejecutar en Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python -m uvicorn app.main:app --reload
```

Abrir:

```text
http://127.0.0.1:8000
```

Credenciales iniciales:

```text
usuario: admin
clave: cambiar123
```

Cambiar en `.env`.

## Estructura

- Lineamientos generales
- Módulo 1: Carga de Productos
- Módulo 2: Venta en Salón
- Módulo 3: Administración
- Módulo 4: Inteligencia Comercial
- Módulo 5: Logística
- Referencias
