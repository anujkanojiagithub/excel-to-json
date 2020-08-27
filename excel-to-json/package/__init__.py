from flask import Flask
import os


app = Flask(__name__)
excelPath = app.config['IMAGE_UPLOADS'] = os.path.join(os.getcwd(),'files')


from package import routes