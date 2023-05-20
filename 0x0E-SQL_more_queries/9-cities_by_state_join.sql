-- sdfasdfds

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
WHERE cities.state_id = state.id;
