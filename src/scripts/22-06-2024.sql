-- Primary Tables
CREATE TABLE IF NOT EXISTS Register(
    Id int primary key,
    Date DATE not null,
    Description varchar(50) not null,
    Value int not null
);
CREATE TABLE IF NOT EXISTS Week(
	Id int primary key,
	Const int not null
);
