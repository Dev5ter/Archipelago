from CommonClient import CommonContext, ClientCommandProcessor, get_base_parser, server_loop, gui_enabled
import Utils
from Utils import Version

import asyncio
import logging
import time
import dolphin_memory_engine as dme

from worlds import network_data_package
from worlds.ww.Items import lookup_id_to_name as item_id_to_name
from worlds.ww.Tools.locationScanner import location_scanner, death_link_watch
from worlds.ww.Tools.itemTable import item_table as IT
from worlds.ww.Tools.item_checker import item_checker
import worlds.ww.Tools.give_and_take_items as gat


ww_loc_name_to_id = network_data_package["games"]["Wind Waker"]["location_name_to_id"]

logger = logging.getLogger("Wind Waker Client")

class WWCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext):
        super().__init__(ctx)

class WWCommonContext(CommonContext):
    command_processor = WWCommandProcessor
    game = "Wind Waker"
    items_handling = 0b011

    def __init__(self, server_address, password):
        super(WWCommonContext, self).__init__(server_address, password)
        self.auth = None
        self.client = None
        self.locations_checked = []
        #self.items_received = []
        self.is_connected = False
        self.send_index = 0
        self.server_version: Version = Version(3, 2, 0)
        self.finished_game = False


    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(WWCommonContext, self).server_auth(password_requested)

        if not self.auth:
            logger.info("Enter slot name: ")
            self.auth = await self.console_input()

        await self.send_connect()

    def on_deathlink(self, data: dict):
        gat.kill_link()
        super().on_deathlink(data)

async def ww_item_giver(ctx):
    dme.hook()
    print(ctx.send_index, len(ctx.items_received))
    while not ctx.exit_event.is_set():
       #print("Item Giver")
        while(ctx.send_index < len(ctx.items_received)):
            while ((ctx.send_index < len(ctx.items_received)) and gat.can_be_given()):
                for x in range(ctx.send_index, len(ctx.items_received)):
                    value = dme.read_word(0x803C50B8)
                    value >>= 8
                    value <<= 8
                    value += ctx.send_index+1
                    dme.write_word(0x803C50B8, value)          
                    name: str = item_id_to_name[ctx.items_received[x].item]
                    
                    found: bool = False
                    for item in IT:
                        if name == item.name:
                            gat.give_item_name(name)
                            ctx.send_index += 1
                            found = True
                            continue
                    if found == True:
                        continue

                    if name[9:14] == "Chart":
                        if name[2] == "i":
                            gat.give_triforce_chart(int(name[15:len(name)]))
                            ctx.send_index += 1
                            continue
                        elif name[2] == "e":
                            gat.give_treasure_chart(int(name[15:len(name)]))
                            ctx.send_index += 1
                            continue
                    if name[-5:] == "Pearl":
                        gat.give_pearl(name)
                        ctx.send_index += 1
                        continue
                    if name[:5] == "Heart":
                        if name[6] == "P":
                            gat.give_heart_piece()
                            ctx.send_index += 1
                            continue
                        if name[6] == "C":
                            gat.give_heart_container()
                            ctx.send_index += 1
                            continue
                    if name == "Progressive Picto Box":
                        gat.give_next_picto()
                        ctx.send_index += 1
                        continue
                    if name == "Progressive Sword":
                        gat.give_next_sword()
                        ctx.send_index += 1
                        continue
                    if name == "Progressive Bow":
                        gat.give_next_bow()
                        ctx.send_index += 1
                        continue
                    if name == "Progressive Shield":
                        gat.give_next_shield()
                        ctx.send_index += 1
                        continue
                    if name == "Triforce Shard":
                        gat.give_next_shard()
                        ctx.send_index += 1
                        continue
                    if name == "Wallet Upgrade":
                        gat.give_next_wallet()
                        ctx.send_index += 1
                        continue
                    if name == "Quiver Upgrade":
                        gat.give_quiver()
                        ctx.send_index += 1
                        continue
                    if name == "Bomb Bag Upgrade":
                        gat.give_bomb_bag()
                        ctx.send_index += 1
                        continue
                    if name == "Bottle":
                        gat.give_next_bottle()
                        ctx.send_index += 1
                        continue
                    if name == "Power Bracelets":
                        gat.power_bracelet()
                        ctx.send_index += 1
                        continue
                    if name == "Heros Charm":
                        gat.give_hero_charm()
                        ctx.send_index += 1
                        continue
                    if name == "Double Magic":
                        gat.double_magic()
                        ctx.send_index += 1
                        continue

                    #SONGS
                    if name == "Winds Requiem":
                        gat.give_link_song(0)
                        ctx.send_index += 1
                        continue
                    if name == "Ballad of the Gales":
                        gat.give_link_song(1)
                        ctx.send_index += 1
                        continue
                    if name == "Command Melody":
                        gat.give_link_song(2)
                        ctx.send_index += 1
                        continue
                    if name == "Earth God Lyrics":
                        gat.give_link_song(3)
                        ctx.send_index += 1
                        continue
                    if name == "Wind Gods Aria":
                        gat.give_link_song(4)
                        ctx.send_index += 1
                        continue
                    if name == "Song of Passing":
                        gat.give_link_song(5)
                        ctx.send_index += 1
                        continue

                    #LETTERS
                    if name == "Note to Mom" or name == "Cabana Deed" or \
                        name == "Maggies Letter" or name == "Moblins Letter":
                        gat.give_letter(name)
                        ctx.send_index += 1
                        continue

                    #MONEY
                    if name == "Tingle Reward":
                        gat.give_link_rupees(500)
                        ctx.send_index += 1
                        continue

                    if name[-5:] == "Rupee":
                        amount: int = 0
                        if name[0] == "G":
                            amount = 1
                        elif name[0] == "B":
                            amount = 5
                        elif name[0] == "Y":
                            amount = 10
                        elif name[0] == "R":
                            amount = 20
                        elif name[0] == "P":
                            amount = 50
                        elif name[0] == "O":
                            amount = 100
                        elif name[0] == "S":
                            amount = 200
                        gat.give_link_rupees(amount)
                        ctx.send_index += 1
                        continue

                    #DUNGEON ITEMS
                    if name[:3] == "DRC":
                        if name[4] == "C":
                            gat.give_drc_comp()
                        elif name[4] == "M":
                            gat.give_drc_map()
                        elif name[4] == "B":
                            gat.give_drc_bk()
                        else:
                            gat.give_drc_sk()
                        ctx.send_index += 1
                        continue

                    if name[:2] == "FW":
                        if name[3] == "C":
                            gat.give_fw_comp()
                        elif name[3] == "M":
                            gat.give_fw_map()
                        elif name[3] == "B":
                            gat.give_fw_bk()
                        else:
                            gat.give_fw_sk()
                        ctx.send_index += 1
                        continue
            
                    if name[:4] == "TotG":
                        if name[5] == "C":
                            gat.give_totg_comp()
                        elif name[5] == "M":
                            gat.give_totg_map()
                        elif name[5] == "B":
                            gat.give_totg_bk()
                        else:
                            gat.give_totg_sk()
                        ctx.send_index += 1
                        continue

                    if name[:2] == "FF":
                        if name[3] == "C":
                            gat.give_ff_comp()
                        else:
                            gat.give_ff_map()
                        ctx.send_index += 1
                        continue
            
                    if name[:2] == "ET":
                        if name[3] == "C":
                            gat.give_et_comp()
                        elif name[3] == "M":
                            gat.give_et_map()
                        elif name[3] == "B":
                            gat.give_et_bk()
                        else:
                            gat.give_et_sk()
                        ctx.send_index += 1
                        continue

                    if name[:2] == "WT":
                        if name[3] == "C":
                            gat.give_wt_comp()
                        elif name[3] == "M":
                            gat.give_wt_map()
                        elif name[3] == "B":
                            gat.give_wt_bk()
                        else:
                            gat.give_wt_sk()
                        ctx.send_index += 1
                        continue

                    if name == "Ghost Ship Chart":
                        gat.give_ghost_ship()
                        ctx.send_index += 1
                        continue

                    if name != "Defeat Ganon":
                        gat.give_spoil(name)
                        ctx.send_index += 1
                        continue

                    #Defeat Ganon (Victory)
                await asyncio.sleep(3)
        await asyncio.sleep(3)


async def ww_location_watcher(ctx: WWCommonContext):
    log = asyncio.create_task(location_scanner(logger, ctx, ww_loc_name_to_id), name="locSc")
    await log

#Doesn't Currently Work
async def death_link_watcher(ctx: WWCommonContext):
    watch = asyncio.create_task(death_link_watch(ctx), name='watt')
    await watch

async def main(args):
    ctx = WWCommonContext(args.connect, args.password)
    ctx.server_task = asyncio.create_task(server_loop(ctx), name="Server Loop")

    if gui_enabled:
        ctx.run_gui()
    ctx.run_cli()

    
    while not ctx.auth:
        await asyncio.sleep(3)


    await ctx.update_death_link(True)
    if 'DeathLink' in ctx.tags:
        death = asyncio.create_task(death_link_watch(ctx))


    check: bool = False
    while not check:
        dme.hook()
        if gat.can_be_given():
            #value = dme.read_word(0x803C50B8)
            #value &= ~(1 << 16)
            #value &= ~(1 << 17)
            #value &= ~(1 << 18)
            #value &= ~(1 << 19)
            #print(value, value>>16&1, value>>17&1, value>>18&1, value>>19&1)
           # dme.write_word(0x803C50B8, value)
            ctx.send_index = dme.read_word(0x803C50B8) & 255
            check = True
        else:
            logger.info("Please Load Into Save File")
            await asyncio.sleep(5)

    location_watcher = asyncio.create_task(ww_location_watcher(ctx), name="WWProgressionWatcher")
    item_giver = asyncio.create_task(ww_item_giver(ctx), name="ItemGiver")
    item_check = asyncio.create_task(item_checker(ctx), name="WWItemChecker")

    await ctx.exit_event.wait()
    ctx.server_address = None

    await location_watcher
    await item_giver
    await item_check
    
    if 'DeathLink' in ctx.tags:
        await death
    await ctx.shutdown()


if __name__ == "__main__":
    Utils.init_logging("Wind Waker Client")

    parser = get_base_parser()
    args, rest = parser.parse_known_args()

    import colorama

    colorama.init()
    asyncio.run(main(args))
    colorama.deinit()