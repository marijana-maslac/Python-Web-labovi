#!python

import subjects
import base
import session
import os
import cgi
from http import cookies

cookies_string = os.environ.get('HTTP_COOKIE', '')
all_cookies_object = cookies.SimpleCookie(cookies_string)

params = cgi.FieldStorage()

session_id = session.get_or_create_session_id()
if os.environ["REQUEST_METHOD"].upper() == "POST":
    session.add_to_session(params)

dicti = subjects.get_cookies(all_cookies_object)

def print_navigation():
    subjects.display_year()
    if params.getvalue("button") is not None:
            if(params.getvalue("button") != "List All"):
                 year = subjects.year_ids[params.getvalue("button")]
            else:
                year = params.getvalue("button")
    else:
        year = 1
    subjects.display_subject_on_year(year, dicti)


subjects.make_cookies(params)

base.start_html()
print_navigation()

base.end_html()


    
#print (params)
#print (os.environ)