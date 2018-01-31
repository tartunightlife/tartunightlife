create table places (
 uuid uuid PRIMARY KEY NOT NULL,
 name varchar(45) NOT NULL,
 address varchar(45),
 url varchar(300));

create table event (
 uuid uuid PRIMARY KEY NOT NULL,
 place_uuid uuid references places(uuid),
 date date,
 url varchar(300),
 comment varchar(300));

