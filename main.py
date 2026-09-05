import zipfile
import sys
import os
import glob

# 1. Dézippe le SDK
if not os.path.exists('./python-bot-sdk-main'):
    with zipfile.ZipFile('python-bot-sdk-main.zip', 'r') as zip_ref:
        zip_ref.extractall('.')

# 2. Trouve le dossier SDK
sdk_paths = glob.glob('./python-bot-sdk-main/**/highrise', recursive=True)
sdk_folder = os.path.dirname(sdk_paths[0])
sys.path.append(sdk_folder)

from highrise import Highrise
import inspect

print("=== METHODES DISPONIBLES DANS HIGRISE ===")
print([m for m in dir(Highrise) if not m.startswith('_')])
print("=========================================")

import time
time.sleep(10) # pour voir les logs
