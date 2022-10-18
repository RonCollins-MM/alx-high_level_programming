--  List all cities in the city of carlifornia
SELECT id, name
FROM
	(SELECT * FROM cities WHERE state_id =
		(SELECT id FROM states WHERE name = 'California')) AS name
