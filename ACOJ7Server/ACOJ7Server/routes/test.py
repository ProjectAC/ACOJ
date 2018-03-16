from flask import request, session
from ACOJ7Server import app
from ACOJ7Server.ACEssentials import response, db

@app.route('/test')
def test():
    res = db.sql('''
        select *
        from user
    ''')

    print(res)

    return response.error(response.OK)