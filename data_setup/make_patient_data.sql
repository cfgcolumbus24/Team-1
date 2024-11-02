use patient_db;

drop table if exists patient;

create table patient (
    patient_id int primary key,
    `name` varchar(100),
    `address` varchar(255),
    phone_number varchar(30),
    age int,
    race varchar(50),
    gender varchar(10),
    insurance varchar(20),
    smoking varchar(20),
    physical_activity varchar(20),
    alcohol varchar(20),
    support_system varchar(20)
);

load data infile '/var/lib/mysql-files/data/patient_data.csv'
into table patient
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 rows;

select * from patient limit 10;