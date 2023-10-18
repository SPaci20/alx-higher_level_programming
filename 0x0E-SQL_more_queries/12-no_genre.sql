-- List shows without a linked genre
SELECT tv_shows.title, NULL AS genre_id
FROM tv_shows
WHERE tv_shows.id NOT IN (SELECT show_id FROM tv_show_genres)
ORDER BY tv_shows.title;