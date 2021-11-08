# 1. In the table actor, what last names are not repeated?

SELECT last_name, count(*) as n_ocurrences FROM sakila.actor
group by last_name
having n_ocurrences=1;

# 2. Which last names appear more than once?

SELECT last_name, count(*) as n_ocurrences FROM sakila.actor
group by last_name
having n_ocurrences>1;

# 3. Using the rental table, find out how many rentals were processed by each employee.

select staff_id, count(*) as processed_rentals from sakila.rental
group by staff_id;

# 4. Using the film table, find out how many films were released.

select count(distinct(film_id)) from sakila.film;

# 5. Using the film table, find out how many films there are of each rating.

select rating, count(*) as n_films from sakila.film
group by rating;

# 6. What is the mean length of the film for each rating type. Round off the average lengths to two decimal places

select rating, round(avg(length),2) as avg_length from sakila.film
group by rating;

# 7. Which kind of movies (rating) have a mean duration of more than two hours?

select rating, round(avg(length),2) as avg_length from sakila.film
group by rating
having avg_length > 120;