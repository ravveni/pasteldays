# PastelDays
A de-noised, low-contrast version of the NeoDays tileset for Cataclysm: Dark Days Ahead. In the process of being re-coloured to the palette, [Duel](https://lospec.com/palette-list/duel). 

Being kept up-to-date with any additions to the OG NeoDays tileset, and added to when fallbacks are found.

![](https://i.imgur.com/sAKg8rd.png?raw=true)

# Contributing 
1. Colouring should be done using the linked/provided palette.
2. Any additions should have a corresponding json file (use `example_tile.json` as a reference).
3. The `id` for missing objects can be found by searching the CDDA json game data. Place added png(s) and json file(s) in respective folder. 
4. Run `generate_tileset.py` to compile the final tileset files into the `pasteldays` directory. 
5. Test in-game and provide screenshots for the PR.

# Credit
Apart from my small additions and modifications, **all credit goes to the contributers of the original NeoDays tileset**. Located in the [main CDDA tileset repository](https://github.com/I-am-Erk/CDDA-Tilesets).

Credit for the Duel palette belongs to [@arilynart](https://lospec.com/arilynart).

Due to my method of mass modification, the pngs and json files for this tileset have been consolidated into two buckets, tiles (10x10px), and large (20x20px) instead of the cleaner, multi-folder organization of the original repo, causing me to ultimately fork it.

# Licensing
Cataclysm:Dark Days Ahead and the Ultimate Cataclysm tileset is the result of contributions from volunteers under the Creative Commons Attribution ShareAlike 3.0 license. The code and content of the game is free to use, modify, and redistribute for any purpose whatsoever. See Creative Commons for details. Some code distributed with the project is not part of the project and is released under different software licenses, the files covered by different software licenses have their own license notices.
