-- A script that displays the average temperature by city
SELECT city, AVG(value) AS avg_temp FROM temperatures
-- ordered by temperature (descending).
GROUP BY city ORDER BY avg_temp DESC;
