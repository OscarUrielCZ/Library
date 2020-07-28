create table users (
	id varchar(36) not null,
	username varchar(50) not null unique,
	password varchar(50) not null,
	primary key (id)
);
create table books (
	id varchar(36) not null,
	title varchar(100) not null,
	author varchar(50) not null,
	description text,
	imguri varchar(50),
	primary key (id)
);
create table libraries (
	userid varchar(36) not null,
	bookid varchar(36) not null,
	progress integer not null,
	foreign key (userid) references users(id),
	foreign key (bookid) references books(id),
	primary key (userid, bookid)
);