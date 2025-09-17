# Révision pour l'épreuve finale - 2025E-930-MA

Vous disposez d'un code initial dans `main.py` contenant plusieurs faiblesses.
Votre objectif est de produire une version refactorisée en applicant les
notions enseignées dans le cours.

## Contexte

Le programme calcule un prix final et autres informations pour un produit en
tenant compte du type de client.

## Problèmes à résoudre dans `main.py`

Les problèmes sont identifiés par des commentaires `# FIXME ...` dans le code.

Vous ne devez PAS ajouter de logique métier nouvelle hors du cadre décrit (pas
de promotions saisonnières supplémentaires, etc.).

## Exigences de Conception (OBLIGATOIRE)

Vous **DEVEZ** appliquer les patrons suivants exactement pour les éléments indiqués :

1. Abstract Factory

	- Pour regrouper la création des familles d'objets suivantes :
	  - Une stratégie de remise
	  - Une stratégie de points de fidélité
	- Chaque type de client est représenté par une fabrique concrète retournant les deux objets cohérents entre eux.

2. Strategy

	- Pour encapsuler le CALCUL EXACT de la remise
	- Pour encapsuler le CALCUL EXACT des points fidélité
	- Le code appelant ne doit pas connaître les détails. Il doit simplement invoquer une méthode uniforme (ex: `calculer(...)`).

3. Structure de données
	- Remplacer la liste de tuples des frais de livraison par une autre structure plus efficace

4. Extensibilité
	- L'ajout d'un nouveau type de client ne doit nécessiter AUCUNE modification dans le code de calcul principal (principe ouvert/fermé). Seul un enregistrement (ex: dans un registre / dictionnaire) et une nouvelle fabrique concrète doivent être ajoutés.

## Livrables

Puisqu'il s'agit d'une révision, faire une pull request sur ce dépôt GitHub. Lors de l'épreuve finale, le code sera à remettre via Omnnivox.

Le code doit pouvoir être exécuté via:

```bash
uv run main
```

comme c'est le cas actuellement.