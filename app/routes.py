import os
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from sqlalchemy import or_

from app import db
from app.models import Recipe, User
from app.forms import RecipeForm
from app.utils import save_uploaded_image  # ✅ Image utility

# Define the blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():
    query = request.args.get('q', '')
    difficulty = request.args.get('difficulty', '')
    cuisine = request.args.get('cuisine', '')
    page = request.args.get('page', 1, type=int)

    recipes_query = Recipe.query.join(User)

    # Search
    if query:
        recipes_query = recipes_query.filter(
            or_(
                Recipe.title.ilike(f"%{query}%"),
                Recipe.cuisine.ilike(f"%{query}%"),
                Recipe.difficulty.ilike(f"%{query}%")
            )
        )

    # Filter by difficulty
    if difficulty:
        recipes_query = recipes_query.filter(Recipe.difficulty == difficulty)

    # Filter by cuisine
    if cuisine:
        recipes_query = recipes_query.filter(Recipe.cuisine.ilike(f"%{cuisine}%"))

    # Paginate
    recipes = recipes_query.order_by(Recipe.created_at.desc()).paginate(page=page, per_page=6)

    return render_template('home.html', recipes=recipes)

@main.route('/recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template('view_recipe.html', recipe=recipe)

@main.route('/add_recipe', methods=['GET', 'POST'])
@login_required
def add_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        image_url = save_uploaded_image(form.image.data)

        recipe = Recipe(
            title=form.title.data,
            description=form.description.data,
            ingredients=form.ingredients.data,
            steps=form.steps.data,
            cuisine=form.cuisine.data,
            prep_time=form.prep_time.data,
            difficulty=form.difficulty.data,
            image_url=image_url,
            user_id=current_user.id
        )
        db.session.add(recipe)
        db.session.commit()
        flash('Recipe added successfully!', 'success')
        return redirect(url_for('main.home'))

    return render_template('add_recipe.html', form=form)

@main.route('/recipe/<int:recipe_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)

    if recipe.user_id != current_user.id:
        flash("You don't have permission to edit this recipe.", "danger")
        return redirect(url_for('main.home'))

    form = RecipeForm(obj=recipe)
    if form.validate_on_submit():
        recipe.title = form.title.data
        recipe.description = form.description.data
        recipe.ingredients = form.ingredients.data
        recipe.steps = form.steps.data
        recipe.cuisine = form.cuisine.data
        recipe.prep_time = form.prep_time.data
        recipe.difficulty = form.difficulty.data

        if form.image.data:
            recipe.image_url = save_uploaded_image(form.image.data)

        db.session.commit()
        flash('Recipe updated successfully!', 'success')
        return redirect(url_for('main.view_recipe', recipe_id=recipe.id))

    return render_template('edit_recipe.html', form=form, recipe=recipe)

@main.route('/recipe/<int:recipe_id>/delete', methods=['POST'])
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)

    if recipe.user_id != current_user.id:
        flash("You don't have permission to delete this recipe.", "danger")
        return redirect(url_for('main.home'))

    db.session.delete(recipe)
    db.session.commit()
    flash('Recipe deleted successfully!', 'success')
    return redirect(url_for('main.home'))
