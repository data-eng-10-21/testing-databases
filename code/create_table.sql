drop table if exists customers;

create table customers (
    id serial primary key,
    first_name varchar(250),
    last_name varchar(250),
    category varchar(250)
);