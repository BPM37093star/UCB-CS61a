.read lab13.sql

CREATE TABLE su19favpets AS
  SELECT pet, count(*) FROM students GROUP BY pet ORDER BY count(*) DESC, pet ASC LIMIT 10;


CREATE TABLE su19dog AS
  SELECT pet, count(*) FROM students WHERE pet = 'dog';


CREATE TABLE obedienceimages AS
  SELECT seven, instructor, count(*) FROM students WHERE seven = '7' GROUP BY instructor;
