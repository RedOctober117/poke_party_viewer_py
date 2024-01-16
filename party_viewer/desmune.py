from desmume.emulator import DeSmuME, DeSmuME_Input
import time

emu = DeSmuME()
emu_mem = emu.memory
emu_in = emu.input
emu_in.

emu.open('Pokemon - SoulSilver Version (USA).nds')

window = emu.create_sdl_window()


with open('ram_dump.txt', 'w') as dump:
    while not window.has_quit():
        window.process_input()
        emu.cycle()
        window.draw()
        party_1 = emu_mem.read_string(0x002C0BC2)
        if party_1 > '':
            dump.write(party_1 + '\n')
        time.sleep(0.001) 
