import sqlite3
def match():
    conn=sqlite3.connect('matchmaking.db')

    pool=get_club_list(conn)
    cursor=conn.cursor()
    pool.sort(key=lambda y:(y[4],y[2]))
    for i in range(0,len(pool)-1,2):
        print(f'{pool[i]} VS {pool[i+1]} \n\
            ------------------------------')
        values=(pool[i][0],pool[i+1][0])
        cursor.execute('''INSERT INTO MATCH (ID_P1,ID_P2) 
                        VALUES (?,?);''',values)
        cursor.execute(''' DELETE FROM POOL
                    WHERE ID=?;''',(pool[i][0],))
        cursor.execute(''' DELETE FROM POOL
                    WHERE ID=?;''',(pool[i+1][0],))
    conn.commit()


def get_club_list(conn):
    cursor=conn.execute('SELECT * FROM POOL')
    
    return cursor.fetchall()
