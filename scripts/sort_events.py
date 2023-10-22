# `pip3 install ruamel.yaml` to install dependencies
import os
from ruamel.yaml import YAML

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Specify the relative path to the YAML file
relative_path = "../events.yaml"

# Construct the absolute path to the YAML file
file_path = os.path.join(current_directory, relative_path)

# Load YAML file with ruamel.yaml
yaml = YAML()
with open(file_path, 'r') as file:
    events = yaml.load(file)

# Sort events by start_date
events.sort(key=lambda x: x['start_date'])

# Write sorted events back to the YAML file
with open(relative_path, 'w') as file:
    yaml.dump(events, file)

print("Events sorted by start_date and written to sorted_events.yaml.")
