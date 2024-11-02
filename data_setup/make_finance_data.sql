use patient_db;

drop table if exists finance;

create table finance (
    year int,
    month int,
    total_funding decimal(15, 2),
    total_expense decimal(15, 2),
    administrative_cost decimal(15, 2),
    operational_cost decimal(15, 2),
    infrastructure_cost decimal(15, 2),
    supply_cost decimal(15, 2),
    salary_cost decimal(15, 2),
    num_patients_seen int,
    primary key (year, month)
);

load data infile '/var/lib/mysql-files/data/financial_data.csv'
into table finance
fields terminated by ','
lines terminated by '\n'
ignore 1 lines;

select * from finance limit 10;