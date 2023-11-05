# `pip3 install ruamel.yaml` to install dependencies
import os
from ruamel.yaml import YAML
import datetime

""" This script will move events that have already ended to past_events.yaml and in the process sort
    all events by start_date."""

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Specify the relative path to the YAML file
events_file = "../events.yaml"
past_events_file = "../past_events.yaml"

# Construct the absolute path to the YAML files
events_path = os.path.join(current_directory, events_file)
past_events_path = os.path.join(current_directory, past_events_file)

# Load YAML file with ruamel.yaml
yaml = YAML()
with open(events_path, 'r') as file:
    events = yaml.load(file)

with open(past_events_path, 'r') as file:
    past_events = yaml.load(file)

# Sort events by start_date
events.sort(key=lambda x: x['start_date'])

today = datetime.date.today()

if past_events is None:
    past_events = [] # First time running the script

for event in events.copy():
    if 'end_date' in event:
        end_date = event['end_date']
    else:
        end_date = event['start_date']

    print("Event: {}, End date: {}".format(event['title'], end_date))
    if today > end_date:
        print("Moving the event {} to past_events.yaml".format(event['title']))
        past_events.append(event)
        events.remove(event)

past_events.sort(key=lambda x: x['start_date'])

# Write sorted events back to the YAML file
with open(events_path, 'w') as file:
    yaml.dump(events, file)

with open(past_events_path, 'w') as file:
    yaml.dump(past_events, file)

print("Events cleaned up!")
