[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod-redirect-0.herokuapp.com/)

# Exemples en classe (chapitre 9)

## Logging (*logging_ex.py*)

Porte sur les slides 8 � 10 des notes du chapitre 9

## Exceptions (*exceptions_ex.py*)

Porte sur les slides 15 � 19 des notes du chapitre 9

## Tests unitaires (*tests_ex.py* et *code_to_test.py*)

Porte sur les slides 20 � 24 des notes du chapitre 9

## Documentation

Porte sur les slides 44 � 52 des notes du chapitre 9.

Apr�s avoir �crit votre documentation dans votre code, vous pouvez g�n�rer un site web l�ger dans lequel la lire, un peu comme la documentation de Python ou celle des diff�rentes librairies tierces.

Un des formats les plus courants ces temps-ci est le format [Sphinx](https://www.sphinx-doc.org/en/master/index.html). Pour s'en servir, on doit suivre quelques �tapes :

1. Installer Make avec [`apt-get install build-essential`](https://packages.ubuntu.com/xenial/build-essential) sur Ubuntu, avec [MSYS2](https://www.msys2.org/) sur Windows ou avec [Homebrew](https://brew.sh/) sur Mac.
2. Installer sphinx avec `pip install sphinx` (probablement d�j� install�).
3. Cr�er un dossier *doc* ou *docs* (ou peu importe comment vous voulez l'appeler) dans votre dossier de projet. On va dire *doc* pour le reste.
4. Dans ce dossier, faire `sphinx-quickstart --ext-autodoc` et choisir de s�parer les sources.
5. Dans doc/source/conf.py, d�coment� le code de la section *Path setup*. Dans le `sys.path`, ajouter le chemin vers les modules de votre projet (dans notre cas `../../`). Le squelette fait d�j� les conversions pour vous, vous n'avez qu'� changer le chemin.
6. Pour ne pas avoir � ajouter � la main chaque fichier de votre projet, aller dans le dossier *doc* et faites `sphinx-apidoc -o source <chemin-vers-projet>`, o� `<chemin-vers-projet>` est `../` dans notre cas, c'est-�-dire le chemin vers votre code Python. Faites cette �tape quand vous ajoutez ou retirez des fichiers sources.
7. Faites `make html` dans le dossier *doc* pour g�n�rer la documentation. Elle sera dans *doc/build/html* (ouvrez le fichier *index.html*)
