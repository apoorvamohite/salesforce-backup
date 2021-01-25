'''

To run the script, you need python3. For installing dependencies, pip is required.

The dependencies are listed in requirements.txt
To install dependencies, run:
pip install -r requirements.txt



The backup-config.json file contains the information of all orgs for which you want a backup. 

"orgAlias" will be used for the final zip name.
"command" specifies the sfdx command that needs to be run. As of now, this is the sfdx retrieve command.
"folderLocation" is where the existing org is located. Currently, I used an org that was setup and authorized using VSCode.
"zipLocation" is a directory where you want the final zip to be in.
"cliArgumentName" is used as an argument name when running the script. If you want to backup only a specific org or a subset, this argument is passed with a '--' prefix.
"backup" is used when ' --all' is passed as a cli argument. If this value is "Y" then the org is backed up.

** When specifying directory paths on windows, make sure to use a double backslash \\  **


To take a backup for all orgs specified in the backup-config, run:
python backup.py --all

To take a backup for all and delete the existing backups, run:
python backup.py --all --del

To take a backup for a specific org, run:
python backup.py --cliArgumentName
or
python backup.py --cliArgumentName1 --cliArgumentName2

'''

import os
import shutil
import sys
import json
from datetime import date
from datetime import timedelta
from win10toast_persist import ToastNotifier 

notifier = ToastNotifier()
today = date.today()
formatted_date = today.strftime("%B-%d-%Y")

args = sys.argv

config_file = open('backup-config.json')
data = json.load(config_file)
orgs = data["orgs"]
for org in orgs:
    if('--del' in args):
        files = os.listdir(org["zipLocation"])
        for item in files:
            if item.endswith(".zip"):
                os.remove(os.path.join(org["zipLocation"], item))

for org in orgs:
    print(org["orgAlias"])
    sfdx_command = org["command"]
    
    if(('--all' in args) and org["backup"]=='Y' ) or ('--'+org["cliArgumentName"] in args):
        exitcode = os.system('cd ' + org["folderLocation"] + ' & ' + org["command"])
        if(exitcode == 1):
            notifier.show_toast("Error", "There was a problem retrieving "+org["orgAlias"], duration = None)
            print(org["orgAlias"] + ' Error')
        else:
            shutil.make_archive(org["zipLocation"] + "\\" + org["orgAlias"] + '-' + formatted_date, 'zip', org["folderLocation"])
            notifier.show_toast(org["orgAlias"]+" Zipped!", "Your "+ org["orgAlias"] +" org backup is ready", duration = None)
