from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/app/activate', methods=['POST'])
def activate():
    data = request.form  # Get form data from POST request
    
    response = {
        "status": ":)",
        "message": {},
        "error": {
            "message": "Valid key."
        }
    }
    
    return jsonify(response),200

if __name__ == '__main__':
    app.run(debug=True)
