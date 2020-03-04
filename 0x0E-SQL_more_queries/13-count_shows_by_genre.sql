-- A script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Fields
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_shows
-- Join
FROM tv_show_genres LEFT JOIN tv_genres
-- Join condition
ON tv_show_genres.genre_id = tv_genres.id
-- Group by
GROUP BY genre
-- Order data
ORDER BY number_shows DESC;
