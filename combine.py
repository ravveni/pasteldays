#!/usr/bin/env python3

import glob
import json
import os
from PIL import Image
import re

## spritesheet creation
def createSpriteSheetFrom(imageFolderPath, spriteSheetName, tileDimension, currentIndex, refDict):
    imagePaths = []

    for image in os.listdir(imageFolderPath):
        if image[-3:] == 'png':
            imagePaths.append(os.path.join(imageFolderPath, image))

    imagePaths.sort()
    pathRegex = '(?<=' + imageFolderPath + ')(.*).png'

    for imagePath in imagePaths:
        name = re.findall(pathRegex, imagePath)[0]
        refDict[name] = currentIndex
        currentIndex += 1

    images = [ Image.open(x) for x in imagePaths ]

    maxWidth = 16 * tileDimension
    max_height = (round(((len(images) / 16) * tileDimension) / tileDimension) * tileDimension) + tileDimension

    tilesSpriteSheet = Image.new('RGBA', (maxWidth, max_height))

    xOffset = 0
    yOffset = 0

    for im in images:
        tilesSpriteSheet.paste(im, (xOffset, yOffset))
        xOffset += im.size[0]

        if xOffset >= maxWidth:
            xOffset = 0
            yOffset += im.size[1]

    spriteSheet = spriteSheetName + '.png'
    tilesSpriteSheet.save(spriteSheet)
    totalTiles = int((max_height / tileDimension) * 16)

    return (currentIndex, refDict, totalTiles)

## in json, replaces names to placement of tile on the spritesheet
def replaceReferenceNameForID(tiles):
    updatedTiles = []

    for tile in tiles:
        ## fg
        if "fg" in tile:
            tileReference = tile["fg"]

            if type(tileReference) == list:
                refList = []

                for ref in tileReference:
                    refList.append(refDict[ref])

                tile["fg"] = refList

            else:
                tile["fg"] = refDict[tileReference]

        ## bg
        if "bg" in tile:
            bgTilePlacement = tile["bg"]
            tile["bg"] = refDict[bgTilePlacement]

        ## multitile
        if "multitile" in tile:
            additionalTiles = tile["additional_tiles"]

            refList = []

            for multiTile in additionalTiles:
                if "fg" in multiTile:
                    tileReference = multiTile["fg"]

                if type(tileReference) == list:
                    refList = []

                    for ref in tileReference:
                        refList.append(refDict[ref])

                    multiTile["fg"] = refList

                else:
                    multiTile["fg"] = refDict[tileReference]

                if "bg" in multiTile:
                    bgTilePlacement = multiTile["bg"]
                    multiTile["bg"] = refDict[bgTilePlacement]

        updatedTiles.append(tile)

    return updatedTiles

currentIndex = 0
refDict = {}

## small spritesheet
smallImageFolderPath = 'Small_10x10/'
smallerSprites = createSpriteSheetFrom(smallImageFolderPath, 'tiles', 10, currentIndex, refDict)

currentIndex = smallerSprites[2]
refDict = smallerSprites[1]

## large spritesheet
largeImageFolderPath = "Large_20x20/"
largerSprites = createSpriteSheetFrom(largeImageFolderPath, 'large', 20, currentIndex, refDict)

currentIndex = largerSprites[0]
refDict = largerSprites[1]

## small tiles json
smallTiles = []

for f in glob.glob("Small_10x10/*.json"):
    with open(f, "rb") as infile:
        smallTiles.append(json.load(infile))

smallTiles = replaceReferenceNameForID(smallTiles)
smallTiles = sorted(smallTiles, key=lambda k: k['id'][0]) 

## large tiles json
largeTiles = []

for f in glob.glob("Large_20x20/*.json"):
    with open(f, "rb") as infile:
        largeTiles.append(json.load(infile))

largeTiles = replaceReferenceNameForID(largeTiles)
largeTiles = sorted(largeTiles, key=lambda k: k['id'][0]) 

## tile_config.json creation
with open("tile_info.json", "r") as read_file:
    data = json.load(read_file)
    tiles_full = data
    tilesets = data["tiles-new"]

    smallTileset = tilesets[0]
    smallTileset['tiles'] = smallTiles

    largeTileset = tilesets[1]
    largeTileset['tiles'] = largeTiles

    with open("tile_config.json", 'w+') as outfile:
        json.dump(data, fp=outfile)
