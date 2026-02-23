import os
import sys
import pprint
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from flask import Flask, render_template,request,escape
from mymodules.vsearch import s4l
from DBcm import UseDatabase
app = Flask(__name__)
app.config ['dbconfig'] = {'host': '127.0.0.1','user': 'vsr', 'password': 'vsp','database':'vsldb',}

def l_r(req,res):
    
    with UseDatabase (app.config ['dbconfig']) as cur:
    

        _SQL = """insert into log
                (phrase, letters, ip, browser_string, results )
                values
                (%s, %s, %s, %s, %s)"""
        use_data = (request.form['phrase'],
                        request.form['letters'],
                        req.remote_addr,
                        ((req.user_agent.string).split(maxsplit=-1))[0],
                        res,)
        cur.execute(_SQL,use_data)
  
            
@app.route('/d_s',methods= ['POST'])
def d_s() :
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are you result'
    results = str (s4l(phrase,letters))

    l_r (request, results)
    return render_template ( 'result.html',
                              the_title = title,
                             the_phrase = phrase,
                             the_letters = letters,
                              the_results = results,)                              
@app.route('/')
@app.route('/en')
def entry_page() :
    return render_template('entry.html', 
                           the_title='Hi to s4l on the web')
@app.route('/vl')
def v_l():
    with UseDatabase (app.config ['dbconfig']) as cur:
        # _SQL = """ (select phrase, letters, ip, browser_string, results from log )"""  
        cur.execute('select*from log')
        answer = cur.fetchall()     
        titles = ('phrase', 'letters', 'User_agent', 'Remote_addr', 'Results')
        return render_template('viewlog.html',
                            the_title = 'View log',
                            the_row_titles = titles,
                             the_data = answer,)


if __name__ == '__main__':
    #app.debug = True
    app.run()
