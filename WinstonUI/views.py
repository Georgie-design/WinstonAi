from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import User
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        pass
 

    first_name = current_user.first_name
    return render_template("home.html", user=current_user, name=first_name)


