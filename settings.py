import sys
import os
import json

homedir = os.path.join(os.path.expanduser("~"), '.WaterIntake')
if not os.path.exists(homedir):
    os.makedirs(homedir)
settings_file = os.path.join(homedir, 'settings.json')

if getattr(sys, 'frozen', False):
    # frozen
    appdir = os.path.dirname(sys.executable)
else:
    # unfrozen
    appdir = os.path.dirname(os.path.realpath(__file__))


def load_settings():
    if not os.path.exists(settings_file):
        with open(settings_file, 'w') as settings_init:
            settings_init.write(json.dumps({}))

load_settings()
try:
    settings = json.loads(open(settings_file, 'r').read())
except:
    os.remove(settings_file)
    load_settings()
    settings = json.loads(open(settings_file, 'r').read())

WATER_GOAL = settings.get('goal', 8)
START_TIME = settings.get('start', '07:00:00')
END_TIME = settings.get('end', '18:00:00')


def update_settings(goal, start, end):
    with open(settings_file, 'w') as settings_update:
        settings_update.write(json.dumps({'goal': goal, 'start': start, 'end': end}))
