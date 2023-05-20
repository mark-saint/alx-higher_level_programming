--sda jkfasdj


SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.show_id

INNER JOIN tv_show
ON tv_show_genres.show_id = tv_show.id

WHERE tv_show.title != "Dexter"
ORDER BY tv_genres.name;
