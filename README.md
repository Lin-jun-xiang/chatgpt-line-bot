# ChatGPT Line Bot

* [English](README.md)
* [Traditional Chinese version README.md](README.zh-TW.md)
* [Simplified Chinese](README.zh-CN.md)
* [French](README.French.md)
* [Arabic](README.Arabic.md)

## Introduction

To import the ChatGPT Bot into Line, simply input text into the input box to start interacting with ChatGPT.

![Image](img/2023-10-25-10-03-47.png)<!--width="30%" -->

## Tools and Features

* `Python FastAPI`: Setting up the ChatGPT response API
* `gpt4free`: **Free usage of the OpenAI API**
* `Line messaging API channel`: Integration with the ChatGPT API
* `Github`: Storage for the code
* `replit`: **Free deployment of your FastAPI**
* `CronJob`: Free scheduled requests to prevent API interruptions

## Installation Steps

### Acquiring Tokens

1. Obtain Line Token:
    1. Log in to [Line Developer](https://developers.line.biz/zh-hant/)
    2. Create a bot:
        1. Create `Provider` -> Click `Create`
        2. Create `Channel` -> Choose `Create a Messaging API channel`
        3. Enter the required basic information
        4. After inputting, under `Basic Settings`, there is a `Channel Secret` -> Click `Issue`, the generated code is the `LINE_CHANNEL_SECRET` (will be used later)
        5. Under `Messaging API`, there is a `Channel access token` -> Click `Issue`, the generated code is the `LINE_CHANNEL_ACCESS_TOKEN` (will be used later)

### Project Setup

1. Fork the Github project:
    1. Register/Log in to [GitHub](https://github.com/)
    2. Go to [ChatGPT-Line-Bot](https://github.com/Lin-jun-xiang/ChatGPT-Line-Bot)
    3. Click `Star` to support the developer
    4. Click `Fork` to copy all the code to your repository
2. Deployment (Free space):
    1. Go to [replit](https://replit.com/)
    2. Click `Sign Up`, log in directly with your `Github` account, and authorize -> Click `Skip` to skip the initial setup
    3. Once inside, click `Create` in the middle of the main page -> A pop-up will appear, click `Import from Github`
    4. If not already added to Github repositories, click the link `Connect GitHub to import your private repos.` -> Check `Only select repositories` -> Choose `ChatGPT-Line-Bot`
    5. Return to step four, now the `Github URL` can select the `ChatGPT-Line-Bot` project -> Click `Import from Github`.

### Project Execution

1. Environment Variables Setup
    1. After the previous `Import`, on the `Replit` project management page, at the bottom left under `Tools`, click `Secrets`.
    2. Click `Got it` on the right side, then add new environment variables:
        1. Line Channel Secret:
            - key: `LINE_CHANNEL_SECRET`
            - value: `[Obtained from step one]`
        2. Line Channel Access Token:
            - key: `LINE_CHANNEL_ACCESS_TOKEN`
            - value: `[Obtained from step one]`

        ![Image](img/2023-10-25-10-00-59.png)<!--width="60%"-->

2. Start Execution
    1. Click `Run` at the top
    2. Upon success, the right-hand screen will display `Hello World`, and **copy the URL** displayed at the top of the screen
    3. Go back to Line Developer, under `Messaging API`, in the `Webhook URL`, paste the above URL and add `/callback`, for example: `https://ChatGPT-Line-Bot.jimmylin.repl.co/callback`
    4. Enable the `Use webhook` option
    5. Turn off the `Auto-reply messages` below
    - Note: If no requests are made within an hour, the program will stop, so the following step is necessary

        ![Image](img/2023-10-25-10-01-21.png)<!--width="60%"-->

3. CronJob for Scheduled Requests
    1. Register/Log in to [cron-job.org](https://cron-job.org/en/)
    2. On the panel, select `CREATE CRONJOB` in the top right
    3. Input the `Title` as `ChatGPT-Line-Bot`, put in the URL from the previous step, for instance: `https://ChatGPT-Line-Bot.jimmylin.repl.co/`
    4. Set to run every `5 minutes` below
    5. Click `CREATE`

### Linking Services and Line Bot

Go back to [Line Developer](https://manager.line.biz/account) and click on `Add Friend Guide`, then scan and add LINE Bot:

Homepage -> Click your bot -> Click on the "Add friends" tool -> Create a friend barcode (https://manager.line.biz/account/<yourBotId>/gainfriends)

Congratulations on creating your first LINE Bot! Try talking to it and it will reply to you!

### Special Commands

| Command | Description |
| ------- | ----------- |
| `@chat` | Type `@chat` + message in the input box to call chatgpt in a Line group |
| `@chat Horoscope <sign>` | Type `@chat Horoscope Scorpio` in the input box to get the weekly horoscope for Scorpio (or any zodiac sign), this feature is limited to Traditional Chinese commands |

![Image](img/2023-11-02-10-00-32.png)

### Advanced - Personalized Bot

Additionally, we can use the `prompt` method to make the Line Bot provide personalized responses. In `./chatgpt_linebot/prompts/template.py`, we can define a `template`, for example:

![Image](img/2023-10-27-10-09-17.png)<!--width="60%"-->

**Question**: What's for breakfast today?

**Bot's Answer**: Sweetheart, are you up in the morning? I'm already in bed waiting for you, feeling so hungry just thinking about you. What should we have for breakfast today? Maybe something spicy like an omelette, as hot as your charming figure? 😏🍳

---

## References

[Line_Bot_Tutorial](https://github.com/FawenYo/LINE_Bot_Tutorial)

[ChatGPT-Line-Bot](https://github.com/TheExplainthis/ChatGPT-Line-Bot)