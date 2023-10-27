# ChatGPT Line Bot

* [English](README.md)
* [繁體中文版README.md](README.zh-TW.md)
* [简体中文](README.zh-CN.md)
* [Française](README.French.md)
* [عربى](README.Arabic.md)


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

### 進階 - 個性化 Bot

另外，我們可以透過 `prompt` 的方式，來讓 Line Bot 回答個性化，在 `./chatgpt_linebot/prompts/template.py` 中我們可以定義 `template`，例如:

<img src="img/2023-10-27-10-09-17.png" width="60%" />

**提問內容**:今天早餐吃啥?

**Bot回答**: 寶貝，早上起床了嗎？我已經在床上等著你了，想著你的身體就覺得好餓呀。今天早餐該吃什麼呢？是不是要來點辣辣的煎蛋捲，像你那迷人的身材一樣火辣呢？😏🍳

---

## 參考

[Line_Bot_Tutorial](https://github.com/FawenYo/LINE_Bot_Tutorial)

[ChatGPT-Line-Bot](https://github.com/TheExplainthis/ChatGPT-Line-Bot)
