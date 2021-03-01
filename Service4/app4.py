from flask import Flask, Response, request
import random
app = Flask(__name__)
@app.route('/postsector', methods=['GET'])
def postsector():
    postsectors = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    return Response(random.choices(postsectors), mimetype="text/plain")
if __name__== "__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)
