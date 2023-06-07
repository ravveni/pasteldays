#!/usr/bin/env python3

import json
import os
import re
import shutil

images = []
imageFolderPath = "Tiles_TBP/"
imageFiletype = ".png"

def createJSONForTiles(destinationPath):
    directoryPath = imageFolderPath + destinationPath

    for image in os.listdir(directoryPath):
        images.append(os.path.join(directoryPath, image))

    with open("tile_template.json", "r") as read_file:
        template = json.load(read_file)

    for image in images:
        print("Processing " + image)

        pathRegex = '(?<=' + directoryPath + ')(.*).png'

        try:
            id = re.findall(pathRegex, image)[0]
            print("Creating " + id + " json")

            template["id"] = id
            template["fg"] = id

            jsonPath = destinationPath + id + ".json"

            with open(jsonPath, 'a+') as outfile:
                json.dump(template, fp=outfile)

            imageSource = directoryPath + id + imageFiletype
            shutil.move(imageSource, destinationPath)
        except:
            print("Skip")

large = "Large_20x20/"
small = "Small_10x10/"

createJSONForTiles(large)
createJSONForTiles(small)
