-- Primary Table
create table Register(
    Id int primary key,
    Date DATE not null,
    Description varchar(50) not null,
    Value int not null
)