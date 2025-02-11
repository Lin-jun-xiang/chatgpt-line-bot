# ChatGPT Line Bot

* [English](README.md)
* [繁體中文版README.md](README.zh-TW.md)
* [简体中文](README.zh-CN.md)
* [Française](README.French.md)

## 🤖 簡介

將 ChatGPT Bot 整合到 Line。只需在輸入框中輸入文字，即可開始與 ChatGPT 互動。

<img src="img/2023-10-25-10-03-47.png" width="30%" />

## ✨ 功能

* **完全免費** 的 ChatGPT Bot
* 每週 **星座資訊**（即時）

    <img src="img/2023-11-02-10-00-32.png" width="20%"/>

* **YouTube 音樂** 頻道的定時推播

    <img src="img/2023-11-03-14-44-41.png" width="30%" />

* **在線圖片搜尋**（即時）

    <img src="img/2024-05-17-15-08-12.png" width="40%"/>

> [!NOTE]
> 如果你有任何功能請求，請隨時提交 PR 或 ISSUE。

## 🔨 工具

* `Python FastAPI`：創建 ChatGPT 回應 API
* `gpt4free`：**免費使用 OpenAI API**
* `zhipuai`：**免費使用 GPT API**
* `Line messaging API channel`：連接 ChatGPT API
* `GitHub`：代碼存儲庫
* `replit/render/ngrok`：**免費部署你自己的 FastAPI**
* `CronJob`：免費發送定時請求，實現定時推播消息

## 🧠 免費 GPT 選項

由於 `g4f` 依賴於逆向工程來調用 OpenAI 的 API，可能會不穩定。因此，作者建議使用 **Zhipu AI** 開放平台作為免費 GPT API 的替代方案。

* `g4f`：使用逆向工程調用 OpenAI API
* `zhipuai`：**Zhipu AI** 開放平台提供免費 GPT API。訪問 [官方網站](https://open.bigmodel.cn/dev/howuse/glm-4) 註冊帳戶，無需信用卡或費用。在 [個人中心](https://open.bigmodel.cn/usercenter/proj-mgmt/apikeys) 添加 API 金鑰，如下所示。將此 API 金鑰設置在環境變量中使用此 GPT 選項。
    ![](static/images/2025-01-02-10-18-10.png)

## 🎈 安裝步驟

### 獲取 Tokens

1. 獲取 Line Tokens：
    1. 登錄 [Line Developer](https://developers.line.biz/en/)
    2. 創建一個 bot：
        1. 創建一個 `Provider` -> 點擊 `Create`
        2. 創建一個 `Channel` -> 選擇 `Create a Messaging API channel`
        3. 填寫所需的基本信息
        4. 完成後，進入 `Basic Settings` -> 在 `Channel Secret` 下，點擊 `Issue` 生成 `LINE_CHANNEL_SECRET`（後面會用到）。
        5. 在 `Messaging API` 下，點擊 `Issue` 生成 `Channel access token`（後面會用到）。

### 專案設置與執行

1. Fork GitHub 專案：
    * 註冊/登錄 [GitHub](https://github.com/)
    * 前往 [ChatGPT-Line-Bot](https://github.com/Lin-jun-xiang/ChatGPT-Line-Bot)
    * 點擊 `Star` 支持開發者
    * 點擊 `Fork` 將所有代碼複製到你的存儲庫

2. 啟動 Python FastAPI Server:
   *  `$env:LINE_CHANNEL_SECRET="..."; $env:LINE_CHANNEL_ACCESS_TOKEN="..."; $env:SERPAPI_API_KEY="..."; $env:GPT_METHOD="..."; $env:GPT_API_KEY="..."; python main.py`
      * `GPT_METHOD`：選擇 `g4f` 或 `zhipuai`
      * `GPT_API_KEY`：如果使用 `zhipuai` 方法，提供你的 API 金鑰

3. `ngrok`：使用本地電腦（或 Google Colab）作為服務器來部署 API
   *  [建立 ngrok 環境](https://dashboard.ngrok.com/get-started/setup/)
   *  下載適合你操作系統的 `ngrok` 版本
   *  將 `ngrok.exe` 路徑添加到系統的環境變量中
   *  執行：`ngrok config add-authtoken <token>`。從你的個人 [ngrok dashboard](https://dashboard.ngrok.com/get-started/your-authtoken) 獲取 token。
   *  執行：`ngrok http --url=<YOUR STATIC DOMAIN>.ngrok-free.app 8090` (若失敗請改嘗試 `ngrok http --hostname=<YOUR STATIC DOMAIN>.ngrok-free.app 8090`)，並轉發 URL 將作為 webhook URL。

      <img src="static/images/2025-02-11-16-16-27.png" width="60%" />

      <img src="img/2024-05-15-14-03-09.png" width="60%"/>

4. 最後，將 `http --url=<YOUR STATIC DOMAIN>.ngrok-free.app/callback` 替換 Line Developer 控制台 `Messaging API` 區域中的 webhook URL。

    <img src="static/images/2025-02-11-16-26-05.png" width="60%" />

### 連接服務與 Line Bot

回到 [Line Developer 首頁](https://manager.line.biz/account)，點擊 `Add Friend Guide`，掃描 QR 碼將 Line Bot 添加為好友。

首頁 -> 選擇你的 bot -> 添加好友工具 -> 創建好友動作條碼（https://manager.line.biz/account/<yourBotId>/gainfriends）

恭喜！你已創建了你的第一個 Line Bot。試著與它交談——它會回覆你！

## ⛄ 群組對話 vs. 個人對話

* 在一對一對話中，任何消息都會觸發回應。
* 在群組對話中，使用 `@chat` 前綴與機器人互動，例如，`@chat hi~`。

## 🎃 特殊功能

### 星座

當你的消息包含星座資訊請求時，網絡爬蟲將抓取每週星座：

* 個人聊天：`給我天蠍座星座`, `我想知道天蠍座星座`, ...
* 群組聊天：`@chat 給我天蠍座星座`, `@chat 我想知道天蠍座星座`, ...

### 在線圖片搜尋

當你的消息包含圖片請求時，網絡爬蟲將抓取圖片：

* 個人聊天：`在線找到林翔抽煙的圖片`, `給我在線林翔抽煙的圖片`, ...
* 群組聊天：`@chat 在線找到林翔抽煙的圖片`, `@chat 給我在線林翔抽煙的圖片`, ...

## 📢 廣播消息 - 每日 YouTube 推薦

* 使用 `broadcast` API，Line Bot 可以一次性推送消息給所有用戶。
* 此示例演示了 Line Bot 如何每天早上推送 3 首隨機選擇的 YouTube 歌曲：
  * 創建文件 `./data/favorite_videos.json`。參考作者的數據集。

    （數據集是使用 `YouTube Data v3 API` 抓取喜愛視頻生成的。本指南不涉及 YouTube API 的使用。）

  * 使用 `./ChatGPT_linebot/modules/youtube_recommend.py` 隨機選擇 3 首歌曲，由 GPT 格式化。
  * 在 `./ChatGPT_linebot/urls.py` 中添加 `/recommend` 路由：

    ```python
    videos = recommend_videos() # 獲取 3 首歌曲

    if videos:
        line_bot_api.broadcast(TextSendMessage(text=videos)) # 廣播給用戶

        # 推送消息給已知群組
        known_group_ids = [
            'C6d-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
            'Ccc-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
            'Cbb-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        ]
        for group_id in known_group_ids:
            line_bot_api.push_message(group_id, TextSendMessage(text=videos))
    ```

    要獲取群組 `group_id`，在控制台中打印：

    ```python
    elif event.source.type == 'group' and user_message.startswith('@chat'):
        group_id = event.source.group_id
        print(group_id) # 輸出 group_id
    ```

  * 現在，訪問 `/recommend` 路由將廣播消息給所有用戶和指定群組。
  * 使用 [cron-job.org](https://cron-job.org/en/) 每天早上 8:00 定時推送：
    1. 註冊/登錄 [cron-job.org](https://cron-job.org/en/)
    2. 點擊右上角的 `CREATE CRONJOB`
    3. 標題：`ChatGPT-Line-Bot`，URL：例如，`https://ChatGPT-Line-Bot.jimmylin.repl.co/`
    4. 設置為每 `5 分鐘` 运行
    5. 點擊 `CREATE`

## 📢 廣播消息 - 天下雜誌財經資訊

* 與 **每日 YouTube 推薦** 一樣，只需要將 `/recommend` 替換成 `/cwsChannel` 即可。
* 可於 CronJob 設置每 `3 小時` 運行

  <img src="static/images/2025-02-11-17-27-24.png" width="60%" />

## ⚔ 進階 - 個性化 Bot

你可以使用提示語來個性化 Line Bot 的回應。在 `./ChatGPT_linebot/prompts/template.py` 中定義 `template`，例如：

<img src="img/2023-10-27-10-09-17.png" width="60%" />

**用戶輸入**：我應該吃什麼早餐？

**Bot 回應**：親愛的，你醒來了嗎？我一直在床上等你，想著你美麗的身材。我們應該吃什麼早餐？要不要來點辣的，比如熱蛋捲，配得上你火辣的魅力？😏🍳

## 參考資料

1. [Line_Bot_Tutorial](https://github.com/FawenYo/LINE_Bot_Tutorial)

2. [ChatGPT-Line-Bot](https://github.com/TheExplainthis/ChatGPT-Line-Bot)

<a href="#top">返回頂部</a>
  