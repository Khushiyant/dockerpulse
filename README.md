# Dockerpulse

## Overview

![DockerPulse](static/dockerpulse.jpg)

DockerPulse is a powerful tool designed to monitor and manage log data from multiple Docker containers. It processes log data from these containers, parses them using Drain and Spell parsers, detects anomalies using a BERT-based neural network called LogBERT, and generates solutions for detected anomalies with GPT-3.5-Turbo. Additionally, DockerPulse can send all updates and notifications to a connected Slack workspace app. This entire system is wrapped in a user-friendly command-line interface (CLI) application, making it easy to schedule and automate log monitoring tasks with the help of cron jobs.

## Technicalities

- Log Collection: DockerPulse collects logs from multiple Docker containers, making it easy to centralize and analyze your application's log data.

- Log Parsing: It uses the `Drain` and `Spell` parsers to extract structured information from log data, enabling more meaningful analysis.

- Anomaly Detection: DockerPulse employs LogBERT, a BERT-based neural network, to detect anomalies in the log data, allowing you to identify issues in real-time.

- Anomaly Solution Generation: When an anomaly is detected, DockerPulse leverages GPT-3.5-Turbo to generate solutions or recommendations to address the detected issue.

- Slack Integration: Connect DockerPulse to your Slack workspace app to receive notifications and updates about log data and anomalies directly in your communication platform.

- CLI Interface: DockerPulse offers a user-friendly CLI for easy interaction and scheduling of log monitoring tasks using cron jobs.


## Getting Started 

### Installation

1. Clone the DockerPulse repository:

   ```shell
   git clone https://github.com/khushiyant/dockerpulse.git
   ```

2. Navigate to the DockerPulse directory:

   ```shell
   cd dockerpulse
   ```

3. Install the required Python dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Set up your Slack API, OpenAI credentials and configuration as mentioned in the Configuration section.

5. Start using DockerPulse by running the CLI commands as described in the Usage section.

### Prerequisites

Before you can use DockerPulse, ensure you have the following prerequisites installed:

- Docker: Make sure Docker is installed on the host machine, as DockerPulse interacts with Docker containers.

- Python: You need Python 3.9 installed to run the DockerPulse CLI.

- DockerPulse: Clone the DockerPulse repository from GitHub and navigate to the project directory.

### Usage

Dockerpulse provide the several commands to interact with the Dockerpulse CLI. The following commands are available:

```bash
python main.py --help
```

```bash
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
    
usage: Dockerpulse CLI [-h] -c CONTAINER [-e ENCODER] [-p PARSER] [-l LOG_FORMAT]

Dockerpulse CLI to detect anomalies in Docker containers and send alerts to Slack and output solution to stdout

options:
  -h, --help            show this help message and exit
  -c CONTAINER, --container CONTAINER
                        Container ID
  -e ENCODER, --encoder ENCODER
                        Large Language Model Encoder
  -p PARSER, --parser PARSER
                        Log Parser
  -l LOG_FORMAT, --log-format LOG_FORMAT
                        Regex for log format
```
## Contributing
We welcome contributions to DockerPulse! If you have suggestions, improvements, or bug fixes, please submit a pull request on the GitHub repository.

## License
DockerPulse is open-source and released under the [MIT License](./LICENSE). Feel free to use and modify it according to your needs.

## Contact
For questions, issues, or support, please contact us at khushiyant2002@gmail.com
Happy log monitoring with DockerPulse! 

## References

- Tien, Chin‐Wei, et al. “KubAnomaly: Anomaly Detection for the Docker Orchestration Platform with Neural Network Approaches.” Engineering Reports, vol. 1, no. 5, 1 Dec. 2019, onlinelibrary.wiley.com/doi/full/10.1002/eng2.12080, https://doi.org/10.1002/eng2.12080. Accessed 7 Nov. 2023.


- Srinivasan, Siddharth, et al. “Probabilistic Real-Time Intrusion Detection System for Docker Containers.” Communications in Computer and Information Science, 1 Jan. 2019, pp. 336–347, link.springer.com/chapter/10.1007/978-981-13-5826-5_26, https://doi.org/10.1007/978-981-13-5826-5_26. Accessed 7 Nov. 2023.

- ‌Zou, Zhuping, et al. “A Docker Container Anomaly Monitoring System Based on Optimized Isolation Forest.” IEEE Transactions on Cloud Computing, vol. 10, no. 1, 1 Jan. 2022, pp. 134–145, ieeexplore.ieee.org/abstract/document/8807263, https://doi.org/10.1109/tcc.2019.2935724. Accessed 7 Nov. 2023.


‌