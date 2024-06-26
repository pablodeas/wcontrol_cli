-- Primary Tables
CREATE TABLE IF NOT EXISTS Register(
    Id SERIAL primary key,
    Date DATE not null,
    Description varchar(50) not null,
    Value int not null
);
CREATE TABLE IF NOT EXISTS Week(
	Id SERIAL primary key,
	Const int not null
);
