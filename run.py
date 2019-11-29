# encoding: utf-8
from app.create_app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='192.168.81.148', debug=True)
