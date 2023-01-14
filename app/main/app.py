from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/benefits')
def benefits():
    return render_template('benefits.html')


@app.route('/types')
def types():
    return render_template('types.html')


@app.route('/postures')
def postures():
    return render_template('postures.html')


@app.route('/pranayama')
def pranayama():
    return render_template('pranayama.html')


@app.route('/meditation')
def meditation():
    return render_template('meditation.html')


@app.route('/precautions')
def precautions():
    return render_template('precautions.html')


@app.route('/healthconditions')
def healthconditions():
    return render_template('healthconditions.html')


@app.route('/diet')
def diet():
    return render_template('diet.html')


@app.route('/philosophy')
def philosophy():
    return render_template('philosophy.html')


@app.route('/dailylife')
def dailylife():
    return render_template('dailylife.html')


@app.route('/safetytips')
def safetytips():
    return render_template('safetytips.html')


@app.route('/resources')
def resources():
    return render_template('resources.html')


@app.route('/interestingfacts')
def interestingfacts():
    return render_template('interestingfacts.html')


@app.route('/mentalhealth')
def mentalhealth():
    return render_template('mentalhealth.html')


@app.route('/nervoussystem')
def nervoussystem():
    return render_template('nervoussystem.html')


@app.route('/chakras')
def chakras():
    return render_template('chakras.html')


@app.route('/agegroups')
def agegroups():
    return render_template('agegroups.html')


@app.route('/breath')
def breath():
    return render_template('breath.html')


@app.route('/pregnancy')
def pregnancy():
    return render_template('pregnancy.html')


@app.route('/stressmanagement')
def stressmanagement():
    return render_template('stressmanagement.html')


@app.route('/sleep')
def sleep():
    return render_template('sleep.html')


@app.route('/mindfulness')
def mindfulness():
    return render_template('mindfulness.html')


@app.route('/flexibility')
def flexibility():
    return render_template('flexibility.html')


@app.route('/sportsperformance')
def sportsperformance():
    return render_template('sportsperformance.html')


@app.route('/aging')
def aging():
    return render_template('aging.html')


@app.route('/trauma')
def trauma():
    return render_template('trauma.html')


@app.route('/spirituality')
def spirituality():
    return render_template('spirituality.html')


@app.route('/socialjustice')
def socialjustice():
    return render_template('socialjustice.html')


@app.route('/environmentalism')
def environmentalism():
    return render_template('environmentalism.html')


@app.route('/womenshealth')
def womenshealth():
    return render_template('womenshealth.html')


@app.route('/children')
def children():
    return render_template('children.html')


@app.route('/technology')
def technology():
    return render_template('technology.html')


@app.route('/business')
def business():
    return render_template('business.html')


@app.route('/travel')
def travel():
    return render_template('travel.html')


@app.route('/donation')
def donation():
    return render_template('donation.html')


if __name__ == '__main__':
    app.run(debug=True)
