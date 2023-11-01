from transformers import BertTokenizer, TFBertModel


class Detection:
    def __init__(self, embeddings):
        self.embeddings = embeddings
        self.model = TFBertModel.from_pretrained('bert-base-uncased')

    def get_anamoly(self):
        return self.model(self.embeddings)


if __name__ == "__main__":
    pass
