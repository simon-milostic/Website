import json
from pathlib import Path
import urllib.request

URL = "https://www.imf.org/external/datamapper/api/v1/GGXWDG_NGDP/USA"

with urllib.request.urlopen(URL) as response:
    data = json.load(response)

data_folder = Path(__file__).resolve().parents[2] / "Data"
data_folder.mkdir(parents=True, exist_ok=True)

output_file = data_folder / "info.json"

count = 300
if count <= 300:
    sample = data
else:
    pick = [round(i * (len(data) - 1)/count - 1) for i in range(count)]
    sample = [data[i] for i in pick]
    
us_economy = sample["values"]["GGXWDG_NGDP"]["USA"]
new_us_economy = [{"year": int(year), "debt_gdp": stuff } for year, stuff in us_economy.items()]

ger_economy = sample["values"]["GGXWDG_NGDP"]["DEU"]
new_ger_economy = [{"year": int(year), "debt_gdp": stuff } for year, stuff in ger_economy.items()]

jpn_economy = sample["values"]["GGXWDG_NGDP"]["JPN"]
new_jpn_economy = [{"year": int(year), "debt_gdp": stuff } for year, stuff in jpn_economy.items()]

ind_economy = sample["values"]["GGXWDG_NGDP"]["IND"]
new_ind_economy = [{"year": int(year), "debt_gdp": stuff } for year, stuff in ind_economy.items()]

bra_economy = sample["values"]["GGXWDG_NGDP"]["BRA"]
new_bra_economy = [{"year": int(year), "debt_gdp": stuff } for year, stuff in bra_economy.items()]

saf_economy = sample["values"]["GGXWDG_NGDP"]["ZAF"]
new_saf_economy = [{"year": int(year), "debt_gdp": stuff } for year, stuff in saf_economy.items()]

sample = {
    "USA" : new_us_economy,
    "GER" : new_ger_economy,
    "JPN" : new_jpn_economy,
    "IND" : new_ind_economy,
    "BRA" : new_bra_economy,
    "ZFA" : new_saf_economy
}

with output_file.open("w", encoding="utf-8") as info:
    json.dump(sample, info, indent=2)

