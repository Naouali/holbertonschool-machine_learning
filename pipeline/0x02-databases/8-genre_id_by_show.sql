-- list tv shows that have genres

SELECT s.title, i.genre_id
FROM tv_shows AS s
INNER JOIN tv_show_genres AS i
ON s.id = i.show_id
ORDER BY s.title ASC, i.genre_id ASC;
