-- Query 1

select client_id from bank.client
where (district_id = 1)
limit 5;

-- Query 2

select client_id from bank.client
where (district_id = 72)
order by client_id DESC
limit 1;

-- Query 3

select amount from bank.loan
order by amount
limit 3;

-- Query 4

select distinct(status) from bank.loan
order by status;

-- Query 5

select loan_id, payments from bank.loan
order by payments desc
limit 1;

-- Query 6

select account_id, amount from bank.loan
order by account_id
limit 5;

-- Query 7

select account_id from bank.loan
where (duration = 60)
order by amount
limit 5;

-- Query 8

select distinct(k_symbol) from bank.order;

-- Query 9

select order_id from bank.order
where (account_id = 34);

-- Query 10

select distinct(account_id) from bank.order
where (order_id > 29540 and order_id <= 29560);

-- Query 11

select amount from bank.order
where (account_to = 30067122);

-- Query 12

select trans_id,date,type,amount from bank.trans
where (account_id = 793)
order by date desc
limit 10;

-- Query 13

select district_id,count(client_id) from bank.client
where (district_id < 10)
group by district_id;

-- Query 14

select type,count(card_id) as n_cards from bank.card
group by type
order by n_cards desc;

-- Query 15

select account_id,sum(amount) as total_amount_loan from bank.loan
group by account_id
order by total_amount_loan desc
limit 10;

-- Query 16

select date,count(loan_id) from bank.loan
where (date < 930907)
group by date
order by date desc;

-- Query 17

select date,duration, count(loan_id) as n_loans from bank.loan
where date like "9712%"
group by duration,date
order by date,duration;


-- Query 18

select account_id,type,sum(amount) from bank.trans
where account_id=396
group by type
having type="VYDAJ" or type="PRIJEM"
order by type;

-- Query 19

select account_id,
replace(replace(`type`, "PRIJEM", "INCOMING"), "VYDAJ", "OUTGOING") as transaction_type,
floor(sum(amount)) as total_amount
from bank.trans
where account_id=396
group by type
having type="VYDAJ" or type="PRIJEM"
order by type;

-- Query 20 - Solution A

with 

incoming_amount as
(select account_id, 
floor(sum(amount)) as total_incoming
from bank.trans
where type="PRIJEM"
group by account_id
having account_id=396
),

outgoing_amount as
(select account_id, 
floor(sum(amount)) as total_outgoing
from bank.trans
where type="VYDAJ"
group by account_id
having account_id=396
)

select incoming_amount.account_id,
incoming_amount.total_incoming,
outgoing_amount.total_outgoing,
incoming_amount.total_incoming - outgoing_amount.total_outgoing as balance
from incoming_amount,outgoing_amount;

-- Query 20 - Solution B

select 
account_id,
type,
(case when type = "VYDAJ" then sum(balance) else 0 end) as total_outgoing,
(case when type = "PRIJEM" then sum(amount) else 0 end) as total_incoming
from bank.trans
group by account_id
having account_id = 396;order

select 
account_id,
sum(amount) as total_amount,
sum(balance) as total_balance
from bank.trans
group by account_id
having account_id = 396;



-- Query 21 - Solution A

with 

incoming_amount as
(select account_id, 
floor(sum(amount)) as total_incoming
from bank.trans
where type="PRIJEM"
group by account_id
),

outgoing_amount as
(select account_id, 
floor(sum(amount)) as total_outgoing
from bank.trans
where type="VYDAJ"
group by account_id
)

select i.account_id,
i.total_incoming,
o.total_outgoing,
i.total_incoming - o.total_outgoing as balance
from incoming_amount as i
join outgoing_amount as o
using(account_id)
order by balance desc
limit 10;

-- Query 21 - Solution B

with 

CTE_trans_balance as
(select 
account_id,
(case when `type` = "PRIJEM" THEN amount END) as incoming_amount,
(case when `type` = "VYDAJ" THEN amount END) as outgoing_amount
from bank.trans
)

-- select * from CTE_trans_balance;

select 
account_id,
floor(sum(incoming_amount)-sum(outgoing_amount)) as balance
from CTE_trans_balance
group by account_id
order by balance desc
limit 10;