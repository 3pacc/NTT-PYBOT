# NTTRAG-CHATBOT

## Description

Ce repository contient le code source pour NTTRAG-CHATBOT, une application développée en Python en utilisant Streamlit. Cette application implémente un chatbot basé sur un modèle de génération augmentée par la récupération (Retrieval-Augmented Generation, RAG) avec des informations sur le développement Python. Le projet est structuré de manière à inclure des modèles d'interface HTML personnalisés et des variables d'environnement pour configurer l'application.

## Contenu du Repository

- **`.env`** : Ce fichier contient les variables d'environnement nécessaires au bon fonctionnement de l'application, telles que les clés API et autres configurations sensibles.

- **`app.py`** : Le fichier principal de l'application Streamlit. Il configure l'interface utilisateur, les options de navigation via la barre latérale, et intègre le chatbot NTTRAG.

- **`htmlTemplates.py`** : Ce fichier contient des templates HTML/CSS utilisés pour styliser les différentes sections de l'application Streamlit, permettant une interface utilisateur personnalisée et responsive.

## Installation

1. Clonez le repository :

    ```bash
    git clone <URL_DU_REPOSITORY>
    cd nttrag-chatbot
    ```

2. Créez un environnement virtuel et activez-le :

    ```bash
    python -m venv env
    source env/bin/activate  # Pour macOS/Linux
    env\Scripts\activate  # Pour Windows
    ```

3. Installez les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

4. Configurez les variables d'environnement :

    Assurez-vous que le fichier `.env` contient toutes les variables nécessaires. Vous pouvez ajuster ces valeurs en fonction de votre configuration locale.

5. Lancez l'application :

    ```bash
    streamlit run app.py
    ```

## Utilisation

- **Navigation** : Utilisez la barre latérale pour naviguer entre les différentes sections de l'application.
- **Chatbot** : Interagissez avec le chatbot NTTRAG pour obtenir des réponses basées sur les documents de développement Python.
- **Personnalisation** : Vous pouvez personnaliser l'interface en modifiant les templates HTML/CSS dans `htmlTemplates.py`.

## Contribution

Les contributions sont les bienvenues ! Si vous souhaitez contribuer à ce projet, veuillez suivre ces étapes :

1. Forkez le repository.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/ma-fonctionnalité`).
3. Commitez vos modifications (`git commit -am 'Ajout de ma fonctionnalité'`).
4. Poussez votre branche (`git push origin feature/ma-fonctionnalité`).
5. Ouvrez une Pull Request.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

