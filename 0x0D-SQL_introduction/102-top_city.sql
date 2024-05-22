-- This script displays the top 3 cities' temperatures during July and August ordered by temperature (descending)
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8) -- Filter data for July and August
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3; -- Select only the top 3 cities
