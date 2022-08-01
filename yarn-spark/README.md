# YARN-Spark cluster:

## Build up the base docker-images:
----

- build up the spark-base image:
    enter the folder 'spark_base' under 'docker_files' and run:
    ```bash
    docker build --tag john/pyspark:2.3.2-hadoop2.7-py3.7 .
    ```

- compose up
    enter the root folder of this project
    ```bash
    docker compose up
    ```
  
## check if everything is ready
----

### Hadoop and YARN

Check YARN (Hadoop ResourceManager) Web UI (localhost:8088). You should see 2 active nodes there. 

Open up a shell in the master node.
```bash
docker exec -it yarn-spark_master_1 /bin/bash
jps
```
jps command outputs a list of running Java processes, which on Hadoop Namenode/Spark Master node should include those:

output:
```bash
102 NameNode
264 SecondaryNameNode
393 ResourceManager
1214 Master
1311 Jps
```
Then let's see if YARN can see all resources we have (2 worker nodes):

```bash
yarn node -list
```
output:
```bash
22/08/01 11:27:50 INFO client.RMProxy: Connecting to ResourceManager at cluster-master/172.18.0.4:8032
Total Nodes:2
         Node-Id	     Node-State	Node-Http-Address	Number-of-Running-Containers
cluster-slave-2:37513	        RUNNING	cluster-slave-2:8042	                           0
cluster-slave-1:37125	        RUNNING	cluster-slave-1:8042	                           0
```

we can check the HDFS(Hadoop distributed file system) condition:

```bash
hdfs dfsadmin -report
```

output:
```bash
Name: 172.18.0.3:50010 (yarn-spark_slave-2_1.yarn-spark_default)
...
Name: 172.18.0.2:50010 (yarn-spark_slave-1_1.yarn-spark_default)
```

Now, we can upload the files from our test case into HDFS and see if those files can be visible from other nodes.

```bash
hadoop fs -put /job /
hadoop fs -ls /
```
output:
```bash
Found 2 items
drwxr-xr-x   - root supergroup          0 2022-08-01 11:35 /job
drwxr-xr-x   - root supergroup          0 2022-08-01 11:21 /spark-jars
```

Let's use Ctrl+D to exit from master node now. 
Repeat for remaining nodes (there's 3 total: master, slave-1 and slave-2):

```bash
docker exec -it yarn-spark_slave-1_1 /bin/bash
hadoop fs -ls /
```
output:
```bash
Found 2 items
drwxr-xr-x   - root supergroup          0 2022-08-01 11:35 /job
drwxr-xr-x   - root supergroup          0 2022-08-01 11:21 /spark-jars
```

## run a simple test of wordcount job
----

to submit the job in client deploy-mode:
```bash
spark-submit --master yarn --deploy-mode client /job/app/wordcount.py
```

to submit the job in cluster deploy-mode:
```bash
spark-submit --master yarn --deploy-mode cluster --py-files /job/packages.zip /job/app/wordcount.py
```
We can check the status of submitted job through the webui of YARN (http://localhost:8088)