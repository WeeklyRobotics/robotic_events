# robotic_events
A repository containing upcoming events in robotics (WIP).

The events in this repository are rendered on [Weekly Robotics website](https://www.weeklyrobotics.com/events)

Please feel free to create a PR adding your event details. To insert the event, modify events.yml file, inserting your event in the following format:

```
- title: Robotics Summit & Expo
  link: https://www.roboticssummit.com/
  start_date: 2024-05-01
  end_date: 2024-05-02
  city: Boston
  country: US
  category: Expo
```

Using any of the categories:
* Conference
* Expo
* Workshop
* Competition
* Meetup

When you insert the event, make sure it is inserted chronically with respect of start_date of other events.

TODOS:
* [] Create a script to automatically sort events.yml by start date
* [] Automatically trigger Weekly Robotics rebuild after a PR merge
* [] Create a script and a GitHub action to automatically remove past events
* [] Create a jinja2 template to populate the README.md with the events

Any help on the above would be highly appreciated!
