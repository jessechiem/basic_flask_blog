'''
Variables for Flask configuration in run and 
other related modules within same folder.
'''
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
DATABASE_NAME = 'my_blog.db'  # name of db for posts
DATABASE_PATH = os.path.join(base_dir, DATABASE_NAME)
USERNAME = 'admin'
PASSWORD = 'admin'
#SECRET_KEY = '0N}+s\x1cE\x91\xaa\xca|j\x98J|\x10W\xbf\x1b]\x94n\x0c\xc6'
SECRET_KEY = 'dev'  # ref: http://bit.ly/2hLUO0P
WTF_CSRF_ENABLED = True  # helps against cross-site request forgery attacks
