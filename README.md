## Aperçu

Ce script est conçu pour extraire des offres d'emploi du site [portaljob-madagascar.com](https://www.portaljob-madagascar.com) et les afficher soit dans la console, soit les enregistrer dans un fichier CSV.

## Fonctionnalités

- Récupérer les offres d'emploi de plusieurs pages.
- Afficher les détails des offres d'emploi tels que le nom de l'entreprise, le titre du poste, le type de contrat, la date limite de candidature et le lien vers la description de l'offre.
- Enregistrer les détails des offres d'emploi dans un fichier CSV.

## Exigences

- Python 3.x
- Bibliothèque `requests`
- Bibliothèque `beautifulsoup4`
- Bibliothèque `argparse` (standard avec Python)

## Installation

1. Clonez le dépôt :

```bash
git clone https://github.com/RazTahiry/Mada_Job_Scraper.git
```

2. Installez les bibliothèques requises à l'aide de pip :

```bash
pip install requests beautifulsoup4
```

## Utilisation

Le script peut être exécuté depuis la ligne de commande. Il accepte deux arguments :
1. Le nombre de pages à extraire (requis).
2. Un argument optionnel pour spécifier un fichier CSV où enregistrer les détails des offres d'emploi.

### Arguments en ligne de commande

- `pages_quantity` (requis) : Nombre de pages à extraire.
- `--csv` (optionnel) : Chemin vers le fichier CSV où les détails des offres d'emploi seront enregistrés.

### Exemples

1. **Afficher les détails des offres d'emploi dans la console :**

```bash
python mada_job_scraper.py 3
```

Cette commande extraira les offres d'emploi des 3 premières pages et affichera les détails dans la console.

2. **Enregistrer les détails des offres d'emploi dans un fichier CSV :**

```bash
python mada_job_scraper.py 3 --csv jobs.csv
```

Cette commande extraira les offres d'emploi des 3 premières pages et enregistrera les détails dans `jobs.csv`.
