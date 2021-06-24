from flask import Blueprint, render_template, request, redirect, flash, url_for, jsonify
from board_game_site.forms import AtlasInfoForm 

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/apisearchrequest', methods = ['GET'])
def getData():
    form = AtlasInfoForm()
    name = form.name.data

    data = requests.get(f)