from application import app
from application import routes

# even though routes is not being used, it needs to be imported

if __name__ == '__main__':
    app.run(debug=True)
    