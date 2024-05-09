# Ellipse Bikes

Ce projet a été développé sur Windows en utilisant le framework Django. Il communique également avec la base de données PostgreSQL installée sur Windows, avec ses Extensions Spatiales (PostGIS) installées.


# Assurez-vous d'abord d'avoir Docker installé sur votre machine.

****

**Ouvrez un terminal ou une invite de commande, puis exécutez :**

***Cloner le projet :***
```
git clone https://github.com/omerAlzain/Ellipse-Bikes.git
```

***Déplacez-vous vers le répertoire racine du projet :***
```
cd Ellipse-Bikes
```

***Exécutez Docker Compose :***
```
docker compose up
```

**Ouvrez un autre terminal ou invite de commande et exécutez :**

```
docker exec -it ellipse-bikes-web-1 bash
```
Les deux commandes suivantes doivent être exécutées une seule fois, mais si **vous avez supprimé la base de données,** vous devez les exécuter à nouveau.

```
root@1eb2904a53b6:/code# python3 manage.py createcachetable
```
```
root@1eb2904a53b6:/code# python3 manage.py createsuperuser
```

Vous serez demander votre nom, votre e-mail et votre mot de passe. Ils sont utilisés pour accéder au site d'administration.
Ensuite, démarrez le cluster, qui est un processus qui exécute les plannings de django-q2.

```
root@1eb2904a53b6:/code# python3 manage.py qcluster &
```

**C'est tout.**

Vous pouvez maintenant accéder au site d'administration à l'adresse suivante :

```
localhost:8000/admin
```

en utilisant le nom et le mot de passe ci-dessus.

Pour accéder à la base de données PostgreSQL fonctionnant sur le conteneur depuis votre hôte pgadmin4 ou tout autre client,
utilisez ces détails de connexion :

```
host: localhost
port: 8001
database: ellipse_bikes
user: bike
password: bike
```
Vous pouvez modifier tout cela depuis le fichier docker-compose.yml.
Remarquez également que les fichiers de la base de données seront stockés dans le répertoire racine du projet dans .postgres_data/db,
donc si vous voulez **supprimer la base de données**, vous devez supprimer le conteneur Docker (Si vous avez Docker Desktop,
il est facile de trouver le conteneur que vous voulez supprimer. Le nôtre est "django_project") puis supprimer le répertoire *(.postgres_data/db)* .

