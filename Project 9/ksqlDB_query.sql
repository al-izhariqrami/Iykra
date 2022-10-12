-- running ksqldb
docker exec -it ksqldb-cli ksql http://ksqldb-server:8088

-- Create stream table 
create stream orders (order_id VARCHAR, product_name VARCHAR, number INT, total_price DOUBLE)
with (kafka_topic='ORDERS', value_format='json', partitions=1);

-- Create final table
CREATE TABLE FINAL_TABLE AS SELECT product_name, SUM(total_price) as sum_total_price 
from ORDERS GROUP BY product_name;

-- Initiate to get data to stream table
select * from orders emit changes;
select * from final_table;
docker-compose exec broker bash
[appuser@broker ~]$ kafka-console-consumer --topic FINAL_TABLE --bootstrap-server broker:9092 --from-beginning --property print.key=true --property key.separator='-'


-- Insert data to stream table: 
INSERT INTO ORDERS (order_id, product_name, number, total_price) VALUES ('1', 'book', 3, 87.43);
INSERT INTO ORDERS (order_id, product_name, number, total_price) VALUES ('10', 'laptop', 4, 1000.85);
INSERT INTO ORDERS (order_id, product_name, number, total_price) VALUES ('2', 'handphone', 2, 500.23);
INSERT INTO ORDERS (order_id, product_name, number, total_price) VALUES ('3', 'mouse', 5, 200.2);
INSERT INTO ORDERS (order_id, product_name, number, total_price) VALUES ('4', 'pen', 2, 87.2);
