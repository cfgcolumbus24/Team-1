use patient_db;

drop table if exists visit;

create table visit (
    patient_id varchar(10),
    first_name varchar(100),
    last_name varchar(100),
    age int,
    gender varchar(20),
    blood_type varchar(3),
    `condition` varchar(255),
    admission_date date,
    contact_number varchar(20),
    allergies varchar(255),
    medications varchar(255),
    emergency_contact varchar(255),
    doctor_assigned varchar(100),
    room_number varchar(10)
);

load data infile '/var/lib/mysql-files/data/patient_data1.csv'
into table visit
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 lines;

select * from visit limit 10;