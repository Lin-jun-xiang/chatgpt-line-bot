# ChatGPT Line Bot

* [English](README.md)
* [繁體中文版README.md](README.zh-TW.md)

## 🤖 Introduction

Integrate ChatGPT Bot into Line. Simply input text into the input box to start interacting with ChatGPT.

<img src="img/2023-10-25-10-03-47.png" width="30%" />

## ✨ Features

* **Completely free** ChatGPT Bot
* Weekly **horoscope information** (real-time)

    <img src="img/2023-11-02-10-00-32.png" width="20%"/>

* Scheduled push for **YouTube music** channels

    <img src="img/2023-11-03-14-44-41.png" width="30%" />

* **Online image search** (real-time)
    <img src="img/2024-05-17-15-08-12.png" width="40%"/>

> [!NOTE]
> If you have any feature requests, feel free to submit a PR or an ISSUE.

## 🔨 Tools

* `Python FastAPI`: Create the ChatGPT response API
* `gpt4free`: **Use OpenAI API for free**
* `zhipuai`: **Use GPT API for free**
* `Line messaging API channel`: Connect ChatGPT API
* `GitHub`: Code repository
* `replit/render/ngrok`: **Deploy your own FastAPI for free**
* `CronJob`: Send scheduled requests for free, enabling scheduled push messages

## 🧠 Free GPT Options

Since `g4f` relies on reverse engineering to call OpenAI's API, it can be unstable. Therefore, the author suggests an alternative solution using the **Zhipu AI** open platform for free GPT API access.

* `g4f`: Use reverse engineering to call OpenAI API
* `zhipuai`: **Zhipu AI** open platform offers free GPT API. Visit the [official site](https://open.bigmodel.cn/dev/howuse/glm-4) to register an account without requiring any credit card or fees. Add an API key in the [Personal Center](https://open.bigmodel.cn/usercenter/proj-mgmt/apikeys) as shown below. Set this API key in the environment variables to use this GPT option.
    ![](static/images/2025-01-02-10-18-10.png)

## 🎈 Installation Steps

### Obtain Tokens

1. Get Line Tokens:
    1. Log in to [Line Developer](https://developers.line.biz/en/)
    2. Create a bot:
        1. Create a `Provider` -> Click `Create`
        2. Create a `Channel` -> Select `Create a Messaging API channel`
        3. Fill in the required basic information
        4. After completion, go to `Basic Settings` -> Under `Channel Secret`, click `Issue` to generate the `LINE_CHANNEL_SECRET` (used later).
        5. Under `Messaging API`, click `Issue` to generate the `Channel access token` (used later).

### Project Setup and Execution

1. Fork the GitHub Project:
    1. Register/Log in to [GitHub](https://github.com/)
    2. Navigate to [ChatGPT-Line-Bot](https://github.com/Lin-jun-xiang/ChatGPT-Line-Bot)
    3. Click `Star` to support the developer
    4. Click `Fork` to copy all the code to your repository
2. Deployment:

* `ngrok`: Use a local computer (or Google Colab) as a server to deploy the API
  * Download the appropriate version of `ngrok` for your OS
  * Add the `ngrok.exe` path to your system's environment variables
  * Launch FastAPI in the terminal: `$env:LINE_CHANNEL_SECRET="..."; $env:LINE_CHANNEL_ACCESS_TOKEN="..."; $env:SERPAPI_API_KEY="..."; $env:GPT_METHOD="..."; $env:GPT_AOI_KEY="..."; python main.py`
    * `GPT_METHOD`: Choose `g4f` or `zhipuai`
    * `GPT_API_KEY`: If using the `zhipuai` method, provide your API key
  * Run: `ngrok config add-authtoken <token>`. Obtain the token from your personal [ngrok dashboard](https://dashboard.ngrok.com/get-started/your-authtoken).
  * Run: `ngrok http 8080`. The forwarding URL will be the webhook URL.

    <img src="img/2024-05-15-14-03-09.png" width="60%"/>

Finally, replace the webhook URL in the Line Developer console's `Messaging API` section. ([See Step 2 in Project Setup](#project-setup-and-execution))

### Connect Service with Line Bot

Go back to the [Line Developer homepage](https://manager.line.biz/account), click `Add Friend Guide`, and scan the QR code to add the Line Bot as a friend.

Homepage -> Select your bot -> Add friend tools -> Create Friend Action Barcode (https://manager.line.biz/account/<yourBotId>/gainfriends)

Congratulations! You've created your first Line Bot. Try talking to it—it will reply to you!

## ⛄ Group vs. Individual Chats

* In a one-on-one chat, any message will trigger a response.
* In group chats, use the `@chat` prefix to interact with the bot, e.g., `@chat hi~`.

## 🎃 Special Features

### Horoscope

When your message contains a request for horoscope information, a web crawler will fetch the weekly horoscope:

* Personal chat: `Give me the Scorpio horoscope`, `I want to know the Scorpio horoscope`, ...
* Group chat: `@chat Give me the Scorpio horoscope`, `@chat I want to know the Scorpio horoscope`, ...

### Online Image Search

When your message contains a request for an image, a web crawler will fetch an image:

* Personal chat: `Find an image of Lin Xiang smoking online`, `Give me an image of Lin Xiang smoking online`, ...
* Group chat: `@chat Find an image of Lin Xiang smoking online`, `@chat Give me an image of Lin Xiang smoking online`, ...

## 📢 Broadcast Messages - Daily YouTube Recommendations

* Using the `broadcast` API, the Line Bot can push messages to all users at once.
* This example demonstrates how the Line Bot can push 3 randomly selected YouTube songs every morning:
  * Create the file `./data/favorite_videos.json`. Refer to the author's dataset.

    (The dataset is generated using the `YouTube Data v3 API` to fetch favorite videos. This guide does not cover YouTube API usage.)

  * Use `./chatgpt_linebot/modules/youtube_recommend.py` to randomly select 3 songs, formatted by GPT.
  * Add a `/recommend` route in `./chatgpt_linebot/urls.py`:

    ```python
    videos = recommend_videos() # Get 3 songs

    if videos:
        line_bot_api.broadcast(TextSendMessage(text=videos)) # Broadcast to users

        # Push messages to known groups
        known_group_ids = [
            'C6d-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
            'Ccc-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
            'Cbb-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        ]
        for group_id in known_group_ids:
            line_bot_api.push_message(group_id, TextSendMessage(text=videos))
    ```

    To retrieve group `group_id`, print it in the console:

    ```python
    elif event.source.type == 'group' and user_message.startswith('@chat'):
        group_id = event.source.group_id
        print(group_id) # Output group_id
    ```

  * Now, hitting the `/recommend` route will broadcast messages to all users and specified groups.
  * Use [cron-job.org](https://cron-job.org/en/) to schedule daily pushes at 8:00 AM:
    1. Register/Log in to [cron-job.org](https://cron-job.org/en/)
    2. Click `CREATE CRONJOB` in the top-right corner
    3. Title: `ChatGPT-Line-Bot`, URL: e.g., `https://ChatGPT-Line-Bot.jimmylin.repl.co/`
    4. Set to run every `5 minutes`
    5. Click `CREATE`

## ⚔ Advanced - Personalized Bot

You can personalize the Line Bot's responses using prompts. Define `template` in `./chatgpt_linebot/prompts/template.py`, for example:

<img src="img/2023-10-27-10-09-17.png" width="60%" />

**User input**: What should I have for breakfast?

**Bot response**: Darling, are you awake yet? I've been waiting in bed, thinking of your lovely figure. What should we have for breakfast? How about something spicy, like a hot omelet to match your fiery charm? 😏🍳

## Free Deployment Options

## References

1. [Line_Bot_Tutorial](https://github.com/FawenYo/LINE_Bot_Tutorial)

2. [ChatGPT-Line-Bot](https://github.com/TheExplainthis/ChatGPT-Line-Bot)

<a href="#top">Back to top</a>
