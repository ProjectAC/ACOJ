from flask import request, session
from ACOJ7Server import app
from ACOJ7Server.ACEssentials import response, db

@app.route('/submission', methods=['GET', 'POST'])
def submission():
    
    # Submit a piece of code for a task
    if request.method == 'POST' :
        # Judge whether the user has logged in
        if 'userInfo' not in session :
            return response.error(response.NOT_LOGGED_IN)
        
        param = request.form

        # Judge whether the form is complete
        if 'language' not in param or\
           'code' not in param or\
           'tid' not in param :
            return response.error(response.INFORMATION_INCOMPLETE)
        
        # Insert
        try :
            res = db.sql('''
                insert into submission
                (uid, tid, language, code, public)
                values
                (%d, %d, '%s', '%s', %d)
            ''' % (
                int(session['userInfo']['uid']),
                int(param['tid']),
                param['language'],
                param['code'],
                int(param['public'] if 'public' in param else False)
            ))
        except:
            return response.error(response.UNEXPECTED)
        return response.error(response.OK)

    # Fetch the submission list
    elif request.method == 'GET' :

        info = request.args

        # If the user wants only one record with a certain id:
        if 'sid' in info :
            
            #if 'userId' not in session:
            #    return response.error(response.NOT_LOGGED_IN)
            
            results = db.sql('''
                select *
                from submission
                where sid = %d
            ''', (
                int(info['sid']),
            ))

            return response.error(response.OK)

        # Else, the user wants the submission list
        else :
            return response.JSON(
		        {
    			    'a': 'AAA'
		        }
	        )