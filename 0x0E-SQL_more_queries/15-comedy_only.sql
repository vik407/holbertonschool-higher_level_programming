-- A script that lists all Comedy shows in the database hbtn_0d_tvshows.
-- Fields
SELECT tv_shows.title
-- Join A
FROM tv_shows INNER JOIN tv_show_genres
-- Join A Conditions
ON tv_shows.id = tv_show_genres.show_id
-- Join B
INNER JOIN tv_genres
-- Join B Conditions
ON tv_show_genres.genre_id = tv_genres.id
-- Filter by
WHERE tv_genres.name = 'Comedy'
-- Order data
ORDER BY tv_shows.title ASC;
