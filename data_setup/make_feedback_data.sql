use patient_db;

drop table if exists feedback;

create table feedback (
    patient_id varchar(10) primary key,
    first_name varchar(50),
    last_name varchar(50),
    age int,
    relief int,              
    satisfaction int,        
    feedback varchar(255)            
);

load data infile '/var/lib/mysql-files/data/patient\ outcomes.csv'
into table feedback
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 lines;

select * from feedback limit 10;