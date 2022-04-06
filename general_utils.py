from pathlib import Path
import pickle


def folder(path):
    '''
    create a folder given the path
    path:pathlib.Path or str
    '''
    Path(path).mkdir(exist_ok=True, parents=True)
    return Path(path)

def pickle_save(x, file):
    with open(file, 'wb') as f:
        pickle.dump(x, f, protocol=pickle.HIGHEST_PROTOCOL)
    f.close()
def pickle_load(file):
    with open(file, 'rb') as f:
        x = pickle.load(f)
    f.close()
    return x