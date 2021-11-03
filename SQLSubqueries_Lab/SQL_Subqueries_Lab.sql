# 1. How many copies of the film Hunchback Impossible exist in the inventory system?

## with group by
select a.film_id, a.title, count(*) as n_copies from sakila.film as a
inner join sakila.inventory as b
using(film_id)
where a.title = "Hunchback Impossible"
group by film_id
order by n_copies desc;

select film_id, count(*) as n_copies from sakila.inventory
where film_id = (select
	film_id from sakila.film
    where title = "Hunchback Impossible")
group by film_id
order by n_copies desc;

# 2. List all films whose length is longer than the average of all the films.
 
 select title,length from sakila.film
 where length > (select
	avg(length) from sakila.film)
order by length desc;

# 3.Use subqueries to display all actors who appear in the film Alone Trip.

select a.film_id, c.title, a.actor_id, b.first_name, b.last_name from sakila.film_actor as a
inner join sakila.actor as b
using(actor_id)
inner join sakila.film as c
using(film_id)
where film_id = (select film_id
	from sakila.film
    where title = "Alone Trip");

# result in a list

select a.film_id, c.title, group_concat(concat(b.first_name," ",b.last_name)) as actors_list from sakila.film_actor as a
inner join sakila.actor as b
using(actor_id)
inner join sakila.film as c
using(film_id)
where film_id = (select film_id
	from sakila.film
    where title = "Alone Trip");
    
# 4. Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all movies categorized as family films.

select a.film_id, c.title, a.category_id, b.`name` as category_name from sakila.film_category as a
inner join sakila.category as b
using(category_id)
inner join sakila.film as c
using(film_id)
where category_id = (select category_id
	from sakila.category
    where `name` = "Family");
    
# 5. Get name and email from customers from Canada using subqueries. 

# all the city_id in Canada

create temporary table canada_city_id 
select city_id from sakila.city
where country_id = (select country_id
	from sakila.country
    where country="Canada");
    
# all the address_id in Canada

create temporary table canada_address_id
select address_id from sakila.address
where city_id in (select *
	from canada_city_id);

select customer_id, first_name, last_name, email from sakila.customer
where address_id in (select *
	from canada_address_id);
 
 # Do the same with joins. Note that to create a join, you will have to identify the correct tables with their primary keys and foreign keys, that will help you get the relevant information.

select a.customer_id, a.first_name, a.last_name, a.email from sakila.customer as a
inner join sakila.address as b
using(address_id)
inner join sakila.city as c
using(city_id)
inner join sakila.country as d
using(country_id)
where d.country="Canada";

# 6. Which are films starred by the most prolific actor? Most prolific actor is defined as the actor that has acted in the most number of films. 
# First you will have to find the most prolific actor and then use that actor_id to find the different films that he/she starred.

## 6.1 with three subqueries to find the actor_id of the most prolific actor

create temporary table actor_id_maxfilms
select actor_id from (select actor_id, count(*) as n_films 
					  from sakila.film_actor
					  group by actor_id) as sub1
where n_films = (select max(n_films)
				 from (select actor_id, count(*) as n_films 
                       from sakila.film_actor
					   group by actor_id) as sub2);

## using rank to find the actor_id of the most prolific actor (one subquery)

create temporary table actor_id_nfilms
select *, rank() over (order by
						n_films desc
                        ) as Ranking
from (select actor_id, count(*) as n_films
	  from sakila.film_actor
      group by actor_id
      ) as sub1;

select a.film_id, b.title, a.actor_id, c.first_name, c.last_name from sakila.film_actor as a
inner join sakila.film as b
using(film_id)
inner join sakila.actor as c
using(actor_id)
where actor_id = (select actor_id
	from actor_id_nfilms
    where Ranking = 1);
    
# 7. Films rented by most profitable customer. You can use the customer table and payment table to find the most profitable customer ie the customer that has made the largest sum of payments

create temporary table customer_id_maxpayment
select customer_id from (select customer_id, sum(amount) as total from sakila.payment
	group by customer_id
	order by total desc) as sub1
where total = (select max(total)
	from (select customer_id, sum(amount) as total from sakila.payment
		group by customer_id
		order by total desc) as sub2);
        
select b.customer_id, b.first_name, b.last_name, a.film_id, c.title from sakila.inventory as a
inner join sakila.rental as d
using(inventory_id)
inner join sakila.customer as b
using(customer_id)
inner join sakila.film as c
using(film_id)
where b.customer_id = (select *
	from customer_id_maxpayment);
    
    # 8. Customers who spent more than the average payments.
    
    create temporary table customer_id_total_payment
    select customer_id, sum(amount) as total_payment from sakila.payment
    group by customer_id;
    
    select a.customer_id, b.first_name, b.last_name, sum(a.amount) as total from sakila.payment as a
	join sakila.customer as b
    using(customer_id)
    group by customer_id
    having total > (select avg(total_payment) 
			from customer_id_total_payment);
    
    
    
