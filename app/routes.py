#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required

import program.users as us
from app import app, db
from app.forms import LoginForm, SignUpForm, SettingsForm
from app.models import User, Event
from program.exceptions import FlashException

@app.route("/")
@app.route("/index/")
def index():
    dct = {"title": "Meet Me"}
    return render_template("index.html", **dct)

@app.route("/login/", methods=["GET", "POST"])
def login():
    dct = {"title": "Login"}
    if current_user.is_authenticated:
        # if you're accidentally routed to the login page
        return redirect(url_for("index"))
    form = LoginForm()
    dct["form"] = form
    if form.validate_on_submit():
        try:
            us.login_user(
                form.username.data, 
                form.password.data, 
                form.remember_me.data)
            return redirect(url_for("index"))
        except FlashException as e:
            flash(e.message, category=e.category)
    return render_template("login.html", **dct)

@app.route("/signup/", methods=["GET", "POST"])
def signup():
    dct = {"title": "Sign Up"}
    if current_user.is_authenticated:
        # if you're accidentally routed to the sign up page
        return redirect(url_for("index"))
    form = SignUpForm()
    dct["form"] = form
    if form.validate_on_submit():
        us.register_user(
            form.username.data, 
            form.email.data, 
            form.first_name.data, 
            form.last_name.data, 
            form.password.data)
        return redirect(url_for("login"))
    return render_template("sign_up.html", **dct)

@app.route("/logout/")
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/settings/", methods=["GET", "POST"])
@login_required
def settings():
    dct = {
        "title": current_user.first_name.capitalize() + "'s Settings",
        "current_user": current_user
    }
    form = SettingsForm()
    dct["form"] = form
    return render_template("settings.html", **dct)
