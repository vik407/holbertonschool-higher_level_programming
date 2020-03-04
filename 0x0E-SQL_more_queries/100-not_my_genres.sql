-- A script that uses the hbtn_0d_tvshows database to list all genres
-- Fields
SELECT DISTINCT tv_genres.name FROM tv_genres
-- Condition not in subquery
WHERE tv_genres.name NOT IN
(SELECT tv_genres.name FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter')
-- Order data
ORDER BY tv_genres.name ASC;
