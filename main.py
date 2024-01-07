import oracledb
from playaudio import playaudio
import random

print("Connecting...")
params = oracledb.ConnectParams(host="bd-dc.cs.tuiasi.ro", port=1539, service_name="orcl")
connection = oracledb.connect(
    user="bd154",
    password="bd154",
    params=params
)
print("Successfully connected to Oracle Database")
cursor = connection.cursor()


def dropTablesBefore(cursor):
    # Delete already existing tables if there are
    cursor.execute("drop table songs")
    cursor.execute("drop table ps")
    cursor.execute("drop table playlists")
    cursor.execute("drop table users")
    cursor.execute("drop table files")


def createTableUser(cursor):
    # Create a table
    cursor.execute("""create table users (
    ID_User number(4) not null,
    CONSTRAINT PK_User primary key(ID_User),
    Name_User varchar(50) not null
    )""")
    # Insert some data
    cursor.execute("insert into users (ID_User, Name_User) VALUES (4884, 'ABBA')")
    cursor.execute("insert into users (ID_User, Name_User) VALUES (2016, 'Martin Garrix')")
    cursor.execute("insert into users (ID_User, Name_User) VALUES (1960, 'Rednex')")
    cursor.execute("insert into users (ID_User, Name_User) VALUES (1990, 'Cindy Lauper')")
    cursor.execute("insert into users (ID_User, Name_User) VALUES (2023,'The Just Dancers')")
    cursor.execute("insert into users (ID_User, Name_User) VALUES (3030, 'Elvis Presley')")
    cursor.execute("insert into users (ID_User, Name_User) VALUES (3484, 'Zara Larsson')")
    cursor.execute("insert into users (ID_User, Name_User) VALUES (8342, 'Becky G')")
    cursor.execute("insert into users (ID_User, Name_User) VALUES (8341, 'Cher Lloyd')")
    cursor.execute("insert into users (ID_User, Name_User) VALUES (2000, 'Boney M')")
    cursor.execute("insert into users (ID_User, Name_User) VALUES (2002, 'Fatboy Slim')")
    cursor.execute("insert into users (ID_User, Name_User) VALUES (1221, 'Nicki Minaj')")
    cursor.execute("insert into users (ID_User, Name_User) VALUES (7089, 'USER')")


def createTablePlaylist(cursor):
    # Create a table
    cursor.execute(""" create table playlists(
    ID_Playlist number(5) not null,
    Name_Playlist varchar(50) not null,
    ID_Maker number(4),
    constraint PK_Playlist primary key (ID_Playlist),
    constraint ID_Maker foreign key (ID_Maker) references users(ID_User))""")
    # Insert some data
    cursor.execute("insert into playlists (ID_Playlist, Name_Playlist, ID_Maker) VALUES (32115, 'Dance tunes',7089)")
    cursor.execute("insert into playlists (ID_Playlist, Name_Playlist, ID_Maker) VALUES (52124, 'Women in music',3484)")
    cursor.execute("insert into playlists (ID_Playlist, Name_Playlist, ID_Maker) VALUES (19871, 'Old but gold',7089)")
    cursor.execute("insert into playlists (ID_Playlist, Name_Playlist, ID_Maker) VALUES (68987, 'DJ masters',2016)")
    cursor.execute("insert into playlists (ID_Playlist, Name_Playlist, ID_Maker) VALUES (11211, 'Liked songs',7089)")


def createTableFiles(cursor):
    # Create a table
    cursor.execute("""create table files(
    ID_Song number(3) not null,
    File_Song varchar(40) not null)""")
    # Insert some data
    cursor.execute("insert  into files (ID_Song, File_Song) VALUES (700, 'music/abbasos.ogg')")
    cursor.execute("insert  into files (ID_Song, File_Song) VALUES (701, 'music/animalscmu.ogg')")
    cursor.execute("insert  into files (ID_Song, File_Song) VALUES (702, 'music/cotton.ogg')")
    cursor.execute("insert  into files (ID_Song, File_Song) VALUES (703, 'music/girlsjust.ogg')")
    cursor.execute("insert  into files (ID_Song, File_Song) VALUES (704, 'music/ifyouwannaparty_demo.mp3')")
    cursor.execute("insert  into files (ID_Song, File_Song) VALUES (705, 'music/jailhouse.ogg')")
    cursor.execute("insert  into files (ID_Song, File_Song) VALUES (706, 'music/lush.ogg')")
    cursor.execute("insert  into files (ID_Song, File_Song) VALUES (707, 'music/oath.ogg')")
    cursor.execute("insert  into files (ID_Song, File_Song) VALUES (708, 'music/rasputin.ogg')")
    cursor.execute("insert  into files (ID_Song, File_Song) VALUES (709, 'music/lush.ogg')")
    cursor.execute("insert  into files (ID_Song, File_Song) VALUES (710, 'music/superbass.ogg')")


def createTableSong(cursor):
    # Create a table
    cursor.execute("""create table songs (
    ID_Song number(3) not null,
    Title_Song varchar(50) not null,
    ID_Artist number(4))""")
    # Insert some data
    cursor.execute("insert  into songs (ID_Song, Title_song, ID_Artist) VALUES (700, 'S.O.S.',4884)")
    cursor.execute("insert  into songs (ID_Song, Title_song, ID_Artist) VALUES (701, 'Animals', 2016)")
    cursor.execute("insert  into songs (ID_Song, Title_song, ID_Artist) VALUES (702, 'Cotton Eyed Joe',1960)")
    cursor.execute("insert  into songs (ID_Song, Title_song, ID_Artist) VALUES (703, 'Girls Just Wanna Have Fun',1990)")
    cursor.execute("insert  into songs (ID_Song, Title_song, ID_Artist) VALUES (704, 'If You Wanna Party',2023)")
    cursor.execute("insert  into songs (ID_Song, Title_song, ID_Artist) VALUES (705, 'Jailhouse Rock',3030)")
    cursor.execute("insert  into songs (ID_Song, Title_song, ID_Artist) VALUES (706, 'Lush Life',3484)")
    cursor.execute("insert  into songs (ID_Song, Title_song, ID_Artist) VALUES (707, 'Oath',8341)")
    cursor.execute("insert  into songs (ID_Song, Title_song, ID_Artist) VALUES (707, 'Oath',8342)")
    cursor.execute("insert  into songs (ID_Song, Title_song, ID_Artist) VALUES (708, 'Rasputin',2000)")
    cursor.execute("insert  into songs (ID_Song, Title_song, ID_Artist) VALUES (709, 'Lush Life',3484)")
    cursor.execute("insert  into songs (ID_Song, Title_song, ID_Artist) VALUES (710, 'Super Bass',1221)")


def createTablePS(cursor):
    # Create a table
    cursor.execute("""create table PS (
    ID_PS_Song number(3), 
    ID_PS_Playlist number(5),
    constraint FK_PS_Playlists foreign key (ID_PS_Playlist) references playlists(ID_Playlist))""")
    # Insert some data
    cursor.execute("insert into PS (ID_PS_Song, ID_PS_Playlist) VALUES (701, 32115)")
    cursor.execute("insert into PS (ID_PS_Song, ID_PS_Playlist) VALUES (702, 32115)")
    cursor.execute("insert into PS (ID_PS_Song, ID_PS_Playlist) VALUES (703, 32115)")
    cursor.execute("insert into PS (ID_PS_Song, ID_PS_Playlist) VALUES (704, 32115)")

    cursor.execute("insert into PS (ID_PS_Song, ID_PS_Playlist) VALUES (710, 52124)")
    cursor.execute("insert into PS (ID_PS_Song, ID_PS_Playlist) VALUES (706, 52124)")

    cursor.execute("insert into PS (ID_PS_Song, ID_PS_Playlist) VALUES (700, 19871)")

    cursor.execute("insert into PS (ID_PS_Song, ID_PS_Playlist) VALUES (701, 68987)")
    cursor.execute("insert into PS (ID_PS_Song, ID_PS_Playlist) VALUES (709, 68987)")

    cursor.execute("insert into PS (ID_PS_Song, ID_PS_Playlist) VALUES (704, 11211)")


def deletePlaylist(playlistname, cursor):
    cursor.execute(
        "delete from PS where ID_PS_Playlist=(select id_playlist from playlists where name_playlist='" + playlistname + "')")
    cursor.execute("delete from playlists where Name_Playlist='" + playlistname + "'")
    print("Playlist deleted successfully")
    connection.commit()


def RegisterUsername(username, cursor):
    cursor.execute("select name_user from users where name_user = '" + username + "'")
    row = cursor.fetchone()
    if row is not None:
        userExists = 1
    else:
        userExists = 0
    if userExists == 0:
        newID = random.randint(0, 9999)
        cmd = "insert into users (ID_User, Name_User) VALUES ( " + str(newID) + ", '" + username + "')"
        cursor.execute(cmd)
        print("User " + username + " registered successfully")
        connection.commit()
    else:
        print("User " + username + " logged in successfully")


def playSong(songname, cursor):
    cursor.execute(
        "select file_song from files f,songs s where f.id_song = s.id_Song and s.title_Song = '" + songname + "'")
    row = cursor.fetchone()
    print("Now playing: " + songname + "...")
    playaudio(row[0])
    print("Thank you for listening!")


def showPlaylistSongs(username, playlistname, cursor):
    cmd = "select distinct s.Title_Song, u.Name_User from songs s, users u, PS ps, playlists p where s.ID_Song = ps.id_ps_song and ps.id_ps_playlist = p.id_playlist and p.name_playlist = 'Women in music' and s.ID_Artist = u.ID_User and p.id_maker = (select ID_user from users where name_user = '" + username + "')"
    cursor.execute(cmd)
    rows = cursor.fetchall()
    song_artists_dict = {}

    for song, artist in rows:
        if song in song_artists_dict:
            song_artists_dict[song].append(artist)
        else:
            song_artists_dict[song] = [artist]
    for song, artists in song_artists_dict.items():
        print(song + " - " + ', '.join(artists))


def showUserPlaylists(username, cursor):
    for row in cursor.execute(
            "select name_playlist from playlists where id_maker = (select id_user from users where name_user = '" + username + "')"):
        print(row[0])


def addSongToPlaylist(songname, playlistname, cursor):
    cursor.execute(
        "select Title_Song, Name_User from songs s, users u where s.ID_Artist = u.ID_User and s.Title_Song = '" + songname + "'")
    rows = cursor.fetchall()
    artist = ""
    for row in rows:
        print(row[1])
        artist = artist + str(row[1]) + ' and '
    artist = artist[:-5]
    print("We found the song " + songname + " by " + artist)
    print("Would you like to add it? (yes/no)")
    confirm = input(">>>>>")
    if confirm == 'yes':
        cursor.execute("select id_song from songs where title_song = '" + songname + "'")
        validsong = cursor.fetchone()
        cursor.execute(
            "insert into PS (ID_PS_Song, ID_PS_Playlist) VALUES (" + str(
                validsong[0]) + ",(select id_playlist from playlists where name_playlist = '" + playlistname + "'))")
        print("Song added successfully")
        connection.commit()


def addPlaylistByUser(username, chosePlaylistName, choseUserName, cursor):
    newID = random.randint(0, 99999)
    # Get a list of songs
    cursor.execute(
        "select ps.id_ps_song from PS ps, playlists p where ps.id_ps_playlist = p.id_playlist and p.id_maker != (select id_user from users where name_user = '" + username + "') and p.name_playlist = '" + chosePlaylistName + "'")
    rows = cursor.fetchall()
    cursor.execute("insert into playlists (ID_Playlist, Name_Playlist, ID_Maker) VALUES ( " + str(
        newID) + ", '" + chosePlaylistName + "'," + "(select id_user from users where name_user = '" + username + "'))")
    for row in rows:
        cursor.execute("insert into PS (ID_PS_Song, ID_PS_Playlist) VALUES (" + str(row[0]) + ", " + str(newID) + ")")
    print("Playlist added successfully")
    connection.commit()


def deleteSongFromPlaylist(songname, playlistname, cursor):
    cursor.execute(
        "delete from PS where ID_PS_Song=(select id_song from songs where title_song = '" + songname + "') and id_ps_playlist = (select id_playlist from playlists where name_playlist = '" + playlistname + "')")
    print("Song deleted successfully!")
    connection.commit()


if __name__ == "__main__":
    # testari
    # dropTablesBefore(cursor)
    # createTableUser(cursor)
    # createTablePlaylist(cursor)
    # createTableSong(cursor)
    # createTableFiles(cursor)
    # createTablePS(cursor)
    print("__________________________________________________________________")
    print('Welcome to E-Player, an Erich21(tm) Original music service.')
    print('Enter your username:')
    username = input('>>')
    print('Hello ' + username + '!')
    RegisterUsername(username, cursor)
    print('To quit the application, press Q at any time')
    print('To go to the previous menu, press B at any time')
    while True:
        print("__________________________________________________________________")
        showUserPlaylists(username, cursor)
        print('Here are your playlists. What would you like to do?')
        print('1. Open')
        print('2. Delete')
        print('3. Add')
        chosePlaylistOption = input('>>')

        if chosePlaylistOption == '1':
            print("__________________________________________________________________")
            print("Which playlist would you like to open?")
            chosePlaylistName = input(">>>")
            showPlaylistSongs(username, chosePlaylistName, cursor)
            print("What would you like to do now?")
            print("1. Play a song")
            print("2. Add a song")
            print("3. Delete a song")
            choseSongOpt = input(">>>")
            if choseSongOpt == '1':
                print("__________________________________________________________________")
                print("Which song would you like to play?")
                chosesong = input('>>>>')
                playSong(chosesong, cursor)
            if choseSongOpt == '2':
                print("__________________________________________________________________")
                print("Let's search for a song! Type the song name you'd like to add")
                songname = input('>>>>')
                addSongToPlaylist(songname, chosePlaylistName, cursor)
            if choseSongOpt == '3':
                print("__________________________________________________________________")
                print("Which song would you like to delete?")
                songname = input('>>>>')
                deleteSongFromPlaylist(songname, chosePlaylistName, cursor)
            if choseSongOpt == 'Q':
                break
        if chosePlaylistOption == '2':
            print("__________________________________________________________________")
            print("Which playlist would you like to delete?")
            chosePlaylistName = input(">>>")
            deletePlaylist(chosePlaylistName, cursor)
        if chosePlaylistOption == '3':
            print("__________________________________________________________________")
            print("Let's find some playlists made by other people. Which user would you like to search for?")
            choseUserName = input(">>>")
            print("User " + choseUserName + " has the following playlists:")
            showUserPlaylists(choseUserName, cursor)
            print("Which playlist would you like to save?")
            chosePlaylistName = input(">>>")
            addPlaylistByUser(username, chosePlaylistName, choseUserName, cursor)
        if chosePlaylistOption == 'Q':
            break
    print("See you next time...")
    connection.close()
