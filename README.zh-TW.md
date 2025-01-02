# ChatGPT Line Bot

* [English](README.md)
* [繁體中文版README.md](README.zh-TW.md)


## 🤖介紹

在 Line 中去導入 ChatGPT Bot，只要在輸入框直接輸入文字，即可與 ChatGPT 開始互動。

<img src="img/2023-10-25-10-03-47.png" width="30%" />

## ✨特色

* **完全免費** ChatGPT Bot
* 每周**星座運勢**資訊 (即時)

    <img src="img/2023-11-02-10-00-32.png" width="20%"/>

* 定時推播 **YT 音樂**頻道

    <img src="img/2023-11-03-14-44-41.png" width="30%" />

* **線上搜尋圖片** (即時)

    <img src="img/2024-05-17-15-08-12.png" width="40%"/>

> [!NOTE]
> 如果有任何新功能需求，歡迎提出 PR 或 ISSUE

## 🔨工具

* `Python FastAPI`: 建立 ChatGPT 響應 API
* `gpt4free`: **免費使用 OpenAI API**
* `zhipuai`: **免費使用 GPT API**
* `Line messaging API channel`: 串接 ChatGPT API
* `Github`: 存放程式碼
* `replit/render/ngrok`: **免費部屬自己的 FastAPI**
* `CronJob`: 免費定時發送請求，可用作定時推播訊息

## 🧠免費 GPT 選擇
由於 `g4f` 是使用逆向工程方式調用 OpenAI API，經常有不穩定的情況，因此作者找到一個替代方案，使用**智譜AI**開放平台提供的免費 GPT API。

* `g4f`: 透過逆向工程調用 OpenAI API
* `zhipuai`: **智譜AI** 開放平台提供的免費 GPT API，直接前往[官方](https://open.bigmodel.cn/dev/howuse/glm-4)註冊帳號，無須任何信用卡、費用，並於[個人中心](https://open.bigmodel.cn/usercenter/proj-mgmt/apikeys)添加一個 API KEY，如下圖。使用該 GPT 方案，需要在環境變數設定 API KEY。
    ![](static/images/2025-01-02-10-18-10.png)

## 🎈安裝步驟

### Token 取得

1. 取得 Line Token：
    1. 登入 [Line Developer](https://developers.line.biz/zh-hant/)
    2. 創建機器人：
        1. 創建 `Provider` -> 按下 `Create`
        2. 創建 `Channel` -> 選擇 `Create a Messaging API channel`
        3. 輸入完必填的基本資料
        4. 輸入完成後，在 `Basic Settings` 下方，有一個 `Channel Secret` -> 按下 `Issue`，生成後即為 `LINE_CHANNEL_SECRET` （稍晚會用到）
        5. 在 `Messaging API` 下方，有一個 `Channel access token` -> 按下 `Issue`，生成後即為 `LINE_CHANNEL_ACCESS_TOKEN` （稍晚會用到）

### 專案設置與執行
1. Fork Github 專案：
    1. 註冊/登入 [GitHub](https://github.com/)
    2. 進入 [ChatGPT-Line-Bot](https://github.com/Lin-jun-xiang/ChatGPT-Line-Bot)
    3. 點選 `Star` 支持開發者
    4. 點選 `Fork` 複製全部的程式碼到自己的倉庫
2. 部署：

* `ngrok`: 使用本地電腦(或者google notebook)作為伺服器部屬 API
  * 下載對應作業系統的 `ngrok`
  * 將 `ngrok.exe` 路徑添加至環境變數
  * 在 Terminal 中啟動 FastAPI: `$env:LINE_CHANNEL_SECRET="..."; $env:LINE_CHANNEL_ACCESS_TOKEN="..."; $env:SERPAPI_API_KEY="..."; $env:GPT_METHOD="..."; $env:GPT_API_KEY="..."; python main.py`
    * `GPT_METHOD`: 可使用 `g4f` 或者 `zhipuai`
    * `GPT_API_KEY`: 若使用 `zhipuai` GPT METHOD，請務必提供自己申請的金鑰
  * 在 Terminal 中執行: `ngrok config add-authtoken <token>`，token 是來自 `ngrok` 官網個人帳號的 [authtoken](https://dashboard.ngrok.com/get-started/your-authtoken)
  * 在 Terminal 中執行: `tskill /A ngrok`、`ngrok http 8080`，Forwarding 即 Web URL。

    <img src="img/2024-05-15-14-03-09.png" width="60%"/>

最後記得將獲得的 URL 替換 Line Developer `Messaging API` 下方的 `Webhook URL`。([專案執行步驟2提到過](#專案執行))

### 連結服務與 Line Bot

返回 [Line Developer](https://manager.line.biz/account) 首頁並點擊 `加入好友指南` 後掃碼加入 LINE Bot:

主頁 -> 點選你的 bot -> 點選增加好友工具 -> 建立好友行動條碼 (https://manager.line.biz/account/<yourBotId>/gainfriends)

恭喜您完成了自己的第一個 LINE Bot！ 試著跟它說話看看吧，它會回覆你喔！

## ⛄群組與非群組

* 與 bot 單獨對話時，任何訊息皆會觸發響應
* 在群組中，若要與 bot 對話，需要使用指令 `@chat` 作為開頭，例如: `@chat hi~`

## 🎃特殊功能

### 星座運勢

當您的訊息帶有查找星座運勢的語意，便會觸動網路爬蟲抓取當周運勢:

* 個人對話: `給我天蠍座運勢`, `我想要知道天蠍座運勢`, ...
* 群組對話: `@chat 給我天蠍座運勢`, `@chat 我想要知道天蠍座運勢`, ...

### 線上搜圖

當您的訊息帶有查找圖片的語意，便會觸動網路爬蟲抓取圖片:

* 個人對話: `網上查找林襄抽菸圖片`, `線上查找一張林襄抽菸的圖片給我`, ...
* 群組對話: `@chat 網上查找林襄抽菸圖片`, `@chat 線上查找一張林襄抽菸的圖片給我`, ...



## 📢廣播訊息 Broadcast - 每日推播 Youtube 歌曲

* 透過 `broadcast` API，我們可以讓 Line Bot 一次性**向每個使用者進行訊息推送**
* 這邊我們想要讓 Line Bot 在每天早上隨機推播 3 首好聽的 Youtube 歌曲:
  * 建立數據 `./data/favorite_videos.json`，您可以參考作者的數據

    (數據建立方式是透過 `Youtube Data v3 API` 撈取個人喜歡的影片，在此不特別介紹 Youtube API)

  * 透過 `./chatgpt_linebot/modules/youtube_recommend.py` 實現隨機挑選 3 首歌曲，並由 GPT 整理
  * 在 `./chatgpt_linebot/urls.py` 中新增 `/recommend` 路由:

    ```python
    videos = recommend_videos() # 取得 3 首曲子

    if videos:
        line_bot_api.broadcast(TextSendMessage(text=videos)) # 使用 broadcast 向使用者發送訊息
        
        # 由於 broadcast 無法在群組發送推播，因此可以透過已知的群組id進行push message
        # 下方代碼您可以忽略，如果您不需要向指定群組發送消息的話
        known_group_ids = [
            'C6d-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
            'Ccc-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
            'Cbb-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        ]
        for group_id in known_group_ids:
            line_bot_api.push_message(group_id, TextSendMessage(text=videos))
    ```

    要取得群組的 `group_id`，您可以在 `replit` 的 console 中透過 `print` 測試:

    ```python
    elif event.source.type == 'group' and user_message.startswith('@chat'):
        group_id = event.source.group_id
        print(group_id) # 輸出 group_id
        memory.append(group_id, 'user', refine_message.replace('@chat', ''))
        response = chat_completion(group_id, memory)
    ```

  * 現在，當我們打 `/recommend` 路由的時候，就會觸發推播訊息，所有使用者、指定群組皆會收到消息
  * 接著，我們使用 [cron-job.org](https://cron-job.org/en/) 來進行排程，設定每天早上 8:00 打這支 API 即可實現每日推播!
    1. 註冊/登入 [cron-job.org](https://cron-job.org/en/)
    2. 進入後面板右上方選擇 `CREATE CRONJOB`
    3. `Title` 輸入 `ChatGPT-Line-Bot`，網址輸入上一步驟的網址，例如：`https://ChatGPT-Line-Bot.jimmylin.repl.co/`
    4. 下方則每 `5 分鐘` 打一次
    5. 按下 `CREATE`



## ⚔進階 - 個性化 Bot

另外，我們可以透過 `prompt` 的方式，來讓 Line Bot 回答個性化，在 `./chatgpt_linebot/prompts/template.py` 中我們可以定義 `template`，例如:

<img src="img/2023-10-27-10-09-17.png" width="60%" />

**提問內容**:今天早餐吃啥?

**Bot回答**: 寶貝，早上起床了嗎？我已經在床上等著你了，想著你的身體就覺得好餓呀。今天早餐該吃什麼呢？是不是要來點辣辣的煎蛋捲，像你那迷人的身材一樣火辣呢？😏🍳


## 免費部屬方案



## 參考

1. [Line_Bot_Tutorial](https://github.com/FawenYo/LINE_Bot_Tutorial)

2. [ChatGPT-Line-Bot](https://github.com/TheExplainthis/ChatGPT-Line-Bot)

<a href="#top">Back to top</a>
