# Query 1

select client_id  
from bank.client
where district_id=1
limit 5;


# Query 2

select client_id  
from bank.client
where district_id=72
order by lient_id desc
limit 1;

# Query 3
 
select amount
from bank.loan
order by amount
limit 3;

# Query 4

select distinct(status)
from bank.loan
order by status;

# Query 5

select loan_id
from bank.loan
order by payments desc
limit 1;

select loan_id
from bank.loan
where payments = (select MAX(payments) from bank.loan);

# Query 6

select account_id as `#id`, amount
from bank.loan
order by account_id
limit 5;

# Query 7

select account_id
from bank.loan
where duration=60
order by amount
limit 5;

# Query 8

select distinct(k_symbol) 
from bank.order
where k_symbol <> ""
order by k_symbol;

# Query 9

select order_id
from bank.order
where account_id=34;

# Query 10

select distinct(account_id)
from bank.order
where order_id >= 29540 AND order_id <= 29560;

# Query 11

select sum(amount) 
from bank.order
where account_to=30067122;

# Query 12

select trans_id,`date`,`type`,amount
from bank.trans
where account_id=793
order by date desc
limit 10;

# Query 13

select district_id,count(client_id)
from bank.client
where district_id < 10
group by district_id
order by district_id;

# Query 14

select `type`,count(card_id) as count_card_id
from bank.card
group by `type`
order by count_card_id desc;

# Query 15

select account_id,sum(amount) as total_amount
from bank.loan
group by account_id
order by total_amount desc
limit 10;

# Query 16

select `date`, count(loan_id) as n_loans
from bank.loan
where `date` < 930907
group by `date`
order by `date` desc;

# Query 17

select `date`,duration,count(loan_id) as n_loans
from bank.loan
where `date` like "9712%"
group by duration,`date`
having n_loans > 0
order by `date`, duration;

# Query 18

select account_id,`type` as transaction_type,sum(amount) as total_amount
from bank.trans
where account_id=396
group by `type`
having `type`="VYDAJ" OR `type`="PRIJEM"
order by `type`;

# Query 19

select account_id,
replace(replace(`type`, "PRIJEM", "INCOMING"), "VYDAJ", "OUTGOING") as transaction_type,
floor(sum(amount)) as total_amount
from bank.trans
where account_id=396
group by `type`
having `type`="VYDAJ" OR `type`="PRIJEM"
order by `type`;

# Query 20

with CTE_trans_balance as
(select
	account_id,
	(case when `type` = "PRIJEM" THEN amount END) as incoming_amount,
    (case when `type` = "VYDAJ" THEN amount END) as outgoing_amount
from bank.trans
where account_id=396
)

select 
	account_id, 
    floor(sum(incoming_amount)) as total_incoming_amount, 
    floor(sum(outgoing_amount)) as total_outgoing_amount, 
    floor(sum(incoming_amount)-sum(outgoing_amount)) as balance
from CTE_trans_balance;
 
# Query 21

with CTE_trans_balance as
(select
	account_id,
	(case when `type` = "PRIJEM" THEN amount END) as incoming_amount,
    (case when `type` = "VYDAJ" THEN amount END) as outgoing_amount
from bank.trans
)

select 
	account_id,
    floor(sum(incoming_amount)-sum(outgoing_amount)) as balance
from CTE_trans_balance
group by account_id
order by balance desc
limit 10;

# Tables Queries

select * from card;
select * from district;
select * from account;
select * from loan;
select * from `order`;
select * from trans;
select * from client;