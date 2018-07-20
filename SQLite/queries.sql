-- Instructions

-- Query all of the entries in the Genre table
    SELECT * from Genre

-- Using the INSERT statement, add one of your favorite artists to the Artist table.
    INSERT into Artist (artistname, yearestablished)
    values ("Kitty Purry", 2018)

-- Using the INSERT statement, add one, or more, albums by your artist to the Album table.
    INSERT into Album
    SELECT null, "Remixes from Hell", 2018, 700, "Seperate Kitty", artist.ArtistId, genre.GenreId
    FROM Artist, Genre
    WHERE artist.artistname = "Kitty Purry"
    AND genre.label = "Pop"

-- Using the INSERT statement, add some songs that are on that album to the Song table.
    INSERT into Song
    SELECT null, "Oops, I'm not a fan", 80, 07/17/2018, genre.GenreId, artist.ArtistId, album.albumid
    WHERE artist.artistname = "Kitty Purry"
    AND genre.label = "Pop"
    AND album.title = "Remixes from Hell"
-- Write a SELECT query that provides the song titles, album title, and artist name for all of the data you just entered in. Use the LEFT JOIN keyword sequence to connect the tables, and the WHERE keyword to filter the results to the album and artist you added.
    SELECT s.title as "Song Name", al.title as "Album Name", ar.artistname as "Artist Name"
    LEFT JOIN 
-- Reminder: Direction of join matters. Try the following statements and see the difference in results.

-- SELECT a.Title, s.Title FROM Album a LEFT JOIN Song s ON s.AlbumId = a.AlbumId;
-- SELECT a.Title, s.Title FROM Song s LEFT JOIN Album a ON s.AlbumId = a.AlbumId;
-- Write a SELECT statement to display how many songs exist for each album. You'll need to use the COUNT() function and the GROUP BY keyword sequence.

-- Write a SELECT statement to display how many songs exist for each artist. You'll need to use the COUNT() function and the GROUP BY keyword sequence.

-- Write a SELECT statement to display how many songs exist for each genre. You'll need to use the COUNT() function and the GROUP BY keyword sequence.

-- Using MAX() function, write a select statement to find the album with the longest duration. The result should display the album title and the duration.

-- Using MAX() function, write a select statement to find the song with the longest duration. The result should display the song title and the duration.

-- Modify the previous query to also display the title of the album