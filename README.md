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

## Example

```bash
python main.py --container f04ebc2c26f5c7f5a67c657e5ca0ec890a08243bc1c5ec7d0d4bfcce004b0dc8 --parser spell --encoder bert
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
    
ening at: http://0.0.0.0:8000 (7)
[2023-10-28 18:46:40 +0000] [7] [INFO] Using worker: sync
[2023-10-28 18:46:40 +0000] [8] [INFO] Booting worker with pid: 8
[2023-11-02 17:32:12 +0000] [7] [INFO] Starting gunicorn 21.2.0
[2023-11-02 17:32:12 +0000] [7] [INFO] Listening at: http://0.0.0.0:8000 (7)
[2023-11-02 17:32:12 +0000] [7] [INFO] Using worker: sync
[2023-11-02 17:32:12 +0000] [8] [INFO] Booting worker with pid: 8
Error grabbing logs: invalid character '\x00' looking for beginning of value


 Approximate Solution proposed: Anomaly: Error grabbing logs: invalid character '\x00' looking for the beginning of value.

Solution:

This anomaly indicates that there is an invalid character (represented by '\x00') in the logs, causing an issue while grabbing the logs.

To troubleshoot and resolve this problem, you can try the following steps:

1. Remove any special characters or non-UTF-8 encoded characters from the logs: Check if there are any special characters, non-printable characters, or unsupported character encodings in the log messages. Remove or replace such characters with valid UTF-8 encoded characters.

2. Verify the log file encoding: Ensure that the log file is encoded in UTF-8. You can check the encoding using a text editor or command-line tools like `file` or `chardet`. If the file is not in UTF-8 encoding, convert it to UTF-8 using appropriate conversion tools or editors.

3. Validate the log structure: Verify if the log messages have the correct structure and formatting. Ensure that each log message is properly formatted and does not contain any unexpected characters or syntax errors.

4. Verify the log source: Check the source generating these logs (e.g., application, container, service) for any potential issues. Ensure that the logs are being generated correctly and there are no issues with the log-producing system.

5. Update Docker and dependencies: Make sure you are using the latest version of Docker and any relevant dependencies. Update Docker to the latest stable version and check if the issue persists.

6. Restart Docker containers or services: Try restarting the Docker containers or relevant services to see if it resolves the issue. Sometimes restarting the containers can help clear any temporary issues or inconsistencies.

If the above steps do not resolve the issue, you may need to provide more context or seek further assistance from Docker support or the relevant community forums.
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