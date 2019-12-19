from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/search')
def search():
    return render_template('search_opgg.html')

@app.route('/opgg')
def opgg():
    userName = request.args.get('userName')
    url = f"http://www.op.gg/summoner/userName={userName}"
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')
    
    tier = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierRank')

    win = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')

    return render_template('opgg.html', name = userName, tier = tier.text, win = win.text[: - 1], url = url)

if __name__ == ("__main__"):
    app.run(debug=True)