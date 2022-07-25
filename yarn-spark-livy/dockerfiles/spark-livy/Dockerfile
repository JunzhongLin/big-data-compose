FROM openjdk:8u332-slim-buster

USER root

# Add Tools and Python
RUN apt-get update && apt-get install -y curl vim wget zip openssh-server software-properties-common \
ssh net-tools ca-certificates python3.7 python3-pip \
&& rm -rf /var/lib/apt/lists/* \
&& pip3 install --no-cache-dir --upgrade pip setuptools \
&& update-alternatives --install "/usr/bin/python" "python" "$(which python3)" 1

# Download Hadoop and Spark
RUN wget -O /hadoop.tar.gz -q http://archive.apache.org/dist/hadoop/core/hadoop-2.7.3/hadoop-2.7.3.tar.gz \
        && tar xfz hadoop.tar.gz \
        && mv /hadoop-2.7.3 /usr/local/hadoop \
        && rm /hadoop.tar.gz

RUN wget -O /spark.tar.gz -q https://archive.apache.org/dist/spark/spark-2.4.1/spark-2.4.1-bin-hadoop2.7.tgz
RUN tar xfz spark.tar.gz
RUN mv /spark-2.4.1-bin-hadoop2.7 /usr/local/spark
RUN rm /spark.tar.gz

ENV HADOOP_HOME=/usr/local/hadoop
ENV SPARK_HOME=/usr/local/spark
ENV JAVA_HOME=/usr/local/openjdk-8
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$SPARK_HOME/bin:$SPARK_HOME:sbin

# add livy
ARG LIVY_VERSION=0.7.0-incubating
ENV SPARK_MASTER="yarn"
ENV LIVY_HOME /opt/livy
ENV LIVY_CONF_DIR "${LIVY_HOME}/conf"
RUN apt-get update && apt-get install unzip && curl --progress-bar -L --retry 3 \
    "http://archive.apache.org/dist/incubator/livy/${LIVY_VERSION}/apache-livy-${LIVY_VERSION}-bin.zip" \
    -o "./apache-livy-${LIVY_VERSION}-bin.zip" \
  && unzip -qq "./apache-livy-${LIVY_VERSION}-bin.zip" -d /usr \
  && mv "/usr/apache-livy-${LIVY_VERSION}-bin" "${LIVY_HOME}" \
  && rm -rf "./apache-livy-${LIVY_VERSION}-bin.zip" \
  && mkdir "${LIVY_HOME}/logs" \
  && chown -R root:root "${LIVY_HOME}"

# config spark & hadoop
COPY config /tmp/
RUN mv /tmp/hadoop-env.sh $HADOOP_HOME/etc/hadoop/hadoop-env.sh \
    && mv /tmp/core-site.xml $HADOOP_HOME/etc/hadoop/core-site.xml \
    && mv /tmp/hdfs-site.xml $HADOOP_HOME/etc/hadoop/hdfs-site.xml \
    && mv /tmp/mapred-site.xml $HADOOP_HOME/etc/hadoop/mapred-site.xml.template \
    && cp $HADOOP_HOME/etc/hadoop/mapred-site.xml.template $HADOOP_HOME/etc/hadoop/mapred-site.xml \
    && mv /tmp/yarn-site.xml $HADOOP_HOME/etc/hadoop/yarn-site.xml \
    && cp /tmp/slaves $HADOOP_HOME/etc/hadoop/slaves \
    && mv /tmp/slaves $SPARK_HOME/conf/slaves \
    && mv /tmp/spark/spark-env.sh $SPARK_HOME/conf/spark-env.sh \
    && mv /tmp/spark/log4j.properties $SPARK_HOME/conf/log4j.properties \
    && mv /tmp/spark/spark.defaults.conf $SPARK_HOME/conf/spark.defaults.conf \
    && mv /tmp/livy/livy-env.sh $LIVY_CONF_DIR/livy-env.sh

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

COPY log4j.properties ${LIVY_CONF_DIR}

HEALTHCHECK CMD curl -f "http://host.docker.internal:${LIVY_PORT}/" || exit 1

ENTRYPOINT ["/entrypoint.sh"]