DROP TABLE IF EXISTS `Advertiser`;
DROP TABLE IF EXISTS `Ad`;

CREATE TABLE `Advertiser` (
  id int,
  name varchar(100) NOT NULL,
  clicks int DEFAULT 0,
  views int DEFAULT 0,
  PRIMARY KEY ( id )
);

CREATE TABLE `Ad` (
  id int,
  title varchar(100) NOT NULL,
  imgUrl varchar(1000) NOT NULL,
  link varchar(1000) NOT NULL,
  clicks int DEFAULT 0,
  views int DEFAULT 0,
  owner_id int references Advertiser(id) NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO Advertiser(id, name) VALUES (1, "name1");
INSERT INTO Advertiser(id, name) VALUES (2, "name2");

INSERT INTO Ad(id, title, link, imgUrl, owner_id) VALUES (1, "no-title", "link1", "url1", 1);
INSERT INTO Ad(id, title, link, imgUrl, owner_id) VALUES (2, "no-title", "link2", "url2", 1);
INSERT INTO Ad(id, title, link, imgUrl, owner_id) VALUES (3, "no-title", "link3", "url3", 2);

SELECT * FROM Advertiser;
SELECT * FROM Ad;