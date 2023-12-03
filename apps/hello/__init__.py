from flask import Blueprint, render_template, redirect, url_for, request


hello_bp = Blueprint("hello_bp", __name__, url_prefix="", template_folder="templates")


@hello_bp.route("/hello")
@hello_bp.route("/hello/<name>")
def default(name=None):
    return render_template("hello/index.html", name=name)

@hello_bp.route("/sayhello", methods=['GET','POST'])
def say_hello():
    if request.method=="POST":
        return redirect(url_for('hello_bp.default', name=request.form['username']))
    else:
        return redirect(url_for('hello_bp.default', name=request.args['name']))

    
