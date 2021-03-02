from flask import Flask, render_template
import requests
app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    # Gets a postcode area
    postarea = requests.get("http://localhost:5001/postarea")
    # Gets a postcode district
    postdistrict = requests.get("http://localhost:5002/postdistrict")
    # Gets a postcode sector
    postsector = requests.get("http://localhost:5003/postsector")
    # Gets a postcode walk
    postwalk = requests.get("http://localhost:5004/postwalk")
    # Get the amount of prize money
    prize = requests.get("http://localhost:5005/prize")
    return render_template('index.html', postarea=postarea.text, postdistrict=postdistrict.text, postsector=postsector.text, postwalk=postwalk.text, prize=prize.text)
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)