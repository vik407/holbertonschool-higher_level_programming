-- A script that displays the max temperature of each state (ordered by State name).
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state
-- Order by state name
ORDER BY state ASC
-- Top 3
LIMIT 3;
