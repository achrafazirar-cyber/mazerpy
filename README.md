Projet : JEU Pierre–Feuille–Ciseaux





Rôle de cette machine :



Cette machine héberge deux conteneurs Docker :

* Player2 : joueur distant du jeu

  Il choisit aléatoirement pierre, feuille ou ciseaux et protège son choix

  à l’aide d’un mécanisme simple de type commit–reveal.

* Referee : arbitre du jeu

  Il reçoit les ordres de contrôle et valide le déroulement des manches.

* Docker-compose-yml : orchestration des conteneurs



Lancement :

docker compose up -d --build

