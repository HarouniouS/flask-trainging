from flask import Flask, render_template, url_for, flash, request, redirect
from forms import RegisterationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '2d4904a0818e55ebf6d4c38e8af9b56c'

posts = [
    {
        'author': 'Saif AlHaroun',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 21, 2020'
    },
    {
        'author': 'Fuad Daoud',
        'title': 'Blog Post 2',
        'content': 'First post content',
        'date_posted': 'April 22, 2020'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, title='Home')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterationForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data }!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)