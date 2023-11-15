# Calculate Time Travelled
Given a sample CSV file containing a list of time-logs for a delivery person to deliver products, calculate the total time spent in traveling by each person (in minutes). Think through boundary conditions like overlapping time, etc..

CSV file content:
Sr. No.,Delivery Person,Product,Pick up time,Delivered time
1,Alice,GoPro Camera,2020-12-21T23:40:00Z,2020-12-22T00:05:00Z
2,Alice,Tennis Shoes,2020-12-22T00:00:00Z,2020-12-22T00:25:00Z
3,Tony,Football,2020-12-22T01:25:00Z,2020-12-22T02:15:00Z
4,Alice,Table Lamp,2020-12-22T02:25:00Z,2020-12-22T02:55:00Z
5,Tony,Frisbee,2020-12-22T03:00:00Z,2020-12-22T03:15:00Z
6,Tony,Telescope,2020-12-22T02:50:00Z,2020-12-22T03:40:00Z
7,Tony,Pizza,2020-12-22T03:35:00Z,2020-12-22T04:10:00Z
8,Tony,Drone,2020-12-22T05:25:00Z,2020-12-22T06:05:00Z

## Stack
* Python

## Start development server

#### Local Server

```sh
# run the script locally with csv filename
python run.py <filename.csv>

``` 

#### Docker

```sh
# set csv file name as env variable
export FILENAME=<filename.csv>
#use docker-compose.yml to get the docker container running
docker-compose up -d
``` 

## Testing

For code testing used python's `unittest`

#### Local Server

```sh
# run tests locally
python -m unittest test.py
``` 

#### Docker

```sh
# use docker-compose.test.yml to run the tests in docker container
docker-compose -f docker-compose.test.yml up -d
``` 


## Dependencies

#### Virtual Envoirnment
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

#### Dev Dependencies

- Install autohooks and plugin dependencies</br>
  pip install autohooks</br>
  pip install autohooks-plugin-isort</br>
  pip install autohooks-plugin-black</br>
  pip install autohooks-plugin-pylint</br>

- Activate autohooks `autohooks activate` and check it has all 3 modules loadable by `autohooks check`
