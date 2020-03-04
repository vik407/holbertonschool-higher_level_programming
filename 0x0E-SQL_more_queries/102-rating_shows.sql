-- A script that lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Fields
SELECT title, SUM(rate) AS rating
-- Join
FROM tv_shows LEFT JOIN tv_show_ratings
-- Join condition
ON tv_shows.id = tv_show_ratings.show_id
-- Group by
GROUP BY title
-- Order data
ORDER BY rating DESC;
