-- 1. How many copies of the film Hunchback Impossible exist in the inventory system?

-- Group by and Join
select 
f.title
,count(*) as n_items
from sakila.film as f
join sakila.inventory as i
using(film_id)
where f.title = "Hunchback Impossible"
group by f.title;

-- sub query

/* child query - gets the film id of title "Hunchback Impossible" */

(select
film_id 
from sakila.film
where title = "Hunchback Impossible");

select 
film_id, count(*) as n_copies from sakila.inventory
where film_id = 
	(select
	film_id 
    from sakila.film
    where title = "Hunchback Impossible")
group by film_id
order by n_copies desc;

-- 2. List all films whose length is longer than the average of all the films.

-- child query - calculate the average of all films

(select 
avg(length) 
from sakila.film);

select
film_id, title, length
from sakila.film
where length > (select avg(length) 
				from sakila.film)
order by length desc;

-- 3. Use subqueries to display all actors who appear in the film Alone Trip.

-- child query - get film_id of movie "Alone Trip"

(select film_id
from sakila.film
where title = "Alone Trip");

select
actor_id, first_name, last_name
from sakila.film_actor
join sakila.actor using(actor_id)
where film_id = (select film_id
                 from sakila.film
				 where title = "Alone Trip")
order by last_name;

-- 4. Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all movies categorized as family films.

-- child query - get the category_id for category family

(select 
category_id 
from sakila.category
where name = "Family");

select 
film_id ,title
from sakila.film
join sakila.film_category using(film_id)
where category_id = (select 
				     category_id 
				     from sakila.category
				     where name = "Family")
order by title;

-- 5. Get name and email from customers from Canada using subqueries.

-- Temporary table storing the city_id of the cities located on Canada
create temporary table canada_city_id
select city_id
from sakila.city
where country_id = (select country_id
					from sakila.country
                    where country = "Canada");
                    
-- Temporary table storing the adress_id of the adressess located in cities on Canada (using previous temp table)
create temporary table canada_city_address_id
select address_id
from sakila.address
where city_id in (select city_id
				  from canada_city_id);

-- and the final query
select customer_id, first_name, last_name, email
from sakila.customer
where address_id in (select address_id
					 from canada_city_address_id);
                     
--  Do the same with joins
select customer_id, first_name, last_name, email
from sakila.customer
join sakila.address using (address_id)
join sakila.city using (city_id)
join sakila.country using (country_id)
where country = "Canada";

/* 6. Which are films starred by the most prolific actor? 
Most prolific actor is defined as the actor that has acted in the most number of films. 
First you will have to find the most prolific actor and then use that actor_id to find the different films that he/she starred. */

-- chill query - find the most prolific actor

select actor_id, count(*) as n_films
from sakila.film_actor
group by actor_id
order by n_films desc
limit 1;

select film_id, title
from sakila.film
join sakila.film_actor using(film_id)
where actor_id = (select actor_id as n_films
				  from sakila.film_actor
				  group by actor_id
				  order by count(*) desc
				  limit 1);

select title from film
	where film_id in (select film_id from film_actor
		where actor_id = (select actor_id from film_actor
							group by actor_id
							order by count(actor_id) desc limit 1));



/* 7. Films rented by most profitable customer. 
You can use the customer table and payment table to find the most profitable customer 
ie the customer that has made the largest sum of payments */

-- chill query - find the most profitable costumer

select customer_id, round(sum(amount)) as profit
from sakila.payment
group by customer_id
order by profit desc
limit 1;

select distinct film_id, title
from sakila.film
join sakila.inventory using(film_id)
join sakila.rental using(inventory_id)
where customer_id = (select customer_id
					 from(select customer_id, round(sum(amount)) as profit
						  from sakila.payment
					      group by customer_id
					      order by profit desc
					      limit 1) as sub1);


/* 8. Customers who spent more than the average payments. */

-- chill query - get the average payment

select round(avg(amount), 2)
from sakila.payment;

select distinct customer_id, first_name, last_name
from sakila.customer
join sakila.payment using(customer_id)
where amount > (select round(avg(amount), 2)
				from sakila.payment);


                                   