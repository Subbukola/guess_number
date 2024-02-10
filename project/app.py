from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

secret_number = random.randint(1, 100)
attempts = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    global attempts, secret_number

    try:
        guess = int(request.form['guess'])
        attempts += 1

        if guess == secret_number:
            return jsonify({'result': 'correct', 'attempts': attempts})
        elif guess < secret_number:
            return jsonify({'result': 'low'})
        else:
            return jsonify({'result': 'high'})
    except ValueError:
        return jsonify({'result': 'error', 'message': 'Invalid input'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

