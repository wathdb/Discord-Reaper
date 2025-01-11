```markdown
# 💻 **Discord Reaper Bot** 🤖

**Discord Reaper Bot** is a powerful tool that allows you to remotely control a PC via Discord. Once configured, it can be launched automatically at system startup and execute commands from Discord with ease.

## 🔥 **Advantages** 🚀

- **Ease of Use**: Create a Discord bot that can execute any system command via Discord. 👨‍💻
- **Auto-Start**: Add your program to Windows startup so it runs automatically every time the PC reboots. 🔄
- **Invisible to Antivirus** 🦠: The generated file is designed not to be detected by traditional antivirus programs.
- **Maximum Permissions**: The bot uses all necessary permissions to control and interact with Discord. ✅
- **Portable**: The bot is compiled into a `.exe` executable file, easy to distribute and run.

---

## 🛠️ **Installation & Usage** ⚙️

### 1️⃣ Prerequisites

Before starting, make sure you have Python and `pip` installed on your machine. You'll also need `requests` and `discord.py`.

In the terminal, install the dependencies:

```bash
pip install -r requirements.txt
```

### 2️⃣ Generate Your Executable File

Download the program and run the script to generate the Discord bot and the `.exe` executable.

```bash
python your_script.py
```

When running, the script will ask for:

- **BOT TOKEN**: Enter your Discord bot token. ⚠️ **WARNING**: Use a unique token for each copy of the program. If you use multiple tokens on the same copy, the program won't work.
- **FILE NAME**: Choose a name for the `.exe` file that will be generated.

The bot will be compiled into a `.exe` file in the `dist` folder.

### 3️⃣ Run the Discord Bot

Once the executable is generated, you can open it. It will automatically add itself to Windows startup so the bot will run without intervention. 🚀

---

## 🔧 **Bot Commands** 📝

- **!command <command>**: Executes a system command on the remote PC.

Example:
```bash
!command echo Hello World
```

---

## 🌟 **Generate an Invitation Link for Your Bot** 🔗

The program generates an invitation link to add it to your Discord servers to interact with it (⚠️ only via DM).

Example of the generated invitation link:
```
https://discord.com/oauth2/authorize?client_id=<BOT_ID>&permissions=8&scope=bot
```

---

## 🚨 **Important** ⚠️

- This bot is for **educational purposes only**. Using this script for malicious or unethical purposes is strictly prohibited.
- It is essential to respect the **legality** and **privacy** of other users. 🚫

---

## 📄 **License** 📝

This project is licensed under the **CC BY-NC-ND 4.0** license. You are free to use this code, but you cannot modify it or use it for commercial purposes without permission.

---

## 📢 **Support** 🤝

If you have any questions or issues with the bot, feel free to open an **issue** or contact me directly via Discord (wathd)!

---

**Create, customize, and remotely control your machines with Discord Reaper Bot!** 🔥
```
