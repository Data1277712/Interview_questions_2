import json

# Sample data to be written to the JSON file
sample_data = {
    "emp_id" : ["1","2","3"],
    "emp_name" : ["sampath","vittal","renu sumanth"] 
}

# Write the sample data to a JSON file
with open('config_sample.json', 'w') as json_file:
    json.dump(sample_data, json_file, indent=4)
    
import json
with open("config_sample.json",'r') as json_file:
      data= json.load(json_file)

print(list(data.keys()))
key="emp_id"
print(data.get(key))
