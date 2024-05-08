-- mysql

create database to_do_list;

use to_do_list;

create table tasks(
	id int primary key auto_increment,
    title nvarchar(255) not null,
    description_task nvarchar(255),
    early_date char(11),
    last_date char(11)
);

create table progress(
	id int,
    title nvarchar(255) not null,
    description_task nvarchar(255),
    early_date char(11),
    last_date char(11)
);

create table completed(
	id int,
    title nvarchar(255) not null,
    description_task nvarchar(255),
    early_date char(11),
    last_date char(11)
);

-- select * from completed;

-- drop database to_do_list;