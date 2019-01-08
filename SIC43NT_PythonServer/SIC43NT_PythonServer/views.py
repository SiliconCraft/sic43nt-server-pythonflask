"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import request
from SIC43NT_PythonServer import app
from SIC43NT_PythonServer.calculation import Calculate

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    calculate = Calculate()

    if request.args.get('d') != None:
        calculate.get_updated_data(request.args.get('d'))

    return render_template(
        'index.html',
        title = 'SIC43NT Demonstration',
        uid = calculate.uid,
        key = calculate.key,
        flag_tamper = calculate.flag_tamper,
        flag_tamper_from_server = calculate.flag_tamper_from_server,
        flag_tamper_decision = calculate.flag_tamper_decision,
        time_stamp_int = calculate.time_stamp_int,
        time_stamp_from_server = calculate.time_stamp_from_server,
        time_stamp_decision = calculate.time_stamp_decision,
        rolling_code = calculate.rolling_code,
        rolling_code_from_server = calculate.rolling_code_from_server,
        rolling_code_decision = calculate.rolling_code_decision,
        )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
