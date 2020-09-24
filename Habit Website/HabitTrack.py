from flask import Flask, render_template, request, session
from flask_session import Session
import numpy as np
import pandas as pd
import json
import os
from glob import glob
import plotly
import plotly.graph_objs as go


app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)


@app.route('/')
def startForm():
    session.clear()
    return render_template('start-form.html')


@app.route('/', methods=['POST'])
def form_post():
    username = (request.form['username'])
    password = (request.form['password'])
    credval = checkCreds(username, password)
    if (credval == True):
        userdata = loadUserData(session['id'])
        pieviz = getPieGraph(userdata)
        trucktable = getDataTable(userdata, 'all')
        return render_template('index.html', name=session['id'], pieviz=pieviz, trucktable=trucktable)
    else:
        return render_template('error-page.html')


def checkCreds(username, password):
    creddf = pd.read_csv('static/data/TychonCreds.csv')
    valid = False
    userdata = creddf[creddf['user'] == username]
    if (len(userdata) > 0):
        if (password == userdata['pass'].values[0]):
            valid = True
            session['id'] = userdata['id'].values[0]
    return valid


def loadUserData(identity):
    fulldata = pd.read_csv('static/data/TychonUsers.csv')
    userdata = fulldata[fulldata['Name'] == identity]
    session['userdata'] = userdata
    return userdata


def getPieGraph(data):
    pieData = data
    pieData = data.groupby('Category')['Duration'].sum().reset_index()
    graphData = [go.Pie(name = "", labels=pieData['Category'].values, values=pieData['Duration'].values, text=pieData['Category'].values)]
    graphJSON = json.dumps(graphData, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


def getDataTable(data, choice):
    truckdata = data
    if (choice != 'all'):
        truckdata = data[data['Category'] == choice]
    truckdata = truckdata.drop(truckdata.iloc[:, 0:2], axis = 1)
    # truckdata = truckdata.sort_values(by='amount', ascending=False)
    truckdata = truckdata.reset_index(drop=True)
    truckdata['Duration'] = truckdata['Duration'].astype(str) + ' min'
    trucktable = truckdata.to_html(classes='trucktable')
    return trucktable


@app.route('/piechange', methods=['GET', 'POST'])
def changePie():
    data = session['userdata']
    choice = request.args['truck']
    graphJSON = getPieGraph(data, choice)
    return graphJSON


@app.route('/tablechange', methods=['GET', 'POST'])
def changeTable():
    data = session['userdata']
    truck = request.args['truck']
    graphJSON = getDataTable(data, truck)
    return graphJSON


@app.route('/addData')
def addData():
    try:
        name = (request.args.get('name', ''))
        activity = (request.args.get('activity', ''))
        category = (request.args.get('category', ''))
        start = (request.args.get('start', '12:00'))
        duration = (request.args.get('duration', 0))
        olddata = pd.read_csv('static/data/TychonUsers.csv')
        newdata = pd.DataFrame({"Name":[name], "Activity":[activity], "Category":[category], "Start":[start], "Duration":[duration]})
        fulldata = olddata.append(newdata, ignore_index = True)
        fulldata.to_csv('static/data/TychonUsers.csv', index=False)
        return {'Message': 'Success'}
    except Exception:
        return {'Message': 'Failure'}


if __name__ == '__main__':
    # write comments for everything later
    app.debug = True
    app.run()