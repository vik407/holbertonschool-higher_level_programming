-- Lists all genres from hbtn_0d_tvshows and displays the number of shows
-- Fields
SELECT tv_genres.name AS genre, count(*) AS number_of_shows
-- Join
FROM tv_show_genres LEFT JOIN tv_genres
-- Join condition
ON tv_show_genres.genre_id = tv_genres.id
-- Group by
GROUP BY tv_genres.name
-- Order data
ORDER BY number_of_shows DESC;
