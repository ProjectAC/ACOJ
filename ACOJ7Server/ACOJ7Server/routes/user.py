from flask import request, session
from ACOJ7Server import app
from ACOJ7Server.ACEssentials import response, db, hash

@app.route('/user/login', methods=['GET', 'POST'])
def login():
    
    # Login 
    if request.method == 'POST' :
        param = request.form
        if 'handle' not in param or \
           'password' not in param :
            return response.error(response.INFORMATION_INCOMPLETE)

        try :
            res = db.sql('''
                select *
                from user
                where
                (username = '%s' or
                email = '%s')
            ''', (
                param['handle'],
                param['handle']
            ))[0][0]

            # Login successful
            #                               SALT       PSWD
            if hash.md5(param['password'], res[4]) != res[3] :
                return response.error(response.AUTHORIZE_FAILED)

            session['userInfo'] = {
                'uid': res[0],
                'email': res[1],
                'username': res[2],
                'op': res[5],
                'ban': res[6]
            }
            return response.JSON(session['userInfo'])
        except:
            return response.error(response.AUTHORIZE_FAILED)
    # Fetch
    else :


        return response.JSON({})
            
#@app.route('/user/register', methods)