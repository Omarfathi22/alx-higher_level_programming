-- Select all shows without the genre Comedy
SELECT DISTINCT title
FROM tv_shows
WHERE id NOT IN (
    -- Subquery to get the IDs of shows with the genre Comedy
    SELECT tv_show_id
    FROM tv_show_genres
    WHERE genre_id = (
        -- Subquery to get the ID of the genre Comedy
        SELECT id
        FROM tv_genres
        WHERE name = 'Comedy' -- Assuming the name of the genre is 'Comedy'
        LIMIT 1
    )
)
ORDER BY title ASC;
