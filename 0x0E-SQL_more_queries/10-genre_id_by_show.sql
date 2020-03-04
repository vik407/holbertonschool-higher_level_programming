-- A script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Fields
SELECT tv_shows.title, tv_show_genres.genre_id
-- Join
FROM tv_shows INNER JOIN tv_show_genres
-- Join condition
ON tv_shows.id = tv_show_genres.show_id
-- Order data
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
