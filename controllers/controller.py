from flask import render_template, request, redirect
from app import app
from models.events_list import events_list, add_new_event
from models.event import Event

@app.route('/events')
def events():
    return render_template('index.html', title = "Home", events_list = events_list)

@app.route('/events', methods=['POST'])
def add_event():
    name = request.form['name']
    date = request.form['date']
    guests = request.form['guests']
    room = request.form['room']
    description = request.form['description']
    recurring = request.form['recurring']
    print (request.form['recurring'])
    new_event = Event(str(date), name, guests, room, description, recurring)
    add_new_event(new_event)
    return redirect('/events')