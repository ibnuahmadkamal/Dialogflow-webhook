from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def hello_world(): 
    return "webhook simple"
    
@app.route('/webhook', methods=['POST'])
def webhook():
  req = request.get_json(silent=True, force=True)
  fulfillmentText = ''
  sum = 0
  query_result = req.get('queryResult')
  if query_result.get('action') == 'add.numbers':
    num1 = int(query_result.get('parameters').get('number1'))
    num2 = int(query_result.get('parameters').get('number2'))
    sum = str(num1 + num2)
    print('here num1 = {0}'.format(num1))
    print('here num2 = {0}'.format(num2))
    fulfillmentText = 'Hasil penjumlahan 2 angka tersebut = '+sum
  elif query_result.get('action') == 'multiply.numbers':
    num1 = int(query_result.get('parameters').get('number1'))
    num2 = int(query_result.get('parameters').get('number2'))
    multiply = str(num1 * num2)
    print('here num1 = {0}'.format(num1))
    print('here num2 = {0}'.format(num2))
    fulfillmentText = 'Hasil perkalian 2 angka tersebut = '+multiply
  return {
        "fulfillmentText": fulfillmentText,
        "source": "webhookdata"
    }
    
   
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)