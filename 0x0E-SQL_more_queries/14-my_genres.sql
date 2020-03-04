-- A script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- Fields
SELECT tv_genres.name
-- Join A
FROM tv_shows INNER JOIN tv_show_genres
-- Join A Conditions
ON tv_shows.id = tv_show_genres.show_id
-- Join B
INNER JOIN tv_genres
-- Join B Conditions
ON tv_show_genres.genre_id = tv_genres.id
-- Filter by
WHERE tv_shows.title = 'Dexter'
-- Order data
ORDER BY tv_genres.name ASC;
