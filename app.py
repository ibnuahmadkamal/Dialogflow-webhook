from warnings import resetwarnings
from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config.db import connection
from models.index import resources



#inti app
app = Flask(__name__)

@app.route('/')
def hello_world(): 
    return "webhook simple"

@app.route('/webhook', methods=['POST'])
def webhook():
  req = request.get_json(silent=True, force=True)
  query_result = req.get('queryResult')

  #mapping
  if query_result.get('action') == 'input.data':
    return webhookResult1(req)
  elif query_result.get('action') == 'show.data':
    return webhookResult2(req)
  elif query_result.get('action') == 'update.data':
    return webhookResult3(req)
  elif query_result.get('action') == 'delete.data':
    return webhookResult4(req)


#Input Data Barang
def webhookResult1(req):
  req = request.get_json(silent=True, force=True)
  query_result = req.get('queryResult')
  namaBarang = str(query_result.get('parameters').get('Namabarang')),
  jumlah = int(query_result.get('parameters').get('Jumlah'))
  namabarang = ''.join(namaBarang)
  connection.execute(resources.insert().values(
    NamaBarang = namabarang,
    Jumlah = jumlah
  ))

  fulfillmentText = 'Data berhasil di input'
  return {
      "fulfillmentText": fulfillmentText,
      "source": "webhookdata"
  }

#Menampilkan Jumlah berdasarkan nama
def webhookResult2(req):
  req = request.get_json(silent=True, force=True)
  query_result = req.get('queryResult')
  Namabarang = query_result.get('parameters').get('Namabarang')
  namabarang = ''.join(Namabarang)
  result = connection.execute(resources.select(resources.c.Jumlah).where(resources.c.NamaBarang == namabarang)).fetchone()
  answer = str(result[0])
  fulfillmentText = 'Jumlah barang ada =' +answer
  return {
      "fulfillmentText": fulfillmentText,
      "source": "webhookdata"
  }

#mengupdate jumlah barang
def webhookResult3(req):
  req = request.get_json(silent=True, force=True)
  query_result = req.get('queryResult')
  Namabarang = query_result.get('parameters').get('Namabarang')
  jumlah = int(query_result.get('parameters').get('Jumlah'))
  namabarang = ''.join(Namabarang)
  connection.execute(resources.update().values(
        NamaBarang = namabarang,
        Jumlah = jumlah
  ).where(resources.c.NamaBarang == namabarang))
  fulfillmentText = "Data berhasil di update"
  return {
      "fulfillmentText": fulfillmentText,
      "source": "webhookdata"
  }

#menghapus data barang
def webhookResult4(req):
  req = request.get_json(silent=True, force=True)
  query_result = req.get('queryResult')
  Namabarang = query_result.get('parameters').get('Namabarang')
  namabarang = ''.join(Namabarang)
  connection.execute(resources.delete().where(resources.c.NamaBarang == namabarang))
  fulfillmentText = "Data berhasil di hapus"
  return {
      "fulfillmentText": fulfillmentText,
      "source": "webhookdata"
  }

#Run app
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)