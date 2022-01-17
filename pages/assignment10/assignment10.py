from flask import Blueprint, render_template, request, redirect, flash,session
from interact_with_DB import interact_db

# assignment10 blueprint definition
assignment10 = Blueprint('/assignment10', __name__, static_folder='static', static_url_path='/assignment10', template_folder='templates')


# Routes
@assignment10.route('/assignment10')
def users():
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=users)


@assignment10.route('/insert_user', methods=['GET','POST'])
def insertUsers():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        check_input = "SELECT name FROM db.users WHERE name='%s';" % name
        answer = interact_db(query=check_input, query_type='fetch')
        if len(answer) == 0:
            query = "insert into db.users (name, email , password)\
                            value ('%s', '%s', '%s');" % (name, email, password)
            interact_db(query=query, query_type='commit')
            # message
            return redirect('/assignment10?p1=User-added')
        else:
            # message
            flash('this user name is already registered')
            return redirect('/assignment10')
    return render_template('assignment10.html', req_method=request.method)



@assignment10.route('/update', methods=['GET','POST'])
def update():
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        id = request.form['id']
        interact_db(query=" UPDATE db.users SET name='%s',email='%s' ,password='%s' WHERE id ='%s';"%\
                             (name,email,password,id), query_type='commit')
        # session['messages'] = 'User Updated !'
        return redirect('/assignment10')

#         id = request.form['id']
#         name = request.form['name']
#         email = request.form['email']
#         password = request.form['password']
#         query = " UPDATE db.users SET name='%s',email='%s' ,password='%s' WHERE id='%s';"%\
#                 (name, email, password, id)
#         interact_db(query=query, query_type='commit')
#         # message
#         return redirect('/assignment10?p1=User-update')



@assignment10.route('/delete_user', methods=['POST'])
def deleteUsers():

    userId = request.form['id']
    check = "SELECT name FROM db.users WHERE id='%s';" % userId
    answer = interact_db(query=check, query_type='fetch')
    if len(answer) > 0:
        query = "delete from db.users where id='%s';" % userId
        interact_db(query=query, query_type='commit')
        #message
        return redirect('/assignment10?p1=User-delete')
    else:
        # message
        return redirect('/assignment10?p1=User-notfound')