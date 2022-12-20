import os
from os.path import join, dirname
from dotenv import load_dotenv

# Determine if the environment is WIN_LOCAL, PI_LOCAL or HEROKU

# Check for HEROKU 1st
Is_Heroku = False
Is_Heroku = 'ENV1' in os.environ
if Is_Heroku:
    ENV = os.environ.get('ENV1')
    BOTNAME = os.environ.get('BOTNAME')
    SECRETTOKEN = os.environ.get('SECRETTOKEN')
    REDISCLOUD_URL = os.environ.get('REDISCLOUD_URL')
    CMC_API_KEY = os.environ.get('CMC_API_KEY')
    print('ENV :'+ENV + '::'+os.environ.get('BOTNAME'))

else:
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    #print(dotenv_path)
    ENV = os.environ.get('ENV1')
    BOTNAME = os.environ.get('BOTNAME')
    SECRETTOKEN = os.environ.get('SECRETTOKEN')
    CHATID = os.environ.get('CHATID')
    # print(os.environ.get('ENV1'))
    # print(os.environ.get('BOTNAME'))
    # print(os.environ.get('SECRETTOKEN'))
    print('ENV :'+ENV + '::'+os.environ.get('BOTNAME'))

