#############################################################################
# Fichier pour créer un .exe

#!/usr/bin/python 
# -*- coding: utf-8 -*-
# Python 2.7
 
"""
NB: Pas d'accent dans le setup, ni dans la description, ni dans les commentaires
 
Icone sous Windows: il faut:
=> xxx.ico pour integration dans le exe, avec "icon=xxx.ico"
=> xxx.png pour integration dans le graphique + demander copie avec includefiles.
"""

#commande "python setup.py build" pur construire le ficher executable

import sys, os
from cx_Freeze import setup, Executable
 
#############################################################################
# preparation des options 

# chemins de recherche des modules
#path = sys.path

# options d'inclusion/exclusion des modules
includes = []
excludes = []

# option d'inclusion des packages
packages = ["idna","os","sys","enigmes"]

# copier les fichiers non-py et non-pyw et/ou repertoires et leur contenu:
includefiles = ["images"]

# inclure si nécessaire les fichiers non-py et non-pyw dans library.zip
#zipincludes = []

# pour que certaines bibliotheques "systeme" soient recopiees aussi
#binpathincludes = []
#if sys.platform == "linux2":
#    binpathincludes += ["/usr/lib"]
 
 # construction du dictionnaire des options
options = {#"path": path,
           "includes": includes,
           "excludes": excludes,
           "packages": packages,
           "include_files": includefiles,
           #"zip_includes": zipincludes,
           #"bin_path_includes": binpathincludes,
           #"create_shared_zip": False,
           #"include_in_shared_zip": False,
           #"compressed": False 
           }

# pour inclure sous Windows les dll system necessaires
#if sys.platform == "win32":
#    options["include_msvcr"] = True
 

#############################################################################
# preparation des cibles
base = None
if sys.platform == "win32":
    base = "Win32GUI"

#icone = None
#if sys.platform == "win32":
#    icone = "images/logo.ico" # mettre ici le fichier de l' icone .ico pour integration a l'exe
 
cible_1 = Executable(
    script = "main.py",
    targetName="EscapeShark.exe",
    base = base,
    #compress = False,
    #copyDependentFiles = True,
    #appendScriptToExe = True,
    #appendScriptToLibrary = False,
    icon = "images/logo.ico"
    )
 
#############################################################################
# creation du setup
setup(
    name = "Escape Shark",
    version = "0.1",
    description = "Projet IHH",
    author = "Alexia LACOMBE et Baptiste MARY",
    options = {"build_exe": options},
    executables = [cible_1]
    )