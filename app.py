# coding: utf-8

from flask import Flask, request, url_for, jsonify, render_template
from db import noticias


app = Flask("flask2")

# por enquanto vamos usar um template html hardcoded
# mas calma! em breve falaremos  sobre os templates com Jinja2

def html_page():
  return render_template("cadastro_page.html")

def formulario_page():
  return render_template("formulario.html")

@app.route("/noticias/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        dados_do_formulario = request.form.to_dict()
        nova_noticia = noticias.insert(dados_do_formulario)
        return u"""
            <h1>Noticia id %s inserida com sucesso!</h1>
            <a href="%s"> Inserir nova notícia </a>
        """ % (nova_noticia, url_for('cadastro'))
    else:  # GET
        return html_page().format(title=u"Inserir nova noticia", 
          body=formulario_page(),
          logo_url=url_for('static', filename='generic_logo.gif')
        )



@app.route("/noticias/")
def index():
    return jsonify(noticias=[noticia for noticia in noticias.all()])     
    

@app.route("/noticias/<int:noticia_id>")
def noticia(noticia_id):
    noticia = noticias.find_one(id=noticia_id)  # query no banco de dados
    return jsonify(noticia=noticia)   
    


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)

