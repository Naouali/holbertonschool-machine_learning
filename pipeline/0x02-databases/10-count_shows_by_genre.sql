-- script to list all genres that have shows

SELECT g.name AS genre, count(i.show_id) AS number_of_shows
FROM tv_genres AS g
INNER JOIN tv_show_genres AS i
ON g.id = i.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC;
