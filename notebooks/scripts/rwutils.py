import pickle
path = "./models/"

def writeModel(model, filename, extrapath=""): 
    pickle.dump(model, open(path+filename, 'wb'))





def readModel(filename, extrapath=""):
    loaded_model = pickle.load(open(path+filename, 'rb'))
    return loaded_model