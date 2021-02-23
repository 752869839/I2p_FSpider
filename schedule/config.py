# -*- coding: utf-8 -*-
from redis import StrictRedis
from elasticsearch import Elasticsearch

#redis
r_host='172.16.20.177'
r_port=6379
db=0

# elasticsearch
e_host='172.16.20.178'
e_port=9200

redis_client = StrictRedis(host=r_host, port=r_port, db=db)

es_client = Elasticsearch(hosts=e_host, port=e_port)