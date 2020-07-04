from application import app, db
from flask import render_template, request, json, Response

courseData = [{"courseID":"1111","title":"PHP 111","description":"Intro to PHP","credits":"3","term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":"4","term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":"3","term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":"3","term":"Fall, Spring"}, {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":"4","term":"Fall"}]


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
	return render_template("index.html", index=True)

@app.route('/login')
def login():
	return render_template("login.html", login=True)

@app.route('/courses/')
@app.route('/courses/<term>')
def courses(term="Spring 2020"):
	return render_template("courses.html", courseData=courseData, courses=True, term=term)

@app.route('/register')
def register():
	return render_template("register.html", register=True)

@app.route('/enrollment', methods=["GET","POST"])
def enrollment():
	id=request.form.get('courseID')
	title=request.form.get('title')
	term=request.form.get('term')
	return render_template("enrollment.html", data={"id":id,"title":title,"term":term})

@app.route('/api/')
@app.route('/api/<idx>')
def api(idx=None):
	if idx==None:
		jData=courseData
	else:
		jData=courseData[int(idx)]

	return Response(json.dumps(jData), mimetype='application/json')

class User(db.Document):
	user_id = db.IntField( unique=True )
	first_name = db.StringField( max_length=50 )
	last_name = db.StringField( max_length=50 )
	email = db.StringField( max_length=30 )
	password = db.StringField( max_length=30 )

@app.route('/user')
def user():
	#User(user_id=1, first_name="Shrey", last_name="Arora", email="shr@gamil.com", password="abc123").save()
	#User(user_id=2, first_name="Shikha", last_name="Saini", email="shi@gamil.com", password="abcd1234").save()
	users=User.objects.all()
	return render_template("user.html", users=users)