from flask import Flask, Response, request
import random
app = Flask(__name__)
@app.route('/postarea', methods=['GET'])
def postarea():
    postareas = ["AB", "AL", "B", "BA", "BB", "BD", "BH", "BL", "BN", "BR", "BS", "BT",
 "CA", "CB", "CF", "CH", "CM", "CO", "CR", "CT", "CV", "CW", "DA", "DD", "DE", "DG", "D
H", "DL", "DN", "DT", "DY", "E", "EC", "EH", "EN", "EX", "FK", "FY", "G", "GL", "GU", "
GY", "HA", "HD", "HG", "HP", "HR", "HS", "HU", "HX", "IG", "IM", "IP", "IV", "JE", "KA"
, "KT", "KW", "KY", "L", "LA", "LD", "LE", "LL", "LN", "LS", "LU", "M", "ME", "MK", "ML
", "N", "NE", "NG", "NN", "NP", "NR", "NW", "OL", "OX", "PA", "PE", "PH", "PL", "PO", "
PR", "RG", "RH", "RM", "S", "SA", "SE", "SG", "SK", "SL", "SM", "SN", "SO", "SP", "SR",
 "SS", "ST", "SW", "SY", "TA", "TD", "TF", "TN", "TQ", "TR", "TS", "TW", "UB", "W", "WA
", "WC", "WD", "WF", "WN", "WR", "WS", "WV", "YO", "ZE"]
    return Response(random.choices(postareas), mimetype="text/plain")
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)

