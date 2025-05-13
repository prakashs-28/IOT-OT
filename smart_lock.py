from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return '''
        <form method="POST" action="/unlock">
            Username: <input name="username"><br>
            PIN: <input name="pin"><br>
            <input type="submit" value="Unlock">
        </form>
    '''

@app.route('/unlock', methods=['POST'])
def unlock():
    username = request.form.get('username')
    pin = request.form.get('pin')
    if username == 'admin' and pin == '2468':
        return "Unlocked!"
    return "Access Denied"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
