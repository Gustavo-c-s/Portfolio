from flask import Flask, render_template
import threading

app = Flask(__name__)

def iniciar_comandos():
    while True:
        comando_voz_usuario()

@app.route("/")
def index():
    # Iniciar a thread para a função comando_voz_usuario
    t = threading.Thread(target=iniciar_comandos)
    t.start()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
