from operator import pos
from flask import Blueprint, request, render_template, redirect, jsonify
from ipdb import set_trace
from app.services.helpers import get_profile
from app.models.profile_model import Profile
from app import db


bp = Blueprint("bp_profile_route", __name__)

@bp.route("/api", methods=["GET"])
def list_profiles():
    profiles: list = Profile.query.all()

    if len(profiles) > 0:
        return render_template("list_profile.html", profiles=profiles)
    else:
        return render_template("no_profile.html")

@bp.route("/", methods=["GET"])
def home():
    return render_template("home.html")


@bp.route("/api/posts", methods=["GET"])
def post_profile_route():
    return render_template("create_profile.html")

@bp.route("/api/posts", methods=["POST"])
def post_profile():
    data = request.form

    if data: 
        try:
            chars : list = get_profile(data)           
            db.session.add_all([Profile(**char) for char in chars])
            db.session.commit()

            return redirect("/api")

        except KeyError as e:
            return e.args

@bp.route("/api/posts/<post_id>", methods=["GET"])
def filter_profile(post_id):
    data : list =  Profile.query.get(post_id)
    
    if post_id:
        if data:
            return render_template("filter_profile.html", filter_profile=data)
        else:
            return render_template("page_not_found.html")


