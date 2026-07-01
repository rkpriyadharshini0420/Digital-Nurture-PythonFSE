import os

# Get the base directory of the project
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # This creates a file named 'app.db' in your project root folder
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    
    # This suppresses a warning about tracking modifications
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Optional: Needed if you use forms or sessions
    SECRET_KEY = 'you-will-never-guess'