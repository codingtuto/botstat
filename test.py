"""
$$$$$$$$\                    $$\                             
\__$$  __|                   $$ |                            
   $$ | $$$$$$\   $$$$$$$\ $$$$$$\        $$$$$$\  $$\   $$\ 
   $$ |$$  __$$\ $$  _____|\_$$  _|      $$  __$$\ $$ |  $$ |
   $$ |$$$$$$$$ |\$$$$$$\    $$ |        $$ /  $$ |$$ |  $$ |
   $$ |$$   ____| \____$$\   $$ |$$\     $$ |  $$ |$$ |  $$ |
   $$ |\$$$$$$$\ $$$$$$$  |  \$$$$  |$$\ $$$$$$$  |\$$$$$$$ |
   \__| \_______|\_______/    \____/ \__|$$  ____/  \____$$ |
                                         $$ |      $$\   $$ |
                                         $$ |      \$$$$$$  |
                                         \__|       \______/ 
"""
from botstat import *

# Charger les statistiques existantes
statistiques = charger_statistiques()

# Mettre à jour les statistiques pour une commande
commande = "/start"
user_id = 12345
heure_commande = "14"
jour_semaine = "Lundi"
mettre_a_jour_statistiques_commande(statistiques, commande, user_id, heure_commande, jour_semaine)

# Enregistrer de nouvelles statistiques
sauvegarder_statistiques(statistiques)

# Afficher les données d'utilisation
stats_text = "Statistiques d'utilisation des commandes:\n"
for date, commands in statistiques['commands'].items():
    stats_text += f"\nDate: {date}\n"
    for command, data in commands.items():
        nombre_utilisations = data['nombre_utilisations']
        utilisateurs_commande = len(data['utilisateurs'])
        heures = data.get('heures', {})
        heures_text = ', '.join([f"{heure}: {utilisations} utilisations" for heure, utilisations in heures.items()])
        stats_text += f"- {command} : {nombre_utilisations} utilisations par {utilisateurs_commande} utilisateurs ({heures_text})\n"

print(stats_text)