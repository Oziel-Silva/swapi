from flask import Flask
import requests
import json
import math
import re

app = Flask(__name__)





@app.route("/")
def get_results():



    url = "https://www.swapi.tech/api/starships?page=1&limit=100"

    payload={}
    headers = {
    'Accept': 'application/json; version=3',
    'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    json_data = json.loads(response.content)
    with open("data.json", "w") as file:
        json.dump(json_data, file,indent=4)

    results = []
    final_results = {}
    MGLT = 1000000
    parameter = 720
    paradas = []
    for result in json_data["results"]:
        
        response = requests.get(result["url"])
        data = json.loads(response.content)
        results.append(data)
        if data["result"]["properties"]["MGLT"] == "unknown":
            final_results [data["result"]["properties"]["name"]] = "unknown"
            continue
        n_paradas = MGLT/int(data["result"]["properties"]["MGLT"])
        match = re.search("year|month|week|day", data["result"]["properties"]["consumables"])
        if match != None:
            if match.group() == "year":
                n_year = int(match.string[0:match.regs[0][0]])
                parameter = 8640 * n_year
                n_paradas = n_paradas/parameter
                n_paradas = math.floor(n_paradas)
                final_results [data["result"]["properties"]["name"]] = n_paradas
            elif match.group() == "month":
                n_month = int(match.string[0:match.regs[0][0]])
                parameter = 720 * n_month
                n_paradas = n_paradas/parameter
                n_paradas = math.floor(n_paradas)
                final_results [data["result"]["properties"]["name"]] = n_paradas
            elif match.group() == "week":
                n_week = int(match.string[0:match.regs[0][0]])
                parameter = 168 * n_week
                n_paradas = n_paradas/parameter
                n_paradas = math.floor(n_paradas)
                final_results [data["result"]["properties"]["name"]] = n_paradas
            elif match.group() == "day":
                n_day = int(match.string[0:match.regs[0][0]])
                parameter = 24 * n_day
                n_paradas = n_paradas/parameter
                n_paradas = math.floor(n_paradas)
                final_results [data["result"]["properties"]["name"]] = n_paradas
            else:
                continue
    return final_results
