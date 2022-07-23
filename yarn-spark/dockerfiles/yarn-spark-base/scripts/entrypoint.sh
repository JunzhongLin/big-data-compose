#!/bin/bash

service ssh start

# start dfs, yarn, spark cluster
if [[ $USRDEF_NODE == "master" ]]; then
  /usr/local/hadoop/spark-services.sh
fi

tail -f /dev/null