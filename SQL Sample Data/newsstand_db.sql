START TRANSACTION;

-- Use (swtich to) newsstand_db
USE newsstand_db;


DROP TABLE IF EXISTS editors;
DROP TABLE IF EXISTS sites;


CREATE TABLE sites(
    news_id int NOT NULL AUTO_INCREMENT,
    news_name varchar(255) NOT NULL,
    news_url varchar(255) NOT NULL,
    news_img_url varchar(255) NOT NULL DEFAULT '/static/images/blank.png',

    PRIMARY KEY (news_id)
);

INSERT INTO `sites` (`news_id`, `news_name`, `news_url`, `news_img_url`) VALUES
(1, 'The Guardian', 'https://www.theguardian.com', '/static/images/the-guardian-logo.png'),
(2, 'The Times', 'https://www.thetimes.co.uk/', '/static/images/The-Times-Logo.png'),
(3, 'The Scotsman', 'https://www.scotsman.com/', '/static/images/scotsman.png'),
(4, 'AnandTech', 'https://www.anandtech.com/', '/static/images/anand.png'),
(5, 'Ars Technica', 'https://arstechnica.com/', '/static/images/Ars_Technica_logo.png'),
(6, 'The Register', 'https://www.theregister.com/', '/static/images/Reg-logo-RED-copy.png'),
(7, 'ZDNet', 'https://www.zdnet.com/', '/static/images/zdnet-logo-large.png'),
(8, 'Windows Central', 'https://www.windowscentral.com/', '/static/images/new-wc-logo_0.png'),
(9, 'Krebs On Security', 'https://krebsonsecurity.com/', '/static/images/kos-27-03-2021.png'),
(10, 'The MEN', 'https://www.manchestereveningnews.co.uk/', '/static/images/men.png'),
(11, 'I Love Manchester', 'https://ilovemanchester.com', '/static/images/love.png'),
(12, 'Manchesters Finest', 'https://www.manchestersfinest.com/', '/static/images/finest.png');



CREATE TABLE editors(
    ed_id int NOT NULL AUTO_INCREMENT,
    news_id int NOT NULL,
    ed_fname varchar(255) NOT NULL,
    ed_lname varchar(255) NOT NULL,
    ed_date varchar(255) NOT NULL,

    PRIMARY KEY (ed_id),	
    FOREIGN KEY (news_id) REFERENCES sites(news_id) 

);

INSERT INTO `editors` (`ed_id`, `news_id`, `ed_fname`, `ed_lname`, `ed_date`) VALUES 
(1, 1, 'Katharine', 'Viner', 'June 2015'),
(2, 2, 'John', 'Witherow', '2013'),
(3, 3, 'Neil', 'McIntosh', 'February 2021'),
(4, 4, 'Ryan', 'Smith', '2014'),
(5, 5, 'Ken', 'Fisher', '1998'),
(6, 6, 'Chris', 'Williams', '1994'),
(7, 7, 'Larry', 'Dignan', '1991'),
(8, 8, 'Dan', 'Thorp-Lancaster', '2016'),
(9, 9, 'Brian', 'Krebs', 'December 2009'),
(10, 10, 'Darren', 'Thwaites', 'April 2018'),
(11, 11, 'Louise', ' Rhind-Tutt', 'June 2016'),
(12, 12, 'Steven', 'Pankhurst', 'April 2018');