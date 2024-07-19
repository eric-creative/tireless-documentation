from tireless import app
from tireless import run

# import the routes
from pages.page import page

# register the routes
app.register_blueprint(page)

if __name__ == '__main__':
    # run() uncomment this line if you want to run the app in production mode
    run(debug=True)  # comment this line if you want to run the app in production mode

