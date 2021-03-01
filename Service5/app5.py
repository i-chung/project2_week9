from flask import Flask, Response, request
import random
app = Flask(__name__)
@app.route('/postwalk', methods=['GET'])
def postwalk():
    postwalks= ["AA", "AB", "AC", "AD", "AE", "AF", "AG", "AH", "AI", "AJ", "AK", "AL"]
    return Response(random.choices(postwalks), mimetype="text/plain")
if __name__== "__main__":
    app.run(debug=True, host='0.0.0.0', port=5004)
                                                              