from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required
from board_game_site.forms import UserCollectionUpdateForm, AtlasInfoForm
from board_game_site.models import Game, db
import requests, json, ast

site = Blueprint('site', __name__, template_folder='site_templates')

"""
"""
@site.route('/')
def home():
    return render_template('index.html')

@site.route('/account')
@login_required
def account():
    return render_template('account.html')

@site.route('/name_update')
@login_required
def name_update():
    return render_template('name_update.html')

@site.route('/upcollectionform', methods = ['GET', 'POST'])
@login_required
def upcollectionform():
    form = UserCollectionUpdateForm()
    
    if request.method == 'POST':
        name = form.name.data
        year = form.year.data
        rating = form.rating.data
        designer = form.designer.data
        genre = form.genre.data
        print(name, year, rating, designer, genre)

        game = Game(name, year, rating, designer, genre)
        db.session.add(game)
        db.session.commit()

        flash(f'You have successfully added {name} to your collection', 'collection-update')

        return redirect(url_for('site.account'))

            
    return render_template('upcollectionform.html', form = form)

@site.route('/reupcollectionform/<Dixit>', methods = ['GET', 'POST'])
@login_required
def reupcollectionform(Dixit):
    form = UserCollectionUpdateForm()
    game_to_update = Game.query.get_or_404(Dixit)
    print(game_to_update)
    if request.method == 'POST':
        game_to_update.name = request.form['name']
        game_to_update.rating = request.form['rating']
        game_to_update.year = request.form['year']
        game_to_update.designer = request.form['designer']
        game_to_update.genre = request.form['genre']
        try: 
            db.session.commit()
            flash(f'You have successfully updated your collection', 'collection-re-update')
            return redirect(url_for('site.account'))
        except: 
            flash(f'Check Your Form Input', 'collection-re-update error')
            
    return render_template('reupcollectionform.html', form = form, game_to_update = game_to_update)


@site.route('/search_form', methods = ['GET', 'POST'])
def search():
    form = AtlasInfoForm()
    if request.method == 'POST':
        name = form.name.data
        print(name)
        data = requests.get(f'https://api.boardgameatlas.com/api/search?name={name}&client_id=BWpM7fTd2i')
        print(data.json())
        name = data.json()['games'][0]['name']
        price = data.json()['games'][0]['price']
        min_players = data.json()['games'][0]['min_players']
        max_players = data.json()['games'][0]['max_players']
        description = data.json()['games'][0]['description']
        commentary = data.json()['games'][0]['commentary']
        image_url = data.json()['games'][0]['image_url']
        publisher = data.json()['games'][0]['publisher']
        rules_url = data.json()['games'][0]['rules_url']
        year_published = data.json()['games'][0]['year_published']

        search = {"name":name, "price":price, "min_players":min_players, "max_players":max_players, "description":description, "commentary":commentary, "image_url":image_url, "publisher":publisher, "rules_url":rules_url, "year_published":year_published}
        print(search)
        return redirect(url_for('site.search_result', search = search))
  
    return render_template("search_form.html", form=form)
    
    
@site.route('/search_result',  methods = ['GET'])
def search_result():
    data = request.args.get('search')
    print(data)
    search_answer = ast.literal_eval(data)
    #print(search_answer['name'])
    return render_template("search_result.html", search_answer= search_answer)
 
#@site.route('/blogging')
#@login_required
#def blogging():
    #return render_template('blogging.html')

# @site.route('/prices_rankings')
# @login_required
# def prices_rankings():
#     form = AtlasInfoForm()
#     return render_template('prices_rankings.html')