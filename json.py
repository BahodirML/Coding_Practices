import json

data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}

data_json = json.dumps(data)

print(data_json)