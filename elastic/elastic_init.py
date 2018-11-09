from elasticsearch import Elasticsearch
esclient = Elasticsearch(['192.168.200.100:9200'])
response = esclient.search(
index='social-*',
body={
    "query": {
        "match": {
            "message": "myProduct"
        }
    },
    "aggs": {
        "top_10_states": {
            "terms": {
                "field": "state",
                "size": 10
            }
        }
    }
}
)