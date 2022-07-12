-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = genre_id
JOIN tv_shows ON tv_shows.id = show_id
WHERE name NOT IN (
	SELECT name
	FROM tv_genres
	JOIN tv_show_genres ON tv_genres.id = genre_id
	JOIN tv_shows ON tv_shows.id = show_id
	WHERE title = "Dexter"
)
GROUP BY name
ORDER BY name
