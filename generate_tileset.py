#!/usr/bin/python3

from PIL import Image
import json, math, os, time

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
  add_tiles_to_ref("gfx/tiles/")
  next_starting_index = math.ceil(len(tile_ref.keys()) / 16) * 16
  previous_keys = len(tile_ref.keys())

  # large
  add_tiles_to_ref("gfx/large/", next_starting_index)
  keys_added = len(tile_ref.keys()) - previous_keys
  # next_starting_index = round(keys_added / 16) * 16

def build_spritesheet(directory, tile_size):
  tiles = []

  directory_path = "gfx/" + directory + "/"
  files = os.listdir(directory_path)
  files.sort()

  for current_file in files :
      try:
          with Image.open(directory_path + current_file) as im :
              tiles.append(im.getdata())
      except:
        # print(current_file + " is not a valid image")
        pass

  max_tiles_per_row = 16.0
  spritesheet_width = 0
  spritesheet_height = 0

  tile_width = tile_size
  tile_height = tile_size

  if len(tiles) > max_tiles_per_row:
      spritesheet_width = tile_width * max_tiles_per_row
      required_rows = math.ceil(len(tiles) / max_tiles_per_row)
      spritesheet_height = tile_height * required_rows
  else:
      spritesheet_width = tile_width  * len(tiles)
      spritesheet_height = tile_height

  spritesheet = Image.new("RGBA", (int(spritesheet_width), int(spritesheet_height)))

  for current_frame in tiles :
      top = tile_height * math.floor((tiles.index(current_frame)) / max_tiles_per_row)
      left = tile_width * (tiles.index(current_frame) % max_tiles_per_row)
      bottom = top + tile_height
      right = left + tile_width

      box = (left, top, right, bottom)
      box = [int(i) for i in box]
      cut_frame = current_frame.crop((0, 0, tile_width,tile_height))

      spritesheet.paste(cut_frame, box)

  spritesheet.save("pasteldays/" + directory + ".png", "PNG")

def create_spritesheets():
  build_spritesheet("tiles", 10)
  build_spritesheet("large", 20)

def change_sprite_values(value_key: str, json_data: dict) -> dict:
  updated_json = json_data

  if value_key in json_data:
    sprite_value_type = type(json_data[value_key])

    if sprite_value_type is str:
      sprite_value = tile_ref[json_data[value_key]]
      updated_json[value_key] = int(sprite_value)

    elif sprite_value_type is list:
      sprite_value_list_type = type(json_data[value_key][0])
      multi_tile_index = 0

      if sprite_value_list_type is str:
        for multi_tile_sprite_value in json_data[value_key]:
          multi_tile_sprite_value_string = tile_ref[multi_tile_sprite_value]
          updated_json[value_key][multi_tile_index] = int(multi_tile_sprite_value_string)
          multi_tile_index += 1

      elif sprite_value_list_type is dict:
        for sprite_value_dict in json_data[value_key]:
          sprite_value_dict_sprite_value = sprite_value_dict["sprite"]
          sprite_value_string = tile_ref[sprite_value_dict_sprite_value]
          updated_json[value_key][multi_tile_index]["sprite"] = int(sprite_value_string)
          multi_tile_index += 1

  if "additional_tiles" in json_data:
    additional_tile_index = 0

    for additional_tile in json_data["additional_tiles"]:
      if value_key in additional_tile:
        sprite_value_type = type(additional_tile[value_key])

        if sprite_value_type is str:
          additional_sprite_value = tile_ref[additional_tile[value_key]]
          updated_json["additional_tiles"][additional_tile_index][value_key] = int(additional_sprite_value)

        elif sprite_value_type is list:
          sprite_value_list_type = type(additional_tile[value_key][0])
          if sprite_value_list_type is str:
            multi_additional_tile_index = 0
            for multi_tile_sprite_value in additional_tile[value_key]:
              multi_additional_sprite_value = tile_ref[multi_tile_sprite_value]
              updated_json["additional_tiles"][additional_tile_index][value_key][multi_additional_tile_index] = int(multi_additional_sprite_value)
              multi_additional_tile_index += 1

      additional_tile_index += 1

  return updated_json

def create_config_addition(directory) -> list:
  directory_path = "gfx/" + directory + "/"
  directory_json = []
  json_files = []

  for filename in os.listdir(directory_path):
    if filename.endswith(".json"):
      json_files.append(filename)

  json_files.sort()

  for filename in json_files:
    with open(directory_path + filename, 'r') as f:
      file_json = json.load(f)
      file_json = change_sprite_values("fg", file_json)
      file_json = change_sprite_values("bg", file_json)
      directory_json.append(file_json)
      f.close()

  return directory_json

def generate_tile_config():
  tile_config = {}

  with open('templates/empty_tile_config.json', 'r') as f:
    tile_config = json.load(f)
    f.close()

  tile_config["tiles-new"][0]["tiles"] = create_config_addition("tiles")
  tile_config["tiles-new"][1]["tiles"] = create_config_addition("large")

  with open("pasteldays/tile_config.json", "w") as outfile:
    json.dump(tile_config, outfile, indent=2)
    outfile.close()

def main():
  build_ref()
  create_spritesheets()
  generate_tile_config()

if __name__ == "__main__":
    main()
