# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
###

####Fact Table
#songplays - records in log data associated with song plays i.e. records with page NextSong
#songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

songplay_table_create = ("""
CREATE TABLE songplays(
             songplay_id int PRIMARY KEY,\
             start_time timestamp,\
             user_id  varchar NOT NULL,\
             level varchar,\
             song_id varchar,\
             artist_id varchar,\
             session_id  int, \
             location    varchar,\
              user_agent  varchar
)
""")

###users - users in the app
#user_id, first_name, last_name, gender, level

user_table_create = ("""
CREATE TABLE users 
    (
        user_id    varchar PRIMARY KEY,\
        first_name varchar,\
        last_name  varchar,\ 
        gender     varchar,\
        level      varchar
    )
""")

##songs - songs in music database
##song_id, title, artist_id, year, duration

song_table_create = ("""

CREATE TABLE songs 
    (
        song_id   varchar PRIMARY KEY,\
        title     varchar,\
        artist_id varchar,\
        year      int,\
        duration  float
    )
""")

artist_table_create = ("""
CREATE TABLE artists 
    (
        artist_id varchar PRIMARY KEY,\
        name      varchar,\
        location  varchar,\
        latitude  varchar,\ 
        longitude varchar
    )

""")

time_table_create = ("""
CREATE TABLE time 
    (
        start_time timestamp PRIMARY KEY,\
        hour       int,\
        day        int,\
        week       int,\
        month      int,\
        year       int,\
        weekday    varchar
)
""")

# INSERT RECORDS

songplay_table_insert = (""" INSERT INTO songplays 
                             (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
                             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) 
                             ON CONFLICT (songplay_id) DO UPDATE SET
                             (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) = 
                             (EXCLUDED.start_time, EXCLUDED.user_id, EXCLUDED.level, EXCLUDED.song_id, EXCLUDED.artist_id, EXCLUDED.session_id,
                              EXCLUDED.location, EXCLUDED.user_agent)

""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]