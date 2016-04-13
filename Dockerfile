FROM registry.access.redhat.com/openshift3/logging-elasticsearch:latest
USER 0
RUN rm -rf /usr/share/elasticsearch/plugins/search-guard
CMD sh /opt/app-root/src/run.sh
