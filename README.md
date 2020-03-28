#FastAPI Movies
FastAPI Framework Example Build


## Setting up

Prepare

    pipenv install
    
Database

    CREATE TABLE movies (
	id serial PRIMARY KEY,
	name varchar(128),
	description varchar(256),
	year varchar(8),
	casts text [],
		UNIQUE(name)
    );

Run
    
    . ./variables.sh
    
    uvicorn main:app --reload --port 8000
    