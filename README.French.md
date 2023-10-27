# ChatGPT Line Bot

* [English](README.md)
* [繁體中文版README.md](README.zh-TW.md)
* [简体中文](README.zh-CN.md)
* [Française](README.French.md)
* [عربى](README.Arabic.md)


## Introduction

Integrate ChatGPT Bot in Line by simply entering text in the input box to start interacting with ChatGPT.

<img src="img/2023-10-25-10-03-47.png" width="30%" />

## Tools and Features

* `Python FastAPI`: Create ChatGPT response API
* `gpt4free`: **Free to use OpenAI API**
* `Line messaging API channel`: Connect to ChatGPT API
* `Github`: Store the code
* `replit`: **Free deployment of your own FastAPI**
* `CronJob`: Free scheduled requests to prevent API interruption


## Installation Steps

### Obtain Token

1. Get Line Token:
    1. Log in to [Line Developer](https://developers.line.biz/zh-hant/)
    2. Create a bot:
        1. Create `Provider` -> Click `Create`
        2. Create `Channel` -> Choose `Create a Messaging API channel`
        3. Fill in the required basic information
        4. After filling in, under `Basic Settings`, there is a `Channel Secret` -> Click `Issue`, and the generated value is `LINE_CHANNEL_SECRET` (will be used later)
        5. Under `Messaging API`, there is a `Channel access token` -> Click `Issue`, and the generated value is `LINE_CHANNEL_ACCESS_TOKEN` (will be used later)

### Project Setup
1. Fork the Github project:
    1. Register/Log in to [GitHub](https://github.com/)
    2. Go to [ChatGPT-Line-Bot](https://github.com/Lin-jun-xiang/ChatGPT-Line-Bot)
    3. Click `Star` to support the developer
    4. Click `Fork` to copy all the code to your own repository
2. Deployment (Free Space):
    1. Go to [replit](https://replit.com/)
    2. Click `Sign Up` to log in with your `Github` account and authorize it -> Click `Skip` to skip the initial setup
    3. On the main page in the middle, click `Create` -> A pop-up window will appear, click the top-right corner `Import from Github`
    4. If you haven't added the Github repository, click the link `Connect GitHub to import your private repos.` -> Check `Only select repositories` -> Choose `ChatGPT-Line-Bot`
    5. Go back to step four, at this time, the `Github URL` can choose the `ChatGPT-Line-Bot` project -> Click `Import from Github`.

### Project Execution
1. Environment Variable Setup
    1. After completing the previous `Import` step, click `Tools` at the bottom left of the project management page in `Replit` and click `Secrets`.
    2. After clicking `Got it` on the right, you can add environment variables. You need to add:
        1. Line Channel Secret:
            - key: `LINE_CHANNEL_SECRET`
            - value: `[Obtained from step one]`
        2. Line Channel Access Token:
            - key: `LINE_CHANNEL_ACCESS_TOKEN`
            - value: `[Obtained from step one]`

        <img src="img/2023-10-25-10-00-59.png" width="60%"/>

2. Start Execution
    1. Click `Run` at the top
    2. After successful execution, the right panel will display `Hello World`, and copy the URL in the upper right corner of the panel
    3. Go back to Line Developer, in `Messaging API`, paste the above URL in `Webhook URL`, and add `/callback` to it, for example: `https://ChatGPT-Line-Bot.jimmylin.repl.co/callback`
    4. Turn on `Use webhook`
    5. Turn off `Auto-reply messages` below
    - Note: If there are no requests within an hour, the program will be interrupted, so the next step is needed

        <img src="img/2023-10-25-10-01-21.png" width="60%"/>

3. CronJob Scheduled Requests
    1. Register/Log in to [cron-job.org](https://cron-job.org/en/)
    2. After logging in, choose `CREATE CRONJOB` at the top right of the panel
    3. Enter `ChatGPT-Line-Bot` for `Title`, enter the URL from the previous step, for example: `https://ChatGPT-Line-Bot.jimmylin.repl.co/`
    4. Set it to run every `5 minutes` below
    5. Click `CREATE`

### Connect Services and Line Bot

Go back to [Line Developer](https://manager.line.biz/account) homepage and click `Add Friend Guide` to scan and add the LINE Bot:

Homepage -> Click on your bot -> Click `Add Friend Tools` -> Create Friend QR Code (https://manager.line.biz/account/<yourBotId>/gainfriends)

Congratulations on creating your first LINE Bot! Try talking to it and it will reply to you!

### Advanced - Personalized Bot

In addition, we can make the Line Bot answer more personalized by using the `prompt` method. In `./chatgpt_linebot/prompts/template.py`, we can define a `template`, for example:

<img src="img/2023-10-27-10-09-17.png" width="60%" />

**Question**: What did you have for breakfast today?

**Bot Answer**: Darling, are you awake yet? I've been waiting for you in bed and I'm feeling so hungry just thinking about your body. What should we have for breakfast today? How about some spicy scrambled eggs, as hot as your charming figure? 😏🍳

---

## References

[Line_Bot_Tutorial](https://github.com/FawenYo/LINE_Bot_Tutorial)

[ChatGPT-Line-Bot](https://github.com/TheExplainthis/ChatGPT-Line-Bot)