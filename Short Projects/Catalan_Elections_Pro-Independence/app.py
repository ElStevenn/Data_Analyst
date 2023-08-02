from flask import Flask, render_template, url_for, redirect, request, flash
import pandas as pd
import os

app = Flask(__name__)
town = None


def search_the_town(town):
    """Returns town party info with the town"""
    town_data_frame = pd.read_csv(os.getcwd() + "/csv_data/barcelona_data.csv", encoding='utf-8')

    Townselected = town_data_frame[town_data_frame["town_name"] == town]
    
    PSC = "PSC: " + str(Townselected["PSC"].values[0])
    PP = "PP: " + str(Townselected["PP"].values[0])
    VOX = "VOX: " + str(Townselected["VOX"].values[0])
    Cs = "Cs: " + str(Townselected["Cs"].values[0])
    ERC = "ERC: " + str(Townselected["ERC"].values[0])
    ECP = "ECP: " + str(Townselected["ECP"].values[0])
    JxCat = "JxCat: " + str(Townselected["JxCat"].values[0])
    CUP = "CUP: " + str(Townselected["CUP"].values[0])

    Total_votes = int(Townselected["PSC"].values[0]) + int(Townselected["PP"].values[0]) + int(Townselected["VOX"].values[0]) + int(Townselected["Cs"].values[0]) + int(Townselected["ERC"].values[0]) + int(Townselected["ECP"].values[0]) + int(Townselected["JxCat"].values[0]) + int(Townselected["CUP"].values[0])

    return [PSC, PP, VOX, Cs, ERC, ECP, JxCat, CUP], Total_votes


@app.route('/', methods = ["GET", "POST"])
def main():
    
    if request.method == 'POST':
        searched_town = request.form['town_data']

    
        return redirect(url_for('search_town', town_name = searched_town))

    return render_template("Data_search.html")


@app.route('/town_search')
@app.route(f'/town_search/<town_name>')
def search_town(town_name = None):
    if town_name is None:
        return redirect(url_for('main'))
    try:
        getData, total_votes = search_the_town(town_name)

        if getData is []:
            # More later include here a flash message like "you have to select a correct town!"
            return redirect(url_for('main'))
        else:
            print(getData)

        return render_template("Town_Data.html", town_name = town_name, party_results = getData, total_votes= total_votes)
    
    except IndexError:
        # In the future show amessage like "this town doesen't exists!" with flash/ 
        return redirect(url_for('main'))

if __name__ == "__main__":
    app.run(debug=True)