from .utils.parser import Parser
from .utils.anamoly import Detection
from typing import AnyStr
from dockerpulse.utils.gptQA import GPTQA

import torch


class Dockerpulse(Parser, Detection):
    options = dict()
    options['device'] = 'cuda' if torch.cuda.is_available() else 'cpu'

    options["output_dir"] = "../output/bgl/"
    options["model_dir"] = options["output_dir"] + "bert/"
    options["model_path"] = options["model_dir"] + "best_bert.pth"
    options["train_vocab"] = options['output_dir'] + 'train'
    options["vocab_path"] = options["output_dir"] + "vocab.pkl"

    options["window_size"] = 128
    options["adaptive_window"] = True
    options["seq_len"] = 512
    options["max_len"] = 512  # for position embedding
    options["min_len"] = 10

    options["mask_ratio"] = 0.5

    options["train_ratio"] = 1
    options["valid_ratio"] = 0.1
    options["test_ratio"] = 1

    # features
    options["is_logkey"] = True
    options["is_time"] = False

    options["hypersphere_loss"] = True
    options["hypersphere_loss_test"] = False

    options["scale"] = None  # MinMaxScaler()
    options["scale_path"] = options["model_dir"] + "scale.pkl"

    # model
    options["hidden"] = 256  # embedding size
    options["layers"] = 4
    options["attn_heads"] = 4

    options["epochs"] = 200
    options["n_epochs_stop"] = 10
    options["batch_size"] = 32

    options["corpus_lines"] = None
    options["on_memory"] = True
    options["num_workers"] = 5
    options["lr"] = 1e-3
    options["adam_beta1"] = 0.9
    options["adam_beta2"] = 0.999
    options["adam_weight_decay"] = 0.00
    options["with_cuda"] = True
    options["cuda_devices"] = None
    options["log_freq"] = None

    # predict
    options["num_candidates"] = 15
    options["gaussian_mean"] = 0
    options["gaussian_std"] = 1

    def __init__(self, container, parser, log_format):
        self.log_format = log_format
        Parser.__init__(self, container=container,
                        parser=parser, log_format=self.log_format)
        Detection.__init__(self, self.options)

    def analysis(self) -> AnyStr:
        anomaly = False
        sol = "Information insufficient to produce solution"

        # TODO: Prompt for complete analysis of the logs
        self.qna = GPTQA()
        try:
            anomaly = self.get_anamoly(self.logs)
            if anomaly:
                sol = self.qna.generate_solution(self.logs)
        except Exception as e:
            return sol, anomaly, self.logs

        return sol, anomaly, self.logs
