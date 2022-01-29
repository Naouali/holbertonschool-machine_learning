-- List shows with the sum of their ratings

SELECT g.name, SUM(r.rate) AS rating
FROM tv_genres AS g
INNER JOIN tv_show_genres AS t
ON g.id = t.genre_id
INNER JOIN tv_show_ratings AS r
ON t.show_id = r.show_id
GROUP BY g.name
ORDER BY rating DESC;


