from flask import Flask, request, render_template_string
from banco_04 import Banco
from entidades_04 import Persona, Empresa

banco_1 = Banco("Duke Bank: el banco de internet")
persona1 = Persona("Agustín", 39081430, 28, "agustindeoro8@gmail.com")
empresa1 = Empresa("Tech Narco", 204, "tnarco@gmail.com")
banco_1.crear_cuenta(persona1)
banco_1.crear_cuenta(empresa1)
banco_1.depositar(persona1, 1800)
banco_1.depositar(empresa1, 5000)
banco_1.depositar(persona1, -700)


app = Flask("Mi servidor")

@app.route("/")
def home():
    return f"Bienvenidos a {banco_1}"

@app.route("/cuentas")
def cuentas():
    return banco_1.mostrar_cuentas()

@app.route("/crear-cuenta-form")
def crear_cuenta_form():
    html_form = """
    <html>
        <body>
            <form action="/crear-cuenta" method="post">
                <label for="tipo_cuenta">Tipo de cuenta:</label><br>
                <select name="tipo_cuenta" id="tipo_cuenta">
                    <option value="persona">Persona</option>
                    <option value="empresa">Empresa</option>
                </select><br><br>
                
                <label for="nombre">Nombre:</label><br>
                <input type="text" id="nombre" name="nombre"><br><br>
                
                <label for="identificador">Documento/Identificador:</label><br>
                <input type="text" id="identificador" name="identificador"><br><br>
                
                <label for="edad">Edad(Solo personas):</label><br>
                <input type="text" id="edad" name="edad"><br><br>
                
                <label for="email">Email:</label><br>
                <input type="text" id="email" name="email"><br><br>
                
                <input type="submit" value="Crear cuenta">
            </form>
        </body>
    </html>
    """
    return render_template_string(html_form)

@app.route("/crear-cuenta", methods=["POST"])
def crear_cuenta():
    print(request.form)
    tipo_cuenta = request.form["tipo_cuenta"]
    nombre = request.form["nombre"]
    identificador = request.form["identificador"]
    edad = request.form["edad"]
    email = request.form["email"]
    
    if tipo_cuenta == "persona":
        cliente = Persona(nombre, identificador, edad, email)
    else: cliente = Empresa(nombre, identificador, email)
    
    banco_1.crear_cuenta(cliente)
    return f"Estamos trabajando para usted"

app.run(debug=True, port=8081)