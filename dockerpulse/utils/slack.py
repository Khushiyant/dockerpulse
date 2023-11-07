
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
import os

load_dotenv()


def _create_channel(self, channel_name="dockerlogs"):
    """
    This function checks if a channel with the given name already exists.
    If it doesn't, it creates a new channel.

    Args:
        channel_name (str): The name of the channel to create. Defaults to "dockerlogs".
    """
    try:
        response = self.client.conversations_list(
            types="public_channel"
        )

        for channel in response["channels"]:
            if channel["name"] == channel_name:
                return
        response = self.client.conversations_create(name=channel_name)
    except SlackApiError as e:
        print(f"Error creating channel: {e}")


class SlackNotifier:
    def __init__(self, channel="dockerlogs",
                 token=os.getenv("SLACK_BOT_TOKEN")):
        """
        This is the constructor for the SlackNotifier class.

        Args:
            channel (str): The name of the channel to send notifications to. Defaults to "dockerlogs".
            token (str): The token to use for the Slack API. Defaults to the value of the "slacktoken" environment variable.
        """
        self.client = WebClient(token=token)
        self.channel = channel
        _create_channel(self)

    def send_notification(self, log, solution):
        try:
            self.client.chat_postMessage(
                channel=self.channel,
                text=f"Anomaly Detected\n```{log}```\n\n```{solution}```"
            )
        except SlackApiError as e:
            print(f"Error sending notification: {e}")


if __name__ == "__main__":
    sn = SlackNotifier()
    sn.send_notification("log", "solution")
