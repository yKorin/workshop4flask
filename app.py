from flask import Flask, render_template, request, redirect, url_for

from dao.studentHelper import UserHelper
from forms.form import userForm

app = Flask(__name__)
app.secret_key = 'development key'




@app.route('/', methods=['GET', 'POST'])
def user():
    form = userForm()
    helper = UserHelper()

    if request.method == 'POST':
        if form.validate() == False:
            errors = []
            errors.append(form.user_year.errors)
            errors.append(form.user_name.errors)
            return render_template('student.html', form=form,errors = errors)
        else:
            status = helper.newUser(

                                            form.user_name.data,

                                            form.user_year.data
                                       )
            allUser = helper.getAllUsers()
            return render_template('all.html',result = allUser)


    return render_template('student.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)