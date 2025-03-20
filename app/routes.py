from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import Recipe  
from app.forms import RecipeForm  

# Define the blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():
    recipes = Recipe.query.all()  # Fetch all recipes from the database
    return render_template('home.html', recipes=recipes)


@main.route('/add_recipe', methods=['GET', 'POST'])
@login_required
def add_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        recipe = Recipe(
            title=form.title.data,
            description=form.description.data,
            ingredients=form.ingredients.data,
            steps=form.steps.data,
            cuisine=form.cuisine.data,
            prep_time=form.prep_time.data,
            difficulty=form.difficulty.data,
            user_id=current_user.id  # Link recipe to logged-in user
        )
        db.session.add(recipe)
        db.session.commit()
        flash('Recipe added successfully!', 'success')
        return redirect(url_for('main.home'))  # Redirect to homepage after submission

    return render_template('add_recipe.html', form=form)

