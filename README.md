Projet : JEU Pierre–Feuille–Ciseaux 





Rôle de cette machine (Linux sans GUI) :



Cette machine héberge deux conteneurs Docker :

\- Player2 : joueur distant du jeu

&nbsp; Il choisit aléatoirement pierre, feuille ou ciseaux et protège son choix

&nbsp; à l’aide d’un mécanisme simple de type commit–reveal.

\- Referee : arbitre du jeu

&nbsp; Il reçoit les ordres de contrôle et valide le déroulement des manches.





Lancement :

docker compose up -d --build





