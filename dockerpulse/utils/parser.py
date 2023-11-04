import docker
from langchain.chat_models import ChatOpenAI as OpenAI
from dotenv import load_dotenv

# Load .env file
load_dotenv()


class Parser:
    def __init__(self, container):
        self.client = docker.from_env()
        self.container = container
        self.logs = self._get_logs()

    def _process_logs(self, logs):
        '''
        `process_logs` returns the embedding for the BERT model

        return:
            BERTEmbeddings
        '''
        # logs = self.llm(self.prompt + "\n\nLogs:\n" + logs)
        return logs

    def _get_logs(self):
        return self._process_logs(self.client.containers.get(self.container).logs().decode('utf-8'))


if __name__ == "__main__":
    print(Parser("87a19310f8445ccf559458944154f091c93e6ef0afe6fcf310b47d2326b580d8").logs)
