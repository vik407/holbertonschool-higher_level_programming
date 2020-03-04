-- A script that lists all cities contained in the database hbtn_0d_usa.
-- Fields
SELECT cities.id, cities.name, states.name
-- Join
FROM cities INNER JOIN states
-- Join condition
ON cities.state_id = states.id
-- Order data
ORDER BY cities.id ASC;
