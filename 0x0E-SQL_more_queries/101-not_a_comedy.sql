-- A script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- Fields A
SELECT DISTINCT title
FROM tv_shows
-- Join A
LEFT JOIN tv_show_genres
-- Join A condition
ON tv_shows.id = tv_show_genres.show_id
-- Join B
LEFT JOIN tv_genres
-- Join B condition
ON tv_show_genres.genre_id = tv_genres.id
-- Subquery with other two joins
WHERE title NOT IN (SELECT title FROM tv_genres LEFT JOIN tv_show_genres
ON genre_id = tv_genres.id LEFT JOIN tv_shows
ON show_id = tv_shows.id WHERE name = "Comedy")
-- Order data
ORDER BY title ASC;
