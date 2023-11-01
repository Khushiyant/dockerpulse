import docker
from .utils.parser import Parser
from .utils.anamoly import Detection
from typing import AnyStr
from dockerpulse.utils.gptQA import GPTQA


class Dockerpulse(Parser, Detection):
    def __init__(self, container):
        Parser.__init__(container)
        Detection.__init__(self._process_logs())

    def analysis(self) -> AnyStr:
        # TODO: Prompt for complete analysis of the logs
        self.qna = GPTQA()
        return self.qna.generate_solution(self.get_anamoly())
