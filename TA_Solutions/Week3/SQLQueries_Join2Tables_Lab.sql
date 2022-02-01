-- 1. Which actor has appeared in the most films?

select a.actor_id, a.first_name, a.last_name, count(*) as n_films from sakila.actor as a
join sakila.film_actor as f_a
using(actor_id)
group by a.actor_id
order by n_films desc;

-- 2. Most active customer (the customer that has rented the most number of films)

select c.customer_id, c.first_name, c.last_name, count(*) as n_rentals
from sakila.customer as c
join sakila.rental as r
using(customer_id)
group by customer_id
order by n_rentals desc;

-- 3. List number of films per category

select c.category_id, c.name, count(*) as n_films from sakila.category as c
join sakila.film_category as f_c
using(category_id)
group by category_id
order by n_films desc;

-- 4. Display the first and last names, as well as the address, of each staff member.

select s.staff_id, s.first_name, s.last_name, a.address from sakila.staff as s
join sakila.address as a
using(address_id);

-- 5. Display the total amount rung up by each staff member in August of 2005.

select s.staff_id, s.first_name, s.last_name, sum(amount) from sakila.staff as s
join sakila.payment as p
using(staff_id)
where p.payment_date like "2005-08-%"
group by staff_id;

-- 6. List each film and the number of actors who are listed for that film.

select f.film_id, f.title, count(*) as n_actors from sakila.film as f
join sakila.film_actor as f_a
using(film_id)
group by film_id
order by n_actors desc;

/* 7. Using the tables payment and customer and the JOIN command, list the total paid by each customer. 
List the customers alphabetically by last name. */

select c.customer_id, c.first_name, c.last_name, sum(p.amount) as total_paid_amount from sakila.customer as c
join sakila.payment as p
using(customer_id)
group by customer_id
order by c.last_name;

/* # Bonus: Which is the most rented film? The answer is Bucket Brotherhood.
This query might require using more than one join statement. Give it a try. */

select f.film_id, f.title, count(*) as n_rentals from sakila.film as f
join sakila.inventory as i
using(film_id)
join sakila.rental as r
using(inventory_id)
group by film_id
order by n_rentals desc;

