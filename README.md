# About

This script is used to backup multiple salesforce orgs. It retrieves the latest version of code from your org and zips the files with a date stamp.

## Prerequisites

You will need a ["source" formatted](https://developer.salesforce.com/tools/vscode/en/user-guide/source-format/) org or an org that is set up and authorized using VSCode. This is a one time setup that is required.

To run the script, you need ```python3```. For installing dependencies, ```pip``` is required.

The dependencies are listed in requirements.txt, To install dependencies, run:

```bash
pip install -r requirements.txt
```
## Configuration
The ```backup-config.json``` file contains the information of all orgs for which you want a backup. 

Key                  |              Purpose
---------------------|--------------------------------------------------------------
"orgAlias"           | Will be used for the final zip name.
"command"            | Specifies the sfdx command that needs to be run. As of now, this is the sfdx retrieve command.
"folderLocation"     | Is where the existing org is located. Currently, I used an org that was setup and authorized using VSCode.
"zipLocation"        | Is a directory where you want the final zip to be in.
"cliArgumentName"    | Is used as an argument name when running the script. If you want to backup only a specific org or a subset, this argument is passed with a '--' prefix.
"backup"             | is used when ' --all' is passed as a cli argument. If this value is "Y" then the org is backed up.

*** When specifying directory paths on windows, make sure to use a double backslash \\\  ***

## Usage
To take a backup for all orgs specified in the ```backup-config.json```, run:

```bash
python backup.py --all
```
To take a backup for all and delete the existing backups, run:
```bash
python backup.py --all --del
```

To take a backup for a specific org, run:
```bash
python backup.py --cliArgumentName
```
or
```bash
python backup.py --cliArgumentName1 --cliArgumentName2
```
## Scheduling
[Scheduling job on Windows](https://datatofish.com/python-script-windows-scheduler/)
## Contributing
Pull requests, suggestions are welcome.
