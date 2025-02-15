""" Импорт папок из других веток
ПРАВИЛЬНЫЙ СПОСОБ ИМПОРТА ИЗ ДРУГОЙ ВЕТКИ
sys.path.insert(1, os.path.join(sys.path[0]))  или sys.path.insert(1, os.path.join(sys.path[0],'..'))"""

""" Импорт в PyCh просто"""
import sys,os,pathlib
p = os.path.relpath(path='vsearch.py',start='aaa.py')
print(p)


# ml = os.path.join(os.getcwd(), "..", "ML_koroteev", "pandas_series_numpy_corr_lin_regr.py", "data")
ml = os.path.join(os.getcwd(), "..", "ML_koroteev")


# sys.path.insert(1,os.path.join(sys.path[0],'..'))
# from lesson.vsearch import t
# print(t)
#
# sys.path.insert(1, str(pathlib.Path(__file__).parent))
# from  v_e_b import s4l_ref
# print(s4l_ref.rt)

""" __________________________________Импорт в PyCh просто"""
# from imp_f.imp2 import gp
# print(gp)
#
# sys.path.insert(1,os.path.join(sys.path[0],'../../'))
# from lesson import vsearch
# print(vsearch.t)
#
sys.path.insert(1,os.path.join(sys.path[0],'../../'))
from lesson.map import t
print(t)
#
# sys.path.insert(1,os.path.join(sys.path[0],'../../'))
# from webapp.DBcm import w
# print(w)
# #sys.path.append( os.path.join(sys.path[0]))        #спсоб с append
# sys.path.insert(1, os.path.join(sys.path[0],'..'))   #   c insert
# #sys.path.insert(1, os.path.join(sys.path[0]))        #  с insert
# #from flask import Flask
# sys.path.insert(1, os.path.join(sys.path[0],'..'))   #   c insert
# from lesson.vsearch import s4l
# print(s4l('assdg','a'))

# sys.path.insert(1, os.path.join(sys.path[0],'..'))
# from webapp.DBcm import UseDatabase

# dbconfig = {'host': '127.0.0.1','user': 'vsr',
#             'password': 'vsp','database':'vsldb',}
# with UseDatabase (dbconfig) as cur:
#     _SQL = """show tables"""
#     cur.execute(_SQL)
#     data = cur.fetchall()
# print(data)

                