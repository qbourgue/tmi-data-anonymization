# data-anonymization

from github.com/sunitparekh/data-anonymization

## Installation

> sudo apt install rubygems ruby-dev build-essential

> sudo gem install data-anonymization

### MongoDB

> wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
> echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
> sudo apt-get update
> sudo apt-get install -y mongodb-org

> sudo gem install mongo

#### Import Database

> sudo service mongod start

> mongoimport -d naisdb -c short_table --type csv --file short_naissance.csv --headerline 

### SQLite database

## Generate whitelist for the anonymiser

> datanon generate_mongo_dsl -h 127.0.0.1 -p 27017 -d naisdb


## Mongo tuto

### List all databases

> db.adminCommand( { listDatabases: 1 } )

(equivalent)
> show dbs

### Switch current db to name_db

> use name_db

### Get collections associated to db
> db.runCommand( { listCollections: 1.0, nameOnly: true } )

(equivalent)
> show collections

### Display database's content

> db.YOURCOLLECTIONS.find()

### Import collection from shell 
> mongoimport -d naisdb -c short_table --type csv --file short_naissance.csv --headerline

### Export collection from shell
> mongoexport --uri="mongodb://127.0.0.1:27017/anony_naisdb" --collection=very_short_table --out=anony_short_nais.csv

### Remove a collection of a db
db.very_short_table.drop()
