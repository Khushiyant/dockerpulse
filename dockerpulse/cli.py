import docker

class Dockerpulse:
    def __init__(self):
        pass

    def get_logs(self, container):
        return docker.from_env().containers.get(container).logs().decode('utf-8')