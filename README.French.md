# ChatGPT Line Bot

* [English](README.md)
* [繁體中文版README.md](README.zh-TW.md)
* [简体中文](README.zh-CN.md)
* [Française](README.French.md)
* [عربى](README.Arabic.md)

Ce projet vous montrera comment créer un **ChatGPT Line Bot** gratuit !

## Introduction

Intégrez le ChatGPT Bot dans Line en saisissant simplement du texte dans la zone de saisie pour commencer à interagir avec ChatGPT.

<img src="img/2023-10-25-10-03-47.png" width="30%" />

## Outils et fonctionnalités

* `Python FastAPI` : Créez une API de réponse ChatGPT
* `gpt4free` : **Utilisation gratuite de l'API OpenAI**
* `Line messaging API channel` : Intégration de l'API ChatGPT
* `Github` : Stockage du code
* `replit` : **Déploiement gratuit de votre propre FastAPI**
* `CronJob` : Envoi de requêtes planifiées gratuites pour éviter les interruptions de l'API


## Étapes d'installation

### Obtention du jeton

1. Obtenez le jeton Line :
    1. Connectez-vous à [Line Developer](https://developers.line.biz/zh-hant/)
    2. Créez un robot :
        1. Créez un `Provider` -> Cliquez sur `Create`
        2. Créez un `Channel` -> Sélectionnez `Create a Messaging API channel`
        3. Saisissez les informations de base obligatoires
        4. Une fois terminé, sous `Basic Settings`, vous trouverez un `Channel Secret` -> Cliquez sur `Issue`, cela générera le `LINE_CHANNEL_SECRET` (utilisé plus tard)
        5. Sous `Messaging API`, vous trouverez un `Channel access token` -> Cliquez sur `Issue`, cela générera le `LINE_CHANNEL_ACCESS_TOKEN` (utilisé plus tard)

### Configuration du projet
1. Fork du projet Github :
    1. Inscrivez-vous / Connectez-vous à [GitHub](https://github.com/)
    2. Accédez à [ChatGPT-Line-Bot](https://github.com/Lin-jun-xiang/ChatGPT-Line-Bot)
    3. Cliquez sur `Star` pour soutenir le développeur
    4. Cliquez sur `Fork` pour copier tout le code dans votre propre dépôt
2. Déploiement (espace gratuit) :
    1. Accédez à [replit](https://replit.com/)
    2. Cliquez sur `Sign Up` pour vous connecter directement avec votre compte `Github` et autoriser l'accès -> Cliquez sur `Skip` pour ignorer la configuration initiale
    3. Une fois connecté, cliquez sur `Create` sur la page principale au milieu -> Une fenêtre contextuelle apparaîtra, cliquez sur `Import from Github` en haut à droite
    4. Si vous n'avez pas encore ajouté de dépôt Github, cliquez sur le lien `Connect GitHub to import your private repos.` -> Cochez `Only select repositories` -> Sélectionnez `ChatGPT-Line-Bot`
    5. Revenez à l'étape 4, à ce stade, vous pouvez sélectionner le projet `ChatGPT-Line-Bot` dans `Github URL` -> Cliquez sur `Import from Github`.

### Exécution du projet
1. Configuration des variables d'environnement
    1. Une fois l'étape précédente d'importation terminée, cliquez sur `Tools` en bas à gauche de la page de gestion du projet dans `Replit` -> Cliquez sur `Secrets`.
    2. Cliquez sur `Got it` à droite pour ajouter des variables d'environnement, vous devez ajouter :
        1. Line Channel Secret :
            - clé : `LINE_CHANNEL_SECRET`
            - valeur : `[obtenue à l'étape 1]`
        2. Line Channel Access Token :
            - clé : `LINE_CHANNEL_ACCESS_TOKEN`
            - valeur : `[obtenue à l'étape 1]`

2. Démarrage de l'exécution
    1. Cliquez sur `Run` en haut
    2. Une fois terminé avec succès, l'écran de droite affichera `Hello World`, copiez l'**URL en haut de l'écran**.
    3. Retournez à Line Developer, dans `Messaging API`, collez l'URL ci-dessus dans `Webhook URL` et ajoutez `/callback`, par exemple : `https://ChatGPT-Line-Bot.jimmylin.repl.co/callback`
    4. Activez `Use webhook`
    5. Désactivez les `Auto-reply messages` ci-dessous
    - Remarque : si aucune requête n'est effectuée dans l'heure, le programme s'arrêtera, vous devez donc suivre l'étape suivante

3. Envoi de requêtes planifiées avec CronJob
    1. Inscrivez-vous / Connectez-vous à [cron-job.org](https://cron-job.org/en/)
    2. Une fois connecté, sélectionnez `CREATE CRONJOB` dans le coin supérieur droit du tableau de bord
    3. Saisissez `ChatGPT-Line-Bot` dans `Title`, entrez l'URL de l'étape précédente, par exemple : `https://ChatGPT-Line-Bot.jimmylin.repl.co/`
    4. En dessous, sélectionnez toutes les `5 minutes`
    5. Cliquez sur `CREATE`

### Lier le service et le Line Bot

Revenez à la page d'accueil de [Line Developer](https://developers.line.biz/zh-hant/) et cliquez sur `加入好友指南` pour scanner le code et ajouter le LINE Bot. Félicitations, vous avez créé votre premier LINE Bot ! Essayez de lui parler et voyez sa réponse !

---

## Références

[Line_Bot_Tutorial](https://github.com/FawenYo/LINE_Bot_Tutorial)

[ChatGPT-Line-Bot](https://github.com/TheExplainthis/ChatGPT-Line-Bot)