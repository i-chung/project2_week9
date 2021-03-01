from flask import Flask, Response, request
import random
app = Flask(__name__)
@app.route('/postdistrict', methods=['GET'])
def postdistrict():
    postdistricts = ["1", "2", "3", "4", "5", "4", "5", "6", "7", "8", "9", "10"]
    return Response(random.choices(postdistricts), mimetype="text/plain")
if __name__== "__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)