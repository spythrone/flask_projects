from flask import render_template, request, Blueprint
from flaskblog.posts.models import Posts
from flask_login import login_required

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
@main.route('/home')
def home():
    page = request.args.get("page", 1, type=int)
    posts = Posts.query.order_by(Posts.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('main/home.html', posts=posts)

@main.route('/about')
@login_required
def about():
    return render_template('main/about.html', title='About')