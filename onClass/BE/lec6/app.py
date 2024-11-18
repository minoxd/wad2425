from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'lmao'  # usually hide in env setup


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
        message = request.form['message']
        print(f'Name: {name}, Message: {message}')
        flash(f'Thank you {name}, your message has been received!')
        return redirect(url_for('home'))
    return render_template(contact.html)


@app.route('/user/<name>')
def user(name):
    return f'Hello, {name}'


if __name__ == '__main__':
    app.run(debug=True)
