import docker
from .utils.logs import Parser
from .utils.anamoly import Detection

class Dockerpulse(Parser, Detection):
    def __init__(self, container, encoder):
        Parser.__init__(container)
        Detection.__init__(encoder, self.logs)
        self.encoder = encoder
