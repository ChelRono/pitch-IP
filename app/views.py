from flask import render_template
from app import app

# Views
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html' ,pitches=pitches)

@app.route('/pitch/<int:pitch_id>')
def pitch(pitch_id):

    '''
    View pitch page function that returns the pitch details page and its data
    '''
    return render_template('pitch.html',id = pitch_id)