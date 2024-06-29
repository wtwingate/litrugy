import json

with open("../lectionary.json") as f:
    data = json.load(f)

for day_name, val in data.items():
    if day_name == "Christmas Day" or day_name == "Easter Day":
        for service_name, years in val.items():
            for year_name in years:
                if year_name == "Year A":
                    print(f"{day_name}: {service_name} ({year_name})")
                elif year_name == "Year B":
                    print(f"{day_name}: {service_name} ({year_name})")
                else:
                    print(f"{day_name}: {service_name} ({year_name})")
    else:
        for year_name in val:
            if year_name == "Year A":
                print(f"{day_name} ({year_name})")
            elif year_name == "Year B":
                print(f"{day_name} ({year_name})")
            else:
                print(f"{day_name} ({year_name})")
