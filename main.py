from flask import Blueprint, render_template, current_app
from threading import Thread
import random
from time import sleep
from . import turbo

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/page2')
def page2():
    return render_template('page2.html')


@main.context_processor
def inject_load():
    load = [int(random.random() * 100) / 100 for _ in range(3)]
    return {'load1': load[0], 'load5': load[1], 'load15': load[2]}

@main.before_app_first_request
def before_first_request():
    Thread(target=update_load,args=(current_app._get_current_object(),)).start()


def update_load(app):
    with app.app_context():
        while True:
            sleep(0.2)
            turbo.push(turbo.replace(render_template('loadavg.html'), 'load'))
