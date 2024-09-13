from flask import Flask, render_template, request, redirect, url_for

app = Flask(_name_)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# About route
@app.route('/about')
def about():
    return render_template('about.html')

# Projects route
@app.route('/projects')
def projects():
    return render_template('projects.html')

# Contact route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Here you can handle the contact form data, e.g., send an email or save to a database
        print(f"Received message from {name} ({email}): {message}")
        return redirect(url_for('contact'))
    return render_template('contact.html')

if _name_ == '_main_':
    app.run(debug=True)