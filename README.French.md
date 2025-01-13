# ChatGPT Line Bot

* [English](README.md)
* [繁體中文版README.md](README.zh-TW.md)
* [简体中文](README.zh-CN.md)
* [Française](README.French.md)

## 🤖 Introduction

Intégrez le bot ChatGPT à Line. Tapez simplement du texte dans la zone de saisie pour commencer à interagir avec ChatGPT.

<img src="img/2023-10-25-10-03-47.png" width="30%" />

## ✨ Fonctionnalités

* **Complètement gratuit** Bot ChatGPT
* Informations **horoscope hebdomadaire** (en temps réel)

    <img src="img/2023-11-02-10-00-32.png" width="20%"/>

* Notification programmée pour les chaînes de **musique YouTube**

    <img src="img/2023-11-03-14-44-41.png" width="30%" />

* **Recherche d'images en ligne** (en temps réel)

    <img src="img/2024-05-17-15-08-12.png" width="40%"/>

> [!NOTE]
> Si vous avez des demandes de fonctionnalités, n'hésitez pas à soumettre un PR ou un ISSUE.

## 🔨 Outils

* `Python FastAPI` : Créer l'API de réponse ChatGPT
* `gpt4free` : **Utiliser l'API OpenAI gratuitement**
* `zhipuai` : **Utiliser l'API GPT gratuitement**
* `Line messaging API channel` : Connecter l'API ChatGPT
* `GitHub` : Dépôt de code
* `replit/render/ngrok` : **Déployer votre propre FastAPI gratuitement**
* `CronJob` : Envoyer des requêtes programmées gratuitement, permettant des messages de notification programmés

## 🧠 Options gratuites GPT

Puisque `g4f` dépend du reverse engineering pour appeler l'API d'OpenAI, il peut être instable. Par conséquent, l'auteur suggère une solution alternative utilisant la plateforme ouverte **Zhipu AI** pour accéder gratuitement à l'API GPT.

* `g4f` : Utiliser le reverse engineering pour appeler l'API OpenAI
* `zhipuai` : La plateforme ouverte **Zhipu AI** offre une API GPT gratuite. Visitez le [site officiel](https://open.bigmodel.cn/dev/howuse/glm-4) pour créer un compte sans nécessiter de carte de crédit ni frais. Ajoutez une clé API dans le [Centre Personnel](https://open.bigmodel.cn/usercenter/proj-mgmt/apikeys) comme indiqué ci-dessous. Définissez cette clé API dans les variables d'environnement pour utiliser cette option GPT.
    ![](static/images/2025-01-02-10-18-10.png)

## 🎈 Étapes d'installation

### Obtenir les Tokens

1. Obtenir les Tokens Line :
    1. Connectez-vous à [Line Developer](https://developers.line.biz/en/)
    2. Créer un bot :
        1. Créer un `Provider` -> Cliquez sur `Create`
        2. Créer un `Channel` -> Sélectionnez `Create a Messaging API channel`
        3. Remplissez les informations de base requises
        4. Après completion, allez dans `Basic Settings` -> Sous `Channel Secret`, cliquez sur `Issue` pour générer le `LINE_CHANNEL_SECRET` (utilisé plus tard).
        5. Sous `Messaging API`, cliquez sur `Issue` pour générer le `Channel access token` (utilisé plus tard).

### Configuration et Exécution du Projet

1. Forker le Projet GitHub :
    1. Inscrivez-vous/Connectez-vous à [GitHub](https://github.com/)
    2. Naviguez vers [ChatGPT-Line-Bot](https://github.com/Lin-jun-xiang/ChatGPT-Line-Bot)
    3. Cliquez sur `Star` pour soutenir le développeur
    4. Cliquez sur `Fork` pour copier tout le code dans votre dépôt
2. Déploiement :

* `ngrok` : Utiliser un ordinateur local (ou Google Colab) comme serveur pour déployer l'API
  * Téléchargez la version appropriée de `ngrok` pour votre OS
  * Ajoutez le chemin de `ngrok.exe` aux variables d'environnement de votre système
  * Lancer FastAPI dans le terminal : `$env:LINE_CHANNEL_SECRET="..."; $env:LINE_CHANNEL_ACCESS_TOKEN="..."; $env:SERPAPI_API_KEY="..."; $env:GPT_METHOD="..."; $env:GPT_API_KEY="..."; python main.py`
    * `GPT_METHOD` : Choisissez `g4f` ou `zhipuai`
    * `GPT_API_KEY` : Si vous utilisez la méthode `zhipuai`, fournissez votre clé API
  * Exécutez : `ngrok config add-authtoken <token>`. Obtenez le token depuis votre tableau de bord personnel [ngrok](https://dashboard.ngrok.com/get-started/your-authtoken).
  * Exécutez : `ngrok http 8080`. L'URL de transfert sera l'URL du webhook.

    <img src="img/2024-05-15-14-03-09.png" width="60%"/>

Enfin, remplacez l'URL du webhook dans la section `Messaging API` de la console Line Developer. ([Voir l'étape 2 dans la Configuration du Projet](#project-setup-and-execution))

### Connecter le Service avec le Bot Line

Revenez à la [page d'accueil Line Developer](https://manager.line.biz/account), cliquez sur `Add Friend Guide`, et scannez le QR code pour ajouter le Bot Line comme ami.

Page d'accueil -> Sélectionnez votre bot -> Outils d'ajout d'ami -> Créer un Code-barres d'Action d'Ami (https://manager.line.biz/account/<yourBotId>/gainfriends)

Félicitations ! Vous avez créé votre premier Bot Line. Essayez de lui parler - il vous répondra !

## ⛄ Chat de Groupe vs Chat Individuel

* Dans un chat en tête-à-tête, n'importe quel message déclenchera une réponse.
* Dans les chats de groupe, utilisez le préfixe `@chat` pour interagir avec le bot, par exemple, `@chat hi~`.

## 🎃 Fonctionnalités Spéciales

### Horoscope

Lorsque votre message contient une demande d'information sur l'horoscope, un crawler web récupérera l'horoscope hebdomadaire :

* Chat personnel : `Donne-moi l'horoscope du Scorpion`, `Je veux connaître l'horoscope du Scorpion`, ...
* Chat de groupe : `@chat Donne-moi l'horoscope du Scorpion`, `@chat Je veux connaître l'horoscope du Scorpion`, ...

### Recherche d'Images en Ligne

Lorsque votre message contient une demande d'image, un crawler web récupérera une image :

* Chat personnel : `Trouve une image de Lin Xiang fumer en ligne`, `Donne-moi une image de Lin Xiang fumer en ligne`, ...
* Chat de groupe : `@chat Trouve une image de Lin Xiang fumer en ligne`, `@chat Donne-moi une image de Lin Xiang fumer en ligne`, ...

## 📢 Messages de Diffusion - Recommandations YouTube Quotidiennes

* En utilisant l'API `broadcast`, le Bot Line peut pousser des messages à tous les utilisateurs en même temps.
* Cet exemple montre comment le Bot Line peut pousser 3 chansons YouTube sélectionnées au hasard chaque matin :
  * Créez le fichier `./data/favorite_videos.json`. Référez-vous au jeu de données de l'auteur.

    (Le jeu de données est généré en utilisant l'API `YouTube Data v3` pour récupérer les vidéos favorites. Ce guide ne couvre pas l'utilisation de l'API YouTube.)

  * Utilisez `./ChatGPT_linebot/modules/youtube_recommend.py` pour sélectionner 3 chansons au hasard, formatées par GPT.
  * Ajoutez une route `/recommend` dans `./ChatGPT_linebot/urls.py` :

    ```python
    videos = recommend_videos() # Obtenir 3 chansons

    if videos:
        line_bot_api.broadcast(TextSendMessage(text=videos)) # Diffuser aux utilisateurs

        # Pousser des messages aux groupes connus
        known_group_ids = [
            'C6d-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
            'Ccc-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
            'Cbb-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        ]
        for group_id in known_group_ids:
            line_bot_api.push_message(group_id, TextSendMessage(text=videos))
    ```

    Pour récupérer le `group_id`, affichez-le dans la console :

    ```python
    elif event.source.type == 'group' and user_message.startswith('@chat'):
        group_id = event.source.group_id
        print(group_id) # Sortir group_id
    ```

  * Maintenant, appeler la route `/recommend` diffusera des messages à tous les utilisateurs et aux groupes spécifiés.
  * Utilisez [cron-job.org](https://cron-job.org/en/) pour programmer des poussées quotidiennes à 8h00 :
    1. Inscrivez-vous/Connectez-vous à [cron-job.org](https://cron-job.org/en/)
    2. Cliquez sur `CREATE CRONJOB` dans le coin supérieur droit
    3. Titre : `ChatGPT-Line-Bot`, URL : par exemple, `https://ChatGPT-Line-Bot.jimmylin.repl.co/`
    4. Définir pour s'exécuter toutes les `5 minutes`
    5. Cliquez sur `CREATE`

## ⚔ Avancé - Bot Personnalisé

Vous pouvez personnaliser les réponses du Bot Line en utilisant des prompts. Définissez `template` dans `./ChatGPT_linebot/prompts/template.py`, par exemple :

<img src="img/2023-10-27-10-09-17.png" width="60%" />

**Entrée utilisateur** : Que devrais-je prendre pour le petit-déjeuner ?

**Réponse du bot** : Chérie, es-tu déjà réveillée ? J'ai attendu au lit, en pensant à ta silhouette adorable. Que devrions-nous prendre pour le petit-déjeuner ? Et si on prenait quelque chose d'épicé, comme une omelette brûlante pour correspondre à ton charme ardent ? 😏🍳

## Options de Déploiement Gratuit

## Références

1. [Line_Bot_Tutorial](https://github.com/FawenYo/LINE_Bot_Tutorial)

2. [ChatGPT-Line-Bot](https://github.com/TheExplainthis/ChatGPT-Line-Bot)

<a href="#top">Retour en haut</a>