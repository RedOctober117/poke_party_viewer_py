from pyboy import PyBoy
from collections import namedtuple
from party_viewer.data_structures import gs_ram_map
from party_viewer.image_manager import render_pokemon
# import pycurl
# import certifi
# from io import BytesIO

def main():
    parsed_dex = parse_dex('gen2dex.txt')
    tupled_dex = pokemon_tuple_generator(parsed_dex)
    nat_dex_dict = dict_of_nat_dex(tupled_dex)
    # for mon in tupled_dex:
    #     print(mon)
    
    initialize_rom('Pokemon - Silver Version (UE) [C][!].gbc', nat_dex_dict)

def initialize_rom(rom, dex):

    pb = PyBoy(rom)
    pb.set_emulation_speed(10)

    prev_members = [0] * 6

    while not pb.tick():
        
        output_buffer = ''
        for i in range(1, pb.get_memory_value(gs_ram_map['party']['total']) + 1):
            mem_value = pb.get_memory_value(gs_ram_map['party'][format(f'party_pokemon_{i}')])
            buffer = update_mon_mem_loop(
                prev_members[i - 1],
                mem_value,
                dex)
            match buffer: 
                case None:
                    pass
                case _:
                    output_buffer += render_pokemon(dex[mem_value]).strip('\n')
            prev_members[i - 1] = mem_value

        match output_buffer:
            case '':
                pass
            case _:
                print(output_buffer)
    pb.stop()

# url template for picture curling https://img.pokemondb.net/sprites/silver/normal/<name>.png
# ie https://img.pokemondb.net/sprites/silver/normal/meganium.png

def update_mon_mem_loop(prev_val, current_val, dex):
    return format(f'Name: {dex[current_val]} NatDexNum: {current_val}') if current_val != prev_val else None

def parse_dex(dex_path):
    parsed_list = []
    with open(dex_path, 'r') as dex:
        for line in dex.readlines():
            parsed_list.append(([ i.strip('\t#') for i in line.split(' ')[:3] if i != '']))
    return parsed_list

def dict_of_nat_dex(tupled_dex):
    nat_dex = {}
    for tuple in tupled_dex:
        nat_dex[int(tuple.nat_dex)] = tuple.name
    return nat_dex

def pokemon_tuple_generator(list_mon):
    fields = ['jho_dex', 'nat_dex', 'name']
    cls = namedtuple("Pokemon", fields)
    tupled_mons = []
    for mon in list_mon:
        if len(mon) > 0:
            tupled_mons.append(cls._make(mon))
    return tupled_mons



# revisit on linux

# def download_sprites(dex, template_url):
#     buffer = BytesIO()
#     curl = pycurl.Curl()
#     for mon in dex:
#         curl.setopt(curl.URL, format(f'{template_url}{mon}.png'))
#         curl.setopt(curl.WRITEDATA, buffer)
#         curl.setopt(curl.CAINFO, certifi.where())
#         curl.perform()
#         curl.close()

    
#     return 1

if __name__ == '__main__':
    main()