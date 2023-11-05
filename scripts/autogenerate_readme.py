import yaml
from jinja2 import Template
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
events_file = "../events.yaml"
events_path = os.path.join(current_directory, events_file)
template_path = os.path.join(current_directory, 'templates/readme.j2')
readme_path = os.path.join(current_directory, '../README.md')

# Read events from events.yaml
with open(events_path, 'r') as file:
    events = yaml.safe_load(file)

category_order = ['Conference', 'Expo', 'Workshop', 'Competition', 'Meetup']

# Group events by category and maintain the desired order
events_by_category = {category: [] for category in category_order}
for event in events:
    category = event['category']
    if category in category_order:
        events_by_category[category].append(event)

# Load the Jinja template
with open(template_path, 'r') as file:
    template_content = file.read()

template = Template(template_content)

# Render the template with events
rendered_template = template.render(events_by_category=events_by_category)

# Write the rendered template to README.md
with open(readme_path, 'w') as file:
    file.write(rendered_template)
