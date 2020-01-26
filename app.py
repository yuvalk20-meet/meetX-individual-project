from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"

from database import *	
import random

##### Code here ######
@app.route('/',  methods=['GET', 'POST'])
def homepage():
	if request.method == 'POST':
		print(request.form['subject'])
		test = query_all()
		return render_template("home2.html", subjecth = request.form['subject'], gradeh = request.form['grade'], tests = test)
	else:
		test = query_all()
		print("get")
		return render_template("home.html", tests = test[::-1], subjecth = "", gradeh = "")



@app.route('/upload',  methods=['GET', 'POST'])
def uploadpage():
	if request.method == 'POST':
		print(request.form.keys())
		print(request.form['username'])
		
		subjectf = request.form['subject']
		gradef = request.form['grade']
		desf = request.form['des']
		usernamef = request.form['username']

		f = request.files['image']     #test
		f.save("Ben El/tests/"+f.filename)
		'''
		if(isExistTest(f)):
			print("error 1")
			f.save("Ben El/tests/"+f.filename)	#saves the file that was recived from the user
		else:
			print("eror 2")
			f.save("Ben El/tests/"+usernamef+random.randint(0,10000)+f.filename)	#saves the file that was recived from the user
		
		'''
		#saves the path of the file (string)
		f2 = request.files['solution']
		f2.save("Ben El/solutions/"+f2.filename)
		'''
		if(isExistTest(f2)):
			print("error 3")
			f2.save("Ben El/solutions/"+f2.filename)	#saves the file that was recived from the user
		else:
			print("eror 4")
			print("!!!!!!!!!!!!!!!!!!!!!!")
			f2.save("Ben El/solutions/"+usernamef+random.randint(0,10000)+f2.filename)	#saves the file that was recived from the user
		
'''
		
        
		add_test(subjectf, gradef, f.filename, desf, f2.filename ,usernamef)
		print("added to db")
		return render_template("response.html", un = usernamef)

	else:
		return render_template("Upload.html")

@app.route('/testid/<string:id>')
def testbyid(id):
	test = test_by_id(id)
	if(test.subject == "math"):
		imagepath1 = "https://www.insidehighered.com/sites/default/server_files/media/iStock_6387974_LARGE.jpg"
	if(test.subject == "cs"):
		imagepath1 = "https://via.vision/wp-content/uploads/2019/02/binary.jpg"

	




	return render_template("about.html", imagepath = imagepath1, grade = test.grade, subject = test.subject, des = test.description, username = test.username, sol = test.solution, test = test.picture)

@app.route('/login')
def loginpage():
	return render_template("login.html")

#####################


if __name__ == '__main__':
    app.run(debug=True)