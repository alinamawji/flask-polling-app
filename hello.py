from flask import Flask
app = Flask(__name__)

fake_poll_db = []

@app.route('/')
def index():
    return 'Index Page 1234'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/get_polls')
def get_polls():
    for poll in fake_poll_db:
        log(poll)
    return 'Successful'

@app.route('/upload_poll/<question>/<answer1>/<answer2>')
def upload_poll(question, answer1, answer2):
    poll = {'q': question, 'a1': answer1, 'a2': answer2}
    fake_poll_db.append(poll)
    log(fake_poll_db)
    return '404 Message Not Found'

def log(inpt):
    print('\t{}'.format(inpt))

if __name__ == '__main__':
    app.run(debug=True)