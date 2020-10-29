import datetime

from elasticsearch_dsl import (
    Document,
    Date,
    Text,
)


class Project(Document):
    title = Text()
    description = Text()
    tags = Text(multi=True)
    created_at = Date()
    last_updated = Date()

    def save(self, **kwargs):
        self.created_at = datetime.datetime.now()
        self.last_updated = datetime.datetime.now()
        return super(Project, self).save(**kwargs)
