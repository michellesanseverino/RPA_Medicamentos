from flask import Flask, jsonify
from db.mongo_connect import colecao

app = Flask(__name__)

@app.route("/medicamentos")
def listar_medicamentos():
    medicamentos = list(colecao.find({}, {"_id": 0}))
    return jsonify(medicamentos)

if __name__ == "__main__":
    app.run(debug=True)
