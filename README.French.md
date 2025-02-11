```markdown
# ChatGPT Line Bot

* [English](README.md)
* [繁體中文版README.md](README.zh-TW.md)
* [简体中文](README.zh-CN.md)
* [Française](README.French.md)

## 🤖 Présentation

Intégrez le ChatGPT Bot à Line. Entrez simplement du texte dans la zone de saisie pour commencer à interagir avec ChatGPT.

<img src="img/2023-10-25-10-03-47.png" width="30%" />

## ✨ Fonctionnalités

* ChatGPT Bot **completement gratuit**
* **Informations astrologiques hebdomadaires** (en temps réel)

    <img src="img/2023-11-02-10-00-32.png" width="20%"/>

* **Push notifications de chaînes YouTube musique** (à heure fixe)

    <img src="img/2023-11-03-14-44-41.png" width="30%" />

* **Recherche d'images en ligne** (en temps réel)

    <img src="img/2024-05-17-15-08-12.png" width="40%"/>

> [!NOTE]
> Si vous avez des demandes de fonctionnalités, veuillez soumettre PR ou ISSUE à tout moment.

## 🔨 Outils

* `Python FastAPI` : Créez une API de réponse ChatGPT
* `gpt4free` : **Utilisation gratuite de l'API OpenAI**
* `zhipuai` : **Utilisation gratuite de l'API GPT**
* `Line messaging API channel` : Connectez l'API ChatGPT
* `GitHub` : Dépôt de code
* `replit/render/ngrok` : **Déploiement gratuit de votre propre FastAPI**
* `CronJob` : Envoyez des demandes programmées gratuites pour effectuer des push notifications

## 🧠 Options GPT gratuites

En raison de la dépendance de `g4f` à l'inversement d'API OpenAI, elle peut être instable. Par conséquent, l'auteur recommande d'utiliser la plate-forme ouverte **Zhipu AI** comme alternative gratuite à l'API GPT.

* `g4f` : Utilise l'inversement pour appeler l'API OpenAI
* `zhipuai` : **Plateforme ouverte Zhipu AI** fournissant une API GPT gratuite. Visitez [site officiel](https://open.bigmodel.cn/dev/howuse/glm-4) pour vous inscrire, sans carte de crédit ni frais. Ajoutez l'API clé dans [centre personnel](https://open.bigmodel.cn/usercenter/proj-mgmt/apikeys) comme indiqué ci-dessous. Configurez cette clé API dans les variables d'environnement pour utiliser cette option GPT.
    ![](static/images/2025-01-02-10-18-10.png)

## 🎈 Instructions d'installation

### Obtenir des Tokens

1. Obtenez des Tokens Line :
    1. Connectez-vous à [Line Developer](https://developers.line.biz/en/)
    2. Créez un bot :
        1. Créez un `Provider` -> Cliquez sur `Create`
        2. Créez un `Channel` -> Choisissez `Create a Messaging API channel`
        3. Remplissez les informations de base nécessaires
        4. Terminez la création, puis accédez à `Basic Settings` -> Cliquez sur `Issue` pour générer `LINE_CHANNEL_SECRET` (utile après) .
        5. Sous `Messaging API`, cliquez sur `Issue` pour générer `Channel access token` (utile après).

### Configuration du projet et exécution

1. Fork le projet GitHub :
    * Inscrivez-vous / connectez-vous à [GitHub](https://github.com/)
    * Allez à [ChatGPT-Line-Bot](https://github.com/Lin-jun-xiang/ChatGPT-Line-Bot)
    * Cliquez sur `Star` pour soutenir le développeur
    * Cliquez sur `Fork` pour copier tout le code dans votre dépôt

2. Démarrer le serveur Python FastAPI :
   * `$env:LINE_CHANNEL_SECRET="..."; $env:LINE_CHANNEL_ACCESS_TOKEN="..."; $env:SERPAPI_API_KEY="..."; $env:GPT_METHOD="..."; $env:GPT_API_KEY="..."; python main.py`
      * `GPT_METHOD` : Choisissez `g4f` ou `zhipuai`
      * `GPT_API_KEY` : Si vous utilisez la méthode `zhipuai`, fournissez votre clé API

3. `ngrok` : Déployez l'API localement en utilisant votre ordinateur (ou Google Colab) comme serveur
   * [Créez l'environnement ngrok](https://dashboard.ngrok.com/get-started/setup/)
   * Téléchargez la version de `ngrok` adaptée à votre système d'exploitation
   * Ajoutez le chemin d'accès à `ngrok.exe` aux variables d'environnement du système
   * Exécutez : `ngrok config add-authtoken <token>` . Obtenez le token à partir de votre [tableau de bord personnel ngrok](https://dashboard.ngrok.com/get-started/your-authtoken) .
   * Exécutez : `ngrok http --url=<YOUR STATIC DOMAIN>.ngrok-free.app 8090` (si cela échoue, essayez `ngrok http --hostname=<YOUR STATIC DOMAIN>.ngrok-free.app 8090`) , puis redirigez l'URL en tant que webhook URL.

      <img src="static/images/2025-02-11-16-16-27.png" width="60%" />

      <img src="img/2024-05-15-14-03-09.png" width="60%"/>

4. Enfin, remplacez `http --url=<YOUR STATIC DOMAIN>.ngrok-free.app/callback` par le webhook URL dans la section `Messaging API` de la console de Line Developer.

    <img src="static/images/2025-02-11-16-26-05.png" width="60%" />

### Connecter les services et le Line Bot

Retournez à [Line Developer Home](https://manager.line.biz/account), cliquez sur `Add Friend Guide`, scannez le QR code pour ajouter le Line Bot comme ami.

Page d'accueil -> Sélectionnez votre bot -> Outils d'ajout d'ami -> Créez un code d'action d'ami (https://manager.line.biz/account/<yourBotId>/gainfriends)

Félicitations ! Vous avez créé votre premier Line Bot. Essayez de lui parler — il vous répondra !

## ⛄ Conversation de groupe vs. Conversation personnelle

* Dans une conversation un à un, tout message déclenche une réponse.
* Dans une conversation de groupe, utilisez le préfixe `@chat` pour interagir avec le robot, par exemple, `@chat hi~`.

## 🎃 Fonctionnalités spéciales

### Astrologie

Lorsque votre message contient une demande d'information astrologique, le spider Web capture chaque semaine les informations astrologiques :

* Conversation personnelle : `Donnez-moi le signe du Scorpion`, `Je veux savoir le signe du Scorpion`, ...
* Conversation de groupe : `@chat Donnez-moi le signe du Scorpion`, `@chat Je veux savoir le signe du Scorpion`, ...

### Recherche d'images en ligne

Lorsque votre message contient une demande d'image, le spider Web capture l'image :

* Conversation personnelle : `Trouver en ligne une photo de Lin Xiang qui fume`, `Donnez-moi une photo en ligne de Lin Xiang qui fume`, ...
* Conversation de groupe : `@chat Trouver en ligne une photo de Lin Xiang qui fume`, `@chat Donnez-moi une photo en ligne de Lin Xiang qui fume`, ...

## 📢 Messages de diffusion - recommandations YouTube quotidiennes

* Comme pour **Daily YouTube Recommendations**, il suffit de remplacer `/recommend` par `/cwsChannel`.
* Il est possible de configurer CronJob pour exécuter toutes les `3 heures`.

  <img src="static/images/2025-02-11-17-27-24.png" width="60%" />

## ⚔ Avancé - Bot personnalisé

Vous pouvez utiliser des prompts pour personnaliser les réponses du Line Bot. Définissez `template` dans `./ChatGPT_linebot/prompts/template.py`, par exemple :

<img src="img/2023-10-27-10-09-17.png" width="60%" />

**Entrée de l'utilisateur** : Je devrais manger quoi pour le petit-déjeuner ?

**Réponse du Bot** : Cher, es-tu réveillé ? Je suis resté au lit, attendant ton magnifique corps. Que devrions-nous manger pour le petit-déjeuner ? Peut-être quelque chose de piquant, comme un wrap chaud, qui correspond à ta charmante personnalité ? 😏🍳

## Ressources de référence

1. [Line_Bot_Tutorial](https://github.com/FawenYo/LINE_Bot_Tutorial)

2. [ChatGPT-Line-Bot](https://github.com/TheExplainthis/ChatGPT-Line-Bot)

<a href="#top">Retour en haut</a>
   --------------------------------
```