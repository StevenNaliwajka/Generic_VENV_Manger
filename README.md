# Generic_VENV_Manger
https://github.com/StevenNaliwajka/Generic_VENV_Manger  
Builds a VENV and handles running python files within the VENV.
------------------
# Integration with Project for Development.
### 1) Install Project as a Subtree with git.

To integrate this repo into your project.  
Navigate to the location of where you want it in CMD and input a variation of this:
```angular2html
git subtree add --prefix=PATH/TO/FOLDER/Generic_VENV_Manger https://github.com/StevenNaliwajka/Generic_VENV_Manger.git main --squash
```

### 2) Run Setup Python Files to create JSON config.
Two setup files, run one or both.

For Package Install Management:
```angular2html
python3 PATH/TO/Generic_VENV_Manager/VENVSetup/setup_packages_file.py
```

For Runtime Environment Variable Management:
```angular2html
python3 PATH/TO/Generic_VENV_Manager/VENVSetup/setup_run_env_file.py
```

### 3) Final git tracking setup.
Ensure to add 'venv' to ".gitignore" file.
```angular2html
# In the new project root folder.
echo venv >> .gitignore
```
IF you added package install management, force tracking.
```angular2html
git add -f PATH/TO/Generic_VENV_Manger/packages.json
```
SAME for IF you added the Runtime Enviroment Variable Management, force tracking.
```angular2html
git add -f PATH/TO/Generic_VENV_Manager/run_env_var.json
```
### 4) Going forward
To get the latest version of this repo.
```angular2html
git subtree pull --prefix=PATH/TO/FILE/Generic_VENV_Manger https://github.com/StevenNaliwajka/Generic_VENV_Manger.git main --squash
```
------------------

## Development Usages
### Create VENV:
Duplicate "packages.example.json"
and rename to "packages.json'.  
Fill out required packages to be installed.
Usage for setting up VENV is:  
```angular2html
VENVUtil.setup_venv("~/PATH/TO/ROOT")
```
### Run with VENV:
If adding enviroment variables  
Duplicate "run_env_var.example.json"  
and rename to "run_env_var.json'.  
Usage for calling python programs in VENV is:  
```angular2html
VENVUtil.run_with_venv("~/PATH/TO/ROOT", "~/PATH/TO/PYTHON.PY")
```
