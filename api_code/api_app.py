from flask import Flask, jsonify

api_app = Flask(__name__)

@api_app.route('/', methods=['GET'])
def index():
    return "SDPX GROUP 3"

@api_app.route('/is_prime', methods=['GET'])
def is_prime_check():
    return "Please provide a number to check if it is prime"

@api_app.route('/is_prime/<num>', methods=['GET'])
def is_prime(num):
    try:
        num = eval(num)
        if num < 2 or num != int(num):
            return jsonify({"Number": num, "Is_prime": False})
        else:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return jsonify({"Number": num, "Is_prime": False})
            return jsonify({"Number": num, "Is_prime": True})
    except:
        return jsonify({"ERROR": "Invalid input"})

if __name__ == '__main__':
    api_app.run(host='0.0.0.0', port=5000)
