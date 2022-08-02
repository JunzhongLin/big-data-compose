# YARN-Spark-Livy cluster

## Compose up
----

```bash
cd yarn-spark-livy
docker compose up
```

## check if everything is ready and run some simple tests
----

Please find WEBUI of Livy at http://localhost:8998.

- pull the sessions
```bash
curl --request GET --url http://localhost:8998/sessions | python3 -mjson.tool
```
output:
```bash
{
    "from": 0,
    "total": 0,
    "sessions": []
}
```

- create a session

```bash
curl --request POST \
  --url http://localhost:8998/sessions \
  --header 'content-type: application/json' \
  --data '{
	"kind": "pyspark"
}' | python3 -mjson.tool
```
response:
```bash
{
    "id": 0,
    "name": null,
    "appId": null,
    "owner": null,
    "proxyUser": null,
    "state": "starting",
    "kind": "pyspark",
    "appInfo": {
        "driverLogUrl": null,
        "sparkUiUrl": null
    },
    "log": [
        "stdout: ",
        "\nstderr: ",
        "\nYARN Diagnostics: "
    ]
}
```

- Wait for session to start (state will transition from "starting" to "idle"):

```bash
curl --request GET \
  --url http://localhost:8998/sessions/0 | python3 -mjson.tool
```
response:
```bash
{
    "id": 0,
    "name": null,
    "appId": "application_1659430749021_0001",
    "owner": null,
    "proxyUser": null,
    "state": "idle",
    "kind": "pyspark",
    "appInfo": {
        "driverLogUrl": "http://cluster-slave-1:8042/node/containerlogs/container_1659430749021_0001_01_000001/root",
        "sparkUiUrl": "http://cluster-master:8088/proxy/application_1659430749021_0001/"
    },
    "log": [
        "\t ApplicationMaster RPC port: -1",
        "\t queue: default",
        "\t start time: 1659431303160",
        "\t final status: UNDEFINED",
        "\t tracking URL: http://cluster-master:8088/proxy/application_1659430749021_0001/",
        "\t user: root",
        "22/08/02 09:08:23 INFO ShutdownHookManager: Shutdown hook called",
        "22/08/02 09:08:23 INFO ShutdownHookManager: Deleting directory /tmp/spark-da023c0e-9a70-4fa1-9ce2-d3cf49444c5b",
        "22/08/02 09:08:23 INFO ShutdownHookManager: Deleting directory /tmp/spark-38b86d1a-2fd5-4f2e-848a-7f85155653b3",
        "\nYARN Diagnostics: "
    ]
}
```

- post some statements:
```bash
curl --request POST \
  --url http://localhost:8998/sessions/0/statements \
  --header 'content-type: application/json' \
  --data '{
	"code": "import sys;print(sys.version)"
}' | python3 -mjson.tool
curl --request POST \
  --url http://localhost:8998/sessions/0/statements \
  --header 'content-type: application/json' \
  --data '{
	"code": "spark.range(1000 * 1000 * 1000).count()"
}' | python3 -mjson.tool
```
response:
```bash
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   164  100   120  100    44   1666    611 --:--:-- --:--:-- --:--:--  2277
{
    "id": 0,
    "code": "import sys;print(sys.version)",
    "state": "waiting",
    "output": null,
    "progress": 0.0,
    "started": 0,
    "completed": 0
}
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   184  100   130  100    54   9285   3857 --:--:-- --:--:-- --:--:-- 13142
{
    "id": 1,
    "code": "spark.range(1000 * 1000 * 1000).count()",
    "state": "waiting",
    "output": null,
    "progress": 0.0,
    "started": 0,
    "completed": 0
}
```

- get the results:

```bash
curl --request GET \
  --url http://localhost:8998/sessions/0/statements | python3 -mjson.tool
```
response:
```bash
{
    "total_statements": 2,
    "statements": [
        {
            "id": 0,
            "code": "import sys;print(sys.version)",
            "state": "available",
            "output": {
                "status": "ok",
                "execution_count": 0,
                "data": {
                    "text/plain": "3.7.3 (default, Jan 22 2021, 20:04:44) \n[GCC 8.3.0]"
                }
            },
            "progress": 1.0,
            "started": 1659431405706,
            "completed": 1659431405707
        },
        {
            "id": 1,
            "code": "spark.range(1000 * 1000 * 1000).count()",
            "state": "available",
            "output": {
                "status": "ok",
                "execution_count": 1,
                "data": {
                    "text/plain": "1000000000"
                }
            },
            "progress": 1.0,
            "started": 1659431405710,
            "completed": 1659431408757
        }
    ]
}
```

- delete the session:
```bash
curl --request DELETE \
  --url http://localhost:8998/sessions/0 | python3 -mjson.tool
```
response:
```bash
{
    "msg": "deleted"
}
```

- get all active batches:

```bash
curl --request GET \
  --url http://localhost:8998/batches | python3 -mjson.tool
```
response:
```bash
{
    "from": 0,
    "total": 0,
    "sessions": []
}
```

- submit the wordcount batch

1) upload the txt file on to the HDFS
firstly enter the node of livy
```bash
docker exec -it yarn-spark-livy_livy_1 /bin/bash
```
2) obtain the url of data node location
```bash
curl -i -X PUT "http://cluster-master:50070/webhdfs/v1/job/data/countme.txt?op=CREATE&overwrite=true&noredirect=false"
```
response:
```bash
HTTP/1.1 307 TEMPORARY_REDIRECT
Cache-Control: no-cache
Expires: Tue, 02 Aug 2022 13:16:00 GMT
Date: Tue, 02 Aug 2022 13:16:00 GMT
Pragma: no-cache
Expires: Tue, 02 Aug 2022 13:16:00 GMT
Date: Tue, 02 Aug 2022 13:16:00 GMT
Pragma: no-cache
Location: http://cluster-slave-2:50075/webhdfs/v1/job/data/countme.txt?op=CREATE&namenoderpcaddress=cluster-master:9000&overwrite=true
Content-Type: application/octet-stream
Content-Length: 0
Server: Jetty(6.1.26)
```

3) upload the data 
```bash
curl -i -X PUT -T /job/data/countme.txt \
"http://cluster-slave-2:50075/webhdfs/v1/job/data/countme.txt?op=CREATE&namenoderpcaddress=cluster-master:9000&overwrite=true&user.name=root"
```
response:
```bash
HTTP/1.1 100 Continue

HTTP/1.1 201 Created
Location: hdfs://cluster-master:9000/job/data/countme.txt
Content-Length: 0
Connection: close
```

4) submit the batch
```bash
curl --request POST \
  --url http://localhost:8998/batches \
  --header 'content-type: application/json' \
  --data '{
	"file": "local:///job/app/wordcount.py",
	"pyFiles": [
		"local:///job/app/wordcount.py",
        "local:///job/packages.zip"
	],
	"files": []
}' | python3 -mjson.tool
```
Please find the application status from http://localhost:8088












