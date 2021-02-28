from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
import json

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:50306/?authSource=test' % (username, password))
        self.database = self.client['AAC']
        
    # Method to implement the C in CRUD.
    def create(self, data):
        
        # If data paramater is not None then save all matching documents
        if data is not None:
            insert = self.database.animals.insert(data)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

    # Method to implement the R in CRUD.
    def read(self, search):
        
        # If search paramater is not None then find all matching documents
        if search is not None:
            match = self.database.animals.find(search,{"_id":False})
            return match
            #for animal in match:
                #return ('{0}: {1},{2} {3}'.format(animal['animal_id'],animal['name'], animal['breed'], animal['animal_type']))
                #return json.dumps('{0}: {1},{2} {3}'.format(animal['animal_id'],animal['name'], animal['breed'], animal['animal_type']))
        else:
            raise Exception("Nothing to find, because the search parameter is empty")
            return False
        
    # Method to implement the U in CRUD.
    def update(self, search, change):

        # If search paramater is not None then find all matching documents
        if change is not None:
            update = self.database.animals.update_many(search, change)
            
            # Return count of deleted documents
            result = "Updated: " + json.dumps(update.modified_count)
            return result
        else:
            raise Exception("Nothing to update, because the change parameter is empty")
        
    # Method to implement the D in CRUD
    def delete(self, animal):

        # If delete paramater is not "None" then delete all matching documents
        if animal is not None:
            delete_count = self.database.animals.delete_many(animal)
            
            # Return count of deleted documents
            result = "Deleted: "+ json.dumps(delete_count.deleted_count)
            return result
        else:
            raise Exception("Nothing to delete, because the parameter is empty")
            return False

 
