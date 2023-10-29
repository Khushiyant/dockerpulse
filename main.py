from dockerpulse.cli import Dockerpulse
import argparse
from dotenv import load_dotenv
from typing import AnyStr
from dockerpulse.utils.gptQA import GPTQA


def config():
    load_dotenv()


def solution(obj: Dockerpulse, logs: AnyStr) -> AnyStr:
    qna = GPTQA()
    return qna.generate_solution(obj.logs)


def main():
    # START: ASCII Art
    docker_ascii = r"""
        $$$$$$$\                      $$\                           $$$$$$$\            $$\                     
        $$  __$$\                     $$ |                          $$  __$$\           $$ |                    
        $$ |  $$ | $$$$$$\   $$$$$$$\ $$ |  $$\  $$$$$$\   $$$$$$\  $$ |  $$ |$$\   $$\ $$ | $$$$$$$\  $$$$$$\  
        $$ |  $$ |$$  __$$\ $$  _____|$$ | $$  |$$  __$$\ $$  __$$\ $$$$$$$  |$$ |  $$ |$$ |$$  _____|$$  __$$\ 
        $$ |  $$ |$$ /  $$ |$$ /      $$$$$$  / $$$$$$$$ |$$ |  \__|$$  ____/ $$ |  $$ |$$ |\$$$$$$\  $$$$$$$$ |
        $$ |  $$ |$$ |  $$ |$$ |      $$  _$$<  $$   ____|$$ |      $$ |      $$ |  $$ |$$ | \____$$\ $$   ____|
        $$$$$$$  |\$$$$$$  |\$$$$$$$\ $$ | \$$\ \$$$$$$$\ $$ |      $$ |      \$$$$$$  |$$ |$$$$$$$  |\$$$$$$$\ 
        \_______/  \______/  \_______|\__|  \__| \_______|\__|      \__|       \______/ \__|\_______/  \_______|                                                                                                                                                                                                        
    """
    print(docker_ascii)
    # END: ASCII Art

    parser = argparse.ArgumentParser(
        prog='Dockerpulse CLI',
        description='Dockerpulse CLI to detect anomalies in Docker containers and send alerts to Slack and output solution to stdout',
        add_help=True)

    parser.add_argument('-c', '--container',
                        help='Container ID', required=True)
    parser.add_argument('-e', '--encoder',
                        help='Large Language Model Encoder', default='bert')

    try:
        args = parser.parse_args()
        pulse = Dockerpulse(args.container, args.llm)
        logs = pulse.process_logs()

        print(pulse.get_anamoly(args.encoder, logs),solution(pulse, logs))

    except Exception as e:
        print(e)


if __name__ == "__main__":
    config()
    main()
