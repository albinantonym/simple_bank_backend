from flask import Flask ,request
from flask_cors import CORS
import psycopg2 as psy

#connecting to database
conn = psy.connect(database = "inte", 
                        user = "admin", 
                        host= 'localhost',
                        password = "123",
                        port = 5432)
app=Flask(__name__)
CORS(app)

@app.route('/ping',methods=["GET"])
def home():
	return "pong!",200

#get the entire list of banks 
@app.route('/api/getbanks',methods=["GET"])
def banklist():
	try:
		cur = conn.cursor()
		cur.execute("Select * from Banks;")
		rows = cur.fetchall()
		return {"message":"success","banks":rows},200;
		cur.close()
	except:
		return {"error":"Unkown error occured"},500

#get the names and ifsc of every branch in a bank with its bank_id
@app.route('/api/getbranches',methods=["GET"])
def branches():
	try:
		data=request.args
		if ("bankid" not in data):
			return {"error":"Insufficient information"},400
		cur = conn.cursor()
		cur.execute("Select Branch , ifsc from branches WHERE bank_id="+data["bankid"]+";")
		rows = cur.fetchall()
		if len(rows)==0:
			return {"error":"Incorrect bank_id"},400
		return {"branches":rows,"message":"success"},200;
		cur.close()
	except Exception as e:
		return {"error":"Unkown error occured"},500

#get the branch details using ifsc number
@app.route('/api/branchdetails',methods=["GET"])
def branchdetails():
	try:
		data=request.args
		if ("ifsc" not in data):
			return {"error":"Insufficient information"},400
		cur = conn.cursor()
		cur.execute("Select * from bank_branches WHERE ifsc='"+data["ifsc"]+"';")
		rows = cur.fetchall()
		print(rows)
		if len(rows)==0:
			return {"error":"Incorrect ifsc number"},400
		return {"message":"success","ifsc":rows[0][0],"bank_id":rows[0][1],"branch":rows[0][2],"address":rows[0][3],"city":rows[0][4],"district":rows[0][5],"state":rows[0][6],"bank":rows[0][7]},200;
		cur.close()
	except Exception as e:
		return {"error":"Unkown error occured"},500

app.run(host="0.0.0.0", port=5000)