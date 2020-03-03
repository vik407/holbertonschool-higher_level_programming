-- A script that displays the top 3 of cities temperature during July and August
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month = 7
OR month = 8 GROUP BY city
-- ordered by temperature (descending)
ORDER BY avg_temp DESC
-- only the top 3 cities
LIMIT 3;
