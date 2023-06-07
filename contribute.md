# Contribution Guide
So you want to help grow the NeoDaysPlus tileset? Thank you, you're awesome! 

Here is a guide to getting started:

## Pre-Requisites:
- Git
- Python3 & pip
- Pillow
    - `python3 -m pip install --upgrade Pillow` - if missing
- VS Code (optional): This is just the editor I use to build and run all scripts if a similar environment is desired

## 1. Checkout the source
- Clone the `main` repository branch (will be the most up to date compared to the source code in 'Releases')
- My suggestion is to not put it directly into the Cataclysm gfx folder to give yourself a clean, safe workspace

## 2. Create a branch
- Wanting to have credit up front, and keep things "organised", please create a branch using the following naming conventions:
    - `code/code-change-short-description` - For any additions/improvements/optimizations you want to make to the scripts
        - eg. `code/faster-spritesheet-gen`
    - `feature/feature-name` - For changes to existing tiles that make them more complex (ones that include auto/multi-tiling, seasonal changes, etc)
        - eg. `feature/autotiled-asphalt`
    - `tiles/tile-kind` - For adding one or more tiles of a specific kind/theme, 
        - eg. `tiles/zombie-cow`, or if the set is of multiple themes, please use `misc-tiles`

## 3. Create some tiles
- Names must be `id` value from the `CDDA/Data/json`
    - Open the `CDDA/Data/json` folder in a text editor for easy searching (I have a copy of this folder saved off for ease of access and protection from accidental saves)
    - Do a project-wide search for the missing tile using the name that appears in-game
    - Copy (don't cut) the corresponding `id` value to the template json file's `id` value (the display name in-game sometimes isn't the same as the `id`)
    - eg. `mon_zow.png`
- For large tiles, the tile dimension is `20x20px`
- For small tiles, the tile dimension is `10x10px`
- When in doubt about sizing/spacing/styling of your tile(s), you can always use an existing tile as a template
- Export image for web as `.png`, this strips all unnecessary data from the image, and if it's not a `.png`, the scripts won't work properly
- Save in the appropriate size folder in the `Tiles_TBP` (to be processed) folder within the project
    - Large tiles --> `Large_20x20/`
    - Small tiles --> `Small_10x10/`

## 4. Create the json file for the tile(s)
- In the terminal, `cd` to the `NeoDaysPlus` directory
- Commands to make the scripts executable:
    - `chmod +x [script]`
    - eg. `chmod +x QuickJSON.py` 
- Run the `QuickJSON.py` script if tiles are basic/not complex stuctured, and the json will be created in the appropriate folder while also moving the tile.png
    - In the case of complex tiles, put the png and json directly in the appropriate tile size folder

## 5. Combine and make tileset
- Make executable and run `./Combine.py`
- Make executable and run `./MakeNDP.sh`

## 6. Move the newly created tileset folder to the Cataclysm gfx folder

## 7. Test your tiles in-game
- Take screenshots (and crop them) of newly-added working tiles

## 8. Create a PR
- More than likely, the auto-generated name for the PR will be sufficient
- In the description of the PR, please list any added tiles by their `id` value, and  the description of any additions/features/improvements/optimizations
- Add cropped screenshots from testing
- Smash that `Create Pull Request` button

## 9. Pat yourself on the back
- Congrats! Once reviewed and merged into the `main` branch, shout-outs for your additions will be made in the following version's release notes, and you will have my eternal gratitude

## 10. Play some CDDA
