#apt install python3-flask
#from flask import Flask
#app = Flask(__name__)

#@app.route("/")
#def homepage():
    #return "<b>Hello App<b>"

#app.run(debug=True)

# Importando o Flask
from flask import Flask

# Criando uma instância do Flask
app = Flask(__name__)

# Definindo a rota raiz ("/") e a função que será executada quando a rota for acessada
@app.route("/")
def homepage():
    return "<b1> Atividade 1 git: Edvaldo Gomes Pereira Júnior<b/1>"
    


# Verificando se este arquivo está sendo executado diretamente
if __name__ == "__main__":
    # Iniciando o servidor Flask na porta 5000 e ativando o modo de depuração
    app.run(debug=True)