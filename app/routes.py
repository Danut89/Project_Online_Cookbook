from flask import request
from app.models import User  # Already imported Recipe, but need User too
import os
from flask import current_app
from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import Recipe  
from app.forms import RecipeForm  
from app.utils import save_uploaded_image  # ✅ Import the utility function

# Define the blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():
    query = request.args.get('q')  # Get the search query from URL
    page = request.args.get('page', 1, type=int)

    if query:
        # Case-insensitive search using ilike()
        recipes = Recipe.query.join(User).filter(
            (Recipe.title.ilike(f"%{query}%")) |
            (Recipe.cuisine.ilike(f"%{query}%")) |
            (Recipe.difficulty.ilike(f"%{query}%"))
        ).paginate(page=page, per_page=6)
    else:
        recipes = Recipe.query.join(User).paginate(page=page, per_page=6)

    return render_template('home.html', recipes=recipes)


@main.route('/recipe/<int:recipe_id>')  # ✅ FIXED: Added missing route decorator
def view_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)  # Get recipe or return 404
    return render_template('view_recipe.html', recipe=recipe)

@main.route('/add_recipe', methods=['GET', 'POST'])
@login_required
def add_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        # Use the utility function to save the image
        image_url = save_uploaded_image(form.image.data)

        recipe = Recipe(
            title=form.title.data,
            description=form.description.data,
            ingredients=form.ingredients.data,
            steps=form.steps.data,
            cuisine=form.cuisine.data,
            prep_time=form.prep_time.data,
            difficulty=form.difficulty.data,
            image_url=image_url,  # ✅ Use the returned image URL
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

    # Ensure only the owner can edit
    if recipe.user_id != current_user.id:
        flash("You don't have permission to edit this recipe.", "danger")
        return redirect(url_for('main.home'))

    form = RecipeForm(obj=recipe)  # Pre-fill form with existing data
    if form.validate_on_submit():
        recipe.title = form.title.data
        recipe.description = form.description.data
        recipe.ingredients = form.ingredients.data
        recipe.steps = form.steps.data
        recipe.cuisine = form.cuisine.data
        recipe.prep_time = form.prep_time.data
        recipe.difficulty = form.difficulty.data

        # Use the utility function to save the image if a new one is uploaded
        if form.image.data:
            recipe.image_url = save_uploaded_image(form.image.data)

        db.session.commit()
        flash('Recipe updated successfully!', 'success')
        return redirect(url_for('main.view_recipe', recipe_id=recipe.id))  # ✅ Redirect now works properly

    return render_template('edit_recipe.html', form=form, recipe=recipe)

@main.route('/recipe/<int:recipe_id>/delete', methods=['POST'])
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)

    # Ensure only the owner can delete
    if recipe.user_id != current_user.id:
        flash("You don't have permission to delete this recipe.", "danger")
        return redirect(url_for('main.home'))

    db.session.delete(recipe)
    db.session.commit()
    flash('Recipe deleted successfully!', 'success')

    return redirect(url_for('main.home'))  # ✅ FIXED: Added return statement


