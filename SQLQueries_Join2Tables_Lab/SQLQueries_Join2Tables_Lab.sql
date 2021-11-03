# 1. Which actor has appeared in the most films?

select actor_id, a.first_name, a.last_name, count(*) as n_films from sakila.actor as a
inner join sakila.film_actor as b
using(actor_id)
group by actor_id
order by n_films desc;

## Gina Degeneres is the actress wich more appereances

# 2. Most active customer (the customer that has rented the most number of films)

select a.customer_id, a.first_name, a.last_name, count(b.rental_id) as n_rentals from sakila.customer as a
inner join sakila.rental as b
using(customer_id)
group by customer_id
order by n_rentals desc;

## Eleanor Hunt is the client with more rentals

# 3. List number of films per category.

select category_id, a.name, count(*) as n_films from sakila.category as a
inner join sakila.film_category as b
using(category_id)
group by category_id
order by n_films desc;

## Category "Sports" has the higher number of films, 74

# 4. Display the first and last names, as well as the address, of each staff member.

select a.staff_id, a.first_name, a.last_name, b.address from sakila.staff as a
inner join sakila.address as b
using(address_id);

# 5. Display the total amount rung up by each staff member in August of 2005.

select staff_id, a.first_name, a.last_name, sum(b.amount) as total_received_payment from sakila.staff as a
inner join sakila.payment as b
using(staff_id)
where b.payment_date like "2005-08-%"
group by staff_id;

# 6. List each film and the number of actors who are listed for that film.

select film_id, a.title, count(*) as n_actors from sakila.film as a
inner join sakila.film_actor as b
using(film_id)
group by film_id
order by n_actors desc;

# 7. Using the tables payment and customer and the JOIN command, list the total paid by each customer. 
# List the customers alphabetically by last name. 

select customer_id, a.first_name, a.last_name, sum(amount) as total_paid_amount from sakila.customer as a
inner join sakila.payment as b
using(customer_id)
group by customer_id
order by a.last_name;

# Bonus: Which is the most rented film? The answer is Bucket Brotherhood This query might require using more than one join statement. Give it a try.

select film_id, a.title, count(*) as n_rentals from sakila.film as a
inner join sakila.inventory as b
using(film_id)
inner join sakila.rental as c
using(inventory_id)
group by film_id
order by n_rentals desc;




# Table Queries
select * from sakila.film_actor;
select * from sakila.actor;
select * from sakila.staff;
select * from sakila.address;
select * from sakila.payment;
