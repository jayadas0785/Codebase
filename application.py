from flask import Flask, render_template, flash, request
from wtforms import Form, StringField, PasswordField, validators

DEBUG = False
application = Flask(__name__)
application.config.from_object(__name__)
application.config['SECRET_KEY'] = '123456'

fixed_user = 'Jayanta'
fixed_password = '12345'

class BITSForm(Form):
    username = StringField('Username:', validators=[
                                              validators.DataRequired()])
    password = PasswordField('Password:', validators=[
                                                  validators.DataRequired()])


@application.route("/", methods=['GET', 'POST'])
def python_form():
    form = BITSForm(request.form)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if form.validate():
            flash('Username and password entered here is: {} and {}'.format(username, password))
            if username == fixed_user and password == fixed_password:
                flash('username and password are correct')
            else:
                flash('Error: username and password combination is NOT correct')
        else:
            flash('Error: All Fields are Required')

    return render_template('index.html', form=form)

if __name__ == "__main__":
    application.run()