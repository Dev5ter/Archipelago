from BaseClasses import Location
from typing import NamedTuple, Optional, Callable, Dict


class AchievementData(NamedTuple):
    id: Optional[int]
    region: str


class WindWakerAchievement(Location):
    game: str = "Wind Waker"


achievement_table: Dict[str, AchievementData] = {
    "Outset - Under Link's House": AchievementData(0x238000, "Outset - Under Grandmas House"),
    "Outset - Grasscutter House": AchievementData(0x238001, "Outset - Grasscutters House"),
    "Outset - Jabun's Cave": AchievementData(0x238002, "Outset - Jabuns Cave"),
    "Outset - Big Pig": AchievementData(0x238003, "The Great Sea"),
    "Outset - Savage Labyrinth Floor 30": AchievementData(0x238004, "Outset - Savage Labyrinth First"),
    "Outset - Savage Labyrinth Floor 50": AchievementData(0x238005, "Savage Labyrinth Second"),
    "Outset - Give Orca 10 Knights Crest": AchievementData(0x238006, "Outset - Orcas House"),

    "Windfall - Tingles Gift 1": AchievementData(0x238007, "Windfall - Jail"),
    "Windfall - Tingles Gift 2": AchievementData(0x238008, "Windfall - Jail"),
    "Windfall - Jail Maze": AchievementData(0x238009, "Windfall - Jail"),
    "Windfall - Lenzo Left": AchievementData(0x23800A, "Windfall - Lenzo Upper"),
    "Windfall - Lenzo Right": AchievementData(0x23800B, "Windfall - Lenzo Upper"),
    "Windfall - Win Sploosh Kaboom Once": AchievementData(0x23800C, "Windfall - Sploosh Kaboom"),
    "Windfall - Win Sploosh Kaboom Twice": AchievementData(0x23800D, "Windfall - Sploosh Kaboom"),
    "Windfall - House of Wealth Chest": AchievementData(0x23800E, "Windfall - Maggie Room"),
    "Windfall - Green Potion Brewery": AchievementData(0x23800F, "Windfall - Potion Shop"),
    "Windfall - Blue Potion Brewery": AchievementData(0x238010, "Windfall - Potion Shop"),
    "Windfall - Light the Lighthouse": AchievementData(0x238011, "The Great Sea"),
    "Windfall - Transparent Chest": AchievementData(0x238012, "The Great Sea"),
    "Windfall - Pirate Ship Chest": AchievementData(0x238013, "Windfall - Pirate Ship"),

    "DRI - Wind Shrine": AchievementData(0x238014, "The Great Sea"),
    "DRI - Top of Boulder": AchievementData(0x238015, "The Great Sea"),
    "DRI - Fly Around Island": AchievementData(0x238016, "Fly Around Island"),
    "DRI - Mail Game": AchievementData(0x238017, "DRI Rito Hub"),
    "DRI - Secret Cave": AchievementData(0x238018, "DRI Secret Cave"),

    "DRC - First Chest": AchievementData(0x238019, "DRC - First Room"),
    "DRC - Water Jug Alcove": AchievementData(0x23801A, "DRC - HUB Room"),
    "DRC - Behind Boards": AchievementData(0x23801B, "DRC - HUB Room"),
    "DRC - Across Lava Pit": AchievementData(0x23801C, "DRC - Past 1st Locked Door"),
    "DRC - Rat Room": AchievementData(0x23801D, "DRC - Past 1st Locked Door"),
    "DRC - Rat Room Boarded Chest": AchievementData(0x23801E, "DRC - Past 1st Locked Door"),
    "DRC - Birds Nest": AchievementData(0x23801F, "DRC - Outside Rat Room"),
    "DRC - Dark Room Chest": AchievementData(0x238020, "DRC - Dark Room"),
    "DRC - Tingle Chest in DRC HUB": AchievementData(0x238021, "DRC - Dark Room"),
    "DRC - Pot Room": AchievementData(0x238022, "DRC - Dark Room"),
    "DRC - Mini-Boss Fight": AchievementData(0x238023, "DRC - Dark Room"),
    "DRC - Under Bridge": AchievementData(0x238024, "DRC - Dark Room"),
    "DRC - Tingle Chest in DRC Basement": AchievementData(0x238025, "DRC - Basement"),
    "DRC - Big Key Chest": AchievementData(0x238026, "DRC - Basement"),
    "DRC - Outside Boss Door Left": AchievementData(0x238027, "DRC - Dark Room"),
    "DRC - Outside Boss Door Right": AchievementData(0x238028, "DRC - Dark Room"),
    "DRC - Gohma Heart Container": AchievementData(0x238029, "DRC - Boss Fight Arena"),

    "Forest Haven - On Tree Branch": AchievementData(0x23802A, "Forest Haven"),
    "Forest Haven - On Small Island": AchievementData(0x23802B, "The Great Sea"),

    "Forbidden Woods - 1st Chest": AchievementData(0x23802C, "Forbidden Woods - Pre HUB Room"),
    "Forbidden Woods - In Bottom Tree": AchievementData(0x23802D, "Forbidden Woods - Pre HUB Room"),
    "Forbidden Woods - Climb to Top": AchievementData(0x23802E, "Forbidden Woods - Pre HUB Room"),
    "Forbidden Woods - Hole in Tree": AchievementData(0x23802F, "Forbidden Woods - Pre HUB Room"),
    "Forbidden Woods - In Morths Pit": AchievementData(0x238030, "Forbidden Woods - HUB Room"),
    "Forbidden Woods - Vine Maze Left": AchievementData(0x238031, "Forbidden Woods - HUB Room"),
    "Forbidden Woods - Vine Maze Right": AchievementData(0x238032, "Forbidden Woods - HUB Room"),
    "Forbidden Woods - Tall Room Before Mini-Boss": AchievementData(0x238033, "Forbidden Woods - Past Locked Door"),
    "Forbidden Woods - Mini-Boss": AchievementData(0x238034, "Forbidden Woods - Past Locked Door"),
    "Forbidden Woods - Past Hanging Vines": AchievementData(0x238035, "Forbidden Woods - Past Locked Door"),
    "Forbidden Woods - Across the Flower": AchievementData(0x238036, "Forbidden Woods - Basement"),
    "Forbidden Woods - Tingle Chest": AchievementData(0x238037, "Forbidden Woods - Basement"),
    "Forbidden Woods - Locked in Basement Trunk": AchievementData(0x238038, "Forbidden Woods - Basement"),
    "Forbidden Woods - Big Key Chest": AchievementData(0x238039, "Forbidden Woods - Basement"),
    "Forbidden Woods - Double Mothula": AchievementData(0x23803A, "Forbidden Woods - Boss Arena"),
    "Forbidden Woods - Kalle Demos Heart Container": AchievementData(0x23803B, "Forbidden Woods - Boss Arena"),

    "Greatfish - Hidden Chest": AchievementData(0x23803C, "The Great Sea"),

    "Tower of Gods - Light Torches": AchievementData(0x23803D, "Tower of Gods - Left Side"),
    "Tower of Gods - Skull Room": AchievementData(0x23803E, "Tower of Gods - Left Side"),
    "Tower of Gods - Skull Room Shoot The Eye": AchievementData(0x23803F, "Tower of Gods - Left Side"),
    "Tower of Gods - Behind Bombable Wall": AchievementData(0x238040, "Tower of Gods - 1st Floor"),
    "Tower of Gods - Hop Across Boxes": AchievementData(0x238041, "Tower of Gods - 1st Floor"),
    "Tower of Gods - Tingle Chest": AchievementData(0x238042, "Tower of Gods - Until Stone Tablet"),
    "Tower of Gods - First Chest Guarded": AchievementData(0x238043, "Tower of Gods - Until Stone Tablet"),
    "Tower of Gods - Stone Tablet": AchievementData(0x238044, "Tower of Gods - Until Stone Tablet"),
    "Tower of Gods - Mini-Boss": AchievementData(0x238045, "Tower of Gods - Mini Boss Arena"),
    "Tower of Gods - Second Chest Guarded": AchievementData(0x238046, "Tower of Gods - Before Locked Door"),
    "Tower of Gods - Flying Platforms 1": AchievementData(0x238047, "Tower of Gods - Before Locked Door"),
    "Tower of Gods - Flying Platforms 2": AchievementData(0x238048, "Tower of Gods - Before Locked Door"),
    "Tower of Gods - Big Key Chest": AchievementData(0x238049, "Tower of Gods - Past Locked Door"),
    "Tower of Gods - Gohdan Heart Container": AchievementData(0x23804A, "Tower of Gods - Boss Arena"),

    "Hyrule - Master Sword Chamber": AchievementData(0x23804B, "Master Sword Chamber"),

    "Forsaken Fortress - Phantom Ganon": AchievementData(0x23804C, "Forsaken Fortress Interior"),
    "Forsaken Fortress - Upper Jail": AchievementData(0x23804D, "Forsaken Fortress - Within the Walls"),
    "Forsaken Fortress - Lower Jail": AchievementData(0x23804E, "Forsaken Fortress - Within the Walls"),
    "Forsaken Fortress - Chest Guarded by Bokoblin": AchievementData(0x23804F, "Forsaken Fortress - Within the Walls"),
    "Forsaken Fortress - Chest on Bed": AchievementData(0x238050, "Forsaken Fortress - Within the Walls"),
    "Forsaken Fortress - Helmaroc King Heart Container": AchievementData(0x238051,
                                                                         "Forsaken Fortress - Within the Walls"),

    "Mother & Child - Interior": AchievementData(0x238052, "Inside Mother & Child"),

    "Fire Mountain - Cave": AchievementData(0x238053, "Fire Mountain Cave"),
    "Fire Mountain - Free Platform": AchievementData(0x238054, "The Great Sea"),
    "Fire Mountain - Cannon Platform": AchievementData(0x238055, "The Great Sea"),
    # "Fire Mountain - Big Octo": AchievementData(0x238056, "The Great Sea"),

    "Ice Ring - Frozen Chest": AchievementData(0x238057, "Ice Ring Cave"),
    "Ice Ring - Cave": AchievementData(0x238058, "Ice Ring Cave"),
    "Ice Ring - Inner Cave": AchievementData(0x238059, "Ice Ring Inner Cave"),

    "Headstone Island - Top of Island": AchievementData(0x23805A, "The Great Sea"),
    "Headstone Island - Submarine": AchievementData(0x23805B, "Headstone Submarine"),

    "Earth Temple - First Room": AchievementData(0x23805C, "Earth Temple - First Rooms"),
    "Earth Temple - Transparent Chest in 1st Crypt": AchievementData(0x23805D, "Earth Temple - First Rooms"),
    "Earth Temple - Behind Destructable Walls": AchievementData(0x23805E, "Earth Temple - First Rooms"),
    "Earth Temple - 3 Blocks Room": AchievementData(0x23805F, "Earth Temple - Left Side"),
    "Earth Temple - Behind Statues": AchievementData(0x238060, "Earth Temple - Left Side"),
    "Earth Temple - Casket in 2nd Crypt": AchievementData(0x238061, "Earth Temple - Left Side"),
    "Earth Temple - Staflos Mini Boss": AchievementData(0x238062, "Earth Temple - Left Side"),
    "Earth Temple - Tingle Chest": AchievementData(0x238063, "Earth Temple - Basement"),
    "Earth Temple - Floormaster Room Free": AchievementData(0x238064, "Earth Temple - Past Song Stone"),
    "Earth Temple - Floormaster Room Fight": AchievementData(0x238065, "Earth Temple - Past Song Stone"),
    "Earth Temple - 3rd Crypt Chest": AchievementData(0x238066, "Earth Temple - Past 2nd Locked Door"),
    "Earth Temple - Many Mirrors Left": AchievementData(0x238067, "Earth Temple - Past 2nd Locked Door"),
    "Earth Temple - Many Mirrors Right": AchievementData(0x238068, "Earth Temple - Past 2nd Locked Door"),
    "Earth Temple - Staflos Crypt Room": AchievementData(0x238069, "Earth Temple - Past 2nd Locked Door"),
    "Earth Temple - Big Key Chest": AchievementData(0x23806A, "Earth Temple - Past 2nd Locked Door"),
    "Earth Temple - Jalhalla Heart Container": AchievementData(0x23806B, "Earth Temple - Boss Arena"),

    "Wind Temple - Two Dirt Patches": AchievementData(0x23806C, "Wind Temple - First Room"),
    "Wind Temple - Tingle Chest": AchievementData(0x23806D, "Wind Temple - HUB Room"),
    "Wind Temple - Behind Stone Head": AchievementData(0x23806E, "Wind Temple - HUB Room"),
    "Wind Temple - Left Alcove": AchievementData(0x23806F, "Wind Temple - HUB Room"),
    "Wind Temple - Big Key Chest": AchievementData(0x238070, "Wind Temple - HUB Room"),
    "Wind Temple - Many Cyclones Room": AchievementData(0x238071, "Wind Temple - HUB Room"),
    "Wind Temple - Middle of HUB Room": AchievementData(0x238072, "Wind Temple - HUB Room"),
    "Wind Temple - Spike Room - Free Chest": AchievementData(0x238073, "Wind Temple - HUB Room"),
    "Wind Temple - Spike Room - Break All Floors": AchievementData(0x238074, "Wind Temple - HUB Room"),
    "Wind Temple - Wizzrobe Mini Boss": AchievementData(0x238075, "Wind Temple - HUB Room"),
    "Wind Temple - Top of HUB Room": AchievementData(0x238076, "Wind Temple - HUB Room"),
    "Wind Temple - Behind 7 Armos": AchievementData(0x238077, "Wind Temple - HUB Room"),
    "Wind Temple - Kill Enemies in Basement": AchievementData(0x238078, "Wind Temple - Basement"),
    "Wind Temple - Molgera Heart Container": AchievementData(0x238079, "Wind Temple - Boss Arena"),

    "Ganons Tower - Maze Chest": AchievementData(0x23807A, "Ganons Tower"),

    "Great Sea - Defeat Cyclos": AchievementData(0x23807B, "The Great Sea"),
    "Great Sea - Withered Trees": AchievementData(0x23807C, "The Great Sea"),
    "Great Sea - Ghost Ship": AchievementData(0x23807D, "The Great Sea"),

    "Private Oasis - Top of Waterfall": AchievementData(0x23807E, "The Great Sea"),
    "Cabana Labyrinth - Lower": AchievementData(0x23807F, "Cabana Labyrinth"),
    "Cabana Labyrinth - Upper": AchievementData(0x238080, "Cabana Labyrinth"),
    # "Private Oasis - Big Octo": AchievementData(0x238081, "The Great Sea"),

    "Needle Rock - Chest in Ring of Fire": AchievementData(0x238082, "The Great Sea"),
    "Needle Rock - Cave": AchievementData(0x238083, "Needle Rock Cave"),
    # "Needle Rock - Golden Gunboat": AchievementData(0x238084, "The Great Sea"),

    "Angular - Peak": AchievementData(0x238085, "The Great Sea"),
    "Angular - Cave": AchievementData(0x238086, "Angular Cave"),

    "Boating Course - Raft": AchievementData(0x238087, "The Great Sea"),
    "Boating Course - Cave": AchievementData(0x238088, "Boating Course Cave"),

    "Stone Watcher - Cave": AchievementData(0x238089, "Stone Watcher Cave"),
    "Stone Watcher - Free Platform": AchievementData(0x23808A, "The Great Sea"),
    "Stone Watcher - Cannon Platform": AchievementData(0x23808B, "The Great Sea"),

    "Islet of Steel - Cave": AchievementData(0x23808C, "Islet of Steel"),
    "Islet of Steel - Enemy Platform": AchievementData(0x23808D, "The Great Sea"),

    "Overlook - Cave": AchievementData(0x23808E, "Overlook Cave"),

    "Birds Peak Rock - Cave": AchievementData(0x23808F, "Birds Peak Rock Cave"),

    "Pawprint - Chu Cave - Chest": AchievementData(0x238090, "Pawprint Chu Cave"),
    "Pawprint - Chu Cave - Left Boulder": AchievementData(0x238091, "Pawprint Chu Cave"),
    "Pawprint - Chu Cave - Right Boulder": AchievementData(0x238092, "Pawprint Chu Cave"),
    "Pawprint - Chu Cave - Scale Wall": AchievementData(0x238093, "Pawprint Chu Cave"),
    "Pawprint - Wizzrobe Cave": AchievementData(0x238094, "Pawprint Wizzrobe Cave"),
    "Pawprint - Free Platform": AchievementData(0x238095, "The Great Sea"),

    "Thorned Fairy - Cannon Platform": AchievementData(0x238096, "The Great Sea"),
    "Thorned Fairy - Enemy Platform": AchievementData(0x238097, "The Great Sea"),
    "Eastern Fairy - Cannon Platform": AchievementData(0x238098, "The Great Sea"),
    "Western Fairy - Free Platform": AchievementData(0x238099, "The Great Sea"),
    "Southern Fairy - NW Cannon Platform": AchievementData(0x23809A, "The Great Sea"),
    "Southern Fairy - SE Cannon Platform": AchievementData(0x23809B, "The Great Sea"),
    "Northern Fairy - Submarine": AchievementData(0x23809C, "Northern Fairy Submarine"),

    # "Tingle Island - Big Octo": AchievementData(0x23809D, "The Great Sea"),

    "Diamond Steppe - Warp Maze 1st": AchievementData(0x23809E, "Diamond Steppe Cave"),
    "Diamond Steppe - Warp Maze 2nd": AchievementData(0x23809F, "Diamond Steppe Cave"),
    # "Diamond Steppe - Big Octo": AchievementData(0x2380A0, "The Great Sea"),

    "Bomb Island - Cave": AchievementData(0x2380A1, "Bomb Island Cave"),
    "Bomb Island - Free Platform": AchievementData(0x2380A2, "The Great Sea"),
    "Bomb Island - Submarine": AchievementData(0x2380A3, "Bomb Island Submarine"),

    "Rock Spire - Cave": AchievementData(0x2380A4, "Rock Spire Cave"),
    "Expensive Beedle - 500 Item": AchievementData(0x2380A5, "Expensive Beedle Ship"),
    "Expensive Beedle - 900 Item": AchievementData(0x2380A6, "Expensive Beedle Ship"),
    "Expensive Beedle - 950 Item": AchievementData(0x2380A7, "Expensive Beedle Ship"),
    "Rock Spire - Western Cannon Platform": AchievementData(0x2380A8, "The Great Sea"),
    "Rock Spire - Eastern Cannon Platform": AchievementData(0x2380A9, "The Great Sea"),
    "Rock Spire - Center Platform": AchievementData(0x2380AA, "The Great Sea"),
    # "Rock Spire - Southeast Gunboat": AchievementData(0x2380AB, "The Great Sea"),

    "Shark Island - Cave": AchievementData(0x2380AC, "Shark Island Cave"),

    "Cliff Plateau - Cave": AchievementData(0x2380AD, "Cliff Plateau Cave"),
    "Cliff Plateau - Upper": AchievementData(0x2380AE, "Cliff Plateau Upper"),
    "Cliff Plateau - Free Platform": AchievementData(0x2380AF, "The Great Sea"),

    "Crescent Moon - Chest": AchievementData(0x2380B0, "The Great Sea"),
    "Crescent Moon - Submarine": AchievementData(0x2380B1, "Crescent Moon Submarine"),

    "Horseshoe - Play Golf": AchievementData(0x2380B2, "The Great Sea"),
    "Horseshoe - Cave": AchievementData(0x2380B3, "Horseshoe Cave"),
    "Horseshoe - NW Free Platform": AchievementData(0x2380B4, "The Great Sea"),
    "Horseshoe - SE Free Platform": AchievementData(0x2380B5, "The Great Sea"),

    "Flight Control - Submarine": AchievementData(0x2380B6, "Flight Control Submarine"),

    "Star Island - Cave": AchievementData(0x2380B7, "Star Island Cave"),
    "Star Island - Free Platform": AchievementData(0x2380B8, "The Great Sea"),

    "Star Belt - Free Platform": AchievementData(0x2380B9, "The Great Sea"),

    "5 Star - Cannon Platform": AchievementData(0x2380BA, "The Great Sea"),
    "5 Star - Raft": AchievementData(0x2380BB, "The Great Sea"),
    "5 Star - Submarine": AchievementData(0x2380BC, "5 Star Submarine"),

    "7 Star - Center Platform": AchievementData(0x2380BD, "The Great Sea"),
    "7 Star - Northern Platform": AchievementData(0x2380BE, "The Great Sea"),
    "7 Star - Southern Platform": AchievementData(0x2380BF, "The Great Sea"),
    # "7 Star - Big Octo": AchievementData(0x2380C0, "The Great Sea"),

    "1 Eye Reef - Top of Eye": AchievementData(0x2380C1, "The Great Sea"),
    "1 Eye Reef - Enemy Platform": AchievementData(0x2380C2, "The Great Sea"),

    "2 Eye Reef - Top of Eye": AchievementData(0x2380C3, "The Great Sea"),
    "2 Eye Reef - Free Platform": AchievementData(0x2380C4, "The Great Sea"),
    "2 Eye Reef - Big Octo Fairy": AchievementData(0x2380C5, "The Great Sea"),

    "3 Eye Reef - Top of Eye": AchievementData(0x2380C6, "The Great Sea"),
    "4 Eye Reef - Top of Eye": AchievementData(0x2380C7, "The Great Sea"),
    "5 Eye Reef - Top of Eye": AchievementData(0x2380C8, "The Great Sea"),
    "5 Eye Reef - Free Platform": AchievementData(0x2380C9, "The Great Sea"),

    "6 Eye Reef - Top of Eye": AchievementData(0x2380CA, "The Great Sea"),
    "6 Eye Reef - Cannon Platform": AchievementData(0x2380CB, "The Great Sea"),
    "6 Eye Reef - Submarine": AchievementData(0x2380CC, "6 Eye Reef Submarine"),

    "Treasure Chart 1 Salvage": AchievementData(0x2380CD, "The Great Sea"),
    "Treasure Chart 2 Salvage": AchievementData(0x2380CE, "The Great Sea"),
    "Treasure Chart 3 Salvage": AchievementData(0x2380CF, "The Great Sea"),
    "Treasure Chart 4 Salvage": AchievementData(0x2380D0, "The Great Sea"),
    "Treasure Chart 5 Salvage": AchievementData(0x2380D1, "The Great Sea"),
    "Treasure Chart 6 Salvage": AchievementData(0x2380D2, "The Great Sea"),
    "Treasure Chart 7 Salvage": AchievementData(0x2380D3, "The Great Sea"),
    "Treasure Chart 8 Salvage": AchievementData(0x2380D4, "The Great Sea"),
    "Treasure Chart 9 Salvage": AchievementData(0x2380D5, "The Great Sea"),
    "Treasure Chart 10 Salvage": AchievementData(0x2380D6, "The Great Sea"),
    "Treasure Chart 11 Salvage": AchievementData(0x2380D7, "The Great Sea"),
    "Treasure Chart 12 Salvage": AchievementData(0x2380D8, "The Great Sea"),
    "Treasure Chart 13 Salvage": AchievementData(0x2380D9, "The Great Sea"),
    "Treasure Chart 14 Salvage": AchievementData(0x2380DA, "The Great Sea"),
    "Treasure Chart 15 Salvage": AchievementData(0x2380DB, "The Great Sea"),
    "Treasure Chart 16 Salvage": AchievementData(0x2380DC, "The Great Sea"),
    "Treasure Chart 17 Salvage": AchievementData(0x2380DD, "The Great Sea"),
    "Treasure Chart 18 Salvage": AchievementData(0x2380DE, "The Great Sea"),
    "Treasure Chart 19 Salvage": AchievementData(0x2380DF, "The Great Sea"),
    "Treasure Chart 20 Salvage": AchievementData(0x2380E0, "The Great Sea"),
    "Treasure Chart 21 Salvage": AchievementData(0x2380E1, "The Great Sea"),
    "Treasure Chart 22 Salvage": AchievementData(0x2380E2, "The Great Sea"),
    "Treasure Chart 23 Salvage": AchievementData(0x2380E3, "The Great Sea"),
    "Treasure Chart 24 Salvage": AchievementData(0x2380E4, "The Great Sea"),
    "Treasure Chart 25 Salvage": AchievementData(0x2380E5, "The Great Sea"),
    "Treasure Chart 26 Salvage": AchievementData(0x2380E6, "The Great Sea"),
    "Treasure Chart 27 Salvage": AchievementData(0x2380E7, "The Great Sea"),
    "Treasure Chart 28 Salvage": AchievementData(0x2380E8, "The Great Sea"),
    "Treasure Chart 29 Salvage": AchievementData(0x2380E9, "The Great Sea"),
    "Treasure Chart 30 Salvage": AchievementData(0x2380EA, "The Great Sea"),
    "Treasure Chart 31 Salvage": AchievementData(0x2380EB, "The Great Sea"),
    "Treasure Chart 32 Salvage": AchievementData(0x2380EC, "The Great Sea"),
    "Treasure Chart 33 Salvage": AchievementData(0x2380ED, "The Great Sea"),
    "Treasure Chart 34 Salvage": AchievementData(0x2380EE, "The Great Sea"),
    "Treasure Chart 35 Salvage": AchievementData(0x2380EF, "The Great Sea"),
    "Treasure Chart 36 Salvage": AchievementData(0x2380F0, "The Great Sea"),
    "Treasure Chart 37 Salvage": AchievementData(0x2380F1, "The Great Sea"),
    "Treasure Chart 38 Salvage": AchievementData(0x2380F2, "The Great Sea"),
    "Treasure Chart 39 Salvage": AchievementData(0x2380F3, "The Great Sea"),
    "Treasure Chart 40 Salvage": AchievementData(0x2380F4, "The Great Sea"),
    "Treasure Chart 41 Salvage": AchievementData(0x2380F5, "The Great Sea"),

    "Triforce Chart 1 Salvage": AchievementData(0x2380F6, "The Great Sea"),
    "Triforce Chart 2 Salvage": AchievementData(0x2380F7, "The Great Sea"),
    "Triforce Chart 3 Salvage": AchievementData(0x2380F8, "The Great Sea"),
    "Triforce Chart 4 Salvage": AchievementData(0x2380F9, "The Great Sea"),
    "Triforce Chart 5 Salvage": AchievementData(0x2380FA, "The Great Sea"),
    "Triforce Chart 6 Salvage": AchievementData(0x2380FB, "The Great Sea"),
    "Triforce Chart 7 Salvage": AchievementData(0x2380FC, "The Great Sea"),
    "Triforce Chart 8 Salvage": AchievementData(0x2380FD, "The Great Sea"),

    "Victory": AchievementData(None, "Ganons Tower"),
}

lookup_id_to_name: Dict[int, str] = {loc_data.id: loc_name for loc_name, loc_data in achievement_table.items() if
                                     loc_data.id}
location_name_groups = {
    "Dragon Roost Cavern": {"DRC - First Chest", "DRC - Water Jug Alcove", "DRC - Behind Boards",
                            "DRC - Across Lava Pit", "DRC - Rat Room", "DRC - Rat Room Boarded Chest",
                            "DRC - Birds Nest", "DRC - Dark Room Chest", "DRC - Tingle Chest in DRC HUB",
                            "DRC - Pot Room", "DRC - Mini-Boss Fight", "DRC - Under Bridge",
                            "DRC - Tingle Chest in DRC Basement", "DRC - Big Key Chest", "DRC - Outside Boss Door Left",
                            "DRC - Outside Boss Door Right", "DRC - Gohma Heart Container"},
    "Forbidden Woods": {"Forbidden Woods - 1st Chest", "Forbidden Woods - In Bottom Tree",
                        "Forbidden Woods - Climb to Top", "Forbidden Woods - Hole in Tree",
                        "Forbidden Woods - In Morths Pit", "Forbidden Woods - Vine Maze Left",
                        "Forbidden Woods - Vine Maze Right", "Forbidden Woods - Tall Room Before Mini-Boss",
                        "Forbidden Woods - Mini-Boss", "Forbidden Woods - Past Hanging Vines",
                        "Forbidden Woods - Across the Flower", "Forbidden Woods - Tingle Chest",
                        "Forbidden Woods - Locked in Basement Trunk", "Forbidden Woods - Big Key Chest",
                        "Forbidden Woods - Double Mothula", "Forbidden Woods - Kalle Demos Heart Container"},
    "Forsaken Fortress": {"Forsaken Fortress - Phantom Ganon", "Forsaken Fortress - Upper Jail",
                          "Forsaken Fortress - Lower Jail", "Forsaken Fortress - Chest Guarded by Bokoblin",
                          "Forsaken Fortress - Chest on Bed", "Forsaken Fortress - Helmaroc King Heart Container"},
    "Wind Temple": {"Wind Temple - Two Dirt Patches", "Wind Temple - Tingle Chest", "Wind Temple - Behind Stone Head",
                    "Wind Temple - Left Alcove", "Wind Temple - Big Key Chest", "Wind Temple - Many Cyclones Room",
                    "Wind Temple - Middle of HUB Room", "Wind Temple - Spike Room - Free Chest",
                    "Wind Temple - Spike Room - Break All Floors", "Wind Temple - Wizzrobe Mini Boss",
                    "Wind Temple - Top of HUB Room", "Wind Temple - Behind 7 Armos",
                    "Wind Temple - Kill Enemies in Basement", "Wind Temple - Molgera Heart Container"},
    "Earth Temple": {"Earth Temple - First Room", "Earth Temple - Transparent Chest in 1st Crypt",
                     "Earth Temple - Behind Destructable Walls", "Earth Temple - 3 Blocks Room",
                     "Earth Temple - Behind Statues", "Earth Temple - Casket in 2nd Crypt",
                     "Earth Temple - Staflos Mini Boss", "Earth Temple - Tingle Chest",
                     "Earth Temple - Floormaster Room Free", "Earth Temple - Floormaster Room Fight",
                     "Earth Temple - 3rd Crypt Chest", "Earth Temple - Many Mirrors Left",
                     "Earth Temple - Many Mirrors Right", "Earth Temple - Staflos Crypt Room",
                     "Earth Temple - Big Key Chest", "Earth Temple - Jalhalla Heart Container"},
    "Tower of the Gods": {"Tower of Gods - Light Torches", "Tower of Gods - Skull Room",
                          "Tower of Gods - Skull Room Shoot The Eye", "Tower of Gods - Behind Bombable Wall",
                          "Tower of Gods - Hop Across Boxes", "Tower of Gods - Tingle Chest",
                          "Tower of Gods - First Chest Guarded", "Tower of Gods - Stone Tablet",
                          "Tower of Gods - Mini-Boss", "Tower of Gods - Second Chest Guarded",
                          "Tower of Gods - Flying Platforms 1", "Tower of Gods - Flying Platforms 2",
                          "Tower of Gods - Big Key Chest", "Tower of Gods - Gohdan Heart Container"
                          },
    "Treasure Salvaging": {"Treasure Chart 1 Salvage", "Treasure Chart 2 Salvage", "Treasure Chart 3 Salvage",
                           "Treasure Chart 4 Salvage", "Treasure Chart 5 Salvage", "Treasure Chart 6 Salvage",
                           "Treasure Chart 7 Salvage", "Treasure Chart 8 Salvage", "Treasure Chart 9 Salvage",
                           "Treasure Chart 10 Salvage", "Treasure Chart 11 Salvage", "Treasure Chart 12 Salvage",
                           "Treasure Chart 13 Salvage", "Treasure Chart 14 Salvage", "Treasure Chart 15 Salvage",
                           "Treasure Chart 16 Salvage", "Treasure Chart 17 Salvage", "Treasure Chart 18 Salvage",
                           "Treasure Chart 19 Salvage", "Treasure Chart 20 Salvage", "Treasure Chart 21 Salvage",
                           "Treasure Chart 22 Salvage", "Treasure Chart 23 Salvage", "Treasure Chart 24 Salvage",
                           "Treasure Chart 25 Salvage", "Treasure Chart 26 Salvage", "Treasure Chart 27 Salvage",
                           "Treasure Chart 28 Salvage", "Treasure Chart 29 Salvage", "Treasure Chart 30 Salvage",
                           "Treasure Chart 31 Salvage", "Treasure Chart 32 Salvage", "Treasure Chart 33 Salvage",
                           "Treasure Chart 34 Salvage", "Treasure Chart 35 Salvage", "Treasure Chart 36 Salvage",
                           "Treasure Chart 37 Salvage", "Treasure Chart 38 Salvage", "Treasure Chart 39 Salvage",
                           "Treasure Chart 40 Salvage", "Treasure Chart 41 Salvage"
                           },
    "Triforce Salvaging": {"Triforce Chart 1 Salvage", "Triforce Chart 2 Salvage", "Triforce Chart 3 Salvage",
                           "Triforce Chart 4 Salvage", "Triforce Chart 5 Salvage", "Triforce Chart 6 Salvage",
                           "Triforce Chart 7 Salvage", "Triforce Chart 8 Salvage"}
}

location_name_groups["Salvaging"] = location_name_groups["Triforce Salvaging"] | location_name_groups[
    "Treasure Salvaging"]
