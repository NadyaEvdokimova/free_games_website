from datetime import datetime
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired
import os
from free_games import FreeGames

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')


class GameForm(FlaskForm):
    platform = SelectField("Choose platform", choices=['pc', 'steam', 'epic-games-store', 'ubisoft', 'gog',
                                                       'itchio', 'ps4', 'ps5', 'xbox-one', 'xbox-series-xs', 'switch',
                                                       'android', 'ios', 'vr', 'battlenet', 'origin', 'drm-free',
                                                       'xbox-360'], validators=[DataRequired()])
    sort = SelectField("Sort", choices=["date", "value", "popularity"], validators=[DataRequired()])
    submit = SubmitField('Get Offers')


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


@app.route('/', methods=["GET", "POST"])
def home():
    data = []
    form = GameForm()
    if form.validate_on_submit():
        platform = form.platform.data
        sort = form.sort.data
        free_games = FreeGames(platform, sort)
        data = free_games.data
        data_length = len(data)
        return render_template("index.html", form=form, data=data, data_length=data_length)
    return render_template("index.html", form=form, data=data)


if __name__ == "__main__":
    app.run(debug=False, port=5001)
