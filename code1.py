import mysql.connector

conn = mysql.connector.connect(user='root', password='', host='localhost', database='dabase')
if conn.is_connected():
    print("connection Established")

mycursor = conn.cursor()


from flask import Flask, jsonify, request
app = Flask(__name__)



in_memory_datastore_students = {
   "Darren" : {"name": "Himanshu"},
   "ALGOL" : {"name": "Amit"},
   "APL" : {"name": "Mukul"}
}

@app.get('/me')
# @app.route('/', methods = ['GET', 'POST'])
def home():
    # if(request.method == 'GET'):
    return {'data': in_memory_datastore_students.values()}
  

@app.route('/home/<name>/<branch>', methods = ['GET'])
def disp(name, branch):
    
  
    mycursor.execute("""INSERT INTO `students` VALUES ('{}', '{}');""".format(name, branch))
    conn.commit()




# driver function
if __name__ == '__main__':
   app.run(debug=True)
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
# in_memory_datastore = {
#    "Darren" : {"name": "Delhi", "Temprature": 32, "Rain": "Yes"},
#    "ALGOL" : {"name": "Rohtak", "Temprature": 30, "Rain": "Yes"},
#    "APL" : {"name": "Pune", "Temprature": 26, "Rain": "Storm"}
# }


# }
# in_memory_datastore_adding = {
#    "StudentName": {"StudentName": "Himanshu"}
# }



# @app.get('/weather')
# def list_programming_languages():
#    return {"Weather":list(in_memory_datastore.values())}

# @app.get('/dtustudents')
# def list_students():
#    return {"Students":list(in_memory_datastore_students.values())}
# @app.get('/addstudent')
# def list_adding():
#    return {"Students":list(in_memory_datastore_adding.values())}


