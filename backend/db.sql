create table places (
 uuid varchar(36) PRIMARY KEY NOT NULL,
 name varchar(300) NOT NULL,
 address varchar(300),
 url varchar(300));

create table events (
 uuid varchar(36) PRIMARY KEY NOT NULL,
 place_uuid varchar(36) references places(uuid),
 name varchar(300) NOT NULL,
 date date,
 url varchar(300),
 comment varchar(300));
