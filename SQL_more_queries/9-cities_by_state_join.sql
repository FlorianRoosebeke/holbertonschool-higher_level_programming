-- Lists all cities from hbtn_0d_usa with their corresponding state.
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
