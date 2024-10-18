from flask import Flask, jsonify,render_template
import Add
import Subtract
import Multiply
import Divide 

app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/<string:operation>/<string:a>/<string:b>', methods=['GET'])
def calculate(operation: str, a: str, b: str):
    try:
        a = float(a)
        b = float(b)

        calculator = None
        
        match operation:
            case "add":
                calculator = Add.add()          
            case "minus":
                calculator = Subtract.subtract()
            case "multiply":
                calculator = Multiply.multiply()
            case "":
                calculator = Divide.divide()
            case _:
                return jsonify({
                    'status': 'error',
                    'message': 'Invalid operation'
                }), 400  # Bad Request

        result = calculator.compute(a, b)
        return jsonify({
            'status': 'success',
            'result': f'the result of {operation} {a} and {b} is {result}'
        }), 200

    except ValueError as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400  # Bad Request

    except ZeroDivisionError:
        return jsonify({
            'status': 'error',
            'message': 'Division by zero'
        }), 422  # Unprocessable Entity

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'An unexpected error occurred: {str(e)}'
        }), 500  # Internal Server Error

if __name__ == '__main__':
    app.run(port=5000) 