from pyboy import PyBoy
from collections import namedtuple
# import pycurl
# import certifi
# from io import BytesIO

def main():
    parsed_dex = parse_dex('gen2dex.txt')
    tupled_dex = pokemon_tuple_generator(parsed_dex)
    nat_dex_dict = dict_of_nat_dex(tupled_dex)
    for mon in tupled_dex:
        print(mon)
    initialize_rom('Pokemon - Silver Version (UE) [C][!].gbc', nat_dex_dict)

def initialize_rom(rom, dex):
    pb = PyBoy(rom)
    pb.set_emulation_speed(10)
    prev_member_1 = 0
    while not pb.tick():
        member_1_num = pb.get_memory_value(0xda2a)
        if member_1_num != prev_member_1:
            prev_member_1 = member_1_num
            print(f'Name: {dex[member_1_num]} NatDexNum: {member_1_num}')
    pb.stop()


# url template for picture curling https://img.pokemondb.net/sprites/silver/normal/<name>.png
# ie https://img.pokemondb.net/sprites/silver/normal/meganium.png

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