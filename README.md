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


## Structure du Projet

### Fichiers Principaux du Projet Django
- `django_project/`
  - `__init__.py`: Fichier d'initialisation Python.
  - `asgi.py`: Point d'entrée pour les serveurs ASGI (Asynchronous Server Gateway Interface).
  - `settings.py`: Fichier de configuration principal du projet Django.
  - `urls.py`: Définition des URLs de l'application.
  - `wsgi.py`: Point d'entrée pour les serveurs WSGI (Web Server Gateway Interface).

### Application Ellipse Bikes
- `ellipse_bikes/`
  - `cron/`: Scripts de tâches cron pour la gestion de tâches périodiques.
    - `func.py`: Fonctions utilisées par les tâches cron.
  - `data/`: Fichiers JSON contenant les données sur les contrats et les stations.
  - `management/`: Gestion des commandes personnalisées pour Django.
    - `commands/`: Commandes personnalisées pour la gestion des données.
  - `migrations/`: Migrations de la base de données.
  - `static/ellipse_bikes/css/`: Fichiers CSS spécifiques à l'application.
  - `templates/ellipse_bikes/`: Modèles HTML spécifiques à l'application.
  - `admin.py`: Configuration de l'interface d'administration.
  - `apps.py`: Configuration de l'application.
  - `forms.py`: Définition des formulaires.
  - `models.py`: Définition des modèles de données.
  - `tests.py`: Fichiers de tests.
  - `urls.py`: Définition des URLs de l'application.
  - `views.py`: Définition des vues de l'application.

### Autres Fichiers et Répertoires
- `.dockerignore`: Fichiers à ignorer lors de la construction des images Docker.
- `.env`: Variables d'environnement.
- `.gitignore`: Fichiers à ignorer lors du suivi avec Git.
- `Dockerfile`: Instructions pour la construction de l'image Docker.
- `docker-compose.yml`: Configuration Docker Compose pour le déploiement et l'exécution du projet.
- `manage.py`: Script de gestion Django.
- `pyproject.toml`: Configuration du projet Python.
- `requirements.txt`: Liste des dépendances Python.
- `setup.cfg`: Configuration du package Python.
- `setup.py`: Script de configuration du package Python.

