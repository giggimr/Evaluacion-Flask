# TA6 — Aplicación Web con Python y Flask

Aplicación web desarrollada con **Python + Flask** como parte del Taller Aplicado 6.
Cuenta con un menú principal desde el que se accede a dos ejercicios, cada uno resuelto
mediante un formulario que envía datos al servidor y procesa el resultado con Python.

\---

## Funcionalidades

### Ejercicio 1 — Promedio y asistencia

Formulario que recibe **3 notas** (rango 10 a 70) y un **porcentaje de asistencia**
(rango 0 a 100). Al enviar, la aplicación calcula el promedio de las notas y determina
el estado del estudiante.

Se considera **APROBADO** únicamente si se cumplen **ambas** condiciones:

* Promedio de las 3 notas mayor o igual a **40**
* Asistencia mayor o igual a **75%**

En cualquier otro caso, el resultado es **REPROBADO**.

### Ejercicio 2 — Nombre más largo

Formulario que recibe **3 nombres distintos**. Al enviar, la aplicación identifica cuál
de ellos tiene la mayor cantidad de caracteres y muestra ese nombre junto al total de
caracteres que lo componen.

### Historial en memoria

Cada resultado calculado se almacena en una lista en memoria durante la ejecución del
servidor, y puede consultarse desde la ruta `/historial`.

\---

## Estructura del proyecto

```
.
├── main.py              # Aplicación Flask: rutas, lógica y funciones
├── requirements.txt     # Dependencias del proyecto
├── .gitignore
├── static/
│   └── estilos.css      # Hoja de estilos, cargada desde la plantilla base
└── templates/
    ├── base.html        # Plantilla base con bloques Jinja
    ├── index.html       # Menú principal
    ├── ejercicio1.html  # Formulario del Ejercicio 1
    ├── ejercicio2.html  # Formulario del Ejercicio 2
    ├── resultado.html   # Vista de resultados
    ├── historial.html   # Registros almacenados en memoria
    └── error404.html    # Página de error personalizada
```

\---

## Rutas de la aplicación

|Ruta|Método|Descripción|
|-|-|-|
|`/`|GET|Menú principal con los dos botones|
|`/ejercicio/<numero>`|GET|Ruta con parámetro por URL. Redirecciona al ejercicio correspondiente; aborta con error 404 si el número no es válido|
|`/ejercicio1`|GET / POST|Muestra y procesa el formulario de notas|
|`/ejercicio2`|GET / POST|Muestra y procesa el formulario de nombres|
|`/historial`|GET|Lista los registros almacenados en memoria|

\---

## Instalación y ejecución

Requiere **Python 3** instalado.

```bash
# 1. Clonar el repositorio
git clone https://github.com/giggimr/Evaluacion-Flask.git
cd Evaluacion-Flask

# 2. Crear y activar el entorno virtual
py -m venv venv
venv\\Scripts\\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# 3. Instalar las dependencias con pip
pip install -r requirements.txt

# 4. Ejecutar la aplicación
py main.py
```

La aplicación queda disponible en **http://127.0.0.1:5000**

Para detener el servidor: `Ctrl + C`

\---

## Tecnologías utilizadas

* **Python 3**
* **Flask** — framework web
* **Jinja2** — motor de plantillas (herencia mediante bloques)
* **HTML5 / CSS3**
* **pip** — gestor de dependencias
* **Git / GitHub** — control de versiones

\---

## Casos de prueba

|Ejercicio|Entrada|Resultado esperado|
|-|-|-|
|1|Notas 50, 60, 40 — Asistencia 80%|Promedio 50.0 — APROBADO|
|1|Notas 50, 60, 40 — Asistencia 60%|Promedio 50.0 — REPROBADO|
|1|Notas 30, 30, 40 — Asistencia 90%|Promedio 33.3 — REPROBADO|
|2|Ana, Cristóbal, Luis|Cristóbal — 9 caracteres|



