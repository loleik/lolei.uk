import os 
import frontmatter
import markdown
from datetime import datetime

from flask import render_template, request, send_from_directory, redirect, url_for, abort
from app import app
import json

names_colour, names_bw = [], []

POSTS_DIR = os.path.join(os.path.dirname(__file__), "posts")

def get_posts():
    posts = []
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".md"):
            with open(os.path.join(POSTS_DIR, filename), "r", encoding="utf-8") as f:
                post = frontmatter.load(f)
                try:
                    # Correct date format for "30/04/2025"
                    post['parsed_date'] = datetime.strptime(post['date'], "%d/%m/%Y")
                except (KeyError, ValueError) as e:
                    print(f"Error parsing date in {filename}: {e}")
                    post['parsed_date'] = datetime.min
                posts.append(post)
    
    return sorted(posts, key=lambda p: p['parsed_date'], reverse=True)

def get_post_by_slug(slug):
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".md"):
            with open(os.path.join(POSTS_DIR, filename), "r", encoding="utf-8") as f:
                post = frontmatter.load(f)
                if post.get('slug') == slug:
                    post['html'] = markdown.markdown(post.content)
                    return post 
    abort(404)

with open(r'app/json/colour.json') as json_colour, open(r'app/json/bw.json') as json_bw:
    data_colour, data_bw = json.loads(json_colour.read()), json.loads(json_bw.read())
    for d in data_colour:
        names_colour.append(d['name'])
    for d in data_bw:
        names_bw.append(d['name'])


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template(
        'index.html', 
        title='Home', 
    )


@app.route('/rust-test', methods=['GET', 'POST'])
def rust_test():
    return render_template(
        'rust_test.html', 
        title='RUST TEST ZONE', 
    )


@app.route('/changelog', methods=['GET', 'POST'])
def changelog():
    with open("app/json/changelog.json") as json_clog:
        clog = json.load(json_clog)

    return render_template(
        "changelog.html", 
        title='Changelog', 
        clog=clog
    )


@app.route('/opad', methods=['GET', 'POST'])
def opad():
    return render_template(
        'opad.html', 
        title='One Photo A Day', 
    )

@app.route("/photos-archive", methods=['GET', 'POST'])
def photos_archive_main():
    return render_template(
        "photos_archive.html", 
        title='Photo Archive', 
        len_bw=len(names_bw), 
        names_bw=names_bw,
        len_colour=len(names_colour), 
        names_colour=names_colour
    )

@app.route('/photos-archive/<type>/<title>', methods=['GET', 'POST'])
def photos_archive_arm(type, title):
    if type == "colour":
        for x in data_colour:
            if x['name'] == title:
                requested = x
        directory = 'img/colour/' + requested['title']
        filenames = []
        for n in range(1, requested['files'] + 1):
            filenames.append(requested['title'] + '-(' + str(n) + ').jpg')
        return render_template(
            'gallery.html', 
            prefix=requested['title'], 
            title=requested['name'],
            files=range(1, requested['files'] + 1), 
            d=directory, 
            fn=filenames,
        )

    elif type == "bw":
        for x in data_bw:
            if x['name'] == title:
                requested = x
        directory = 'img/b-w/' + requested['title']
        filenames = []
        for n in range(1, requested['files'] + 1):
            filenames.append(requested['title'] + '-(' + str(n) + ').jpg')
        return render_template(
            'gallery.html', 
            prefix=requested['title'], 
            title=requested['name'],
            files=range(1, requested['files'] + 1), 
            d=directory, 
            fn=filenames,
        )


@app.route("/posts")
def posts():
    posts = get_posts()
    return render_template(
        "posts.html", 
        posts=posts,
        title='Posts', 
    )

@app.route("/posts/<slug>")
def show_post(slug):
    post = get_post_by_slug(slug)
    return render_template(
        "post.html", 
        post=post,
        title=post['title'], 
    )

@app.route("/photos/<month_key>")
def show_month(month_key):
    try:
        with open(f"app/json/opad/{month_key}.json", encoding="utf-8") as f:
            posts = json.load(f)
    except FileNotFoundError:
        abort(404)

    return render_template(
        "photos.html", 
        posts=posts, 
        month=month_key,
    )


@app.route("/ahz7n8t3j.txt")
def serve_txt():
    return send_from_directory("static", "ahz7n8t3j.txt")
