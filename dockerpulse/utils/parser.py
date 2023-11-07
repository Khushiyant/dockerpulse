import docker
from ..lgbert.logparser import Drain, Spell
from dotenv import load_dotenv

# Load .env file
load_dotenv()


class Parser:
    def __init__(self, container, parser, log_format):
        self.client = docker.from_env()
        self.container = container
        self.parser = parser
        self.logs = self._get_logs()
        self.log_format = log_format

    def _process_logs(self, logs):
        '''
        `process_logs` returns the embedding for the BERT model

        return:
            BERTEmbeddings
        '''
        # parse = Drain.LogParser(log_format=self.log_format) if self.parser == "drain" else Spell.LogParser(log_format=self.log_format)

        # parse.parse(logs)
        return logs[-400:]

    def _get_logs(self):
        return self._process_logs(self.client.containers.get(
            self.container).logs().decode('utf-8'))


if __name__ == "__main__":
    print(Parser("87a19310f8445ccf559458944154f091c93e6ef0afe6fcf310b47d2326b580d8").logs)
