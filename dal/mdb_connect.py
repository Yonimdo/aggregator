import pymongo
import secret


# insert or updating an item
def insert_update(collaction_name, id=None, data=[]):
    if id == None:
        assert False, 'you must enter an id for update'
    client = pymongo.MongoClient()
    db = client.get_database(secret.DB)
    pages = db.get_collection(collaction_name)
    pages.create_index('id', unique=True)
    update_rst = pages.update({'id': id},
                              data,
                              upsert=True)
    return


# removes an item from a collection
def remove_item(collection_name, page_id):
    client = pymongo.MongoClient()
    db = client.get_database(secret.DB)
    # pages = db.drop_collection('pages')
    pages = db.get_collection(collection_name)
    pages.delete_one({'id': page_id})


# gets a collection with yield or by id
def get_collection(collection_name, find_param=None):
    client = pymongo.MongoClient()
    db = client.get_database(secret.DB)
    if find_param != None:
        return db.get_collection(collection_name).find(find_param)
    else:
        for element in db.get_collection(collection_name).find():
            yield element


# reset a collection
def reset_db(collection_name):
    client = pymongo.MongoClient()
    db = client.get_database(secret.DB)
    db.drop_collection(collection_name)
