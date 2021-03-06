#!/usr/bin/env python

import sys
import os
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, jsonify, redirect
from src.progress import Progress
from src.scraping_process import CrawlingThreading

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS,'templates')
    app = Flask(__name__, template_folder = template_folder )
else:
    template_folder = os.path.join(os.path.dirname(__file__),'templates')
    app = Flask(__name__, template_folder = template_folder )

Bootstrap(app)
progress = Progress()
progress.init()

@app.route('/')
def app_entrypoint():
    global progress
    try:
        progress_result = progress.read_progress()
    except Exception:
        progress_result = progress
    return render_template('index.html', progress=progress_result)

@app.route('/scrape')
def scrape_beerwulf():
    global progress

    CrawlingThreading('')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)