#!/bin/bash

$HADOOP_HOME/sbin/start-dfs.sh
$HADOOP_HOME/sbin/start-yarn.sh

jps -lm

hdfs dfsadmin -report

# hdfs dfs -mkdir -p /apps/spark
# zip /usr/local/spark/jars/spark-jars.zip /usr/local/spark/jars/*
# hadoop fs -put /usr/local/spark/jars/spark-jars.zip  /apps/spark

SPARK_JARS_HDFS_PATH=/spark-jars
hadoop fs -mkdir -p /spark-jars
hadoop fs -copyFromLocal "${SPARK_HOME}/jars" "${SPARK_JARS_HDFS_PATH}"

$SPARK_HOME/sbin/start-all.sh
# scala -version
jps -lm



