import csv
import json

def convert_csv_to_json(filename):
    try:
        data = []

        # Read CSV and convert it to dictionaries
        with open(filename, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)

        # Write JSON data to data.json
        with open("data.json", mode='w', encoding='utf-8') as f:
            json.dump(data, f)

        return True
    except:
        return False
    
