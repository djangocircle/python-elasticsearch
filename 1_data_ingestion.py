import elasticsearch_client

from models import Project
from faker import Faker


INDICES_LIST = ["project_1", "project_2", "project_3", "my_project", "all_project"]

def init_indexes():
    '''
        Intialize indexes with document mapping
    '''
    for index in INDICES_LIST:
        document_class = Project()
        document_class.init(index)
        print("Initializing index {} - Success!".format(index))


def project_ingestion_process():
    '''
        Intializer indexes and insert data in indexed documents
    '''

    init_indexes()

    fake = Faker()
    for index in INDICES_LIST[:3]:
        for i in range(1000):
            project = Project(
                meta={"index": index},
                name=fake.name(),
                email=fake.email(),
                phone_number=fake.phone_number(),
            )

            project.save()
            print("Project saved in {} : {}".format(index, i))


if __name__ == "__main__":
    project_ingestion_process()