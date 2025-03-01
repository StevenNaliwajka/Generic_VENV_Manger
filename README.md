# Generic_VENV_Manger
Builds a VENV and handles running programs automaticaly within the VENV.


## Development Usages
Duplicate "packages.example.json"
and rename to "packages.json'.  
Fill out required packages to be installed.  
Call 'VENVUtil.setup_venv()'

To run program


## Integration with Project
To integrate this repo into your project.  
Navigate to the location of where you want it in CMD and paste this
```angular2html
git submodule add https://github.com/StevenNaliwajka/Generic_VENV_Manger Generic_VENV_Manger
git submodule update --init --recursive
```
To my understanding you have to also include in your install script  
```angular2html
#!/bin/bash
git submodule update --init --recursive
```
