from dockerpulse.cli import Dockerpulse
import argparse
from dotenv import load_dotenv
from dockerpulse.utils.slack import SlackNotifier


def config():
    load_dotenv()


def main():
    # START: ASCII Art
    docker_ascii = r"""
        $ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - $

            $$$$$$$\                      $$\                           $$$$$$$\            $$\
            $$  __$$\                     $$ |                          $$  __$$\           $$ |
            $$ |  $$ | $$$$$$\   $$$$$$$\ $$ |  $$\  $$$$$$\   $$$$$$\  $$ |  $$ |$$\   $$\ $$ | $$$$$$$\  $$$$$$\
            $$ |  $$ |$$  __$$\ $$  _____|$$ | $$  |$$  __$$\ $$  __$$\ $$$$$$$  |$$ |  $$ |$$ |$$  _____|$$  __$$\
            $$ |  $$ |$$ /  $$ |$$ /      $$$$$$  / $$$$$$$$ |$$ |  \__|$$  ____/ $$ |  $$ |$$ |\$$$$$$\  $$$$$$$$ |
            $$ |  $$ |$$ |  $$ |$$ |      $$  _$$<  $$   ____|$$ |      $$ |      $$ |  $$ |$$ | \____$$\ $$   ____|
            $$$$$$$  |\$$$$$$  |\$$$$$$$\ $$ | \$$\ \$$$$$$$\ $$ |      $$ |      \$$$$$$  |$$ |$$$$$$$  |\$$$$$$$\
            \_______/  \______/  \_______|\__|  \__| \_______|\__|      \__|       \______/ \__|\_______/  \_______|

        $ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - $
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
    parser.add_argument('-p', '--parser',
                        help='Log Parser', default='drain')
    parser.add_argument('-l', '--log-format',
                        help="Regex for log format", default=open('log_format.txt', 'r').read())

    try:
        args = parser.parse_args()

        pulse = Dockerpulse(args.container, args.parser, args.log_format)

        sol, anomaly, error_logs = pulse.analysis()
        if anomaly:
            sn = SlackNotifier()
            sn.send_notification(error_logs, sol)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    config()
    main()
