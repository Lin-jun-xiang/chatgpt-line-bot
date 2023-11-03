# ChatGPT Line Bot

* [English](README.md)
* [繁體中文版README.md](README.zh-TW.md)


## 介紹

在 Line 中去導入 ChatGPT Bot，只要在輸入框直接輸入文字，即可與 ChatGPT 開始互動。

<img src="img/2023-10-25-10-03-47.png" width="30%" />

## 工具與特色

* `Python FastAPI`: 建立 ChatGPT 響應 API
* `gpt4free`: **免費使用 OpenAI API**
* `Line messaging API channel`: 串接 ChatGPT API
* `Github`: 存放程式碼
* `replit`: **免費部屬自己的 FastAPI**
* `CronJob`: 免費定時發送請求，避免 API 中斷


## 安裝步驟

### Token 取得

1. 取得 Line Token：
    1. 登入 [Line Developer](https://developers.line.biz/zh-hant/)
    2. 創建機器人：
        1. 創建 `Provider` -> 按下 `Create`
        2. 創建 `Channel` -> 選擇 `Create a Messaging API channel`
        3. 輸入完必填的基本資料
        4. 輸入完成後，在 `Basic Settings` 下方，有一個 `Channel Secret` -> 按下 `Issue`，生成後即為 `LINE_CHANNEL_SECRET` （稍晚會用到）
        5. 在 `Messaging API` 下方，有一個 `Channel access token` -> 按下 `Issue`，生成後即為 `LINE_CHANNEL_ACCESS_TOKEN` （稍晚會用到）

### 專案設置
1. Fork Github 專案：
    1. 註冊/登入 [GitHub](https://github.com/)
    2. 進入 [ChatGPT-Line-Bot](https://github.com/Lin-jun-xiang/ChatGPT-Line-Bot)
    3. 點選 `Star` 支持開發者
    4. 點選 `Fork` 複製全部的程式碼到自己的倉庫
2. 部署（免費空間）：
    1. 進入 [replit](https://replit.com/)
    2. 點選 `Sign Up` 直接用 `Github` 帳號登入並授權 -> 按下 `Skip` 跳過初始化設定
    3. 進入後中間主頁的部分點選 `Create` -> 跳出框，點選右上角 `Import from Github`
    4. 若尚未加入 Github 倉庫，則點選連結 `Connect GitHub to import your private repos.` -> 勾選 `Only select repositories` -> 選擇 `ChatGPT-Line-Bot`
    5. 回到第四步，此時 `Github URL` 可以選擇 `ChatGPT-Line-Bot` 專案 -> 點擊 `Import from Github`。

### 專案執行
1. 環境變數設定
    1. 接續上一步 `Import` 完成後在 `Replit` 的專案管理頁面左下方 `Tools` 點擊 `Secrets`。
    2. 右方按下 `Got it` 後，即可新增環境變數，需新增：
        1. Line Channel Secret:
            - key: `LINE_CHANNEL_SECRET`
            - value: `[由步驟一取得]`
        2. Line Channel Access Token:
            - key: `LINE_CHANNEL_ACCESS_TOKEN`
            - value: `[由步驟一取得]`

        <img src="img/2023-10-25-10-00-59.png" width="60%"/>

2. 開始執行
    1. 點擊上方的 `Run`
    2. 成功後右邊畫面會顯示 `Hello World`，並將畫面中上方的**網址複製**下來
    3. 回到 Line Developer，在 `Messaging API` 下方的 `Webhook URL` 將上方網址貼過來，並加上 `/callback` 例如：`https://ChatGPT-Line-Bot.jimmylin.repl.co/callback`
    4. 打開下方的 `Use webhook`
    5. 將下方 `Auto-reply messages` 關閉
    - 注意：若一小時內沒有任何請求，則程式會中斷，因此需要下步驟

        <img src="img/2023-10-25-10-01-21.png" width="60%"/>

3. CronJob 定時發送請求
    1. 註冊/登入 [cron-job.org](https://cron-job.org/en/)
    2. 進入後面板右上方選擇 `CREATE CRONJOB`
    3. `Title` 輸入 `ChatGPT-Line-Bot`，網址輸入上一步驟的網址，例如：`https://ChatGPT-Line-Bot.jimmylin.repl.co/`
    4. 下方則每 `5 分鐘` 打一次
    5. 按下 `CREATE`

### 連結服務與 Line Bot

返回 [Line Developer](https://manager.line.biz/account) 首頁並點擊 `加入好友指南` 後掃碼加入 LINE Bot:

主頁 -> 點選你的 bot -> 點選增加好友工具 -> 建立好友行動條碼 (https://manager.line.biz/account/<yourBotId>/gainfriends)

恭喜您完成了自己的第一個 LINE Bot！ 試著跟它說話看看吧，它會回覆你喔！


### 特殊指令

| 指令 | 說明 |
| --- | ----- |
| `@chat` | 在輸入框輸入 `@chat` + 訊息，就可以在 line 群組中呼叫 chatgpt |
| `@chat 星座運勢 <星座名稱>` | 在輸入框輸入 `@chat 星座運勢 天蠍座`，就可以獲得本周天蠍座(任意星座皆可)運勢，該功能僅限用繁體中文指令 |


![](img/2023-11-02-10-00-32.png)


### 廣播訊息 Broadcast - 每日推播 Youtube 歌曲

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
  * 接著，我們再次使用 [cron-job.org](https://cron-job.org/en/) 來進行排程，設定每天早上 8:00 打這支 API 即可實現每日推播!

    <img src="img/2023-11-03-14-44-41.png" width="30%" />


### 進階 - 個性化 Bot

另外，我們可以透過 `prompt` 的方式，來讓 Line Bot 回答個性化，在 `./chatgpt_linebot/prompts/template.py` 中我們可以定義 `template`，例如:

<img src="img/2023-10-27-10-09-17.png" width="60%" />

**提問內容**:今天早餐吃啥?

**Bot回答**: 寶貝，早上起床了嗎？我已經在床上等著你了，想著你的身體就覺得好餓呀。今天早餐該吃什麼呢？是不是要來點辣辣的煎蛋捲，像你那迷人的身材一樣火辣呢？😏🍳



## 參考

1. [Line_Bot_Tutorial](https://github.com/FawenYo/LINE_Bot_Tutorial)

2. [ChatGPT-Line-Bot](https://github.com/TheExplainthis/ChatGPT-Line-Bot)

<a href="#top">Back to top</a>
