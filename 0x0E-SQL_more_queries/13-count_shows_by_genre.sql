-- List genres and the number of shows linked to each genre
SELECT tv_show_genres.genre AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_show_genres
GROUP BY genre
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;