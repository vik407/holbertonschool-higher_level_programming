-- A script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT name, SUM(rate) AS rating
-- Join A
FROM tv_genres RIGHT JOIN tv_show_genres
-- Join A condition
ON tv_show_genres.genre_id = tv_genres.id
-- Join B
LEFT JOIN tv_show_ratings
-- Join B condition
ON tv_show_ratings.show_id = tv_show_genres.show_id
-- Group by
GROUP BY name
-- Order data
ORDER BY rating DESC;
