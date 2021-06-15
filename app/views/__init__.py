from flask import Flask


def init_app(app: Flask):
    from .profile_view import bp as bp_profile

    app.register_blueprint(bp_profile)
