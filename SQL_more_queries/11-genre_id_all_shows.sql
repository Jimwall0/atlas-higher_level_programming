-- Import the database dump of hbtn_0d_tvshows to your MySQL server: download (same as 10-genre_id_by_show.sql)
SELECT tv_shows.title, IF(tv_show_genres.genre_id IS NULL, NULL, tv_show_genres.genre_id) AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
