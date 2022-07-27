from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "layan"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]

@app.route('/',methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method=='GET':

		return render_template("login.html")


	else:

		name=request.form['username']
		password1=request.form['password']
		if username==name and password1==password:
			return redirect(url_for('home'))
		else:

			return render_template('login.html')






@app.route('/home')  # '/' for the default page
def home():
  return render_template('home.html', facebook_friends=facebook_friends) 




@app.route('/fry/<string:name>',methods=['GET', 'POST'])  # '/' for the default page
def friend(name):
	if name in facebook_friends:
		return render_template('friend_exists.html',check=True)
	else:
	  return render_template('friend_exists.html',check=False)
  





if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)