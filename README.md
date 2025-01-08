# Discord Message Sender

This Python script allows you to send messages to multiple Discord channels at regular intervals.

## Configuration

1. Create a `config.json` file in the same directory as the script with the following structure:

    ```json
    {
        "servers": {
            "server1": {
                "token": "YOUR_DISCORD_BOT_TOKEN",
                "channel_id": "YOUR_DISCORD_CHANNEL_ID"
            },
            "server2": {
                "token": "YOUR_DISCORD_BOT_TOKEN",
                "channel_id": "YOUR_DISCORD_CHANNEL_ID"
            }
        }
    }
    ```

2. Replace `YOUR_DISCORD_BOT_TOKEN` and `YOUR_DISCORD_CHANNEL_ID` with your actual Discord bot tokens and channel IDs.

## Usage

1. Install the required dependencies:

    ```sh
    pip install requests
    ```

2. Run the script:

    ```sh
    python send_to_discord.py
    ```

3. Enter the message you want to send when prompted.

## Files

- : The main script to send messages to Discord channels.
- : Configuration file containing server tokens and channel IDs.
- `messages.txt`: File to save sent messages.

## License

This project is licensed under the MIT License.
