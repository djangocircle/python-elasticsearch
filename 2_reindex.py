import os
import logging
import datetime

from models import Project
from elasticsearch_client import es_client
from elasticsearch_dsl import UpdateByQuery

def reindex_documents():
    '''
        Reindex document from source index to target index
    '''
    destination_index = "all_project"

    # reindex documents
    result = es_client.reindex({
        "source": {"index": "project_*"},
        "dest": {"index": destination_index}
    })
    es_client.indices.refresh(index=destination_index)


    # update document last_updated field
    es_client.update_by_query(index=destination_index,
        body={
            "script": {
                "source": "ctx._source['last_updated'] = params.last_updated",
                "lang": "painless",
                "params" : {
                    "last_updated": datetime.datetime.now()
                }
            },
        },
        wait_for_completion=False
    )


if __name__ == "__main__":
    reindex_documents()