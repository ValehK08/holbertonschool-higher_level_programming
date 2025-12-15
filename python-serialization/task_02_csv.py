import csv
import json

def convert_csv_to_json(filename):
    try:
        # CSV to Dictionaries
        s = []
        with open(filename, mode='r', newline='', encoding="utf-8") as f:
            ict_reader = csv.DictReader(f)

            for row in dict_reader:
                s.append(row)
    
        # Dictionaries to JSON
        data = json.dumps(s)

        # Save the data into data.json
        with open("data.json", 'w') as f:
            json.dump(data, f)
        return True
    except:
        return False
    
