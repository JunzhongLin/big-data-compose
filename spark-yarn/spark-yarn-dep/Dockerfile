FROM test/spark-yarn-base:0.1

# ADD Python dependencies
# Please add the external dependent packages here by pip install -r requirements.txt

# Entry point: start all services and applications.
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh
CMD ["/bin/bash", "/entrypoint.sh"]