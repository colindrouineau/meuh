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