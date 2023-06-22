# PastelDays
A de-noised, low-contrast version of the NeoDays tileset for Cataclysm: Dark Days Ahead.

Being kept up-to-date with any additions to the OG NeoDays tileset, and added to when fallbacks are found.

![](https://i.imgur.com/sAKg8rd.png?raw=true)

# Contributing 
1. Limit colours to those those within `templates/palette.png`
2. Any additions should have a corresponding json file (use `templates/example_tile.json` as a reference)
    - The `id` for objects can be found by searching the CDDA json game data.  
3. Place png(s) and json file(s) in correct respective size folder within `gfx/`.
4. Run `generate_tileset.py` to compile the final tileset into the `pasteldays` directory.
5. Test in-game to provide screenshots for the PR.

# Credit
Apart from my personal additions and modifications, **all credit goes to the contributers of the original NeoDays tileset**. Located in the [main CDDA tileset repository](https://github.com/I-am-Erk/CDDA-Tilesets).

Credit for the Duel colour palette belongs to [@arilynart](https://lospec.com/arilynart).

Due to my method of mass modification, the pngs and json files for this tileset have been consolidated into two buckets (for now): tiles (10x10px) and large (20x20px), instead of the cleaner, multi-folder organization of the original repo, causing me to ultimately fork it.

---

This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.<br /><a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/3.0/88x31.png" /></a>