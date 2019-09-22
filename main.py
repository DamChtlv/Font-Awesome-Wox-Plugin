# -*- coding: utf-8 -*-

# Imports
import json
import os
# import pyperclip
import webbrowser
from wox import Wox, WoxAPI

# Wox fix - missing "pyperclip" module
try:
    import pyperclip
except ImportError:
    from pip._internal import main as pip
    pip(['install', '--user', 'pyperclip'])
    import pyperclip

# Wox fix - missing "requests" module
try:
    import requests
except ImportError:
    from pip._internal import main as pip
    pip(['install', '--user', 'requests'])
    import requests

# Wox fix - missing "bs4" module
try:
    from bs4 import BeautifulSoup
except ImportError:
    from pip._internal import main as pip
    pip(['install', '--user', 'bs4'])
    from bs4 import BeautifulSoup

# Variables
CURRENT_DIR = os.getcwd()
ICON_DIR_NAME = 'Images/Icons'
ICON_DIR = os.path.join(CURRENT_DIR, ICON_DIR_NAME) + os.sep
JSON_DIR_NAME = 'Json'
JSON_DIR = os.path.join(CURRENT_DIR, JSON_DIR_NAME) + os.sep
REFERENCES = [
    'solid',
    'regular',
    'light',
    'duotone',
    'brands',
]
STR_REFERENCES = ' '.join(REFERENCES)

class FontAwesome(Wox):
    fa_ref_version = '5.11.1'

    def __init__(self):
        super().__init__()
        self.load_json()

    def copy(self, text):
        pyperclip.copy(text)

    def query(self, query):

        # Array to store results matching
        results = []

        # Array to store all items found in all json files
        icons = []

        search = query.replace(' ', '-')
        firstSearch = query.split(' ')[0].replace(' ', '-')

        # Download latest version of json file if we don't have it yet
        json_file = self.get_json_file_path()
        if not os.path.isfile(json_file):
            self.get_json_file()

        # Open json file content
        with open(json_file, 'r') as openFile:
            iconsData = json.load(openFile)

        # self.fa_ref_version = fa_ref_version

        for iconName, iconData in iconsData.items():

            cleanIcon               = {}
            cleanIcon['name']       = iconName
            cleanIcon['label']      = iconData['label']
            cleanIcon['unicode']    = iconData['unicode']
            cleanIcon['search']     = iconData['search']['terms']
            cleanIcon['svg']        = iconData['svg'][iconData['styles'][0]]['raw']
            cleanIcon['style']      = ', '.join(iconData['styles']).capitalize()
            cleanIcon['version']    = 'v' + iconData['changes'][0]

            iconClass = ''
            # if cleanIcon['style'] == 'solid':
            #     iconClass = 'fas'
            # elif cleanIcon['style'] == 'regular':
            #     iconClass = 'far'
            # elif cleanIcon['style'] == 'light':
            #     iconClass = 'fal'
            # elif cleanIcon['style'] == 'duotone':
            #     iconClass = 'fad'
            # elif cleanIcon['style'] == 'brands':
            #     iconClass = 'fab'

            # iconClass = iconClass + ' fa-' + cleanIcon['name']
            iconClass = 'fa-' + cleanIcon['name']
            cleanIcon['class'] = iconClass

            icons.append(cleanIcon)

        firstLevelMatchs = []
        secondLevelMatchs = []
        thirdLevelMatchs = []

        # Split the query by words for the search words scoring system
        splitWords = query.split(' ')
        for icon in icons:

            wordsScore = 0
            for splitWord in splitWords:
                if str(splitWord) in str(icon['name']):
                    wordsScore += 1
                else:
                    if isinstance(icon['search'], list) and len(icon['search']) >= 1:
                        for term in icon['search']:
                            if str(splitWord) in str(term):
                                wordsScore += 1

            resultObject = {
                'Title': icon['name'],
                'SubTitle': icon['label'] + ' - ' + icon['style'] + ' - ' + icon['version'],
                'IcoPath': ICON_DIR + icon['name'] + '.png',
                'JsonRPCAction': {
                    'method': 'copy',
                    'parameters': [icon['class']],
                }
            }

            # If we found the perfect match, prepend it first in the results.
            if len(splitWords) == wordsScore and search == icon['name']:
                firstLevelMatchs.insert(0, resultObject)

            # If we found a match that have all words in it, prepend it in the results after first.
            elif len(splitWords) == wordsScore and icon['name'].split('-')[0] == search.split('-')[0]:
                secondLevelMatchs.append(resultObject)

            # If we found a match that have all words in it, prepend it in the results after first.
            elif len(splitWords) == wordsScore:
                thirdLevelMatchs.insert(1, resultObject)

            # Else fallback and append something that match a little
            elif search in icon['name']:
                results.append(resultObject)

        results = firstLevelMatchs + secondLevelMatchs + thirdLevelMatchs + results

        return results

    def get_json_file_name(self):
        json_name = 'icons.json'
        return json_name

    def get_json_file_path(self):
        json_name = self.get_json_file_name()
        return os.path.join(JSON_DIR, json_name)

    def get_json_file(self):
        json_file = self.get_json_file_path()
        json_name = self.get_json_file_name()
        json_url = 'https://github.com/FortAwesome/Font-Awesome/raw/master/metadata/icons.json'

        try:
            request = requests.get(json_url)
            distantFileContent = request.json()

            # If no json file found, try to fetch it and make local json file
            if not os.path.isfile(json_file):
                with open(json_file, 'w') as createFile:
                    json.dump(distantFileContent, createFile)

        except:
            self.debug('Error while trying to download "' + json_name + '", please try again :)')

    def openUrl(self, url):
        webbrowser.open(url)
        WoxAPI.change_query(url)

    # Create "Json" dir if it doesn't exist and grab json files
    def load_json(self):
        if not os.path.isdir(JSON_DIR):
            try:
                os.mkdir(JSON_DIR)
            except:
                self.debug('Error while making "Json" folder in the plugin directory')

if __name__ == "__main__":
    FontAwesome()
