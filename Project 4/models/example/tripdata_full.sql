{{ config(materialized='table') }}

SELECT ROW_NUMBER() OVER (ORDER BY lpep_pickup_datetime) AS tripID, * FROM

(
SELECT * FROM `applied-well-362908.taxi_dataset.green_tripdata_2021-01`
UNION DISTINCT
SELECT * FROM `applied-well-362908.taxi_dataset.green_tripdata_2021-02`
UNION DISTINCT
SELECT * FROM `applied-well-362908.taxi_dataset.green_tripdata_2021-03`
UNION DISTINCT
SELECT * FROM `applied-well-362908.taxi_dataset.green_tripdata_2021-04`
UNION DISTINCT
SELECT * FROM `applied-well-362908.taxi_dataset.green_tripdata_2021-05`
UNION DISTINCT
SELECT * FROM `applied-well-362908.taxi_dataset.green_tripdata_2021-06`
UNION DISTINCT
SELECT * FROM `applied-well-362908.taxi_dataset.green_tripdata_2021-07`
UNION DISTINCT
SELECT * FROM `applied-well-362908.taxi_dataset.green_tripdata_2021-08`
UNION DISTINCT
SELECT * FROM `applied-well-362908.taxi_dataset.green_tripdata_2021-09`
UNION DISTINCT
SELECT * FROM `applied-well-362908.taxi_dataset.green_tripdata_2021-10`
UNION DISTINCT
SELECT * FROM `applied-well-362908.taxi_dataset.green_tripdata_2021-11`
UNION DISTINCT
SELECT * FROM `applied-well-362908.taxi_dataset.green_tripdata_2021-12`
)
