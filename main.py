"""
TA6 - Aplicación web con Flask
Ejercicio 1: promedio de 3 notas + asistencia -> aprobado / reprobado
Ejercicio 2: de 3 nombres, cuál es el más largo y cuántos caracteres tiene
"""

from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)

# ---------------------------------------------------------------
# Registros almacenados en memoria (se pierden al reiniciar el server)
# ---------------------------------------------------------------
historial = []


# ---------------------------------------------------------------
# Funciones de lógica (separadas de las rutas)
# ---------------------------------------------------------------
def calcular_promedio(notas):
    """Recibe una lista de notas y devuelve el promedio redondeado a 1 decimal."""
    return round(sum(notas) / len(notas), 1)


def obtener_estado(promedio, asistencia):
    """Aprobado solo si promedio >= 40 Y asistencia >= 75."""
    if promedio >= 40 and asistencia >= 75:
        return "APROBADO"
    return "REPROBADO"


def nombre_mas_largo(nombres):
    """Devuelve una tupla (nombre_mas_largo, cantidad_de_caracteres)."""
    ganador = max(nombres, key=len)
    return ganador, len(ganador)


def registrar(tipo, detalle):
    """Guarda un registro en memoria."""
    historial.append({"id": len(historial) + 1, "tipo": tipo, "detalle": detalle})


# ---------------------------------------------------------------
# Rutas
# ---------------------------------------------------------------
@app.route("/")
def index():
    """Página principal con los dos botones."""
    return render_template("index.html", total_registros=len(historial))


@app.route("/ejercicio/<int:numero>")
def ejercicio(numero):
    """Ruta CON parámetro por URL. Redirecciona al formulario correspondiente.
    Si el número no es 1 ni 2, se aborta la conexión con un error 404."""
    if numero == 1:
        return redirect(url_for("ejercicio1"))
    elif numero == 2:
        return redirect(url_for("ejercicio2"))
    else:
        abort(404)


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    """GET: muestra el formulario. POST: procesa las notas y la asistencia."""
    if request.method == "POST":
        try:
            nota1 = float(request.form["nota1"])
            nota2 = float(request.form["nota2"])
            nota3 = float(request.form["nota3"])
            asistencia = float(request.form["asistencia"])
        except (ValueError, KeyError):
            return render_template(
                "ejercicio1.html",
                error="Debes ingresar valores numéricos en todos los campos.",
            )

        notas = [nota1, nota2, nota3]

        # Validación de rangos
        if any(n < 10 or n > 70 for n in notas):
            return render_template(
                "ejercicio1.html", error="Las notas deben estar entre 10 y 70."
            )
        if asistencia < 0 or asistencia > 100:
            return render_template(
                "ejercicio1.html", error="La asistencia debe estar entre 0 y 100."
            )

        promedio = calcular_promedio(notas)
        estado = obtener_estado(promedio, asistencia)

        registrar("Ejercicio 1", f"Promedio {promedio} - Asistencia {asistencia}% - {estado}")

        return render_template(
            "resultado.html",
            titulo="Resultado Ejercicio 1",
            lineas=[
                f"Notas ingresadas: {nota1} - {nota2} - {nota3}",
                f"Asistencia: {asistencia}%",
                f"Promedio: {promedio}",
            ],
            destacado=f"Estado: {estado}",
            aprobado=(estado == "APROBADO"),
        )

    return render_template("ejercicio1.html")


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    """GET: muestra el formulario. POST: procesa los 3 nombres."""
    if request.method == "POST":
        nombre1 = request.form.get("nombre1", "").strip()
        nombre2 = request.form.get("nombre2", "").strip()
        nombre3 = request.form.get("nombre3", "").strip()

        nombres = [nombre1, nombre2, nombre3]

        if any(n == "" for n in nombres):
            return render_template(
                "ejercicio2.html", error="Debes ingresar los 3 nombres."
            )

        if len(set(n.lower() for n in nombres)) < 3:
            return render_template(
                "ejercicio2.html", error="Los 3 nombres deben ser diferentes."
            )

        ganador, cantidad = nombre_mas_largo(nombres)

        registrar("Ejercicio 2", f"Nombre más largo: {ganador} ({cantidad} caracteres)")

        return render_template(
            "resultado.html",
            titulo="Resultado Ejercicio 2",
            lineas=[
                f"Nombres ingresados: {nombre1} - {nombre2} - {nombre3}",
                f"El nombre más largo es: {ganador}",
            ],
            destacado=f"Cantidad de caracteres: {cantidad}",
            aprobado=True,
        )

    return render_template("ejercicio2.html")


@app.route("/historial")
def ver_historial():
    """Muestra los registros almacenados en memoria."""
    return render_template("historial.html", historial=historial)


@app.errorhandler(404)
def pagina_no_encontrada(e):
    return render_template("error404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
