from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return render_template('contact_success.html', name=name)
    return render_template('contact.html')

@app.route('/api/users')
def api_users():
    users = [
        {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
        {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'},
        {'id': 3, 'name': 'Charlie', 'email': 'charlie@example.com'}
    ]
    return users

@app.route('/user/<int:user_id>')
def user_profile(user_id):
    users = {
        1: {'name': 'Alice', 'email': 'alice@example.com', 'age': 25},
        2: {'name': 'Bob', 'email': 'bob@example.com', 'age': 30},
        3: {'name': 'Charlie', 'email': 'charlie@example.com', 'age': 35}
    }
    user = users.get(user_id)
    if user:
        return render_template('user_profile.html', user=user, user_id=user_id)
    else:
        return "用户未找到", 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)