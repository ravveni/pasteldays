#!/usr/bin/python3

from PIL import Image
import json, math, os, time

config_ref = {}
sheet_ref = {}

def add_directory_to_refs(directory, starting_index: int = 0):
  filenames = files_of(directory, ".png")
  file_index = starting_index

  for filename in filenames:
    if filename not in sheet_ref:
      sheet_ref[filename] = file_index
      config_ref[os.path.splitext(os.path.basename(filename))[0]] = file_index
      file_index += 1

def draw_spritesheet(directory, tile_size):
  tiles = []

  directory_path = "gfx/" + directory + "/"
  files = files_of(directory_path, ".png")

  for current_file in files :
    try:
      with Image.open(os.path.normpath(current_file)) as im :
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

def change_config_value(value_key: str, json_data: dict) -> dict:
  updated_json = json_data

  if value_key in json_data:
    sprite_value_type = type(json_data[value_key])

    if sprite_value_type is str:
      sprite_value = config_ref[json_data[value_key]]
      updated_json[value_key] = int(sprite_value)

    elif sprite_value_type is list:
      sprite_value_list_type = type(json_data[value_key][0])
      multi_tile_index = 0

      if sprite_value_list_type is str:
        for multi_tile_sprite_value in json_data[value_key]:
          multi_tile_sprite_value_string = config_ref[multi_tile_sprite_value]
          updated_json[value_key][multi_tile_index] = int(multi_tile_sprite_value_string)
          multi_tile_index += 1

      elif sprite_value_list_type is dict:
        for sprite_value_dict in json_data[value_key]:
          sprite_value_dict_sprite_value = sprite_value_dict["sprite"]
          sprite_value_string = config_ref[sprite_value_dict_sprite_value]
          updated_json[value_key][multi_tile_index]["sprite"] = int(sprite_value_string)
          multi_tile_index += 1

  if "additional_tiles" in json_data:
    additional_tile_index = 0

    for additional_tile in json_data["additional_tiles"]:
      if value_key in additional_tile:
        sprite_value_type = type(additional_tile[value_key])

        if sprite_value_type is str:
          additional_sprite_value = config_ref[additional_tile[value_key]]
          updated_json["additional_tiles"][additional_tile_index][value_key] = int(additional_sprite_value)

        elif sprite_value_type is list:
          sprite_value_list_type = type(additional_tile[value_key][0])
          if sprite_value_list_type is str:
            multi_additional_tile_index = 0
            for multi_tile_sprite_value in additional_tile[value_key]:
              multi_additional_sprite_value = config_ref[multi_tile_sprite_value]
              updated_json["additional_tiles"][additional_tile_index][value_key][multi_additional_tile_index] = int(multi_additional_sprite_value)
              multi_additional_tile_index += 1

      additional_tile_index += 1

  return updated_json

def files_of(directory, extension) -> list:
  filenames = []

  for filename in os.listdir(directory):
    if filename.endswith(extension):
      filenames.append(directory + filename)

    if os.path.isdir(directory + filename):
      holder = files_of(directory + filename + "/", extension)
      for nested_file in holder:
        filenames.append(nested_file)

  filenames.sort()
  return filenames

def fill_item_config(directory) -> list:
  directory_path = "gfx/" + directory + "/"
  directory_json = []
  json_files = files_of(directory_path, ".json")

  for filename in json_files:
    with open(filename, 'r') as f:
      file_json = json.load(f)
      file_json = change_config_value("fg", file_json)
      file_json = change_config_value("bg", file_json)
      directory_json.append(file_json)
      f.close()

  return directory_json

def generate_refs():
  # tiles
  add_directory_to_refs("gfx/tiles/")
  next_starting_index = math.ceil(len(sheet_ref.keys()) / 16) * 16
  previous_keys = len(sheet_ref.keys())

  # large
  add_directory_to_refs("gfx/large/", next_starting_index)
  keys_added = len(sheet_ref.keys()) - previous_keys
  # next_starting_index = round(keys_added / 16) * 16

def generate_spritesheets():
  draw_spritesheet("tiles", 10)
  draw_spritesheet("large", 20)

def generate_tile_config():
  tile_config = {}

  with open('templates/empty_tile_config.json', 'r') as f:
    tile_config = json.load(f)
    f.close()

  tile_config["tiles-new"][0]["tiles"] = fill_item_config("tiles")
  tile_config["tiles-new"][1]["tiles"] = fill_item_config("large")

  with open("pasteldays/tile_config.json", "w") as outfile:
    json.dump(tile_config, outfile, indent=2)
    outfile.close()

def main():
  generate_refs()
  generate_spritesheets()
  generate_tile_config()

if __name__ == "__main__":
    main()
