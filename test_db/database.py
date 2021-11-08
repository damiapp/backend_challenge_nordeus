import logging
import sqlite3

def create_db(data):
    conn = sqlite3.connect('matchmaking.db')
    try:
        #this should not look like this do to security issues
        conn.execute('''CREATE TABLE IF NOT EXISTS POOL
                (ID           INTEGER       PRIMARY KEY AUTOINCREMENT,
                NAME            CHAR(25)      NOT NULL,
                RATING          INTEGER       NOT NULL,
                TEAM_POWER      INTEGER       NOT NULL,
                POOL_SECTION    INTEGER       NOT NULL
                );''')
        conn.execute('''CREATE TABLE IF NOT EXISTS MATCH
                (ID_MATCH       INTEGER       PRIMARY KEY AUTOINCREMENT,
                ID_P1           INTEGER       NOT NULL,
                ID_P2           INTEGER       NOT NULL,
                FOREIGN KEY(ID_P1) REFERENCES POOL(ID)
                FOREIGN KEY(ID_P2) REFERENCES POOL(ID)
                );''')

        logging.info('Table created successfully')
    except Exception as e:
        logging.exception(f'Exception while creating db: {e}')
    
    insert_club(conn,data)

    conn.close()

def insert_club(conn,data):
    try:
        #All players inserted into MM POOL
        for i in data:
            values=(i['name'],i['rating'],i['team_power'],pool_section(i))
            conn.execute('''INSERT INTO POOL (NAME,RATING,TEAM_POWER,POOL_SECTION) 
            VALUES (?,?,?,?);''',values)
        conn.commit()
    except Exception as e:
        logging.exception(f'Insert club exception: {e}')   

def pool_section(player):
    pool_num= player['rating']//10
    if(player['team_power']<20):
        pool_num=pool_num-1
    if(player['team_power']>80):
        pool_num=pool_num+1
    
    if(pool_num<0):
        pool_num=pool_num+1
    
    if(pool_num>10):
        pool_num=pool_num-1
   
    return pool_num
