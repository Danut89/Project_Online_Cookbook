from flask import Blueprint, render_template

# Define the blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')  # Ensure 'home.html' exists in templates

# Ensure this file has no other import issues
