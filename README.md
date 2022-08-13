# Telegram Message Sender

## Introduction

This is a repository to understand the usage of [Telethon](https://docs.telethon.dev/en/stable/index.html) and the
[Telegram Developer API](https://my.telegram.org/).

## How to use

### 1. Generating API id and hash

First of all, you should create a new App under My Telegram site, to get an API id and hash to use the Telethon library.

1. Access to the site https://my.telegram.org/
2. Introduce your Telegram phone number (in international format)
3. Type the code you've received in your Telegram mobile or desktop client
4. Set "App title" and "Short name" with any desired names
5. Get the "App api_id" and "App api_hash" values to use them in following steps

### 2. Setup the client

After you get the API id and hash, you will need to set them in your environment file, and then you can start using
the Telethon client for sending messages.

1. Copy `.env.sample` to `.env` and set the variables:

   `TELEGRAM_API_ID` => The `api_id` value from step 5 of previous section

   `TELEGRAM_API_HASH` => The `api_hash` value from step 5 of previous section

   `TELEGRAM_API_SESSION` => This variable will be set on the next section

   `TELEGRAM_USER_TO` => The user or bot you want to send the message

   `TELEGRAM_MESSAGE` => The message you want to send

   `SLEEP_RANDOM_SECONDS_BEFORE_MESSAGE` => Random seconds to delay before sending the message. Set 0 if you don't want to be delayed

2. Build the Docker image so you can use it later, typing the following command in your terminal:

    `docker build -t <your_github_user>/telegram-message-sender .`

### 3. Creating a Telegram Session

Now you have the configuration done and built the Docker image, you must create a Telegram Session to be set in your
environment file on the `TELEGRAM_API_SESSION` variable.

Just type the following command and copy the Session value to the variable:

    docker run -it --rm --env-file=.env <your_github_user>/telegram-message-sender python generate_session_string.py

Once you set the Session value into the variable, you'll be ready to send messages

### 4. Send the message

To send the message you've been set in the environment file, you only have to type the following command:

    docker run -it --rm --env-file=.env <your_github_user>/telegram-message-sender python send_message.py
