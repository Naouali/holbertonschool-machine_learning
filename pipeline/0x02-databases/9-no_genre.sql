-- list tv shows that have genres

SELECT s.title, i.genre_id
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS i
ON s.id = i.show_id
WHERE i.show_id IS NULL
ORDER BY s.title ASC, i.genre_id ASC;
