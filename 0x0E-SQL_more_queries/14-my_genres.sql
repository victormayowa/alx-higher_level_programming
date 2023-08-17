-- List all genres of the show Dexter
SELECT DISTINCT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres AS genres
ON tv_genres.id = genres.genre_id
INNER JOIN tv_shows AS shows
ON shows.id = genres.show.id
WHERE shows.title = 'Dexter'
ORDER BY tv_genres.name;
