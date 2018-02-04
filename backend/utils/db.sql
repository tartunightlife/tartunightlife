create table places (
 fb_id varchar(300) PRIMARY KEY NOT NULL,
 name varchar(300) NOT NULL,
 address varchar(300),
 url varchar(300));

create table events (
 id varchar(300) PRIMARY KEY NOT NULL,
 place_id varchar(300) references places(fb_id),
 name varchar(300) NOT NULL,
 date date,
 url varchar(300),
 comment varchar(300));
