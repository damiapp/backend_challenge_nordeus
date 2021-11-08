import names
import random
from match_making import match

from test_db.database import create_db 

def create_clubs() -> list:
    try:
        data = []

        for i in range(51):
            data.append({
                'name':names.get_first_name(),
                'rating':random.randint(1,100),
                'team_power':random.randint(1,100) 
            })

        return data
    except Exception as e:
        return []


data=create_clubs()
create_db(data)
match()