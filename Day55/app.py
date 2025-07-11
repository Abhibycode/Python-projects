from flask import Flask

app = Flask(__name__)


# def make_bold(function):
#     def wrapper():
#         return "<b>" + function + "</b>"
#     return wrapper
#
# def make_emphasis(function):
#     def wrapper():
#         return "<em>" + function + "</em>"
#     return wrapper
#
# def make_underline(function):
#     def wrapper():
#         return "<u>" + function + "</u>"
#     return wrapper
#
# @app.route("/bye")
# @make_bold
# @make_underline
# @make_emphasis
# def bye():
#     return bye


class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("angela")
new_user.is_logged_in = True
create_blog_post(new_user)

if __name__ == "__app__":
    app.run(debug=True)