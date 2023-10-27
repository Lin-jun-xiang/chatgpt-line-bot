# ChatGPT Line Bot

* [English](README.md)
* [繁體中文版README.md](README.zh-TW.md)
* [简体中文](README.zh-CN.md)
* [Française](README.French.md)
* [عربى](README.Arabic.md)


## 介绍

在 Line 中去导入 ChatGPT Bot，只要在输入框直接输入文字，即可与 ChatGPT 开始互动。

<img src="img/2023-10-25-10-03-47.png" width="30%" />

## 工具与特色

* `Python FastAPI`: 建立 ChatGPT 响应 API
* `gpt4free`: **免费使用 OpenAI API**
* `Line messaging API channel`: 串接 ChatGPT API
* `Github`: 存放程式码
* `replit`: **免费部署自己的 FastAPI**
* `CronJob`: 免费定时发送请求，避免 API 中断


## 安装步骤

### Token 取得

1. 取得 Line Token：
    1. 登入 [Line Developer](https://developers.line.biz/zh-hant/)
    2. 创建机器人：
        1. 创建 `Provider` -> 按下 `Create`
        2. 创建 `Channel` -> 选择 `Create a Messaging API channel`
        3. 输入完必填的基本资料
        4. 输入完成后，在 `Basic Settings` 下方，有一个 `Channel Secret` -> 按下 `Issue`，生成后即为 `LINE_CHANNEL_SECRET` （稍晚会用到）
        5. 在 `Messaging API` 下方，有一个 `Channel access token` -> 按下 `Issue`，生成后即为 `LINE_CHANNEL_ACCESS_TOKEN` （稍晚会用到）

### 專案設置
1. Fork Github 專案：
    1. 注册/登入 [GitHub](https://github.com/)
    2. 进入 [ChatGPT-Line-Bot](https://github.com/Lin-jun-xiang/ChatGPT-Line-Bot)
    3. 点击 `Star` 支持开发者
    4. 点击 `Fork` 复制全部的程式码到自己的仓库
2. 部署（免费空间）：
    1. 进入 [replit](https://replit.com/)
    2. 点击 `Sign Up` 直接用 `Github` 帐号登入并授权 -> 按下 `Skip` 跳过初始化设定
    3. 进入后中间主页的部分点击 `Create` -> 弹出框，点击右上角 `Import from Github`
    4. 若尚未加入 Github 仓库，则点击链接 `Connect GitHub to import your private repos.` -> 勾选 `Only select repositories` -> 选择 `ChatGPT-Line-Bot`
    5. 回到第四步，此时 `Github URL` 可以选择 `ChatGPT-Line-Bot` 專案 -> 点击 `Import from Github`。

### 專案執行
1. 环境变数设定
    1. 接续上一步 `Import` 完成后在 `Replit` 的專案管理页面左下方 `Tools` 点击 `Secrets`。
    2. 右方按下 `Got it` 后，即可新增环境变数，需新增：
        1. Line Channel Secret:
            - key: `LINE_CHANNEL_SECRET`
            - value: `[由步驟一取得]`
        2. Line Channel Access Token:
            - key: `LINE_CHANNEL_ACCESS_TOKEN`
            - value: `[由步驟一取得]`

        <img src="img/2023-10-25-10-00-59.png" width="60%"/>

2. 开始执行
    1. 点击上方的 `Run`
    2. 成功后右边画面会显示 `Hello World`，并将画面中上方的**网址复制**下来
    3. 回到 Line Developer，在 `Messaging API` 下方的 `Webhook URL` 将上方网址贴过来，并加上 `/callback` 例如：`https://ChatGPT-Line-Bot.jimmylin.repl.co/callback`
    4. 打开下方的 `Use webhook`
    5. 将下方 `Auto-reply messages` 关闭
    - 注意：若一小时内没有任何请求，则程式会中断，因此需要下步骤

        <img src="img/2023-10-25-10-01-21.png" width="60%"/>

3. CronJob 定时发送请求
    1. 注册/登入 [cron-job.org](https://cron-job.org/en/)
    2. 进入后面板右上方选择 `CREATE CRONJOB`
    3. `Title` 输入 `ChatGPT-Line-Bot`，网址输入上一步驟的网址，例如：`https://ChatGPT-Line-Bot.jimmylin.repl.co/`
    4. 下方则每 `5 分钟` 打一次
    5. 按下 `CREATE`

### 連結服務與 Line Bot

返回 [Line Developer](https://manager.line.biz/account) 首页并点击 `加入好友指南` 后扫码加入 LINE Bot:

主页 -> 点击你的 bot -> 点击增加好友工具 -> 建立好友行动条码 (https://manager.line.biz/account/<yourBotId>/gainfriends)

恭喜您完成了自己的第一个 LINE Bot！ 试着跟它说话看看吧，它会回复你喔！

### 進階 - 個性化 Bot

另外，我们可以透过 `prompt` 的方式，来让 Line Bot 回答个性化，在 `./chatgpt_linebot/prompts/template.py` 中我们可以定义 `template`，例如:

<img src="img/2023-10-27-10-09-17.png" width="60%" />

**提问内容**:今天早餐吃啥?

**Bot回答**: 宝贝，早上起床了吗？我已经在床上等着你了，想着你的身体就觉得好饿呀。今天早餐该吃什么呢？是不是要来点辣辣的煎蛋卷，像你那迷人的身材一样火辣呢？😏🍳

---

## 参考

[Line_Bot_Tutorial](https://github.com/FawenYo/LINE_Bot_Tutorial)

[ChatGPT-Line-Bot](https://github.com/TheExplainthis/ChatGPT-Line-Bot)