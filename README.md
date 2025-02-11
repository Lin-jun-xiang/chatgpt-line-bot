```markdown
# ChatGPT Line Bot

* [English](README.md)
* [繁體中文版README.md](README.zh-TW.md)
* [简体中文](README.zh-CN.md)
* [Française](README.French.md)

## 🤖 Introduction

Integrate ChatGPT Bot into Line. Just type text in the input box to start interacting with ChatGPT.

<img src="img/2023-10-25-10-03-47.png" width="30%" />

## ✨ Features

* **Completely free** ChatGPT Bot
* **Weekly horoscope information** (real-time)

    <img src="img/2023-11-02-10-00-32.png" width="20%"/>

* **YouTube music channel** scheduled push notifications

    <img src="img/2023-11-03-14-44-41.png" width="30%" />

* **Online image search** (real-time)

    <img src="img/2024-05-17-15-08-12.png" width="40%"/>

> [!NOTE]
> If you have any feature requests, please submit PR or ISSUE at any time.

## 🔨 Tools

* `Python FastAPI`: Create ChatGPT response API
* `gpt4free`: **Free use of OpenAI API**
* `zhipuai`: **Free use of GPT API**
* `Line messaging API channel`: Connect to ChatGPT API
* `GitHub`: Code repository
* `replit/render/ngrok`: **Free deployment of your own FastAPI**
* `CronJob`: Free scheduled requests, implementing scheduled push notifications

## 🧠 Free GPT Options

Since `g4f` relies on reverse engineering to call OpenAI's API, it may be unstable. Therefore, the author suggests using the **Zhipu AI** open platform as an alternative for free GPT API.

* `g4f`: Reverse engineering to call OpenAI API
* `zhipuai`: **Zhipu AI** open platform provides free GPT API. Visit [official website](https://open.bigmodel.cn/dev/howuse/glm-4) to register an account, no credit card or cost required. Add API key in [personal center](https://open.bigmodel.cn/usercenter/proj-mgmt/apikeys) as shown below. Set this API key in the environment variable to use this GPT option.
    ![](static/images/2025-01-02-10-18-10.png)

## 🎈 Installation Steps

### Obtain Tokens

1. Obtain Line Tokens:
    1. Log in to [Line Developer](https://developers.line.biz/en/)
    2. Create a bot:
        1. Create a `Provider` -> click `Create`
        2. Create a `Channel` -> select `Create a Messaging API channel`
        3. Fill in the required basic information
        4. After completion, go to `Basic Settings` -> under `Channel Secret`, click `Issue` to generate `LINE_CHANNEL_SECRET` (to be used later).
        5. Under `Messaging API`, click `Issue` to generate `Channel access token` (to be used later).

### Project Setup and Execution

1. Fork GitHub Project:
    * Register/login to [GitHub](https://github.com/)
    * Go to [ChatGPT-Line-Bot](https://github.com/Lin-jun-xiang/ChatGPT-Line-Bot)
    * Click `Star` to support the developer
    * Click `Fork` to copy all code to your repository

2. Start Python FastAPI Server:
   * `$env:LINE_CHANNEL_SECRET="..."; $env:LINE_CHANNEL_ACCESS_TOKEN="..."; $env:SERPAPI_API_KEY="..."; $env:GPT_METHOD="..."; $env:GPT_API_KEY="..."; python main.py`
      * `GPT_METHOD`: Choose `g4f` or `zhipuai`
      * `GPT_API_KEY`: If using `zhipuai` method, provide your API key

3. `ngrok`: Use local computer (or Google Colab) as a server to deploy API
   *  [Set up ngrok environment](https://dashboard.ngrok.com/get-started/setup/)
   *  Download the `ngrok` version suitable for your operating system
   *  Add the `ngrok.exe` path to the system environment variables
   *  Execute: `ngrok config add-authtoken <token>`. Get the token from your personal [ngrok dashboard](https://dashboard.ngrok.com/get-started/your-authtoken).
   *  Execute: `ngrok http --url=<YOUR STATIC DOMAIN>.ngrok-free.app 8090` (if failed, try `ngrok http --hostname=<YOUR STATIC DOMAIN>.ngrok-free.app 8090`). Forward the URL as webhook URL.

      <img src="static/images/2025-02-11-16-16-27.png" width="60%" />

      <img src="img/2024-05-15-14-03-09.png" width="60%"/>

4. Finally, replace `http --url=<YOUR STATIC DOMAIN>.ngrok-free.app/callback` with the webhook URL in the `Messaging API` area of the Line Developer console.

    <img src="static/images/2025-02-11-16-26-05.png" width="60%" />

### Connect Services and Line Bot

Go back to [Line Developer homepage](https://manager.line.biz/account), click `Add Friend Guide`, scan the QR code to add Line Bot as a friend.

Home -> Select your bot -> Add Friend Tool -> Create Friend Action Barcode (https://manager.line.biz/account/<yourBotId>/gainfriends)

Congratulations! You have created your first Line Bot. Try talking to it—it will reply to you!

## ⛄ Group Chat vs. Private Chat

* In one-on-one chats, any message will trigger a response.
* In group chats, use the `@chat` prefix to interact with the bot, for example, `@chat hi~`.

## 🎃 Special Features

### Horoscope

When your message contains a horoscope information request, the web crawler will fetch the weekly horoscope:

* Personal chat: `給我天蠍座星座`, `我想知道天蠍座星座`, ...
* Group chat: `@chat 給我天蠍座星座`, `@chat 我想知道天蠍座星座`, ...

### Online Image Search

When your message contains an image request, the web crawler will fetch the image:

* Personal chat: `在線找到林翔抽煙的圖片`, `給我在線林翔抽煙的圖片`, ...
* Group chat: `@chat 在線找到林翔抽煙的圖片`, `@chat 給我在線林翔抽煙的圖片`, ...

## 📢 Broadcast Messages - Daily YouTube Recommendations

* Using the `broadcast` API, the Line Bot can send messages to all users at once.
* This example demonstrates how the Line Bot sends 3 randomly selected YouTube songs every morning:
  * Create a file `./data/favorite_videos.json`. Refer to the author's dataset.

    （The dataset is generated by using `YouTube Data v3 API` to crawl favorite videos. This guide does not involve the use of YouTube API.）

  * Use `./ChatGPT_linebot/modules/youtube_recommend.py` to randomly select 3 songs, formatted by GPT.
  * Add a `/recommend` route in `./ChatGPT_linebot/urls.py`:

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

    To get `group_id`, print in the console:

    ```python
    elif event.source.type == 'group' and user_message.startswith('@chat'):
        group_id = event.source.group_id
        print(group_id) # Output group_id
    ```

  * Now, visit the `/recommend` route to broadcast messages to all users and specified groups.
  * Use [cron-job.org](https://cron-job.org/en/) to schedule a push at 8:00 AM every day:
    1. Register/login to [cron-job.org](https://cron-job.org/en/)
    2. Click the top right corner `CREATE CRONJOB`
    3. Title: `ChatGPT-Line-Bot`, URL: for example, `https://ChatGPT-Line-Bot.jimmylin.repl.co/`
    4. Set to run every `5 minutes`
    5. Click `CREATE`

## 📢 Broadcast Messages - Caijing Finance Information

* Just like **Daily YouTube Recommendations**, just replace `/recommend` with `/cwsChannel`.
* It can be set to run every `3 hours` in CronJob

  <img src="static/images/2025-02-11-17-27-24.png" width="60%" />

## ⚔ Advanced - Personalized Bot

You can use prompts to personalize the Line Bot's responses. Define `template` in `./ChatGPT_linebot/prompts/template.py`, for example:

<img src="img/2023-10-27-10-09-17.png" width="60%" />

**User Input**: I should eat what for breakfast?

**Bot Response**: Dear, have you woken up? I have been lying in bed waiting for you, thinking about your beautiful figure. What should we eat for breakfast? Shall we have something spicy, like a hot egg roll, to match your fiery charm? 😏🍳

## References

1. [Line_Bot_Tutorial](https://github.com/FawenYo/LINE_Bot_Tutorial)

2. [ChatGPT-Line-Bot](https://github.com/TheExplainthis/ChatGPT-Line-Bot)

<a href="#top">Back to Top</a>
   --------------------------------
```