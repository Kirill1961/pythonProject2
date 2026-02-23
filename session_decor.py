from flask import Flask, session

app = Flask(__name__)


@app.route('/status')
def chek_status():
    if 'logged_in' in session:
        return 'You are currently logged in'
    return 'You are not logged in'

from  class_init import Cat
print (Cat('Joe', 10, 'Wite'))
