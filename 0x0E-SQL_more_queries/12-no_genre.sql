-- Select tv_shows.title and tv_show_genres.genre_id from the tv_shows table and LEFT JOIN with tv_show_genres
-- Filter records where genre_id is NULL
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
