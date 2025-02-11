# ChatGPT Line Bot

* [English](README.md)
* [繁體中文版README.md](README.zh-TW.md)
* [简体中文](README.zh-CN.md)
* [Française](README.French.md)

## 🤖 简介

將 ChatGPT Bot 整合到 Line。只需在輸入框中輸入文字，即可開始與 ChatGPT 互動。

<img src="img/2023-10-25-10-03-47.png" width="30%" />

## ✨ 功能

* **完全免费** 的 ChatGPT Bot
* 每周 **星座资讯**（即时）

    <img src="img/2023-11-02-10-00-32.png" width="20%"/>

* **YouTube 音乐** 频道的定时推送

    <img src="img/2023-11-03-14-44-41.png" width="30%" />

* **在线图片搜索**（即时）

    <img src="img/2024-05-17-15-08-12.png" width="40%"/>

> [!NOTE]
> 如果你有任何功能请求，请随时提交 PR 或 ISSUE。

## 🔨 工具

* `Python FastAPI`：创建 ChatGPT 回应 API
* `gpt4free`：**免费使用 OpenAI API**
* `zhipuai`：**免费使用 GPT API**
* `Line messaging API channel`：连接 ChatGPT API
* `GitHub`：代码存储库
* `replit/render/ngrok`：**免费部署你自己的 FastAPI**
* `CronJob`：免费发送定时请求，实现定时推送消息

## 🧠 免费GPT选项

由于 `g4f` 依赖逆向工程来调用 OpenAI 的 API，可能会不稳定。因此，作者建议使用 **智谱 AI** 开放平台作为免费 GPT API 的替代方案。

* `g4f`：使用逆向工程调用 OpenAI API
* `zhipuai`：**智谱 AI** 开放平台提供免费 GPT API。访问 [官方网站](https://open.bigmodel.cn/dev/howuse/glm-4) 注册账户，无需信用卡或费用。在 [个人中心](https://open.bigmodel.cn/usercenter/proj-mgmt/apikeys) 添加 API 密钥，如下所示。将此 API 密钥设置在环境变量中使用此 GPT 选项。
    ![](static/images/2025-01-02-10-18-10.png)

## 🎈 安装步骤

### 获取 Tokens

1. 获取 Line Tokens：
    1. 登录 [Line Developer](https://developers.line.biz/en/)
    2. 创建一个 bot：
        1. 创建一个 `Provider` -> 点击 `Create`
        2. 创建一个 `Channel` -> 选择 `Create a Messaging API channel`
        3. 填写所需的基本信息
        4. 完成后，进入 `Basic Settings` -> 在 `Channel Secret` 下，点击 `Issue` 生成 `LINE_CHANNEL_SECRET`（后面会用到）。
        5. 在 `Messaging API` 下，点击 `Issue` 生成 `Channel access token`（后面会用到）。

### 项目设置与执行

1. Fork GitHub 项目：
    * 注册/登录 [GitHub](https://github.com/)
    * 前往 [ChatGPT-Line-Bot](https://github.com/Lin-jun-xiang/ChatGPT-Line-Bot)
    * 点击 `Star` 支持开发者
    * 点击 `Fork` 将所有代码复制到你的存储库

2. 启动 Python FastAPI Server:
   * `$env:LINE_CHANNEL_SECRET="..."; $env:LINE_CHANNEL_ACCESS_TOKEN="..."; $env:SERPAPI_API_KEY="..."; $env:GPT_METHOD="..."; $env:GPT_API_KEY="..."; python main.py`
      * `GPT_METHOD`：选择 `g4f` 或 `zhipuai`
      * `GPT_API_KEY`：如果使用 `zhipuai` 方法，提供你的 API 密钥

3. `ngrok`：使用本地电脑（或 Google Colab）作为服务器来部署 API
   *  [建立 ngrok 环境](https://dashboard.ngrok.com/get-started/setup/)
   *  下载适合你操作系统的 `ngrok` 版本
   *  将 `ngrok.exe` 路径添加到系统的环境变量中
   *  执行：`ngrok config add-authtoken <token>`。从你的个人 [ngrok dashboard](https://dashboard.ngrok.com/get-started/your-authtoken) 获得token。
   *  执行：`ngrok http --url=<YOUR STATIC DOMAIN>.ngrok-free.app 8090` (若失败请尝试 `ngrok http --hostname=<YOUR STATIC DOMAIN>.ngrok-free.app 8090`)，并将 URL 转发为 webhook URL。

      <img src="static/images/2025-02-11-16-16-27.png" width="60%" />

      <img src="img/2024-05-15-14-03-09.png" width="60%"/>

4. 最后，将 `http --url=<YOUR STATIC DOMAIN>.ngrok-free.app/callback` 替换 Line Developer 控制台 `Messaging API` 区域中的 webhook URL。

    <img src="static/images/2025-02-11-16-26-05.png" width="60%" />

### 连接服务与 Line Bot

回到 [Line Developer 首页](https://manager.line.biz/account)，点击 `Add Friend Guide`，扫描 QR 码将 Line Bot 添加为好友。

首页 -> 选择你的 bot -> 添加好友工具 -> 创建好友动作条码（https://manager.line.biz/account/<yourBotId>/gainfriends）

恭喜！你已经创建了你的第一个 Line Bot。试着与它交谈——它会回复你！

## ⛄ 群组对话 vs. 个人对话

* 在一对一对话中，任何消息都会触发回复。
* 在群组对话中，使用 `@chat` 前缀与机器人互动，例如，`@chat hi~`。

## 🎃 特殊功能

### 星座

当你的消息包含星座资讯请求时，网络爬虫将抓取每周星座：

* 个人聊天：`给我天蝎座星座`, `我想知道天蝎座星座`, ...
* 群组聊天：`@chat 给我天蝎座星座`, `@chat 我想知道天蝎座星座`, ...

### 在线图片搜索

当你的消息包含图片请求时，网络爬虫将抓取图片：

* 个人聊天：`在线找到林翔抽烟的图片`, `给我在线林翔抽烟的图片`, ...
* 群组聊天：`@chat 在线找到林翔抽烟的图片`, `@chat 给我在线林翔抽烟的图片`, ...

## 📢 广播消息 - 每日 YouTube 推荐

* 使用 `broadcast` API，Line Bot 可以一次性推送消息给所有用户。
* 此示例演示了 Line Bot 如何每天早上推送 3 首随机选择的歌曲：
  * 创建文件 `./data/favorite_videos.json`。参考作者的数据集。

    （数据集是使用 `YouTube Data v3 API` 抓取喜爱视频生成的。本指南不涉及 YouTube API 的使用。）

  * 使用 `./ChatGPT_linebot/modules/youtube_recommend.py` 随机选择 3 首歌曲，由 GPT 格式化。
  * 在 `./ChatGPT_linebot/urls.py` 中添加 `/recommend` 路由：

    ```python
    videos = recommend_videos() # 获取 3 首歌曲

    if videos:
        line_bot_api.broadcast(TextSendMessage(text=videos)) # 广播给用户

        # 推送消息给已知群组
        known_group_ids = [
            'C6d-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
            'Ccc-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
            'Cbb-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        ]
        for group_id in known_group_ids:
            line_bot_api.push_message(group_id, TextSendMessage(text=videos))
    ```

    要获取群组 `group_id`，在控制台中打印：

    ```python
    elif event.source.type == 'group' and user_message.startswith('@chat'):
        group_id = event.source.group_id
        print(group_id) # 输出 group_id
    ```

  * 现在，访问 `/recommend` 路由将广播消息给所有用户和指定群组。
  * 使用 [cron-job.org](https://cron-job.org/en/) 每天早上 8:00 定时推送：
    1. 注册/登录 [cron-job.org](https://cron-job.org/en/)
    2. 点击右上角的 `CREATE CRONJOB`
    3. 标题：`ChatGPT-Line-Bot`，URL：例如，`https://ChatGPT-Line-Bot.jimmylin.repl.co/`
    4. 设置为每 `5 分钟` 运行
    5. 点击 `CREATE`

## 📢 广播消息 - 天下杂志财经资讯

* 与 **每日 YouTube 推荐** 一样，只需要将 `/recommend` 替换成 `/cwsChannel` 即可。
* 可于 CronJob 设置每 `3 小时` 运行

  <img src="static/images/2025-02-11-17-27-24.png" width="60%" />

## ⚔ 高级 - 个性化 Bot

你可以使用提示语来个性化 Line Bot 的回复。在 `./ChatGPT_linebot/prompts/template.py` 中定义 `template`，例如：

<img src="img/2023-10-27-10-09-17.png" width="60%" />

**用户输入**：我该吃些什么早餐？

**Bot 回复**：亲爱的，你醒来了吗？我一直在床上等你，想着你美丽的身材。我们该吃些什么早餐？要不要来点辣的，比如热蛋卷，配得上你火辣的魅力？😏🍳

## 参考资料

1. [Line_Bot_Tutorial](https://github.com/FawenYo/LINE_Bot_Tutorial)

2. [ChatGPT-Line-Bot](https://github.com/TheExplainthis/ChatGPT-Line-Bot)

<a href="#top">返回顶部</a>
  --------------------------------