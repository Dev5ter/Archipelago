class Location:
    def __init__(self, name, stageID, isChestID, isPickID, isMemID, which_mem, isChart, which_chart, isVar, which_bit):
        self.name: str = name
        self.stageID: int = stageID
        self.isChestID: bool = isChestID
        self.isPickID: bool = isPickID
        self.isMemID: bool = isMemID
        self.which_mem: int = which_mem
        self.isChart: bool = isChart
        self.which_chart: int = which_chart
        self.isVar: bool = isVar
        self.which_bit: int = which_bit
        self.hasGotten: bool = False

location_table: list[Location] = [  # 240/254/304
   #Location( "Name of Check"     StageID, chest, pickup, mem, bit#) 

    #Stage 0x0 (Sea) 34 FORMATTED
    Location("Angular - Peak"          , 0x0, True, False, False, -1, False, -1, False, 0),
    Location("Cliff Plateau - Upper"    , 0x0, True, False, False, -1, False, -1, False, 1),
    Location("5 Star - Raft"           , 0x0, True, False, False, -1, False, -1, False, 2),
    Location("Outset - Big Pig"        , 0x0, False, True, False, -1, False, -1, False, 2),
    Location("Needle Rock - Chest in Ring of Fire", 0x0, True, False, False, -1, False, -1, False, 3),
    Location("Crescent Moon - Chest"  , 0x0, True, False, False, -1, False, -1, False, 4),
    Location("2 Eye Reef - Big Octo Fairy" , 0x0, False, False, True, 0, False, -1, False,  4),
    Location("Horseshoe - Play Golf"   , 0x0, True, False, False, -1, False, -1, False, 5),
    Location("Greatfish - Hidden Chest", 0x0, True, False, False, -1, False, -1, False, 6),
    Location("Forest Haven - On Small Island"   , 0x0, True, False, False, -1, False, -1, False, 7),
    Location("Headstone Island - Top of Island" , 0x0, False, True, False, -1, False, -1, False, 8),
    Location("DRI - Top of Boulder" , 0x0, True, False, False, -1, False, -1, False, 8),
    Location("DRI - Fly Around Island", 0x0, True, False, False, -1, False, -1, False, 9),
    Location("Windfall - Transparent Chest", 0x0, True, False, False, -1, False, -1, False, 10),
    Location("1 Eye Reef - Top of Eye" , 0x0, True, False, False, -1, False, -1, False, 11),
    Location("3 Eye Reef - Top of Eye" , 0x0, True, False, False, -1, False, -1, False, 12),
    Location("2 Eye Reef - Top of Eye" , 0x0, True, False, False, -1, False, -1, False, 13),
    #Location("7 Star - Big Octo"       , 0x0, False, False, True, 0, False, -1, False, 13),
    Location("4 Eye Reef - Top of Eye" , 0x0, True, False, False, -1, False, -1, False, 14),
    #Location("Tingle Island - Big Octo"  , 0x0, False, False, True, 0, False, -1, False, 14),
    Location("5 Eye Reef - Top of Eye" , 0x0, True, False, False, -1, False, -1, False, 15),
    #Location("Fire Mountain - Big Octo", 0x0, False, False, True, 0, False, -1, False, 15),
    Location("Forsaken Fortress - Phantom Ganon" , 0x0, True, False, False, -1, False, -1, False, 16),
    #Location("Private Oasis - Big Octo", 0x0, False, False, True, 0, False, -1, False, 16),
    Location("DRI - Wind Shrine"       , 0x0, False, False, True, 1, False, -1, False, 16),
    Location("6 Eye Reef - Top of Eye" , 0x0, True, False, False, -1, False, -1, False, 17),
    #Location("Diamond Steppe - Big Octo", 0x0, False, False, True, 0, False, -1, False, 17),
    Location("Ice Ring - Frozen Chest"  , 0x0, True, False, False, -1, False, -1, False, 18),
    Location("Private Oasis - Top of Waterfall"   , 0x0, True, False, False, -1, False, -1, False, 19),
    Location("Stone Watcher - Cannon Platform" , 0x0, True, False, False, -1, False, -1, False, 20),
    #Location("Rock Spire - Southeast Gunboat", 0x0, False, False, True, 0, False, -1, False, 20),
    Location("Boating Course - Raft"   , 0x0, True, False, False, -1, False, -1, False, 21),
    Location("7 Star - Southern Platform" , 0x0, True, False, False, -1, False, -1, False, 22),
    #Location("Needle Rock - Golden Gunboat" , 0x0, False, False, True, 0, False, -1, False, 23),
    Location("Southern Fairy - NW Cannon Platform" , 0x0, True, False, False, -1, False, -1, False, 23),
    Location("Mother & Child - Interior"  , 0x0, True, False, False, -1, False, -1, False, 28),
    Location("Windfall - Light the Lighthouse"  , 0x0, False, False, True, 2, False, -1, False, 29),

    #Stage 0x0 (Sea (SALVAGES)) 49 FORMATTED
    Location("Triforce Chart 1 Salvage" , 0x0, False, False, False, -1, True, 0, False, 0),
    Location("Triforce Chart 2 Salvage" , 0x0, False, False, False, -1, True, 0, False, 1),
    Location("Triforce Chart 3 Salvage" , 0x0, False, False, False, -1, True, 0, False, 2),
    Location("Triforce Chart 4 Salvage" , 0x0, False, False, False, -1, True, 0, False, 3),
    Location("Triforce Chart 5 Salvage" , 0x0, False, False, False, -1, True, 0, False, 4),
    Location("Triforce Chart 6 Salvage" , 0x0, False, False, False, -1, True, 0, False, 5),
    Location("Triforce Chart 7 Salvage" , 0x0, False, False, False, -1, True, 0, False, 6),
    Location("Triforce Chart 8 Salvage" , 0x0, False, False, False, -1, True, 0, False, 7),
    Location("Treasure Chart 11 Salvage" , 0x0, False, False, False, -1, True, 0, False, 8),
    Location("Treasure Chart 15 Salvage" , 0x0, False, False, False, -1, True, 0, False, 9),
    Location("Treasure Chart 30 Salvage" , 0x0, False, False, False, -1, True, 0, False, 10),
    Location("Treasure Chart 20 Salvage" , 0x0, False, False, False, -1, True, 0, False, 11),
    Location("Treasure Chart 5 Salvage" , 0x0, False, False, False, -1, True, 0, False, 12),
    Location("Treasure Chart 23 Salvage" , 0x0, False, False, False, -1, True, 0, False, 13),
    Location("Treasure Chart 31 Salvage" , 0x0, False, False, False, -1, True, 0, False, 14),
    Location("Treasure Chart 33 Salvage" , 0x0, False, False, False, -1, True, 0, False, 15),
    Location("Treasure Chart 2 Salvage" , 0x0, False, False, False, -1, True, 0, False, 16),
    Location("Treasure Chart 38 Salvage" , 0x0, False, False, False, -1, True, 0, False, 17),
    Location("Treasure Chart 39 Salvage" , 0x0, False, False, False, -1, True, 0, False, 18),
    Location("Treasure Chart 24 Salvage" , 0x0, False, False, False, -1, True, 0, False, 19),
    Location("Treasure Chart 6 Salvage" , 0x0, False, False, False, -1, True, 0, False, 20),
    Location("Treasure Chart 12 Salvage" , 0x0, False, False, False, -1, True, 0, False, 21),
    Location("Treasure Chart 35 Salvage" , 0x0, False, False, False, -1, True, 0, False, 22),
    Location("Treasure Chart 1 Salvage" , 0x0, False, False, False, -1, True, 0, False, 23),
    Location("Treasure Chart 29 Salvage" , 0x0, False, False, False, -1, True, 0, False, 24),
    Location("Treasure Chart 34 Salvage" , 0x0, False, False, False, -1, True, 0, False, 25),
    Location("Treasure Chart 18 Salvage" , 0x0, False, False, False, -1, True, 0, False, 26),
    Location("Treasure Chart 16 Salvage" , 0x0, False, False, False, -1, True, 0, False, 27),
    Location("Treasure Chart 28 Salvage" , 0x0, False, False, False, -1, True, 0, False, 28),
    Location("Treasure Chart 4 Salvage" , 0x0, False, False, False, -1, True, 0, False, 29),
    Location("Treasure Chart 3 Salvage" , 0x0, False, False, False, -1, True, 0, False, 30),
    Location("Treasure Chart 40 Salvage" , 0x0, False, False, False, -1, True, 0, False, 31),
    Location("Treasure Chart 10 Salvage" , 0x0, False, False, False, -1, True, 1, False, 0),
    Location("Treasure Chart 14 Salvage" , 0x0, False, False, False, -1, True, 1, False, 1),
    Location("Treasure Chart 9 Salvage" , 0x0, False, False, False, -1, True, 1, False, 4),
    Location("Treasure Chart 22 Salvage" , 0x0, False, False, False, -1, True, 1, False, 5),
    Location("Treasure Chart 36 Salvage" , 0x0, False, False, False, -1, True, 1, False, 6),
    Location("Treasure Chart 17 Salvage" , 0x0, False, False, False, -1, True, 1, False, 7),
    Location("Treasure Chart 25 Salvage" , 0x0, False, False, False, -1, True, 1, False, 8),
    Location("Treasure Chart 37 Salvage" , 0x0, False, False, False, -1, True, 1, False, 9),
    Location("Treasure Chart 8 Salvage" , 0x0, False, False, False, -1, True, 1, False, 10),
    Location("Treasure Chart 26 Salvage" , 0x0, False, False, False, -1, True, 1, False, 11),
    Location("Treasure Chart 41 Salvage" , 0x0, False, False, False, -1, True, 1, False, 12),
    Location("Treasure Chart 19 Salvage" , 0x0, False, False, False, -1, True, 1, False, 13),
    Location("Treasure Chart 32 Salvage" , 0x0, False, False, False, -1, True, 1, False, 14),
    Location("Treasure Chart 13 Salvage" , 0x0, False, False, False, -1, True, 1, False, 15),
    Location("Treasure Chart 21 Salvage" , 0x0, False, False, False, -1, True, 1, False, 16),
    Location("Treasure Chart 27 Salvage" , 0x0, False, False, False, -1, True, 1, False, 17),
    Location("Treasure Chart 7 Salvage" , 0x0, False, False, False, -1, True, 1, False, 18),

    #Stage 0x1 (SEA ALT) 24
    Location("Fire Mountain - Cannon Platform", 0x1, True, False, False, -1, False, -1, False, 0),
    Location("Fire Mountain - Free Platform"  , 0x1, True, False, False, -1, False, -1, False, 1),
    Location("5 Star - Cannon Platform"          , 0x1, True, False, False, -1, False, -1, False, 2),
    Location("Bomb Island - Free Platform"      , 0x1, True, False, False, -1, False, -1, False, 3),
    Location("Star Island - Free Platform"      , 0x1, True, False, False, -1, False, -1, False, 4),
    Location("Pawprint - Free Platform"          , 0x1, True, False, False, -1, False, -1, False, 5),
    Location("Western Fairy - Free Platform"    , 0x1, True, False, False, -1, False, -1, False, 6),
    Location("7 Star - Northern Platform"       , 0x1, True, False, False, -1, False, -1, False, 7),
    Location("7 Star - Center Platform"         , 0x1, True, False, False, -1, False, -1, False, 8),
    Location("Eastern Fairy - Cannon Platform"   , 0x1, True, False, False, -1, False, -1, False, 10),
    Location("Star Belt - Free Platform"        , 0x1, True, False, False, -1, False, -1, False, 11),
    Location("1 Eye Reef - Enemy Platform"      , 0x1, True, False, False, -1, False, -1, False, 12),
    Location("6 Eye Reef - Cannon Platform"      , 0x1, True, False, False, -1, False, -1, False, 13),
    Location("Thorned Fairy - Cannon Platform"   , 0x1, True, False, False, -1, False, -1, False, 14),
    Location("Thorned Fairy - Enemy Platform"   , 0x1, True, False, False, -1, False, -1, False, 15),
    Location("Islet of Steel - Enemy Platform" , 0x1, True, False, False, -1, False, -1, False, 16),
    Location("Southern Fairy - SE Cannon Platform"   , 0x1, True, False, False, -1, False, -1, False, 17), 
    Location("Stone Watcher - Free Platform"      , 0x1, True, False, False, -1, False, -1, False, 18),
    Location("Cliff Plateau - Free Platform"     , 0x1, True, False, False, -1, False, -1, False, 19),
    Location("5 Eye Reef - Free Platform"       , 0x1, True, False, False, -1, False, -1, False, 20),
    Location("2 Eye Reef - Free Platform"       , 0x1, True, False, False, -1, False, -1, False, 21),
    Location("Rock Spire - Western Cannon Platform",  0x1, True, False, False, -1, False, -1, False, 23),
    Location("Rock Spire - Eastern Cannon Platform", 0x1, True, False, False, -1, False, -1, False, 24),
    Location("Rock Spire - Center Platform"     , 0x1, True, False, False, -1, False, -1, False, 25),
    Location("Horseshoe - NW Free Platform"     , 0x1, True, False, False, -1, False, -1, False, 26),
    Location("Horseshoe - SE Free Platform"     , 0x1, True, False, False, -1, False, -1, False, 27),

    #Stage 0x2 (Forsaken Fortress) 5 FORMATTED
    Location("Forsaken Fortress - Upper Jail", 0x2, True, False, False, -1, False, -1, False, 0),
    Location("Forsaken Fortress - Chest on Bed", 0x2, True, False, False, -1, False, -1, False, 1),
    Location("Forsaken Fortress - Chest Guarded by Bokolin", 0x2, True, False, False, -1, False, -1, False, 2),
    Location("Forsaken Fortress - Lower Jail", 0x2, True, False, False, -1, False, -1, False, 3),
    Location("Forsaken Fortress - Helmaroc King Heart Container", 0x2, False, True, False, -1, False, -1, False, 21),

    #Stage 0x3 (DRC) 17 FORMATTED
    Location("DRC - First Chest"     , 0x3, True, False, False, -1, False, -1, False, 0),
    Location("DRC - Behind Boards"   , 0x3, True, False, False, -1, False, -1, False, 1),
    Location("DRC - Water Jug Alcove", 0x3, True, False, False, -1, False, -1, False, 2),
    Location("DRC - Rat Room Boarded Chest", 0x3, True, False, False, -1, False, -1, False, 3),
    Location("DRC - Birds Nest"     , 0x3, False, True, False, -1, False, -1, False, 3),
    Location("DRC - Dark Room Chest", 0x3, True, False, False, -1, False, -1, False, 4),
    Location("DRC - Pot Room"        , 0x3, True, False, False, -1, False, -1, False, 6),
    Location("DRC - Under Bridge"    , 0x3, True, False, False, -1, False, -1, False, 7),
    Location("DRC - Outside Boss Door Left" , 0x3, True, False, False, -1, False, -1, False, 10),
    Location("DRC - Outside Boss Door Right", 0x3, True, False, False, -1, False, -1, False, 11),
    Location("DRC - Big Key Chest"   , 0x3, True, False, False, -1, False, -1, False, 12),
    Location("DRC - Across Lava Pit" , 0x3, True, False, False, -1, False, -1, False, 13),
    Location("DRC - Rat Room"        , 0x3, True, False, False, -1, False, -1, False, 14),
    Location("DRC - Tingle Chest in DRC Basement" , 0x3, True, False, False, -1, False, -1, False, 15),
    Location("DRC - Tingle Chest in DRC HUB", 0x3, True, False, False, -1, False, -1, False, 16),
    Location("DRC - Mini-Boss Fight", 0x3, True, False, False, -1, False, -1, False, 17),
    Location("DRC - Gohma Heart Container", 0x3, False, True, False, -1, False, -1, False, 21),
    
    #Stage 0x4 (Forbidden Woods) 16 FORMATTED
    Location("Forbidden Woods - 1st Chest"       , 0x4, True, False, False, -1, False, -1, False, 0),
    Location("Forbidden Woods - In Bottom Tree", 0x4, True, False, False, -1, False, -1, False, 1),
    Location("Forbidden Woods - Climb to Top", 0x4, True, False, False, -1, False, -1, False, 2),
    Location("Forbidden Woods - Past Hanging Vines"   , 0x4, True, False, False, -1, False, -1, False, 3),
    Location("Forbidden Woods - Big Key Chest"    , 0x4, True, False, False, -1, False, -1, False, 4),
    Location("Forbidden Woods - Vine Maze Right"  , 0x4, True, False, False, -1, False, -1, False, 5),
    Location("Forbidden Woods - Hole in Tree"    , 0x4, True, False, False, -1, False, -1, False, 6),
    Location("Forbidden Woods - Vine Maze Left"   , 0x4, True, False, False, -1, False, -1, False, 7),
    Location("Forbidden Woods - In Morths Pit"    , 0x4, True, False, False, -1, False, -1, False, 8),
    Location("Forbidden Woods - Locked in Basement Trunk"  , 0x4, True, False, False, -1, False, -1, False, 9),
    Location("Forbidden Woods - Mini-Boss"        , 0x4, True, False, False, -1, False, -1, False, 10),
    Location("Forbidden Woods - Across the Flower", 0x4, True, False, False, -1, False, -1, False, 11),
    Location("Forbidden Woods - Tall Room Before Mini-Boss", 0x4, True, False, False, -1, False, -1, False, 12),
    Location("Forbidden Woods - Double Mothula"   , 0x4, True, False, False, -1, False, -1, False, 14),
    Location("Forbidden Woods - Tingle Chest"     , 0x4, True, False, False, -1, False, -1, False, 15),
    Location("Forbidden Woods - Kalle Demos Heart Container"  , 0x4, False, True, False, -1, False, -1, False, 21),

    #Stage 0x5 (Tower of the Gods) 14 FORMATTED
    Location("Tower of Gods - Big Key Chest"   , 0x5, True, False, False, -1, False, -1, False, 0),
    Location("Tower of Gods - Hop Across Boxes", 0x5, True, False, False, -1, False, -1, False, 1),
    Location("Tower of Gods - Behind Bombable Wall" , 0x5, True, False, False, -1, False, -1, False, 2),
    Location("Tower of Gods - Skull Room", 0x5, True, False, False, -1, False, -1, False, 3),
    Location("Tower of Gods - Flying Platforms 1", 0x5, True, False, False, -1, False, -1, False, 4),
    Location("Tower of Gods - Mini-Boss"   , 0x5, True, False, False, -1, False, -1, False, 5),
    Location("Tower of Gods - First Chest Guarded" , 0x5, True, False, False, -1, False, -1, False, 6),
    Location("Tower of Gods - Second Chest Guarded" , 0x5, True, False, False, -1, False, -1, False, 8),
    Location("Tower of Gods - Stone Tablet" , 0x5, False, False, True,  1, False, -1, False, 9),
    Location("Tower of Gods - Skull Room Shoot The Eye", 0x5, True, False, False, -1, False, -1, False, 9),
    Location("Tower of Gods - Light Torches" , 0x5, True, False, False, -1, False, -1, False, 10),
    Location("Tower of Gods - Flying Platforms 2"  , 0x5, True, False, False, -1, False, -1, False, 11),
    Location("Tower of Gods - Tingle Chest"    , 0x5, True, False, False, -1, False, -1, False, 15),
    Location("Tower of Gods - Gohdan Heart Container", 0x5, False, True, False, -1, False, -1, False, 21),

    #Stage 0x6 (Earth Temple) 16 FORMATTED
    Location("Earth Temple - First Room"       , 0x6, True, False, False, -1, False, -1, False, 0),
    Location("Earth Temple - Transparent Chest in 1st Crypt", 0x6, True, False, False, -1, False, -1, False, 1),
    Location("Earth Temple - 3 Blocks Room"     , 0x6, True, False, False, -1, False, -1, False, 2),
    Location("Earth Temple - Behind Statues"   , 0x6, True, False, False, -1, False, -1, False, 3),
    Location("Earth Temple - Floormaster Room Free", 0x6, True, False, False, -1, False, -1, False, 4),
    Location("Earth Temple - 3rd Crypt Chest" , 0x6, True, False, False, -1, False, -1, False, 5),
    Location("Earth Temple - Big Key Chest"    , 0x6, True, False, False, -1, False, -1, False, 6),
    Location("Earth Temple - Staflos Mini Boss"        , 0x6, True, False, False, -1, False, -1, False, 7),
    Location("Earth Temple - Many Mirrors Left"     , 0x6, True, False, False, -1, False, -1, False, 9),
    Location("Earth Temple - Many Mirrors Right"    , 0x6, True, False, False, -1, False, -1, False, 10),
    Location("Earth Temple - Floormaster Room Fight", 0x6, True, False, False, -1, False, -1, False, 11),
    Location("Earth Temple - Behind Destructable Walls"  , 0x6, True, False, False, -1, False, -1, False, 12),
    Location("Earth Temple - Staflos Crypt Room"    , 0x6, True, False, False, -1, False, -1, False, 14),
    Location("Earth Temple - Casket in 2nd Crypt"     , 0x6, False, True, False, -1, False, -1, False, 14),
    Location("Earth Temple - Tingle Chest"     , 0x6, True, False, False, -1, False, -1, False, 15),
    Location("Earth Temple - Jalhalla Heart Container"  , 0x6, False, True, False, -1, False, -1, False, 21),

    #Stage 0x7 (Wind Temple) 14 FORMATTED
    Location("Wind Temple - Two Dirt Patches"         , 0x7, True, False, False, -1, False, -1, False, 0),
    Location("Wind Temple - Top of HUB Room"          , 0x7, True, False, False, -1, False, -1, False, 2),
    Location("Wind Temple - Behind Stone Head"        , 0x7, True, False, False, -1, False, -1, False, 3),
    Location("Wind Temple - Behind 7 Armos"           , 0x7, True, False, False, -1, False, -1, False, 4),
    Location("Wind Temple - Wizzrobe Mini Boss"       , 0x7, True, False, False, -1, False, -1, False, 5),
    Location("Wind Temple - Left Alcove"              , 0x7, True, False, False, -1, False, -1, False, 7),
    Location("Wind Temple - Big Key Chest"            , 0x7, True, False, False, -1, False, -1, False, 8),
    Location("Wind Temple - Spike Room - Free Chest"  , 0x7, True, False, False, -1, False, -1, False, 9),
    Location("Wind Temple - Spike Room - Break All Floors", 0x7, True, False, False, -1, False, -1, False, 10),
    Location("Wind Temple - Many Cyclones Room"       , 0x7, True, False, False, -1, False, -1, False, 11),
    Location("Wind Temple - Kill Enemies in Basement" , 0x7, True, False, False, -1, False, -1, False, 12),
    Location("Wind Temple - Middle of HUB Room"       , 0x7, True, False, False, -1, False, -1, False, 13),
    Location("Wind Temple - Tingle Chest"             , 0x7, True, False, False, -1, False, -1, False, 15),
    Location("Wind Temple - Molgera Heart Container"  , 0x7, False, True, False, -1, False, -1, False, 21),

    #Stage 0x8 (Ganon's Tower) FORMATTED
    Location("Ganons Tower - Maze Chest", 0x8, True, False, False, -1, False, -1, False, 0),

    #Stage 0x9 (Hyrule) 1 FORMATTED
    Location("Hyrule - Master Sword Chamber", 0x9, True, False, False, -1, False, -1, False, 0),

    #Stage 0xA (Submarines) 7 FORMATTED
    Location("6 Eye Reef - Submarine"      , 0xA, True, False, False, -1, False, -1, False, 0),
    Location("5 Star - Submarine"          , 0xA, True, False, False, -1, False, -1, False, 1),
    Location("Bomb Island - Submarine"     , 0xA, True, False, False, -1, False, -1, False, 2),
    Location("Flight Control - Submarine"  , 0xA, True, False, False, -1, False, -1, False, 3),
    Location("Headstone Island - Submarine", 0xA, True, False, False, -1, False, -1, False, 4),
    Location("Northern Fairy - Submarine"  , 0xA, True, False, False, -1, False, -1, False, 6),
    Location("Crescent Moon - Submarine"        , 0xA, True, False, False, -1, False, -1, False, 7),
    Location("Great Sea - Ghost Ship"      , 0xA, True, False, False, -1, False, -1, False, 23),

    #Stage 0xB (Houses & Misc Places) 10 FORMATTED
    Location("Windfall - Jail Maze"  , 0xB, True, False, False, -1, False, -1, False, 0),
    Location("Windfall - Lenzo Left" , 0xB, True, False, False, -1, False, -1, False, 1),
    Location("Windfall - Lenzo Right", 0xB, True, False, False, -1, False, -1, False, 2),
    Location("Forest Haven - On Tree Branch"  , 0xB, False, True, False, -1, False, -1, False, 2),
    Location("Windfall - House of Wealth Chest" , 0xB, True, False, False, -1, False, -1, False, 3), 
    Location("Outset - Grasscutter House", 0xB, True, False, False, -1, False, -1, False, 4),
    Location("Outset - Under Link's House" , 0xB, True, False, False, -1, False, -1, False, 5),
    Location("Windfall - Tingles Gift 1", 0xB, False, False, True,  0, False, -1, False, 5),
    Location("Outset - Jabun's Cave", 0xB, True, False, False, -1, False, -1, False, 6),
    Location("Windfall - Tingles Gift 2", 0xB, False, False, True,  0, False, -1, False, 6),

    #Stage 0xC (Cave Interiors & Fairies) 17 FORMATTED
    Location("Fire Mountain - Cave"      , 0xC, True, False, False, -1, False, -1, False, 0),
    Location("Ice Ring - Cave"      , 0xC, True, False, False, -1, False, -1, False, 1),
    Location("Pawprint - Chu Cave - Scale Wall", 0xC, True, False, False, -1, False, -1, False, 2),
    Location("Diamond Steppe - Warp Maze 2nd" , 0xC, True, False, False, -1, False, -1, False, 3),
    Location("Islet of Steel - Cave"     , 0xC, True, False, False, -1, False, -1, False, 4),
    Location("Bomb Island - Cave"  , 0xC, True, False, False, -1, False, -1, False, 5),
    Location("Star Island - Cave"  , 0xC, True, False, False, -1, False, -1, False, 6),
    Location("Cliff Plateau - Cave"  , 0xC, True, False, False, -1, False, -1, False, 7),
    Location("Rock Spire - Cave"     , 0xC, True, False, False, -1, False, -1, False, 8),
    Location("Stone Watcher - Cave"    , 0xC, True, False, False, -1, False, -1, False, 10),
    Location("Overlook - Cave"       , 0xC, True, False, False, -1, False, -1, False, 11),
    Location("Birds Peak Rock - Cave"   , 0xC, True, False, False, -1, False, -1, False, 16),
    Location("Cabana Labryinth - Upper" , 0xC, True, False, False, -1, False, -1, False, 17),
    Location("Ice Ring - Inner Cave", 0xC, True, False, False, -1, False, -1, False, 21),
    Location("Cabana Labryinth - Lower" , 0xC, True, False, False, -1, False, -1, False, 22),
    Location("Diamond Steppe - Warp Maze 1st" , 0xC, True, False, False, -1, False, -1, False, 23),
    Location("Pawprint - Chu Cave - Left Boulder"   , 0xC, True, False, False, -1, False, -1, False, 24),
    Location("Pawprint - Chu Cave - Right Boulder"  , 0xC, True, False, False, -1, False, -1, False, 25),
    Location("Pawprint - Chu Cave - Chest"          , 0xC, True, False, False, -1, False, -1, False, 26),

    #Stage 0xD (More Cave/Ship Interiors) 9
    Location("DRI - Secret Cave"        , 0xD, True, False, False, -1, False, -1, False, 0),
    Location("Horseshoe - Cave"         , 0xD, True, False, False, -1, False, -1, False, 1),
    Location("Pawprint - Wizzrobe Cave" , 0xD, True, False, False, -1, False, -1, False, 2),
    Location("Windfall - Pirate Ship Chest", 0xD, True, False, False, -1, False, -1, False, 5),
    Location("Angular - Cave"           , 0xD, True, False, False, -1, False, -1, False, 6),
    Location("Needle Rock - Cave"       , 0xD, True, False, False, -1, False, -1, False, 9),
    Location("Outset - Savage Labryinth Floor 30", 0xD, True, False, False, -1, False, -1, False, 11),
    Location("Outset - Savage Labryinth Floor 50", 0xD, True, False, False, -1, False, -1, False, 12),
    Location("Boating Course - Cave"    , 0xD, True, False, False, -1, False, -1, False, 15),
    Location("Shark Island - Cave"      , 0xD, True, False, False, -1, False, -1, False, 22),

    #Various locations 11 FORMATTED
    Location("Great Sea - Defeat Cyclos"    , 0x0, False, False, False, -1, False, -1, False, -1),
    Location("Great Sea - Withered Trees"   , 0x0, False, False, False, -1, False, -1, True, -1),
    Location("Expensive Beedle - 500 Item"  , 0xA, False, False, False, -1, False, -1, True, 5),
    Location("Expensive Beedle - 950 Item"  , 0xA, False, False, False, -1, False, -1, True, 4),
    Location("Expensive Beedle - 900 Item"  , 0xA, False, False, False, -1, False, -1, True, 3),
    Location("Outset - Give Orca 10 Knights Crest", 0xB, False, False, False, -1, False, -1, True, -1),
    Location("Windfall - Win Sploosh Kaboom Once" , 0xB, False, False, False, -1, False, -1, True, 1),
    Location("Windfall - Win Sploosh Kaboom Twice", 0xB, False, False, False, -1, False, -1, True, 2),
    Location("DRI - Mail Game"              , 0xB, False, False, False, -1, False, -1, True, 3),
    Location("Windfall - Green Potion Brewery", 0xB, False, False, False, -1, False, -1, True, 2),
    Location("Windfall - Blue Potion Brewery" , 0xB, False, False, False, -1, False, -1, True, 1),

    #Goals
    Location("Victory", 0x8, False, False, True, 0, False, -1, False, 16)
]


