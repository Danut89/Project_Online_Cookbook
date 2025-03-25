import os
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from sqlalchemy import or_

from app import db
from app.models import Recipe, User, Category  
from app.forms import RecipeForm
from app.utils import save_uploaded_image  
from app.models import Recipe, User, Category, Comment 
from app.forms import RecipeForm, CommentForm  
from app.models import Like

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

    # Paginate results for normal listing
    recipes_paginated = recipes_query.order_by(Recipe.created_at.desc()).paginate(page=page, per_page=6)

    # Get all for featured and random pick
    all_recipes = recipes_query.all()

    # Get all categories
    categories = Category.query.order_by(Category.name).all()

    return render_template(
        'home.html',
        recipes=recipes_paginated,
        featured_recipes=all_recipes,
        categories=categories
    )


@main.route('/recipe/<int:recipe_id>', methods=['GET', 'POST'])
def view_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)

    # Check if the user has liked this recipe
    is_liked = False
    if current_user.is_authenticated:
        is_liked = recipe.is_liked_by(current_user)

    #  Handle comments
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(
            content=form.content.data,
            user_id=current_user.id,
            recipe_id=recipe.id
        )
        db.session.add(comment)
        db.session.commit()
        flash("Comment posted successfully!", "success")
        return redirect(url_for('main.view_recipe', recipe_id=recipe.id))

    comments = Comment.query.filter_by(recipe_id=recipe.id).order_by(Comment.created_at.desc()).all()

    return render_template(
        'view_recipe.html',
        recipe=recipe,
        is_liked=is_liked,
        form=form,
        comments=comments
    )


@main.route('/add_recipe', methods=['GET', 'POST'])
@login_required
def add_recipe():
    form = RecipeForm()
    next_url = request.args.get('next') or url_for('main.home')  # Get 'next' or fallback to home

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

        selected_categories = Category.query.filter(Category.id.in_(form.categories.data)).all()
        recipe.categories.extend(selected_categories)

        db.session.add(recipe)
        db.session.commit()
        flash('Recipe added successfully!', 'success')
        return redirect(next_url)  # Redirect to 'next_url'

    return render_template('add_recipe.html', form=form, next_url=next_url)


@main.route('/recipe/<int:recipe_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)

    # Only the author can edit
    if recipe.user_id != current_user.id:
        flash("You don't have permission to edit this recipe.", "danger")
        return redirect(url_for('main.view_recipe', recipe_id=recipe.id))

    form = RecipeForm(obj=recipe)

    # Pre-select categories for GET
    if request.method == 'GET':
        form.categories.data = [c.id for c in recipe.categories]

    if form.validate_on_submit():
        # Update fields
        recipe.title = form.title.data
        recipe.description = form.description.data
        recipe.ingredients = form.ingredients.data
        recipe.steps = form.steps.data
        recipe.cuisine = form.cuisine.data
        recipe.prep_time = form.prep_time.data
        recipe.difficulty = form.difficulty.data

        # Update categories
        recipe.categories = Category.query.filter(Category.id.in_(form.categories.data)).all()

        # Save new image if uploaded
        if form.image.data:
            image_url = save_uploaded_image(form.image.data)
            recipe.image_url = image_url

        db.session.commit()
        flash('Recipe updated successfully!', 'success')
        return redirect(url_for('main.view_recipe', recipe_id=recipe.id))

    return render_template('edit_recipe.html', form=form, recipe=recipe)





    form = RecipeForm(obj=recipe)

    # ✅ Pre-fill selected categories
    if request.method == 'GET':
        form.categories.data = [c.id for c in recipe.categories]

    if form.validate_on_submit():
        recipe.title = form.title.data
        recipe.description = form.description.data
        recipe.ingredients = form.ingredients.data
        recipe.steps = form.steps.data
        recipe.cuisine = form.cuisine.data
        recipe.prep_time = form.prep_time.data
        recipe.difficulty = form.difficulty.data

        # ✅ Replace categories
        recipe.categories = Category.query.filter(Category.id.in_(form.categories.data)).all()

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

@main.route('/recipe/<int:recipe_id>/like', methods=['POST'])
@login_required
def like_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)

    existing_like = next((like for like in recipe.likes if like.user_id == current_user.id), None)

    if existing_like:
        db.session.delete(existing_like)
        flash("Removed from your favorites.", "info")
    else:
        from app.models import Like  # Import here to avoid circular imports
        new_like = Like(user_id=current_user.id, recipe_id=recipe.id)
        db.session.add(new_like)
        flash("Added to your favorites!", "success")

    db.session.commit()
    return redirect(url_for('main.view_recipe', recipe_id=recipe.id))

@main.route('/profile')
@login_required
def profile():
    # Recipes created by the user
    my_recipes = Recipe.query.filter_by(user_id=current_user.id).all()

    # Recipes the user has liked
    from app.models import Like  # ensure Like is imported
    liked_recipe_ids = [like.recipe_id for like in current_user.likes]
    liked_recipes = Recipe.query.filter(Recipe.id.in_(liked_recipe_ids)).all()

    return render_template('profile.html', my_recipes=my_recipes, liked_recipes=liked_recipes)

@main.route('/comment/<int:comment_id>/delete', methods=['POST'])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)

    if comment.user_id != current_user.id:
        flash("You are not authorized to delete this comment.", "danger")
        return redirect(url_for('main.view_recipe', recipe_id=comment.recipe_id))

    db.session.delete(comment)
    db.session.commit()
    flash("Comment deleted.", "info")
    return redirect(url_for('main.view_recipe', recipe_id=comment.recipe_id))

# 🔍 View all categories
@main.route('/categories')
def browse_categories():
    categories = Category.query.order_by(Category.name).all()
    return render_template('browse_categories.html', categories=categories)

# 📂 View all recipes in a specific category
@main.route('/category/<string:category_name>')
def recipes_by_category(category_name):
    category = Category.query.filter_by(name=category_name).first_or_404()
    recipes = category.recipes.order_by(Recipe.created_at.desc()).all()
    featured_recipes = recipes[:3]  # Get top 3 from this category
    categories = Category.query.order_by(Category.name).all()

    return render_template(
        'home.html',
        recipes=recipes,
        featured_recipes=featured_recipes,
        selected_category=category.name,
        categories=categories
    )


from functools import wraps
from flask import abort

# ✅ Admin-only access decorator
def admin_required(f):
    @wraps(f)
    @login_required
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

# ✅ Admin Dashboard route
@main.route('/admin')
@admin_required
def admin_dashboard():
    users = User.query.all()
    recipes = Recipe.query.all()
    comments = Comment.query.all()
    total_likes = Like.query.count()  # ✅ Add this line

    return render_template('admin/dashboard.html',
                           users=users,
                           recipes=recipes,
                           comments=comments,
                           total_likes=total_likes)

@main.route('/admin/users')
@admin_required
def manage_users():
    # Placeholder logic
    users = User.query.all()
    return render_template('admin/manage_users.html', users=users)

@main.route('/admin/recipes')
@admin_required
def manage_recipes():
    # Placeholder logic
    recipes = Recipe.query.all()
    return render_template('admin/manage_recipes.html', recipes=recipes)

@main.route('/recipes')
def all_recipes():
    page = request.args.get('page', 1, type=int)
    recipes = Recipe.query.order_by(Recipe.created_at.desc()).paginate(page=page, per_page=6)
    return render_template('all_recipes.html', recipes=recipes)
