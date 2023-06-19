#!/usr/bin/python3

import json
import math

tile_ref = {}

def add_tiles_to_ref(directory: str, starting_index: int = 1):
  filenames = []

  for filename in os.listdir(directory):
    if filename == "0000.png": continue

    if filename.endswith(".png"):
      filename = filename.split(".")[0]
      filenames.append(filename)

  filenames.sort()

  file_index = starting_index

  for filename in filenames:
    if filename not in tile_ref:
      tile_ref[filename] = file_index
      file_index += 1

def build_ref():
  # tiles
  add_tiles_to_ref("tiles/")
  next_starting_index = math.ceil(len(tile_ref.keys()) / 16) * 16 + 1
  previous_keys = len(tile_ref.keys())

  # large
  add_tiles_to_ref("large/", next_starting_index)
  keys_added = len(tile_ref.keys()) - previous_keys
  # next_starting_index = round(keys_added / 16) * 16 + 1

def build_spritesheet(directory):
  filenames = []

  for filename in os.listdir(directory):
    if not filename.endswith(".png"): continue
    filename = filename.split(".")[0]
    filenames.append(filename)

  filenames.sort()

def create_spritesheets():
  build_spritesheet("tiles/")
  build_spritesheet("large/")

def create_tile_config(directory):
  pass

def generate_tile_config():
  pass

def main():
  build_ref()
  create_spritesheets()
  generate_tile_config()

if __name__ == "__main__":
    main()
