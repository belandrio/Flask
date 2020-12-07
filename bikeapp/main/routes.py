
from flask import render_template, request, Blueprint, redirect, url_for
from flask_login import login_required
from bikeapp.models import Post 
from bikeapp.main.forms import SearchForm
from bikeapp.search import query_index

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/posts")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')
    

@main.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    form = SearchForm()
    if not form.validate():
        return redirect(url_for('main.home'))
    page = request.args.get('page', 1, type=int)
    postIds, total = query_index("posts", form.q.data, page, 5)
    posts = []
    for post in postIds:
        posts.append(Post.query.get(post))
    return render_template('search.html', title='Search', posts=posts)