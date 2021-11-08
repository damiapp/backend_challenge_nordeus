# Database for the match making
Creates two necessary tables for the program two work. Generates random data for testing.

## Required
- *import sqlib3*

## POOL Table

| Parameters        | TYPES          |
| :---------------- | :-------------------------------- |
| *ID*              | INTEGER PRIMARY KEY  AUTOINCREMNET|
| *NAME*            | CHAR(25)                          |
| *RATING*          | INTEGER                           |
| *TEAM_POWER*      | INTEGER                           |
| *POOL_SECTION*    | INTEGER                           |

## MATCH Table

| Parameters        | TYPES          |
| :---------------- | :-------------------------------- |
| *ID*              | INTEGER PRIMARY KEY  AUTOINCREMNET|
| *ID_P1*           | INTEGER FOREIGN KEY-->POOL(ID)    |
| *ID_P2*           | INTEGER FOREIGN KEY-->POOL(ID)    |

## Functions
### insert_club()
    Inserts random data into POOL table.
### pool_section()
    Generates pool section which is the main anchor for match making, and is based on two atributes (rating and team_power).    
