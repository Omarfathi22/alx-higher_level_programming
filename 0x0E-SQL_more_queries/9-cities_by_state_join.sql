-- Select cities.id, cities.name, and states.name from the cities and states tables
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
