from flask import Flask, render_template

#create a Flask Instance
app = Flask(__name__)

#create a route decorator
@app.route('/')
def index():
	first_name = "BoB"
	stuff = "not bold txt"
	favourite_pizza = ["Pepperoni", "Cheese", "mushroom", "meatfeast", 555]
	return render_template("index.html",
						   first_name=first_name,
						   stuff=stuff,
						   favourite_pizza=favourite_pizza)

#0.0.0.0/user/johnetc
@app.route('/user/<name>')
def user(name):
	return render_template("user.html", name=name)


#404 page not found
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

#Internal server error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500

 




if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)	

