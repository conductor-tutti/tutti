# -*- coding:utf-8 -*-
'''


    ___________________________________
___/ YOUR GOOGLE APPENGINE FOLDER PATH \__________________________________________________
                                                                                       '''

GOOGLE_APPENGINE_PATH = "C:\\Program Files (x86)\\Google\\google_appengine"
MODE = 'UPDATE'

'''
GOOGLE_APPENGINE_PATH : Path of directory which has appcfg.py
MODE :
    'UPDATE'   => execute update
    'ROLLBACK' => execute appengine rollback

______________________________________________________________________________________/'''


































def auto_newline(string, bound) :
    if bound < 3 : raise ValueError("bound value should be bigger than 2.")
    splitted_str, bound = "", bound - 2
    while True :
        if len(string) <= bound : return splitted_str + ' ' + string
        splitted_str += ' %s %s' % (string[:bound], os.linesep)
        string = string[bound:]

""" Path Setting : MODIFY YOUR GOOGLE-APPENGINE PATH """
import os, sys
sys.path.insert(0, GOOGLE_APPENGINE_PATH)

""" Deploy """
print "======= Google App Engine Deploy Script ========================================"
cfg_path = os.path.join(GOOGLE_APPENGINE_PATH, "appcfg.py")
if MODE == 'ROLLBACK' : cmd_depl = 'rollback'
elif MODE == 'UPDATE' : cmd_depl = 'update'
else : raise ValueError('MODE VALUE IS NOT VALID : %s not in [ROLLBACK, UPDATE]' % MODE)
prj_path = os.path.abspath(".")
print auto_newline(
    " ".join([
        "python",
        "'%s'" % cfg_path,
        "--oauth2",
        cmd_depl,
        "'%s'" % prj_path
    ]),
    80
)
print "================================================================================"

""" Execute """
from appcfg import run_file
while len(sys.argv) > 0 :
    sys.argv.pop()
sys.argv.append(cfg_path)
sys.argv.append("--oauth2")
sys.argv.append(cmd_depl)
sys.argv.append(prj_path)
run_file(cfg_path, globals())

""" Recover Path """
sys.path.pop(0)