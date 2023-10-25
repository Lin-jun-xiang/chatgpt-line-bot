# ChatGPT Line Bot

* [English](README.md)
* [繁體中文版README.md](README.zh-TW.md)
* [简体中文](README.zh-CN.md)
* [Française](README.French.md)
* [عربى](README.Arabic.md)

本项目将教你如何打造一个免费的 **ChatGPT Line Bot**!

## 介绍

在 Line 中去导入 ChatGPT Bot，只要在输入框直接输入文字，即可与 ChatGPT 开始互动。

<img src="img/2023-10-25-10-03-47.png" width="30%" />

## 工具与特色

* `Python FastAPI`: 建立 ChatGPT 响应 API
* `gpt4free`: **免费使用 OpenAI API**
* `Line messaging API channel`: 串接 ChatGPT API
* `Github`: 存放代码
* `replit`: **免费部署自己的 FastAPI**
* `CronJob`: 免费定时发送请求，避免 API 中断

## 安装步骤

### Token 获取

1. 获取 Line Token：
    1. 登入 [Line Developer](https://developers.line.biz/zh-hant/)
    2. 创建机器人：
        1. 创建 `Provider` -> 按下 `Create`
        2. 创建 `Channel` -> 选择 `Create a Messaging API channel`
        3. 输入完必填的基本资料
        4. 输入完成后，在 `Basic Settings` 下方，有一个 `Channel Secret` -> 按下 `Issue`，生成后即为 `LINE_CHANNEL_SECRET` （稍后会用到）
        5. 在 `Messaging API` 下方，有一个 `Channel access token` -> 按下 `Issue`，生成后即为 `LINE_CHANNEL_ACCESS_TOKEN` （稍后会用到）

### 项目设置

1. Fork Github 项目：
    1. 注册/登录 [GitHub](https://github.com/)
    2. 进入 [ChatGPT-Line-Bot](https://github.com/Lin-jun-xiang/ChatGPT-Line-Bot)
    3. 点选 `Star` 支持开发者
    4. 点选 `Fork` 复制全部的代码到自己的仓库
2. 部署（免费空间）：
    1. 进入 [replit](https://replit.com/)
    2. 点选 `Sign Up` 直接用 `Github` 帐号登录并授权 -> 按下 `Skip` 跳过初始化设置
    3. 进入后中间主页的部分点选 `Create` -> 弹出框，点选右上角 `Import from Github`
    4. 若尚未加入 Github 仓库，则点选链接 `Connect GitHub to import your private repos.` -> 勾选 `Only select repositories` -> 选择 `ChatGPT-Line-Bot`
    5. 回到第四步，此时 `Github URL` 可以选择 `ChatGPT-Line-Bot` 项目 -> 点击 `Import from Github`。

### 项目执行

1. 环境变数设定
    1. 接续上一步 `Import` 完成后在 `Replit` 的项目管理页面左下方 `Tools` 点击 `Secrets`。
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
    - 注意：若一小时内没有任何请求，则程序会中断，因此需要下步骤

        <img src="img/2023-10-25-10-01-21.png" width="60%"/>

3. CronJob 定时发送请求
    1. 注册/登录 [cron-job.org](https://cron-job.org/en/)
    2. 进入后面板右上方选择 `CREATE CRONJOB`
    3. `Title` 输入 `ChatGPT-Line-Bot`，网址输入上一步骤的网址，例如：`https://ChatGPT-Line-Bot.jimmylin.repl.co/`
    4. 下方则每 `5 分钟` 打一次
    5. 按下 `CREATE`

### 连结服务与 Line Bot

返回 [Line Developer](https://developers.line.biz/zh-hant/) 首页并点击 `加入好友指南` 后扫码加入 LINE Bot，恭喜您完成了自己的第一个 LINE Bot！ 试着跟它说话看看吧，它会回复你喔！

---

## 参考

[Line_Bot_Tutorial](https://github.com/FawenYo/LINE_Bot_Tutorial)

[ChatGPT-Line-Bot](https://github.com/TheExplainthis/ChatGPT-Line-Bot)
