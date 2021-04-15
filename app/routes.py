from flask import render_template
from app import app
from flask import request
import json

names_colour, names_bw = [], []

with open(r'app/static/json/colour.json') as json_colour, open(r'app/static/json/bw.json') as json_bw:
    data_colour, data_bw = json.loads(json_colour.read()), json.loads(json_bw.read())
    for d in data_colour:
        names_colour.append(d['name'])
    for d in data_bw:
        names_bw.append(d['name'])


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title='Home', len_bw=len(names_bw), names_bw=names_bw,
                           len_colour=len(names_colour), names_colour=names_colour)

'''
@app.route('/posts', methods=['GET', 'POST'])
def posts():
    return render_template("posts.html", title='Posts', len_bw=len(names_bw), names_bw=names_bw,
                           len_colour=len(names_colour), names_colour=names_colour)
'''

@app.route('/bw', methods=['GET', 'POST'])
def bw():
    requested_name = request.args.get('title')
    for x in data_bw:
        if x['name'] == requested_name:
            requested = x
    directory = 'img/b-w/' + requested['title']
    filenames = []
    for n in range(1, requested['files'] + 1):
        filenames.append(requested['title'] + '-(' + str(n) + ').jpg')
    return render_template('gallery.html', prefix=requested['title'], title=requested['name'],
                           files=range(1, requested['files'] + 1), d=directory, fn=filenames,
                           len_bw=len(names_bw), names_bw=names_bw, len_colour=len(names_colour),
                           names_colour=names_colour)


@app.route("/colour", methods=['GET', 'POST'])
def colour():
    requested_name = request.args.get('title')
    for x in data_colour:
        if x['name'] == requested_name:
            requested = x
    directory = 'img/colour/' + requested['title']
    filenames = []
    for n in range(1, requested['files'] + 1):
        filenames.append(requested['title'] + '-(' + str(n) + ').jpg')
    return render_template('gallery.html', prefix=requested['title'], title=requested['name'],
                           files=range(1, requested['files'] + 1), d=directory, fn=filenames, len_bw=len(names_bw),
                           names_bw=names_bw, len_colour=len(names_colour), names_colour=names_colour)
