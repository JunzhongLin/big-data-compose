# YARN-Spark-Hive cluster

## Compose up
----

```bash
cd yarn-spark-hive
docker compose up
```

## check if everything is ready and run a simple test
----

Firstly, let's enter the master node

```bash
docker exec -it yarn-spark-hive-master-1 /bin/bash
hadoop fs -put /grades.csv /
hive
```
output:
```bash
Logging initialized using configuration in jar:file:/usr/local/hive/lib/hive-common-3.1.2.jar!/hive-log4j2.properties 
Async: true
Hive Session ID = 7670b7c2-8e62-40ad-a88a-558eb70aae3d
```

create a table:

```bash
CREATE TABLE grades(
    `Last name` STRING,
    `First name` STRING,
    `SSN` STRING,
    `Test1` DOUBLE,
    `Test2` INT,
    `Test3` DOUBLE,
    `Test4` DOUBLE,
    `Final` DOUBLE,
    `Grade` STRING)
COMMENT 'https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
tblproperties("skip.header.line.count"="1");
```

load the data
```bash
LOAD DATA INPATH '/grades.csv' INTO TABLE grades;
```

show the data:

```bash
SELECT * FROM grades;
```
output:
```
Alfalfa	Aloysius	123-45-6789	40.0	90	100.0	83.0	49.0	D-
Alfred	University	123-12-1234	41.0	97	96.0	97.0	48.0	D+
Gerty	Gramma	567-89-0123	41.0	80	60.0	40.0	44.0	C
Android	Electric	087-65-4321	42.0	23	36.0	45.0	47.0	B-
Bumpkin	Fred	456-78-9012	43.0	78	88.0	77.0	45.0	A-
Rubble	Betty	234-56-7890	44.0	90	80.0	90.0	46.0	C-
Noshow	Cecil	345-67-8901	45.0	11	-1.0	4.0	43.0	F
Buff	Bif	632-79-9939	46.0	20	30.0	40.0	50.0	B+
Airpump	Andrew	223-45-6789	49.0	1	90.0	100.0	83.0	A
Backus	Jim	143-12-1234	48.0	1	97.0	96.0	97.0	A+
Carnivore	Art	565-89-0123	44.0	1	80.0	60.0	40.0	D+
Dandy	Jim	087-75-4321	47.0	1	23.0	36.0	45.0	C+
Elephant	Ima	456-71-9012	45.0	1	78.0	88.0	77.0	B-
Franklin	Benny	234-56-2890	50.0	1	90.0	80.0	90.0	B-
George	Boy	345-67-3901	40.0	1	11.0	-1.0	4.0	B
Heffalump	Harvey	632-79-9439	30.0	1	20.0	30.0	40.0	C
Time taken: 1.29 seconds, Fetched: 16 row(s)
```

The table we just created should be accessible from all nodes.