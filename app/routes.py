import os
from flask import current_app
from werkzeug.utils import secure_filename
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

@main.route('/recipe/<int:recipe_id>')  # ✅ FIXED: Added missing route decorator
def view_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)  # Get recipe or return 404
    return render_template('view_recipe.html', recipe=recipe)

@main.route('/add_recipe', methods=['GET', 'POST'])
@login_required
def add_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        image_filename = None
        if form.image.data:
            image_file = form.image.data
            image_filename = secure_filename(image_file.filename)
            image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], image_filename)
            os.makedirs(os.path.dirname(image_path), exist_ok=True)  # Ensure the folder exists
            image_file.save(image_path)  # Save the image

        recipe = Recipe(
            title=form.title.data,
            description=form.description.data,
            ingredients=form.ingredients.data,
            steps=form.steps.data,
            cuisine=form.cuisine.data,
            prep_time=form.prep_time.data,
            difficulty=form.difficulty.data,
            image_url=f"/static/uploads/{image_filename}" if image_filename else None,
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

        # Handle image upload
        if form.image.data:
            image_file = form.image.data
            image_filename = secure_filename(image_file.filename)
            image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], image_filename)
            os.makedirs(os.path.dirname(image_path), exist_ok=True)  # Ensure the folder exists
            image_file.save(image_path)  # Save the image
            recipe.image_url = f"/static/uploads/{image_filename}"  # Update the image URL

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


