create table users (
	id varchar(15) not null,
	username varchar(50) not null unique,
	password varchar(50) not null,
	usertype varchar(20) not null,
	primary key (id)
);
create table books (
	id varchar(15) not null,
	title varchar(50) not null,
	author varchar(50) not null,
	desc text,
	imguri varchar(50),
	primary key (id)
);
create table libraries (
	userid varchar(15) not null,
	bookid varchar(15) not null,
	progress varchar(15) not null,
	foreign key (userid) references users(id),
	foreign key (bookid) references books(id),
	primary key (userid, bookid)
);