-- 1. Write a query to display for each store its store ID, city, and country.

select 
s.store_id,
city.city,
country.country
from sakila.store as s
join sakila.address as a
using(address_id)
join sakila.city as city
using(city_id)
join sakila.country as country
using(country_id);

-- 2. Write a query to display how much business, in dollars, each store brought in.

select 
s.store_id, 
round(sum(p.amount)) as business_brought
from sakila.store as s
join sakila.customer as c
using(store_id)
join sakila.payment as p
using(customer_id)
group by s.store_id;

-- 3. What is the average running time(length) of films by category?

select 
c.name, 
round(avg(f.length)) as avg_film_length
from sakila.category as c
join sakila.film_category as f_c
using(category_id)
join sakila.film as f
using(film_id)
group by c.name
order by avg_film_length desc;

-- 4.

-- Games and Sports

-- 5. Display the most frequently(number of times) rented movies in descending order.

select
f.title,
count(r.rental_id) as n_rentals
from sakila.film as f
join sakila.inventory as i
using(film_id)
join sakila.rental as r
using(inventory_id)
group by f.title
order by n_rentals desc;

-- 6. List the top five genres in gross revenue in descending order.

select c.name,
round(sum(p.amount)) as gross_revenue
from sakila.category as c
join sakila.film_category as f_c
using(category_id)
join sakila.inventory as i
using(film_id)
join sakila.rental as r
using(inventory_id)
join sakila.payment as p
using(rental_id)
group by c.name
order by gross_revenue desc;

-- 7. Is "Academy Dinosaur" available for rent from Store 1?

select
distinct
f.title,
i.store_id
from sakila.film as f
join sakila.inventory as i
where f.title = "Academy Dinosaur";

