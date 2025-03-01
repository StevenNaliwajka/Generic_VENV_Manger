# Generic_VENV_Manger
https://github.com/StevenNaliwajka/Generic_VENV_Manger  
Builds a VENV and handles running python files within the VENV.

## Integration with Project
To integrate this repo into your project.  
Navigate to the location of where you want it in CMD and input a variation of this:
```angular2html
git subtree add --prefix=PARENTFOLDERHERE/Generic_VENV_Manger https://github.com/StevenNaliwajka/Generic_VENV_Manger.git main --squash
```
To get the latest version of this repo.
```angular2html
git subtree pull --prefix=PARENTFOLDERHERE/Generic_VENV_Manger https://github.com/StevenNaliwajka/Generic_VENV_Manger.git main --squash
```

Ensure to add 'venv' to ".ignore" file for git.

## Development Usages
### Create VENV:
Duplicate "packages.example.json"
and rename to "packages.json'.  
Fill out required packages to be installed.
Usage for setting up VENV is:  
```angular2html
VENVUtil.setup_venv("~/PATH/TO/VENV")
```

### Run with VENV:
If adding enviroment variables  
Duplicate "run_env_var.example.json"  
and rename to "run_env_var.json'.  
Usage for calling python programs in VENV is:  
```
VENVUtil.run_with_venv("~/PATH/TO/VENV/", "~/PATH/TO/PYTHON.PY")
```
