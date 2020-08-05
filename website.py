"""
from flask import Flask, redirect, url_for
# from forms import SearchForm
# from models import User

@app.route("/admin")
def admin():
    return redirect(url_for("home"))
"""
import datetime
import json, requests
from flask import Flask, request, render_template

url_venues = 'https://api.foursquare.com/v2/venues/explore'
url_hours = 'https://api.foursquare.com/v2/venues/{}/hours'
url_photos = 'https://api.foursquare.com/v2/venues/{}/photos'
url_here = 'https://api.foursquare.com/v2/venues/{}'

CLIENT_ID = 'UNXKPYYYPY2PQFGNYL3KXWTKGNT20SO4ISO0YDROW0HORX2W'
CLIENT_SECRET = 'QWPXY050I0NWIEIGIGHGNUBM0XXWN42SNS2XGBGKL3RXBKP3'

app=Flask(__name__)

@app.route('/')
def home():
    app.route('/')
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/query', methods=['POST'])
def search_query():
    quer = request.form['fquery']
    floc = request.form['floc']
    params_venues = dict(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         v='20200601',
                         near=floc,
                         query=quer,
                         limit=3
                         )
    resp = requests.get(url=url_venues, params=params_venues)
    data = json.loads(resp.text)

    # gather the data lads
    loc1=data['response']['groups'][0]['items'][0]['venue']['name']
    id1=data['response']['groups'][0]['items'][0]['venue']['id']
    url1 = "/"+loc1.replace(" ", "-") + "/" + id1

    loc2=data['response']['groups'][0]['items'][1]['venue']['name']
    id2=data['response']['groups'][0]['items'][1]['venue']['id']
    url2="/"+loc2.replace(" ", "-") + "/" + id2

    loc3=data['response']['groups'][0]['items'][2]['venue']['name']
    id3=data['response']['groups'][0]['items'][2]['venue']['id']
    url3="/"+loc3.replace(" ", "-")+ "/" + id3

    return render_template('search_query.html', query=quer, loc=floc, loc1=loc1,
                           url1=url1, loc2=loc2, url2=url2,
                           loc3=loc3, url3=url3)

@app.route("/<name>/<id>")
def user(name, id):
    hour = int(datetime.datetime.now().hour * 100)
    day = int(datetime.datetime.today().weekday()+1)

    populars_fosho = {}
    busy = "medium"
    name = name.replace("-", " ")
    '''
    basic - using popular hours api
    if in popular hours - "highly"
    if an hour before or after popular - "medium"
    else - "not"
    '''
    url_hours_id = url_hours.format(id)
    params_hours = dict(client_id=CLIENT_ID,
                        client_secret=CLIENT_SECRET,
                        v='20200601',
                        VENUE_ID=id)
    resp_hours = requests.get(url=url_hours_id, params=params_hours)
    data_hours = json.loads(resp_hours.text)
    for i in range(len(data_hours['response']['popular']['timeframes'])):
        for j in range(len(data_hours['response']['popular']['timeframes'][i]
                           ['days'])):
            populars_fosho[data_hours['response']['popular']['timeframes'][i]
            ['days'][j]] = range(int(data_hours['response']['popular']['timeframes']
                                             [i]['open'][0]['start']),
                                 int(data_hours['response']['popular']['timeframes'][i]['open'][0]['end']))

    if hour in populars_fosho[day]:
        busy = "highly"
    elif hour in range(populars_fosho[day].start-100, populars_fosho[day].stop+100):
        busy = "medium"
    else:
        busy = "not"

    '''
    trying to see if hereNow is accurate - seems like its always 0 when i check
    tho, maybe bc no one is checking in rn since everything is pick up?
    '''
    url_here_id = url_here.format(id)
    params_here = dict(client_id=CLIENT_ID,
                        client_secret=CLIENT_SECRET,
                        v='20200601',
                        VENUE_ID=id)
    resp_here = requests.get(url=url_here_id, params=params_here)
    data_here = json.loads(resp_here.text)
    print(data_here)


    url_photos_id = url_photos.format(id)
    params_photos = dict(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     v='20200601',
                     VENUE_ID=id)

    photos = requests.get(url=url_photos_id, params=params_photos)
    data_photos = json.loads(photos.text)
    pref = data_photos['response']['photos']['items'][0]['prefix']
    suf = data_photos['response']['photos']['items'][0]['suffix']
    size = str(data_photos['response']['photos']['items'][0]['width']) + 'x' + \
           str(data_photos['response']['photos']['items'][0]['height'])
    url = pref+size+suf
    return render_template('places.html', name=name, url=url, busy=busy)


if __name__=="__main__":
    app.run(debug=True)