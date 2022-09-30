{{ config(materialized='table') }}

select 
    tripID,
    lpep_pickup_datetime as pickup_datetime,
    lpep_dropoff_datetime as dropoff_datetime,
    CAST(PULocationID as INT64) as PULocationID
from {{ ref('tripdata_full') }}
ORDER BY tripID
