# ChatGPT Line Bot

* [English](README.md)
* [Traditional Chinese Version README.md](README.zh-TW.md)
* [Simplified Chinese](README.zh-CN.md)
* [French](README.French.md)
* [Arabic](README.Arabic.md)


## Introduction

Introduce ChatGPT Bot in Line, you can start interacting with ChatGPT by entering text directly in the input box.

<img src="img/2023-10-25-10-03-47.png" width="30%" />

## Tools and Features

* `Python FastAPI`: Build a response API for ChatGPT
* `gpt4free`: **Free use of OpenAI API**
* `Line messaging API channel`: Integrate with ChatGPT API
* `Github`: Store the code
* `replit`: **Free deployment of your own FastAPI**
* `CronJob`: Free scheduled request sending to prevent API interruption


## Installation Steps

### Token Acquisition

1. Get the Line Token:
    1. Log in to [Line Developer](https://developers.line.biz/zh-hant/)
    2. Create a bot:
        1. Create a `Provider` -> click `Create`
        2. Create a `Channel` -> choose `Create a Messaging API channel`
        3. Fill in the required basic information
        4. After completion, under `Basic Settings`, there is a `Channel Secret` -> click `Issue`, it will be generated as `LINE_CHANNEL_SECRET` (will be used later)
        5. Under `Messaging API`, there is a `Channel access token` -> click `Issue`, it will be generated as `LINE_CHANNEL_ACCESS_TOKEN` (will be used later)

### Project Setup
1. Fork the Github project:
    1. Register/Login to [GitHub](https://github.com/)
    2. Go to [ChatGPT-Line-Bot](https://github.com/Lin-jun-xiang/ChatGPT-Line-Bot)
    3. Click `Star` to support the developer
    4. Click `Fork` to copy all the code to your own repository
2. Deployment (Free Space):
    1. Go to [replit](https://replit.com/)
    2. Click `Sign Up` to log in with your `Github` account and authorize it -> click `Skip` to skip the initialization setup
    3. After entering, click `Create` on the middle homepage -> a pop-up box will appear, click the top right corner `Import from Github`
    4. If you haven't joined the Github repository, click the link `Connect GitHub to import your private repos.` -> check `Only select repositories` -> choose `ChatGPT-Line-Bot`
    5. Go back to step four, at this time the `Github URL` can choose the `ChatGPT-Line-Bot` project -> click `Import from Github`.

### Project Execution
1. Environment Variable Setup
    1. After completing the previous step `Import` in `Replit`, click `Tools` at the bottom left of the project management page of `Replit` and click `Secrets`.
    2. After clicking `Got it` on the right side, you can add environment variables. You need to add:
        1. Line Channel Secret:
            - key: `LINE_CHANNEL_SECRET`
            - value: `[obtained from step one]`
        2. Line Channel Access Token:
            - key: `LINE_CHANNEL_ACCESS_TOKEN`
            - value: `[obtained from step one]`

        <img src="img/2023-10-25-10-00-59.png" width="60%"/>

2. Start Execution
    1. Click `Run` at the top
    2. After successful execution, the right panel will display `Hello World`, and copy the **URL** in the upper right corner of the panel
    3. Go back to Line Developer, paste the URL from the previous step into `Webhook URL` under `Messaging API`, and add `/callback` to it, for example: `https://ChatGPT-Line-Bot.jimmylin.repl.co/callback`
    4. Turn on `Use webhook` below
    5. Turn off `Auto-reply messages` below
    - Note: If there is no request within an hour, the program will be interrupted, so the next step is needed

        <img src="img/2023-10-25-10-01-21.png" width="60%"/>

3. CronJob Scheduled Request Sending
    1. Register/Login to [cron-job.org](https://cron-job.org/en/)
    2. After logging in, select `CREATE CRONJOB` in the upper right corner of the dashboard
    3. Enter `ChatGPT-Line-Bot` for `Title`, enter the URL of the previous step, for example: `https://ChatGPT-Line-Bot.jimmylin.repl.co/`
    4. Set it to trigger every `5 minutes` below
    5. Click `CREATE`

### Connect Services and Line Bot

Go back to [Line Developer](https://manager.line.biz/account) homepage and click `Add Friend Guide` to scan the LINE Bot QR code:

Homepage -> Click your bot -> Click `Add Friend Tools` -> Create a Friend QR code (https://manager.line.biz/account/<yourBotId>/gainfriends)

Congratulations on creating your first LINE Bot! Try talking to it and see how it responds!

### Advanced - Personalized Bot

In addition, we can make the Line Bot answer personalized by using the `prompt` method. In `./chatgpt_linebot/prompts/template.py`, we can define a `template`, for example:

<img src="img/2023-10-27-10-09-17.png" width="60%" />

**Question**: What did you have for breakfast today?

**Bot's Answer**: Darling, are you awake in the morning? I've been waiting for you in bed, and thinking about your body makes me so hungry. What should we have for breakfast today? How about some spicy scrambled eggs, as hot as your charming figure? 😏🍳

---

## References

[Line_Bot_Tutorial](https://github.com/FawenYo/LINE_Bot_Tutorial)

[ChatGPT-Line-Bot](https://github.com/TheExplainthis/ChatGPT-Line-Bot)