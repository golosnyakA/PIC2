import yaml


def _get_token():
    with open("alex.yml") as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
    return cfg["telegram"]["token"]

def _get_chat_id():
    with open("alex.yml") as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
    return cfg["telegram"]["chat_id"]

def _get_broker_address():
    with open("alex.yml") as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
    return cfg["mqtt"]["broker_address"]

