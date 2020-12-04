from flask import Flask , render_template, request , redirect
from flask_mysqldb import MySQL
app = Flask (__name__ )



app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'mydetails'


mysql = MySQL(app)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        userDetails = request.form

        name = userDetails['name']
        city = userDetails['city']
        state = userDetails['state']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, city,state) VALUES(%s, %s, %s)", (name, city, state))
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    return render_template('index.html')



@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html', userDetails=userDetails)



if __name__ == "__main__":
    app.run(debug= True)