FROM john/pyspark:2.3.2-hadoop2.7-py3.7

ARG LIVY_VERSION=0.7.0-incubating
ENV SPARK_MASTER="local[1]"
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

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

COPY log4j.properties ${LIVY_CONF_DIR}

HEALTHCHECK CMD curl -f "http://host.docker.internal:${LIVY_PORT}/" || exit 1

ENTRYPOINT ["/entrypoint.sh"]