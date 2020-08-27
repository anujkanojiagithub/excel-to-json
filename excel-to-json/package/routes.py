from flask import Flask, render_template,url_for,request,jsonify
from package import app,excelPath
import json
import requests
from datetime import date, timedelta,datetime
import os
import pandas as pd



@app.route('/',methods=['GET','POST'])
def index():
   return render_template('main.html')

@app.route('/json',methods=['GET','POST'])
def uploadExel():
    if request.method == "POST":
        if request.files:
            excel = request.files['file']
            final_path = os.path.join(excelPath, excel.filename)
            excel.save(final_path)
            fjson = pd.read_excel(final_path)
            return jsonify(fjson.to_dict())
    

