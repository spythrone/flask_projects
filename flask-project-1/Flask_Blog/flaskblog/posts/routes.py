from flask import render_template, url_for, redirect, flash, request, Blueprint, abort
from flaskblog import db
from flaskblog.posts.forms import CreateNewPost
from flaskblog.posts.models import Posts
from flask_login import current_user, login_required

posts = Blueprint('posts', __name__,
                  template_folder='templates', url_prefix='/post')


@posts.route('/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = CreateNewPost()
    print(current_user.id)
    if form.validate_on_submit():
        post = Posts(title=form.title.data,
                     content=form.content.data, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash(f'New Post Added', 'success')
        return redirect(url_for('main.home'))
    return render_template('posts/new_post.html', title='New Post', form=form, legend='New Post')


@posts.route('/<int:post_id>')
def post(post_id):
    post = Posts.query.get_or_404(post_id)
    return render_template('posts/post.html', title='Post', post=post)


@posts.route('/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Posts.query.get_or_404(post_id)
    if post.user != current_user:
        abort(403)
    form = CreateNewPost()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('posts/new_post.html', title='Post', form=form, legend='Updata Post')


@posts.route('/<int:post_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_post(post_id):
    post = Posts.query.get_or_404(post_id)
    if post.user != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash(f'Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))
