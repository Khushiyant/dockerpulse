import docker


class Parser:
    def __init__(self):
        self.client = docker.from_env()

    def process_logs(self, logs):
        # logs = logs.split('\n')
        # logs = [log.split(' ') for log in logs]
        # logs = [log for log in logs if len(log) > 1]
        return logs

    def get_logs(self, container):
        return self.process_logs(self.client.containers.get(container).logs().decode('utf-8'))
    

if __name__ == "__main__":
    print(Parser().get_logs('511f5704047eb79baf6abb65cd7c7ada0d3803eb82bb09b722b2d5af94686be0'))

        