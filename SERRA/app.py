from flask import Flask, render_template, request, url_for

app=Flask(__name__)
app.config["DEBUG"]= True

@app.route("/")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route('/registrazione', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        cognome = request.form['cognome']
        username = request.form['username']
        password = request.form['password']
        return render_template("login.html")
    return render_template('registrazione.html')


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port= 5500
    )