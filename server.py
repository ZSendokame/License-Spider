from flask import Flask, request

app = Flask(__name__)


@app.get('/')
def root():
    license_key = request.args.get('license')
    username = request.args.get('username')

    with open('licenses.txt', 'a') as license_dump:
        license_dump.write(f'{username}:{license_key}\n')

    return request.args.get('license')


app.run()
