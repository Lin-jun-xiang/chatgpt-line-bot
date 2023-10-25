# ChatGPT Line Bot

* [English](README.md)
* [Traditional Chinese Version README.md](README.zh-TW.md)
* [Simplified Chinese](README.zh-CN.md)
* [French](README.French.md)
* [Arabic](README.Arabic.md)

This project will teach you how to create a free **ChatGPT Line Bot**!

## Introduction

To integrate a ChatGPT Bot into Line, simply input text into the chat box to start interacting with ChatGPT.

<img src="img/2023-10-25-10-03-47.png" width="30%" />

## Tools and Features

* `Python FastAPI`: Build the ChatGPT response API
* `gpt4free`: **Free use of OpenAI API**
* `Line messaging API channel`: Integrate the ChatGPT API
* `Github`: Store the code
* `replit`: **Free deployment of your FastAPI**
* `CronJob`: Free periodic requests to prevent API interruptions

## Installation Steps

### Getting the Token

1. Obtain the Line Token:
    1. Log in to [Line Developer](https://developers.line.biz/zh-hant/)
    2. Create a bot:
        1. Create a `Provider` -> Click on `Create`
        2. Create a `Channel` -> Choose `Create a Messaging API channel`
        3. Fill in the required basic information
        4. After completing, under `Basic Settings`, there is a `Channel Secret` -> Click on `Issue` to generate it, which will be the `LINE_CHANNEL_SECRET` (used later)
        5. Under `Messaging API`, there is a `Channel access token` -> Click on `Issue` to generate it, which will be the `LINE_CHANNEL_ACCESS_TOKEN` (used later)

### Project Setup

1. Fork the Github project:
    1. Register/log in to [GitHub](https://github.com/)
    2. Go to [ChatGPT-Line-Bot](https://github.com/Lin-jun-xiang/ChatGPT-Line-Bot)
    3. Click `Star` to support the developer
    4. Click `Fork` to copy all the code to your own repository
2. Deployment (Free Space):
    1. Go to [replit](https://replit.com/)
    2. Click `Sign Up` and log in directly with your GitHub account and authorize it -> Click `Skip` to skip the initial setup
    3. After entering, click `Create` in the middle of the main page -> A pop-up will appear, click on the top-right corner `Import from Github`
    4. If you haven't joined the GitHub repository, click the link `Connect GitHub to import your private repos.` -> Check `Only select repositories` -> Choose `ChatGPT-Line-Bot`
    5. Go back to step four, and now the `Github URL` can select the `ChatGPT-Line-Bot` project -> Click `Import from Github`.

### Project Execution

1. Environment Variable Configuration
    1. After completing the previous step, on the left bottom of the project management page in `Replit`, click `Tools` -> Click on `Secrets`.
    2. After clicking `Got it` on the right, you can add environment variables, you need to add:
        1. Line Channel Secret:
            - key: `LINE_CHANNEL_SECRET`
            - value: `[Obtained from step one]`
        2. Line Channel Access Token:
            - key: `LINE_CHANNEL_ACCESS_TOKEN`
            - value: `[Obtained from step one]`

2. Start Execution
    1. Click `Run` at the top
    2. After a successful run, the right-side screen will display `Hello World`, and copy the **URL** at the top of the screen
    3. Go back to Line Developer, in the `Webhook URL` under `Messaging API`, paste the above URL and add `/callback`, for example: `https://ChatGPT-Line-Bot.jimmylin.repl.co/callback`
    4. Turn on `Use webhook` below
    5. Turn off `Auto-reply messages` below
    - Note: If there are no requests within an hour, the program will be interrupted, so this step is necessary

3. CronJob Scheduled Requests
    1. Register/log in to [cron-job.org](https://cron-job.org/en/)
    2. Go to the panel and select `CREATE CRONJOB` in the upper right
    3. Enter `Title` as `ChatGPT-Line-Bot`, enter the URL from the previous step, for example: `https://ChatGPT-Line-Bot.jimmylin.repl.co/`
    4. Set it to run every `5 minutes` below
    5. Click `CREATE`

### Connect to Service and Line Bot

Go back to [Line Developer](https://developers.line.biz/zh-hant/) homepage and click on `Join Bot Guide`. Scan the LINE Bot QR code to add it. Congratulations on creating your first LINE Bot! Try talking to it, and it will reply to you!

---

## References

[Line_Bot_Tutorial](https://github.com/FawenYo/LINE_Bot_Tutorial)

[ChatGPT-Line-Bot](https://github.com/TheExplainthis/ChatGPT-Line-Bot)