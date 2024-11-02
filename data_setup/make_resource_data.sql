use patient_db;

drop table if exists `resource`;

create table resource (
    year int,
    month int,
    total_funding decimal(15, 2),
    total_expense decimal(15, 2),
    hr_cost decimal(15, 2),
    tech_cost decimal(15, 2),
    training_cost decimal(15, 2),
    equipment_cost decimal(15, 2),
    total_staff int,
    hr_staff int,
    tech_staff int,
    clinical_staff int,
    admin_staff int,
    support_staff int,
    primary key (year, month)
);

load data infile '/var/lib/mysql-files/data/resource_data.csv'
into table `resource`
fields terminated by ','
lines terminated by '\n'
ignore 1 lines;

select * from `resource` limit 10;