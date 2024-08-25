# NTTRAG-CHATBOT

## Description

NTTBOT est une application interactive développée en Python utilisant Streamlit, conçue pour offrir une assistance sur le développement Python à travers un chatbot sophistiqué. L'application utilise l'approche RAG (Retrieval-Augmented Generation) pour fournir des réponses précises et contextuelles en se basant sur les documents fournis par l'utilisateur.

### Technologies et Méthodes Utilisées

1. **Streamlit** : 
   - Utilisé pour construire l'interface utilisateur de manière interactive et réactive. Streamlit permet une création rapide de tableaux de bord et d'applications web en Python avec une intégration facile des widgets interactifs comme les champs de texte et les menus déroulants.

2. **RAG (Retrieval-Augmented Generation)** :
   - NTTBOT s'appuie sur l'approche RAG pour générer des réponses informées. Cette technique combine la génération de texte par modèle de langage (LLM) avec la récupération d'informations pertinentes à partir d'une base de données de documents. Cela permet de fournir des réponses plus précises et contextualisées par rapport au simple usage d'un modèle de langage.

3. **OpenAI API et ChatOpenAI** :
   - Initialement, le modèle OpenAI est utilisé pour générer des embeddings et traiter les requêtes des utilisateurs. Cependant, le code est configuré pour basculer entre les modèles OpenAI et Hugging Face selon les besoins, en permettant une flexibilité dans le choix des modèles de langage.

4. **dotenv** :
   - Utilisé pour charger les variables d'environnement à partir du fichier `.env`. Cela permet de garder les configurations sensibles (comme les clés API) sécurisées et séparées du code source.

5. **PyPDF2** :
   - Une bibliothèque Python permettant de lire et d'extraire du texte à partir de fichiers PDF. Dans NTTBOT, PyPDF2 est utilisé pour extraire le contenu textuel des documents PDF fournis, afin de les analyser et les utiliser pour la génération de réponses.

6. **LangChain** :
   - Cette application fait appel à plusieurs modules de LangChain, une bibliothèque conçue pour faciliter la création de chaînes de traitement de texte avec des modèles de langage :
     - **CharacterTextSplitter** : Sépare le texte en segments gérables (chunks) pour optimiser le traitement par les modèles de langage.
     - **OpenAIEmbeddings et HuggingFaceEmbeddings** : Convertissent le texte en vecteurs numériques, permettant leur utilisation dans les modèles de recherche et d'analyse.
     - **FAISS** : Une bibliothèque permettant la recherche de similarité à grande échelle, utilisée pour stocker et interroger les embeddings textuels.
     - **ConversationalRetrievalChain** : Crée une chaîne de récupération conversationnelle pour traiter les requêtes des utilisateurs en utilisant un modèle de langage et un historique des conversations.

7. **Hugging Face** :
   - Pour les embeddings, le modèle "sentence-transformers/all-mpnet-base-v2" est utilisé, offrant une alternative aux modèles OpenAI. Hugging Face est une plateforme ouverte fournissant une multitude de modèles de langage pour diverses applications NLP.

8. **Custom HTML/CSS Templates** :
   - Le fichier `htmlTemplates.py` contient des modèles HTML et CSS personnalisés pour styliser l'application Streamlit. Cela inclut les templates pour les messages du chatbot (bot_template) et les messages de l'utilisateur (user_template), permettant une interface utilisateur cohérente et visuellement agréable.

9. **Gestion de l'historique des conversations** :
   - Utilisation de `ConversationBufferMemory` pour stocker l'historique des conversations, permettant au chatbot de conserver le contexte lors des interactions avec les utilisateurs.

Grâce à l'utilisation de l'approche RAG, NTTBOT peut fournir une assistance avancée et contextuelle aux développeurs Python, en s'appuyant sur les documents fournis pour générer des réponses pertinentes et éclairées.

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

