use patient_db;

drop table if exists `call`;

create table `call` (
    id int primary key,
    `name` varchar(100),
    call_date date,
    call_duration decimal(5, 2),
    caller_status varchar(50),
    urgency varchar(20),
    support_requested varchar(255),
    mental_health_history varchar(255),
    support_recommended varchar(255),
    notes text
);

load data infile '/var/lib/mysql-files/data/call_data.csv'
into table `call`
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 lines;

select * from `call` limit 10;