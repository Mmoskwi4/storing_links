--top 10 users with maximum links--
SELECT users_user.email, COUNT(links_link.id) AS count_links,
	SUM(CASE WHEN links_link.type = 'website' THEN 1 ELSE 0 END) AS website,
	SUM(CASE WHEN links_link.type = 'book' THEN 1 ELSE 0 END) AS book,
	SUM(CASE WHEN links_link.type = 'article' THEN 1 ELSE 0 END) AS article,
	SUM(CASE WHEN links_link.type = 'music' THEN 1 ELSE 0 END) AS music,
	SUM(CASE WHEN links_link.type = 'video' THEN 1 ELSE 0 END) AS video
FROM users_user
JOIN links_link ON users_user.id = links_link.owner_id
GROUP BY users_user.id, users_user.email
ORDER BY count_links DESC, users_user.date_joined ASC LIMIT 10;