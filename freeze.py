from flask_frozen import Freezer
from application import app

freezer = Freezer(app)

if __name__ == '__main__':
    print(freezer.freeze())
    freezer.freeze()
