FROM registry.access.redhat.com/openshift3/logging-elasticsearch:latest
USER 0
#RUN rm -rf /usr/share/elasticsearch/plugins/search-guard
ADD . /opt/app-root/src
RUN python modify_es_config.py
CMD sh /opt/app-root/src/run.sh
