from flaskapp import app, render_template, request

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.form['data']
    return render_template('home.html')