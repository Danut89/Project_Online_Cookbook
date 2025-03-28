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

from functools import wraps
from flask import abort

from datetime import datetime, timedelta
from sqlalchemy import func
from urllib.parse import urlparse

import cloudinary.uploader

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

    # ✅ Icon map (category name → Font Awesome icon class)
    icon_map = {
        "Breakfast": "fa-sun",
        "Dessert": "fa-ice-cream",
        "Dinner": "fa-drumstick-bite",
        "Lunch": "fa-utensils",
        "Snack": "fa-cookie",
        "Vegan": "fa-leaf",
        "Vegetarian": "fa-carrot"
    }

    return render_template(
        'home.html',
        recipes=recipes_paginated,
        featured_recipes=all_recipes,
        categories=categories,
        icon_map=icon_map
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
    form.categories.choices = [(c.id, c.name) for c in Category.query.all()] #Ensure categories are available

    next_url = request.args.get('next') or url_for('main.home')

    if form.validate_on_submit():
        image_url = None

        if form.image.data:
            # Upload to Cloudinary
            upload_result = cloudinary.uploader.upload(form.image.data)
            image_url = upload_result['secure_url']

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
        return redirect(next_url)  # Redirect back to where user came from

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
    form.categories.choices = [(c.id, c.name) for c in Category.query.all()] # Ensure categories are available

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
             # Upload to Cloudinary
            upload_result = cloudinary.uploader.upload(form.image.data)
            recipe.image_url = upload_result['secure_url']

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

    if current_user.id != recipe.user_id and not current_user.is_admin:
        flash("You don't have permission to delete this recipe.", "danger")
        return redirect(url_for('main.home'))

    db.session.delete(recipe)
    db.session.commit()
    flash("Recipe deleted successfully.", "success")

    # Handle redirect safely
    next_url = request.form.get('next') or request.referrer
    if next_url:
        # If coming from the same page (view_recipe), avoid redirecting to deleted content
        parsed_url = urlparse(next_url)
        if f'/recipe/{recipe_id}' in parsed_url.path:
            return redirect(url_for('main.home'))
        return redirect(next_url)

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

    if comment.user_id != current_user.id and not current_user.is_admin:
        flash("You are not authorized to delete this comment.", "error")
        return redirect(url_for('main.view_recipe', recipe_id=comment.recipe_id))

    db.session.delete(comment)
    db.session.commit()
    flash("Comment deleted.", "info")
    # Redirect depending on where delete came from
    if request.referrer and '/admin' in request.referrer:
        return redirect(url_for('main.admin_dashboard'))
    
    return redirect(url_for('main.view_recipe', recipe_id=comment.recipe_id))

# 🔍 View all categories
@main.route('/browse')
def browse_recipes():
    query = request.args.get('q', '')
    category = request.args.get('category', '')
    difficulty = request.args.get('difficulty', '')
    sort_by = request.args.get('sort', 'newest')
    page = request.args.get('page', 1, type=int)

    recipes_query = Recipe.query

    if query:
        recipes_query = recipes_query.filter(
            or_(
                Recipe.title.ilike(f"%{query}%"),
                Recipe.cuisine.ilike(f"%{query}%"),
                Recipe.description.ilike(f"%{query}%")
            )
        )

    if category:
        recipes_query = recipes_query.join(Recipe.categories).filter(Category.name == category)

    if difficulty:
        recipes_query = recipes_query.filter(Recipe.difficulty == difficulty)

    # ✅ Sorting logic
    if sort_by == 'oldest':
        recipes_query = recipes_query.order_by(Recipe.created_at.asc())
    elif sort_by == 'title':
        recipes_query = recipes_query.order_by(Recipe.title.asc())
    elif sort_by == 'prep_time_asc':
        recipes_query = recipes_query.order_by(Recipe.prep_time.asc())
    elif sort_by == 'prep_time_desc':
        recipes_query = recipes_query.order_by(Recipe.prep_time.desc())
    else:
        recipes_query = recipes_query.order_by(Recipe.created_at.desc())

    recipes_paginated = recipes_query.paginate(page=page, per_page=6)

    categories = Category.query.order_by(Category.name).all()
    difficulties = ['Easy', 'Medium', 'Hard']

    return render_template(
        'browse_recipes.html',
        recipes=recipes_paginated,
        categories=categories,
        selected_category=category,
        selected_difficulty=difficulty,
        query=query,
        sort=sort_by,
        difficulties=difficulties
    )



# 📂 View all recipes in a specific category
@main.route('/category/<string:category_name>')
def recipes_by_category(category_name):
    category = Category.query.filter_by(name=category_name).first_or_404()
    recipes = category.recipes.order_by(Recipe.created_at.desc()).all()
    featured_recipes = recipes[:3]  # Get top 3 from this category
    categories = Category.query.order_by(Category.name).all()

    return render_template(
    'browse_recipes.html',
    recipes=recipes,
    selected_category=category.name
)

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
    # ✅ Fetch full lists (for count display)
    users = User.query.all()
    recipes = Recipe.query.all()

    # ✅ Fetch limited for recent previews
    recent_users = User.query.order_by(User.id.desc()).limit(3).all()
    recent_recipes = Recipe.query.order_by(Recipe.created_at.desc()).limit(3).all()

    comments = Comment.query.all()
    total_likes = Like.query.count()

    # 🕒 Time-based analytics
    today = datetime.utcnow()
    start_of_week = today - timedelta(days=today.weekday())
    start_of_month = today.replace(day=1)

    recipes_this_week = Recipe.query.filter(Recipe.created_at >= start_of_week).count()
    recipes_this_month = Recipe.query.filter(Recipe.created_at >= start_of_month).count()

    # ❤️ Most liked recipe
    most_liked_recipe = (
        db.session.query(Recipe)
        .outerjoin(Recipe.likes)
        .group_by(Recipe.id)
        .order_by(func.count(Recipe.likes).desc())
        .first()
    )

    return render_template('admin/dashboard.html',
                           users=users,
                           recipes=recipes,
                           recent_users=recent_users,
                           recent_recipes=recent_recipes,
                           comments=comments,
                           total_likes=total_likes,
                           recipes_this_week=recipes_this_week,
                           recipes_this_month=recipes_this_month,
                           most_liked_recipe=most_liked_recipe)



@main.route('/admin/users')
@admin_required
def manage_users():
    if not current_user.is_admin:
        abort(403)

    users = User.query.order_by(User.id).all()
    return render_template('admin/manage_users.html', users=users)

@main.route('/admin/user/<int:user_id>/promote', methods=['POST'])
@login_required
def promote_user(user_id):
    if not current_user.is_admin:
        abort(403)

    user = User.query.get_or_404(user_id)
    user.is_admin = True
    db.session.commit()
    flash(f'{user.username} has been promoted to admin.', 'success')
    return redirect(url_for('main.manage_users'))

@main.route('/admin/user/<int:user_id>/demote', methods=['POST'])
@login_required
def demote_user(user_id):
    if not current_user.is_admin or current_user.id == user_id:
        abort(403)

    user = User.query.get_or_404(user_id)
    user.is_admin = False
    db.session.commit()
    flash(f'{user.username} has been demoted from admin.', 'info')
    if request.referrer and '/admin' in request.referrer:
        return redirect(url_for('main.admin_dashboard'))
    return redirect(url_for('main.manage_users'))

@main.route('/admin/user/<int:user_id>/delete', methods=['POST'])
@login_required
def delete_user(user_id):
    if not current_user.is_admin or current_user.id == user_id:
        abort(403)

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash(f'User {user.username} has been deleted.', 'danger')
    return redirect(url_for('main.manage_users'))

@main.route('/admin/comment/<int:comment_id>/delete', methods=['POST'])
@admin_required
def admin_delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    flash('Comment deleted by admin.', 'warning')

    return redirect(url_for('main.admin_dashboard'))


@main.route('/admin/recipes')
@admin_required
def manage_recipes():
    if not current_user.is_admin:
        abort(403)

    page = request.args.get('page', 1, type=int)
    per_page = 10
    recipes = Recipe.query.order_by(Recipe.created_at.desc()).paginate(page=page, per_page=per_page)
    return render_template('admin/manage_recipes.html', recipes=recipes)

@main.route('/recipes')
def all_recipes():
    page = request.args.get('page', 1, type=int)
    recipes = Recipe.query.order_by(Recipe.created_at.desc()).paginate(page=page, per_page=6)
    return render_template('all_recipes.html', recipes=recipes)

