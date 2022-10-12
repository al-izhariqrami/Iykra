-- Create Table
create table orders (
	order_id int,
	product_name varchar(255),
	numbers int,
	total_price float
);
-- Table contents in postgresql
insert into orders (order_id, product_name, numbers, total_price)
values (1, 'book', 3, 87.43), 
        (2, 'laptop', 4, 1000.85), 
        (4, 'mouse', 2, 100), 
        (3, 'handphone', 2, 200);