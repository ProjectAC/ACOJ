create table user(
	uid integer primary key auto_increment,
	email varchar(30) not null unique,
	username varchar(30) not null unique,
	password varchar(60) not null,
	salt varchar(10) not null,
	op tinyint default 0,
	ban tinyint default 0
);

create table task(
	tid integer primary key auto_increment,
	owner integer default 0,
	title varchar(60),
	description text,
	level smallint default 13,
	foreign key (owner) references user(uid)
);

create table submission(
	sid integer primary key auto_increment,
	tid integer,
	uid integer,
	language varchar(10),
	code text,
	result varchar(200) default 'Pending',
	score numeric default 0,
	submit_time datetime default now(),
	foreign key (tid) references task(tid),
	foreign key (uid) references user(uid)
);