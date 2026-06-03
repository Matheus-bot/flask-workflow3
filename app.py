from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Sistema de Biblioteca"

@app.route("/sobre")
def sobre():
    return "Projeto desenvolvido na disciplina de Integração e Entrega Contínua"

@app.route("/livros")
def livros():
    return "Lista de livros cadastrados"

@app.route("/autores")
def autores():
    return "Lista de autores cadastrados"

@app.route("/contato")
def contato():
    return "Página de contato do sistema"

@app.route("/cadastro-livro")
def cadastro_livro():
    return "Página de cadastro de livros"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
