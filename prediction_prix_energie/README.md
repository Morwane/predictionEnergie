# Projet: Prédiction des Prix de l'Électricité et du Gaz

## Description

Ce projet vise à développer un modèle de Machine Learning pour prédire les prix spot de l'électricité et du gaz sur des horizons de court terme. Il utilise des données historiques de prix, météorologiques et de marché pour fournir des prévisions précises, utiles pour l'optimisation des stratégies de trading et de hedging.

## Fonctionnalités

- **Collecte de Données:** Intégration conceptuelle avec l'API Refinitiv/LSEG pour récupérer des données historiques.
- **Prétraitement et Feature Engineering:** Nettoyage des données, gestion des valeurs manquantes, création de caractéristiques temporelles, de lags et de moyennes glissantes.
- **Modélisation:** Entraînement et optimisation de modèles de régression (XGBoost) avec validation croisée pour séries temporelles.
- **Backtesting:** Simulation d'une stratégie de hedging simple pour évaluer la performance du modèle dans un scénario réaliste.
- **Reporting:** Génération de visualisations clés et d'un rapport de synthèse des performances.

## Structure du Projet

```
prediction_prix_energie/
├── data/
│   ├── raw/                # Données brutes
│   └── processed/          # Données prétraitées
├── notebooks/              # Notebooks Jupyter pour l'exploration et le prototypage
├── src/                    # Code source organisé en modules
│   ├── data_ingestion/
│   ├── data_preprocessing/
│   ├── modeling/
│   ├── backtesting/
│   ├── reporting/
│   └── utils/
├── models/                 # Modèles entraînés
├── reports/                # Rapports et visualisations générés
├── tests/                  # Tests unitaires
├── main.py                 # Point d'entrée principal
├── requirements.txt        # Dépendances Python
├── README.md               # Ce fichier
├── .env                    # Variables d'environnement (non versionné)
└── .gitignore              # Fichiers et dossiers à ignorer par Git
```

## Installation

1.  **Cloner le dépôt:**
    ```bash
    git clone <URL_DU_DEPOT>
    cd prediction_prix_energie
    ```

2.  **Créer un environnement virtuel et l'activer:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows: .\venv\Scripts\activate
    ```

3.  **Installer les dépendances:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuration des variables d'environnement:**
    Créez un fichier `.env` à la racine du projet et ajoutez vos clés API Refinitiv/LSEG (si vous en avez) ou d'autres configurations sensibles. Exemple:
    ```
    RDP_APP_KEY=YOUR_APP_KEY
    RDP_USERNAME=YOUR_USERNAME
    ELECTRICITY_RIC=EEX_EL_BASE_DE_DA
    GAS_RIC=TTF_DA
    START_DATE=2022-01-01
    END_DATE=2023-12-31
    ```

## Utilisation

Pour exécuter le pipeline complet du projet, lancez le script `main.py`:

```bash
python main.py
```

Les résultats (modèles sauvegardés, rapports, graphiques) seront générés dans les dossiers `models/` et `reports/`. Pour la connexion à LSEG, assurez-vous que le SDK `refinitiv-data` est correctement configuré avec vos identifiants.

## Exécution des Tests

Pour exécuter les tests unitaires, assurez-vous d'être dans l'environnement virtuel activé et exécutez:

```bash
pytest
```

## Auteur

Manus AI

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.


