from flask import Flask, render_template, request, redirect, url_for, flash
import random
import os
from pathlib import Path

# Local json utilities (created alongside this file)
from flask import current_app

try:
	# prefer package import if the app is run as a package
	from . import json_utils as ju
except Exception:
	# fallback to sibling module
	import json_utils as ju

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET', 'dev-secret-change-me')

# flashcards.json moved to repository root — point DATA_FILE to the new location
DATA_FILE = Path(__file__).parent.parent / 'flashcards.json'


@app.route('/')
def index():
	data = ju.load(DATA_FILE)
	cards = data.get('cards', [])
	return render_template('index.html', cards=cards)


@app.route('/cards/new', methods=['GET', 'POST'])
def create_card():
	if request.method == 'POST':
		front = request.form.get('front', '').strip()
		back = request.form.get('back', '').strip()
		if not front or not back:
			flash('Front and back are required.', 'danger')
			return render_template('create.html', front=front, back=back)
		data = ju.load(DATA_FILE)
		cards = data.setdefault('cards', [])
		next_id = max((c['id'] for c in cards), default=0) + 1
		card = {'id': next_id, 'front': front, 'back': back}
		cards.append(card)
		ju.save(DATA_FILE, data)
		flash('Card created.', 'success')
		return redirect(url_for('index'))
	return render_template('create.html')


@app.route('/cards/<int:card_id>')
def view_card(card_id):
	data = ju.load(DATA_FILE)
	card = next((c for c in data.get('cards', []) if c['id'] == card_id), None)
	if not card:
		flash('Card not found.', 'warning')
		return redirect(url_for('index'))
	return render_template('view.html', card=card)


@app.route('/cards/<int:card_id>/edit', methods=['GET', 'POST'])
def edit_card(card_id):
	data = ju.load(DATA_FILE)
	cards = data.get('cards', [])
	card = next((c for c in cards if c['id'] == card_id), None)
	if not card:
		flash('Card not found.', 'warning')
		return redirect(url_for('index'))
	if request.method == 'POST':
		front = request.form.get('front', '').strip()
		back = request.form.get('back', '').strip()
		if not front or not back:
			flash('Front and back are required.', 'danger')
			return render_template('edit.html', card=card)
		card['front'] = front
		card['back'] = back
		ju.save(DATA_FILE, data)
		flash('Card updated.', 'success')
		return redirect(url_for('view_card', card_id=card_id))
	return render_template('edit.html', card=card)


@app.route('/cards/<int:card_id>/delete', methods=['POST'])
def delete_card(card_id):
	data = ju.load(DATA_FILE)
	cards = data.get('cards', [])
	new_cards = [c for c in cards if c['id'] != card_id]
	data['cards'] = new_cards
	ju.save(DATA_FILE, data)
	flash('Card deleted.', 'info')
	return redirect(url_for('index'))


@app.route('/quiz')
def quiz():
	data = ju.load(DATA_FILE)
	cards = data.get('cards', [])
	if not cards:
		flash('No cards available. Create some first.', 'warning')
		return redirect(url_for('index'))
	card = random.choice(cards)
	return redirect(url_for('quiz_card', card_id=card['id']))


@app.route('/quiz/<int:card_id>')
def quiz_card(card_id):
	data = ju.load(DATA_FILE)
	card = next((c for c in data.get('cards', []) if c['id'] == card_id), None)
	if not card:
		flash('Card not found.', 'warning')
		return redirect(url_for('index'))
	return render_template('quiz.html', card=card)


if __name__ == '__main__':
	app.run(debug=True)

