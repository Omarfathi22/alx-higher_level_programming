-- Select all genres not linked to the show Dexter
SELECT DISTINCT name
FROM tv_genres
WHERE id NOT IN (
    -- Subquery to get the genre IDs linked to the show Dexter
    SELECT genre_id
    FROM tv_show_genres
    WHERE tv_show_id = (
        -- Subquery to get the ID of the show Dexter
        SELECT id
        FROM tv_shows
        WHERE title = 'Dexter' -- Assuming the title of the show is 'Dexter'
        LIMIT 1
    )
)
ORDER BY name ASC;
