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
        user_id    varchar PRIMARY KEY,
        first_name varchar,
        last_name  varchar,
        gender     varchar,
        level      varchar
    )
""")

##songs - songs in music database
##song_id, title, artist_id, year, duration

song_table_create = ("""

CREATE TABLE songs 
    (
        song_id   varchar PRIMARY KEY,
        title     varchar,
        artist_id varchar,
        year      int,
        duration  float
    )
""")

artist_table_create = ("""
CREATE TABLE artists 
    (
        artist_id varchar PRIMARY KEY,
        name      varchar,
        location  varchar,
        latitude  varchar,
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
#https://www.postgresql.org/docs/9.5/sql-insert.html

songplay_table_insert = (""" INSERT INTO songplays 
                             (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)  
                             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)  
                             ON CONFLICT (songplay_id) DO UPDATE SET  
                             (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) =   
                             (EXCLUDED.start_time, EXCLUDED.user_id, EXCLUDED.level, EXCLUDED.song_id, EXCLUDED.artist_id, EXCLUDED.session_id, 
                              EXCLUDED.location, EXCLUDED.user_agent)

""")

user_table_insert = (""" INSERT INTO users 
                         (user_id, first_name, last_name, gender, level) 
                         VALUES (%s, %s, %s, %s, %s) 
                         ON CONFLICT (user_id) DO UPDATE SET 
                         (gender, level) = (
                         CASE WHEN users.gender != EXCLUDED.gender 
                         THEN users.gender || ';' || EXCLUDED.gender ELSE users.gender END, 
                         CASE WHEN users.level != EXCLUDED.level
                         THEN users.level || ';' || EXCLUDED.level ELSE users.level END)
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) 
                         VALUES (%s, %s, %s, %s, %s) 
                         ON CONFLICT (song_id) DO UPDATE SET 
                         (title, artist_id, year, duration) = (EXCLUDED.title, EXCLUDED.artist_id, EXCLUDED.year, EXCLUDED.duration)


""")

artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude) 
                           VALUES (%s, %s, %s, %s, %s) 
                           ON CONFLICT (artist_id) DO UPDATE SET 
                           (name, location, latitude, longitude) = 
                           (CASE WHEN artists.name != EXCLUDED.name 
                            THEN artists.name || ';' || EXCLUDED.name ELSE artists.name END,
                            CASE WHEN artists.location != EXCLUDED.location
                            THEN artists.location ||';'|| EXCLUDED.location ELSE artists.location END, 
                            CASE WHEN artists.latitude != EXCLUDED.latitude
                            THEN artists.latitude ||';'|| EXCLUDED.latitude ELSE artists.latitude END,
                            CASE WHEN artists.longitude != EXCLUDED.longitude
                            THEN artists.longitude ||';'|| EXCLUDED.longitude ELSE artists.longitude END)

""")


time_table_insert = ("""INSERT INTO time 
                         (start_time, hour, day, week, month, year, weekday) 
                         VALUES (%s, %s, %s, %s, %s, %s, %s) 
                         ON CONFLICT (start_time) DO UPDATE SET
                         (hour, day, week, month, year, weekday) = (EXCLUDED.hour, EXCLUDED.day, EXCLUDED.week, EXCLUDED.month, EXCLUDED.year, EXCLUDED.weekday)
""")

# FIND SONGS

song_select = ("""SELECT songs.artist_id, songs.song_id FROM songs 
                   JOIN artists ON songs.artist_id = artists.artist_id 
                   WHERE songs.title = %s AND
                   artists.name = %s AND
                   songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]