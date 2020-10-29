from elasticsearch import Elasticsearch
from elasticsearch_dsl import connections

ELASTIC_CLOUD_HOSTS='localhost'
ELASTIC_CLOUD_USER=''
ELASTIC_CLOUD_PASSWORD=''

es_client = Elasticsearch()

try:
    connections.create_connection(
        timeout=15,
        hosts=ELASTIC_CLOUD_HOSTS,
        http_auth=(
            ELASTIC_CLOUD_USER,
            ELASTIC_CLOUD_PASSWORD,
        ),
    )
except (TypeError, OSError):
    pass    
