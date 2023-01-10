# blind-keyboard-practitioner

# Dev setup

## Virtualenv

If you don't have virtualenv installed, install it with 
```bash
pip install virtualenv
```

Create a virtualenv with
```bash
python -m venv enviroment
```

Activate the virtualenv with
```bash
source enviroment/bin/activate
```
(In Powershell: )
```powershell
.\enviroment\Scripts\activate
```

### To close the virtualenv
```bash
deactivate
```
### To delete the virtualenv
```bash
rm -rf enviroment
```

(On Windows: )
```powershell
Remove-Item -Recurse enviroment
```

## Requirements
Install the requirements in the virtualenv with
```bash
pip install -r requirements.txt
```

## Run the app
```bash
python main
```

### For later
```bash
pipreqs --encoding=utf8 --force
```