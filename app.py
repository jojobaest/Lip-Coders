from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__, template_folder='templates')

openai.api_key = //api key placeholder

received_rgb = None

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/send_data', methods=['POST'])
def receive_data():
    global received_rgb

    data = request.get_json()
    received_rgb = data.get('data', '')  # Extract the user's input from JavaScript.

    # Do something with the variable in Python.
    # For example, you can print it.
    print('Received from JavaScript:', received_rgb)

    # You can also send a response back to JavaScript (if needed).
    return jsonify({'message': 'Data received by Python'})

@app.route('/get_openai_response', methods=['GET'])
def get_openai_response():  
  global received_rgb

  if received_rgb is None:
     return jsonify({'error': 'Data not received from JavaScript yet'})

  rgb = received_rgb
  result = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "user",
        "content": "Give a name of a good lipstick color that fits rgb" + rgb + " colored lips. Then on a newline character, recommend two specific lipstick products of that lipstick color name in bullet point format."
      }
    ]
  )
    
  response_content = result.choices[0].message.content
    
  return jsonify({'dataForTheFrontEnd': response_content})

if __name__ == '__main__':
    app.run()
