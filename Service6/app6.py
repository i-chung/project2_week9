from flask import Flask, request, Response
import requests
import random
app = Flask(__name__)
@app.route('/prize', methods=['GET', 'POST'])
def prize():
    postsector=request.data.decode('utf-8')
    if postsector == "0":
        prize = "£10"
    elif postsector == "5":
        prize = "£50"
    elif postsector == "8":
        prize = "£500"
    else:
        prize = "£0"
    return Response(prize, mimetype="text/plain")
	
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5005)