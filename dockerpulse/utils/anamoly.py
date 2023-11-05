from .lgbert.bert_pytorch.predict_log import Predictor

class Detection:
    def __init__(self, options):
        self.model = Predictor(options=options)

    def get_anamoly(self) -> bool:
        return self.model.predict()


if __name__ == "__main__":
    pass
