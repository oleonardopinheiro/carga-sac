from flask import Flask
import os
import warnings
from hdbcli import dbapi

app = Flask(__name__)

class hanadb:
    def getConnection():
        warnings.filterwarnings('ignore')

        connection = dbapi.connect(
            address = "ab5701ee-9c6d-4b44-99bc-6b317aec1a1c.hana.prod-br10.hanacloud.ondemand.com",
            port = 443,
            user = "APP_USER",
            password = "USPedra20210617b"
        )

        cursor = connection.cursor()
        cursor.execute("SET SCHEMA " + "USPEDRASAPS4_HDI_DB_1")

        return connection

    def getCursor():
        connection = getConnection()
        cursor = connection.cursor()
        return cursor

@app.route('/', methods=['GET'])
def home():
    return "<h1>Você não pode acessar essa Pagina</h1><p>tente contado com o Leonardo Pinheiro - Inovação e Dados</p>"

@app.route('/api/procedure', methods=['GET', 'POST'])
def cargaCSCProcedure():
    conHana = hanadb.getConnection()
    cursor = conHana.cursor()
    
    query = 'CALL "S_USPEDRA_1"."SP_PRODUC_V_CSC_PROJETOS"'
    cursor.execute(query)
    print('Cursor executado')   
    return 'Carga Rodada com sucesso, a Inovação e Dados agradece!'

@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return "<h1>Pagina não existente, favor</h1><p>entrar em contato com a Inovação e Dados</p>", 404

if __name__ == "__main__":
    app.run(debug=False, threaded=True, port=5000)

