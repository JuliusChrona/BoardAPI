# boardAPI
## Start services
1. Clone repo
2. Install docker and docker-compose
3. Create .env file
4. Run docker
```bash
docker-compose up -d
```
### .env file

```sh
SECRET_KEY= <Django secret key>
DB = <db_name>
USER = <db_username>
PASSWORD = <user_password>
PORT = <port>
HOST = <db_host>
```
__SECRET_KEY__  - Your token for using bot in telegram. 
:warning:`Don't add your token in repository`

__DB__ - Name of the PostgreSQL database

__USER__ - Login for connect to the database (PostgreSQL)

__PASSWORD__ - Password need for connect to the database (PostgreSQL)

__PORT__ - Port to the PostgreSQL database

__HOST__ - IP_Address to the PostgreSQL database that stores information about songs


### Create super user
1. Start bash in container
```bash
docker exec -it web_api bash
```
2. Create admin user
```bash
python3 manage.py createsuperuser
```
3. Choose username and password
5. Exit from container
```bash
exit
```

###Additional links
You can test API [here](https://board-news.herokuapp.com/). Debug mode is enabled