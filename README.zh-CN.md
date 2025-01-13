# ChatGPT Line Bot

* [English](README.md)
* [繁體中文版README.md](README.zh-TW.md)
* [简体中文](README.zh-CN.md)
* [Française](README.French.md)

## 🤖 简介

将 ChatGPT Bot 集成到 Line。只需在输入框中输入文本即可开始与 ChatGPT 互动。

<img src="img/2023-10-25-10-03-47.png" width="30%" />

## ✨ 特性

* **完全免费** 的 ChatGPT Bot
* 每周 **星座信息**（实时）

    <img src="img/2023-11-02-10-00-32.png" width="20%"/>

* **YouTube 音乐** 频道的定时推送

    <img src="img/2023-11-03-14-44-41.png" width="30%" />

* **在线图片搜索**（实时）

    <img src="img/2024-05-17-15-08-12.png" width="40%"/>

> [!NOTE]
> 如果你有任何功能请求，请随时提交 PR 或 ISSUE。

## 🔨 工具

* `Python FastAPI`：创建 ChatGPT 响应 API
* `gpt4free`：**免费使用 OpenAI API**
* `zhipuai`：**免费使用 GPT API**
* `Line messaging API channel`：连接 ChatGPT API
* `GitHub`：代码仓库
* `replit/render/ngrok`：**免费部署你自己的 FastAPI**
* `CronJob`：免费发送定时请求，实现定时推送消息

## 🧠 免费 GPT 选项

由于 `g4f` 依赖于逆向工程来调用 OpenAI 的 API，可能会不稳定。因此，作者建议使用 **智谱 AI** 开放平台作为免费 GPT API 的替代方案。

* `g4f`：使用逆向工程调用 OpenAI API
* `zhipuai`：**智谱 AI** 开放平台提供免费 GPT API。访问 [官方网站](https://open.bigmodel.cn/dev/howuse/glm-4) 注册账号，无需信用卡或费用。在 [个人中心](https://open.bigmodel.cn/usercenter/proj-mgmt/apikeys) 添加 API 密钥，如下所示。将此 API 密钥设置在环境变量中使用此 GPT 选项。
    ![](static/images/2025-01-02-10-18-10.png)

## 🎈 安装步骤

### 获取 Tokens

1. 获取 Line Tokens：
    1. 登录 [Line Developer](https://developers.line.biz/en/)
    2. 创建一个 bot：
        1. 创建一个 `Provider` -> 点击 `Create`
        2. 创建一个 `Channel` -> 选择 `Create a Messaging API channel`
        3. 填写所需的基本信息
        4. 完成后，进入 `Basic Settings` -> 在 `Channel Secret` 下，点击 `Issue` 生成 `LINE_CHANNEL_SECRET`（后续使用）。
        5. 在 `Messaging API` 下，点击 `Issue` 生成 `Channel access token`（后续使用）。

### 项目设置与执行

1. Fork GitHub 项目：
    1. 注册/登录 [GitHub](https://github.com/)
    2. 导航至 [ChatGPT-Line-Bot](https://github.com/Lin-jun-xiang/ChatGPT-Line-Bot)
    3. 点击 `Star` 支持开发者
    4. 点击 `Fork` 将所有代码复制到你的仓库
2. 部署：

* `ngrok`：使用本地计算机（或 Google Colab）作为服务器部署 API
  * 下载适用于你操作系统的 `ngrok` 版本
  * 将 `ngrok.exe` 路径添加到系统的环境变量
  * 在终端启动 FastAPI：`$env:LINE_CHANNEL_SECRET="..."; $env:LINE_CHANNEL_ACCESS_TOKEN="..."; $env:SERPAPI_API_KEY="..."; $env:GPT_METHOD="..."; $env:GPT_API_KEY="..."; python main.py`
    * `GPT_METHOD`：选择 `g4f` 或 `zhipuai`
    * `GPT_API_KEY`：如果使用 `zhipuai` 方法，提供你的 API 密钥
  * 运行：`ngrok config add-authtoken <token>`。从你的个人 [ngrok dashboard](https://dashboard.ngrok.com/get-started/your-authtoken) 获取 token。
  * 运行：`ngrok http 8080`。转发 URL 将是 webhook URL。

    <img src="img/2024-05-15-14-03-09.png" width="60%"/>

最后，替换 Line Developer 控制台 `Messaging API` 部分的 webhook URL。（[参见项目设置步骤 2](#project-setup-and-execution)）

### 将服务与 Line Bot 连接

返回 [Line Developer 主页](https://manager.line.biz/account)，点击 `Add Friend Guide`，扫描二维码将 Line Bot 添加为好友。

主页 -> 选择你的 bot -> 添加好友工具 -> 创建好友行动条码 (https://manager.line.biz/account/<yourBotId>/gainfriends)

恭喜！你已创建你的第一个 Line Bot。试着和它聊天——它会回复你！

## ⛄ 群聊 vs. 单聊

* 在一对一聊天中，任何消息都会触发回复。
* 在群聊中，使用 `@chat` 前缀与 bot 互动，例如，`@chat hi~`。

## 🎃 特殊功能

### 星座

当你的消息包含星座信息请求时，网络爬虫将获取每周星座：

* 个人聊天：`给我天蝎座星座`, `我想知道天蝎座星座`, ...
* 群聊：`@chat 给我天蝎座星座`, `@chat 我想知道天蝎座星座`, ...

### 在线图片搜索

当你的消息包含图片请求时，网络爬虫将获取图片：

* 个人聊天：`在线找一张林翔抽烟的图片`, `给我一张林翔抽烟的图片`, ...
* 群聊：`@chat 在线找一张林翔抽烟的图片`, `@chat 给我一张林翔抽烟的图片`, ...

## 📢 广播消息 - 每日 YouTube 推荐

* 使用 `broadcast` API，Line Bot 可以一次性向所有用户推送消息。
* 此示例演示了 Line Bot 如何每天早上推送 3 首随机选择的 YouTube 歌曲：
  * 创建文件 `./data/favorite_videos.json`。参考作者的数据集。

    （数据集是使用 `YouTube Data v3 API` 获取收藏视频生成的。本指南不涵盖 YouTube API 使用。）

  * 使用 `./ChatGPT_linebot/modules/youtube_recommend.py` 随机选择 3 首歌曲，由 GPT 格式化。
  * 在 `./ChatGPT_linebot/urls.py` 中添加 `/recommend` 路由：

    ```python
    videos = recommend_videos() # 获取 3 首歌曲

    if videos:
        line_bot_api.broadcast(TextSendMessage(text=videos)) # 向用户广播

        # 向已知群组推送消息
        known_group_ids = [
            'C6d-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
            'Ccc-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
            'Cbb-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        ]
        for group_id in known_group_ids:
            line_bot_api.push_message(group_id, TextSendMessage(text=videos))
    ```

    要获取群组 `group_id`，在控制台打印：

    ```python
    elif event.source.type == 'group' and user_message.startswith('@chat'):
        group_id = event.source.group_id
        print(group_id) # 输出 group_id
    ```

  * 现在，访问 `/recommend` 路由将向所有用户和指定群组广播消息。
  * 使用 [cron-job.org](https://cron-job.org/en/) 每天早上 8:00 安排定时推送：
    1. 注册/登录 [cron-job.org](https://cron-job.org/en/)
    2. 点击右上角的 `CREATE CRONJOB`
    3. 标题：`ChatGPT-Line-Bot`，URL：例如，`https://ChatGPT-Line-Bot.jimmylin.repl.co/`
    4. 设置为每 `5 分钟` 运行
    5. 点击 `CREATE`

## ⚔ 高级 - 个性化 Bot

你可以使用提示词个性化 Line Bot 的回复。在 `./ChatGPT_linebot/prompts/template.py` 中定义 `template`，例如：

<img src="img/2023-10-27-10-09-17.png" width="60%" />

**用户输入**：早餐吃什么？

**Bot 回复**：亲爱的，你醒了吗？我在床上等着，想着你可爱的身材。我们早餐吃什么？要不要来点辣的，比如一个热腾腾的煎蛋卷，配得上你火辣的魅力？😏🍳

## 免费部署选项

## 参考文献

1. [Line_Bot_Tutorial](https://github.com/FawenYo/LINE_Bot_Tutorial)

2. [ChatGPT-Line-Bot](https://github.com/TheExplainthis/ChatGPT-Line-Bot)

<a href="#top">回到顶部</a>