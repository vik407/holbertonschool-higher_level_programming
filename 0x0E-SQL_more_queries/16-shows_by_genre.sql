-- A script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- Fields
SELECT tv_shows.title, tv_genres.name
-- Join A
FROM tv_shows LEFT OUTER JOIN tv_show_genres
-- Join A Conditions
ON tv_shows.id = tv_show_genres.show_id
-- Join B
LEFT OUTER JOIN tv_genres
-- Join B Conditions
ON tv_show_genres.genre_id = tv_genres.id
-- Order data
ORDER BY tv_shows.title, tv_genres.name ASC;
