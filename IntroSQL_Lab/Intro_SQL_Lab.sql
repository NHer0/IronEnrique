# Exercise 2

select * from sakila.actor;
select * from sakila.address;
select * from sakila.category;
select * from sakila.city;
select * from sakila.country;
select * from sakila.customer;
select * from sakila.film;
select * from sakila.film_actor;
select * from sakila.film_category;
select * from sakila.film_text;
select * from sakila.inventory;
select * from sakila.language;
select * from sakila.payment;
select * from sakila.reantal;
select * from sakila.staff;
select * from sakila.store;

# Exercise 3

select title from sakila.film;

# Exercise 4

select distinct(name) as language from sakila.language;

# Exercise 5.1

select count(store_id) from sakila.store;

# Exercise 5.2

select count(distinct(staff_id)) from sakila.staff;

# Exercise 5.3

select first_name from sakila.staff


