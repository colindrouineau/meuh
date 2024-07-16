08 « Outil de traçabilité et qualité multi-sites pour des fermes laitières » RESAN -
http://projets-mines.pl.sophia.inria.fr/subjects/RESAN-bastien-debras-1/projet-p23-bastien-debras-resan-1.html

Propriétaire du code : Meuh group, composé de Cyrianne Chabert, Elisa Skowronek et Colin Drouineau

Ce code est une ébauche d'un code de développement d'un site internet de l'entreprise RESAN. 

RESAN équipe des agriculteurs et agricultrices (agris) d'une unité complète pour produire des yaourts et crèmes dessert. Pour des besoins de traçabilité et de contrôle des pratiques, les agris doivent faire parvenir à RESAN des informations précises sur la fabrication des produits (lot de pots, lot d'arôme, date de tirage du lait, température, dates de nettoyages, etc). De même, RESAN doit faire parvenir certaines informations aux agris, comme les dates d'arrivée des pots, des arômes, les dates de livraison. RESAN doit s'assurer que les agris s'acquittent des mesures d'hygiène, que les procédures sont bien respectées.

Vue la quantité d'informations échangées, il devient de plus en plus pressant d'automatiser et de normaliser les données, surtout si le nombre d'agris venait à augmenter.

Le site répond à ce besoin : il est une interface entre RESAN et les agris. A chaque fois qu'un.e agri effectue une tâche au sein de l'installation, iel répertorie sa tâche sur le site. L'agri transmet aussi toutes les informations utiles à la traçabilité par le site. Toutes ces informations sont stockées dans une base de données accessible à RESAN. Notre code prévoit d'envoyer périodiquement un mail à RESAN avec un tableau excell des tâches de la période. 
En plus d'être une interface, le site doit aider les agris à avoir une vision claire des tâches accomplies et des tâches à accomplir. Nous proposons le format d'un calendrier. Celui-ci est en cours de développement.

Nous ne l'avons pas implémenté, mais on pourrait imaginer avoir une version semblable du côté de RESAN : quels fournisseurs appeler, quand, où en est le stock de chaque agri (calculable à partir de la base de données). Le site, s'il est bien codé, complet et pratique, pourrait grandement faciliter le travail logistique chez RESAN.


How to launch the code :
Start signup.py



À quoi servent tous les documents qu’il y a sur ce repo GitHub ?

Il y a le premier document : signup.py qui est le document principal qui créé l’architecture du site.
Ce code python renvoit vers tous les autres documents du repo.


Ligne 30 : le document HTML “home.html” qui permet de donner les noms aux boutons de connexion et d’inscription.

Ligne 57 : le document HTML “signup.html” qui créé le format des cases d’inscription (Nom, prénom, email, identifiant et mot de passe)

Ligne 109 : le document HTML “login.html” qui créé le format des cases de connexion (identifiant et mot de passe)

Ligne 148 : le document HTML “index_accueil.html” qui créé la page d’accueil du site. Ce code HTML permet de créer les boutons qui redirigent vers les pages “paramètres”, “recettes” et “calendrier”, donne la date du jour et créé les cases à cocher des tasks du jour ainsi que le menu déroulant des produits à faire.

Ligne 155 : le document HTML “calendrier.html”. Ce document renvoie aux codes CSS et JavaScipt aux noms calendrier.css et calendrier.js. Ces trois documents permettent de formater le calendrier que nous voulons. Le principal problème pour l’instant est l’accès aux évènements créés. Nous n’arrivons pas à synchroniser le calendrier avec la base de donnée, ainsi pour le moment, aucun des évènements rajoutés dans le calendrier ne s’ajoutent automatiquement dans la base de données et donc dans les tasks à faire dans la journée. Nous pensons qu’une manière de faire ça est de transformer les évènements en “bouton”, ainsi nous pourrions accéder directement à la valeur de l’évènement et donc l’ajouter dans la BDD.



Ligne 160 : le document HTML “menu.html” qui créé l’onglet “recettes” (toutes les recettes des produits ainsi que les notices de nettoyage).
