CREATE TABLE rubrics (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name TEXT(30) NOT NULL
);

CREATE TABLE "source" (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name TEXT(70) NOT NULL
);

CREATE TABLE news (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	source_link TEXT NOT NULL,
	title TEXT(256) NOT NULL,
	"text" TEXT NOT NULL,
	"timestamp" REAL NOT NULL,
	image_link TEXT,
	rubric_id INTEGER NOT NULL,
	source_id INTEGER NOT NULL,
	CONSTRAINT news_FK FOREIGN KEY (rubric_id) REFERENCES rubrics(id),
	CONSTRAINT news_FK_1 FOREIGN KEY (source_id) REFERENCES "source"(id)
);

-- INSERT INTO source (name) VALUES ({!r0}), ({!r1});
-- INSERT INTO source (name) VALUES ('{0}'), ('{1}');
-- INSERT INTO rubrics (name) VALUES ('{0}'), ('{1}');
-- """
-- i = INSERT INTO source (name) VALUES {};
-- v = ('{}')
-- n = ["name", "name2", "name3"]
-- values = [v.format(name) for name in n]
-- sql = i.format(", ".join(values))
-- """

SELECT COUNT(id) FROM rubrics WHERE id IN (2, 4, 7, 9);

INSERT INTO news (source_link, title, "text", "timestamp", image_link, rubric_id, source_id)
VALUES ("https://tut.by", "News", "Full news", 12345.0, "https://image.png", 
(SELECT id FROM rubrics WHERE name='Sport'), 
(SELECT id FROM source WHERE name='REPUBLIC'));

DELETE FROM rubrics WHERE id=1;
