![](https://github.com/ravveni/pasteldays/blob/main/preview.png?raw=true)

# PastelDays
A desaturated, low-contrast version of the NeoDays tileset for Cataclysm: Dark Days Ahead (Experimental branch).

# Contributing
0. Consider contributing to the [main CDDA tileset repository](https://github.com/I-am-Erk/CDDA-Tilesets).
    - Updates to NeoDays are ported over regularly (with credit)
1. Limit colours to those those within `templates/duel_palette.png`.
2. Any additions should have a corresponding json file (`templates/example_tile.json` as reference).
    - The `id` for objects can be found by searching the CDDA json game data.
    - For most tiles, the `id`, `fg`, and image name should be the same
3. Place png(s) and json file(s) in their respective size and category directories.
   - tiles - 10x10px
   - large - 20x20px
4. Run `generate_tileset.py` to compile the final tileset into the `pasteldays` directory.
5. Test in-game to provide screenshots for the PR.
    - Prefixes - `Bugfix, Change, Chore, Feature`
    - Branch name - `prefix-branch_name`
    - PR title - `[Prefix] Branch name`

# Credit
Apart from unique additions and modifications to this project, all credit goes to the contributers of the original NeoDays tileset, located in the [main CDDA tileset repository](https://github.com/I-am-Erk/CDDA-Tilesets).

Credit to [@arilynart](https://lospec.com/arilynart) for creating the Duel colour palette.

---

This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.<br /><a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/3.0/88x31.png" /></a>
