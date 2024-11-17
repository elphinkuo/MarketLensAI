
import pickle


def deepcopy(data):
    # use pickle to deepcopy, it's faster than copy.deepcopy
    data_copied = pickle.loads(pickle.dumps(data, protocol=pickle.HIGHEST_PROTOCOL))
    assert type(data) == type(data_copied)
    return data_copied