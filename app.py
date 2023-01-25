import json, math, re, requests
from flask import Flask, request
from waitress import serve

app = Flask(__name__)

@app.route("/")
def get_results():
    MGLT = request.args.get("MGLT",1000000,int)
    url = "https://www.swapi.tech/api/starships?page=1&limit=100"
    headers = {
    'Accept': 'application/json; version=3',
    'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers)
    session = requests.Session()
    session.headers.update(headers)
    json_data = json.loads(response.content)
    results = []
    final_results = {}
    for result in json_data["results"]:
        
        response = requests.get(result["url"])
        data = json.loads(response.content)
        results.append(data)
        if data["result"]["properties"]["MGLT"] == "unknown":
            final_results [data["result"]["properties"]["name"]] = "unknown"
            continue
        n_stops = MGLT/int(data["result"]["properties"]["MGLT"])
        match = re.search("year|month|week|day", data["result"]["properties"]["consumables"])
        if match is not None:
            if match.group() == "year":
                n_year = int(match.string[0:match.regs[0][0]])
                parameter = 8640 * n_year
                n_stops = n_stops/parameter
                n_stops = math.floor(n_stops)
                final_results[data["result"]["properties"]["name"]] = n_stops
            elif match.group() == "month":
                n_month = int(match.string[0:match.regs[0][0]])
                parameter = 720 * n_month
                n_stops = n_stops/parameter
                n_stops = math.floor(n_stops)
                final_results[data["result"]["properties"]["name"]] = n_stops
            elif match.group() == "week":
                n_week = int(match.string[0:match.regs[0][0]])
                parameter = 168 * n_week
                n_stops = n_stops/parameter
                n_stops = math.floor(n_stops)
                final_results[data["result"]["properties"]["name"]] = n_stops
            elif match.group() == "day":
                n_day = int(match.string[0:match.regs[0][0]])
                parameter = 24 * n_day
                n_stops = n_stops/parameter
                n_stops = math.floor(n_stops)
                final_results[data["result"]["properties"]["name"]] = n_stops
            
    results_to_show = ""
    for key, value in final_results.items():
        results_to_show += f'Starship: {key} &nbsp Stops: {value}<br>'
   
    return results_to_show
    
if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)