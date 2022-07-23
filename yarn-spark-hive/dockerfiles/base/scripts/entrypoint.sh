#!/bin/bash

service ssh start

# start dfs, yarn, spark cluster
if [[ $USRDEF_NODE == "master" ]]; then
  /usr/local/hadoop/spark-services.sh && \
  schematool -dbType postgres -initSchema && \
  hive --service metastore && hiveserver2 &
fi

# start hive server
# /wait-for-it.sh cluster-master:8080 -t 0 --strict -- \
# schematool -dbType postgres -initSchema && \
# hive --service metastore && hiveserver2 &

tail -f /dev/null