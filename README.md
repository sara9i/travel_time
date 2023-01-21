# Calculate Time Travelled
https://docs.google.com/document/d/1XgHwXSE0c-JvsEHq_ELfwl7P8U_-T_8TntHHNmuEpqg/edit#
## Stack
* Python

## Start development server
```sh

# run the script locally with csv filename
python run.py <filename.csv>

# run script in Docker
# set csv file name as env variable
export FILENAME=<filename.csv>
#use docker-compose.yml to get the docker container running
docker-compose up -d
``` 

## Testing

For code testing used python's `unittest`

```sh

# run tests locally
python -m unittest test.py

# run tests in Docker
docker-compose -f docker-compose.test.yml up -d
``` 


## Dependencies

###Virtual Envoirnment
- Create a virtual env: `virtualenv .venv`
- Start the virtual env: `source .venv/bin/activate`
- Install dependencies inside virtual env

Python dependencies can be installed via **pip** or **piptools**

```
pip install -r requirements.txt 
```

On Docker

```
docker-compose -d
```

###Dev Dependencies

- Install autohooks and plugin dependencies
  pip install autohooks
  pip install autohooks-plugin-isort
  pip install autohooks-plugin-black
  pip install autohooks-plugin-pylint

- Activate autohooks `autohooks activate` and check it has all 3 modules loadable by `autohooks check`
