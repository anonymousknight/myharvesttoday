from flask import Flask, redirect, url_for, request, render_template, copy_current_request_context
from flask_mail import Mail, Message
import threading

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'myharvestindia@gmail.com'
app.config['MAIL_PASSWORD'] = 'myharvest'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/')
def hello_world():
    return "myharvest_r&d"


@app.route('/task1', methods=['POST'])
def signup():
    if request.method == 'POST':
        print('mailing!')
        name, phone, username = request.form['name'], request.form['phone'], request.form['username']
        msg = Message('Hello', sender='myharvestindia@gmail.com',
                      recipients=['archustalin@gmail.com'])
        msg.body = "NAME: {}, PHONE: {}, EMAIL: {}".format(
            name, phone, username)

        @copy_current_request_context
        def mail_sender(message):
            mail.send(message)
        t = threading.Thread(target=mail_sender, args=((msg,)))
        t.start()
    return render_template("thank.html", name=name)


@app.route('/task2', methods=['POST'])
def pack():
    if request.method == 'POST':
        name, phone, email, package = request.form['name'], request.form[
            'phone'], request.form['email'], request.form['package']
        msg = Message('Hello', sender='myharvestindia@gmail.com',
                      recipients=['archustalin@gmail.com'])
        msg.body = "NAME: {}, PHONE: {}, EMAIL: {}, PACKAGE: {}".format(
            name, phone, email, package)
        @copy_current_request_context
        def mail_sender(message):
            mail.send(message)
        t = threading.Thread(target=mail_sender, args=((msg,)))
        t.start()
        return render_template("thank.html", name=name)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True)
