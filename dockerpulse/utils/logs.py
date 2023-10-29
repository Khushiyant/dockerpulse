import docker
from langchain.llms import OpenAI
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class Parser:
    def __init__(self):
        self.client = docker.from_env()
        self.prompt = "Here is a list of the logs from a docker container. Your job is to split the logs into individual log entries with logid, logdate and log line. Before splitting please understand the structure of logs. Write NA where information is not available. Return data in a csv format. Do not return any other text other than the csv data."
        self.temperature = 0.5
        self.max_tokens = 2048
        self.model_engine = "gpt-3.5-turbo"
        self.llm = OpenAI(model_name=self.model_engine,temperature=self.temperature,max_tokens=self.max_tokens)


    def process_logs(self, logs):
        logs = self.llm(self.prompt + "\n\nLogs:\n" + logs)
        return logs

    def get_logs(self, container):
        return self.process_logs(self.client.containers.get(container).logs().decode('utf-8'))
    

if __name__ == "__main__":
    print("\n"+ Parser().process_logs("""/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2021/08/28 09:02:59 [notice] 1#1: using the "epoll" event method
2021/08/28 09:02:59 [notice] 1#1: nginx/1.21.1
2021/08/28 09:02:59 [notice] 1#1: built by gcc 8.3.0 (Debian 8.3.0-6)
2021/08/28 09:02:59 [notice] 1#1: OS: Linux 5.8.0-1039-azure
2021/08/28 09:02:59 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2021/08/28 09:02:59 [notice] 1#1: start worker processes
2021/08/28 09:02:59 [notice] 1#1: start worker process 31
2021/08/28 09:02:59 [notice] 1#1: start worker process 32
"""))

        