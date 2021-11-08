# Backend Challenge Nordeus
A small implementation of matchmaking in a game like Football Manager.

## Required
- *python3 https://www.python.org/downloads/*
- *pip https://github.com/pypa/get-pip*
- *pip install names*

## Explenation
The program start off by making a database with all the players that are currently waiting in a match making pool. The players have two main atributes(*rating and team_power*) and one more that derives from previous two (*pool_section*) which is the main anchor for the machmaking. After running __app.py__
you will have a __matchmaking.db__ with two tables:
###    
    - POOL: information about players who are waiting
    - MATCH: matched players with there ID

## app.py
__Start the program with command:__
```
python3 app.py
```

## match_making.py

```
match() --> Transfers players from POOL table to MATCH table
get_club_list() --> gets all players from the POOL
```

Starts matchmaking. <br>
