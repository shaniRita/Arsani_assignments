import requests
from flask import Flask, redirect, url_for, render_template, request, session, jsonify

from interact_with_DB import interact_db

app = Flask(__name__)
app.secret_key = '12345'

users = {'user1': {'name': 'shani', 'email': 'shani@gmail.com'},
         'user2': {'name': 'itamar', 'email': 'itamar@gmail.com'},
         'user3': {'name': 'shay', 'email': 'shay@gmail.com'},
         'user4': {'name': 'agam', 'email': 'agam@gmail.com'},
         'user5': {'name': 'eden', 'email': 'eden@gmail.com'},
         'user6': {'name': 'coral', 'email': 'coral@gmail.com'}
         }


@app.route('/cv1')
def c1():
    return render_template('cv1.html')


@app.route('/')
@app.route('/cv2')
def c2():
    return render_template('cv2.html')


@app.route('/cv11')
def c11():
    return render_template('cv11.html')


@app.route('/assignment8')
def music():
    print("im in about ")
    name = 'shani'
    fname = 'freiman'
    return render_template('assignment8.html',
                           profile={'name': 'shani', 'second_name': 'freiman'},
                           university='BGU',
                           degree=['BSc', 'MS'],
                           hobbies=('art', 'music', 'sql'))
    return render_template('assignment8.html')


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9_func():
    print(users.values())
    if request.method == 'GET':
        if 'username' in session and session['username']:
            if 'search' in request.args:
                search = request.args['search']
                return render_template('assignment9.html', username=session['username']
                                       , search=search
                                       , users=users)
            return render_template('assignment9.html', users=users, username=session['username'])
        return render_template('assignment9.html', users=users)
    if request.method == 'POST':
        username = request.form['username']
        Password = request.form['password']
        found = True
        if found:
            session['username'] = username
            session['user_login'] = True
            return render_template('assignment9.html', username=username, users=users)
        else:
            return render_template('assignment9.html')


@app.route('/logout')
def logout_func():
    session['username'] = ''  ##Log out excist user
    return render_template('assignment9.html')


@app.route('/assignment11/users', methods=['GET'])
def json_users():
    query = "select * from users"
    query_results = interact_db(query=query, query_type='fetch')
    print(query_results)
    return jsonify(query_results)


@app.route('/assignment11/outer_source_backend', methods=['GET'])
def outer_source_backend():
    user_id = int(request.args['id']) if 'id' in request.args else None
    if user_id:
        return requests.get('https://reqres.in/api/users/%d' % user_id).json().get('data')
    else:
        return "Not a valid id"


@app.route('/assignment11/outer_source', methods=['GET'])
def assignment11_get_user():
    return render_template('assignment11.html')


from pages.assignment10.assignment10 import assignment10

app.register_blueprint(assignment10)


@app.route('/assignment12/restapi_users', defaults={'user_id': 2})
@app.route("/assignment12/restapi_users/<int:user_id>")
def ex12(user_id):
    print('yes')
    return_dict = {}
    query = "select * from db.users where id= '%s';" % user_id
    user = interact_db(query=query, query_type='fetch')
    if len(user) > 0:
        return_dict[f'user_{user_id}'] = {
            'name': user[0].name,
            'email': user[0].email,
            'day created': user[0].create_date,
            'password': user[0].password
        }

    else:
        return_dict = {
            'sucsses': 'false'
        }
    return jsonify(return_dict)


if __name__ == '__main__':
    app.run(debug=True)
