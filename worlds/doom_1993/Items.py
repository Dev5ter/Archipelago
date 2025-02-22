# This file is auto generated. More info: https://github.com/Daivuk/apdoom

from BaseClasses import ItemClassification
from typing import TypedDict, Dict, Set 


class ItemDict(TypedDict, total=False): 
    classification: ItemClassification 
    count: int 
    name: str 
    doom_type: int # Unique numerical id used to spawn the item. -1 is level item, -2 is level complete item. 
    episode: int # Relevant if that item targets a specific level, like keycard or map reveal pickup. 
    map: int 


item_table: Dict[int, ItemDict] = {
    350000: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Hangar (E1M1)',
             'doom_type': -1,
             'episode': 1,
             'map': 1},
    350001: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Hangar (E1M1) - Computer area map',
             'doom_type': 2026,
             'episode': 1,
             'map': 1},
    350002: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Nuclear Plant (E1M2)',
             'doom_type': -1,
             'episode': 1,
             'map': 2},
    350003: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Nuclear Plant (E1M2) - Red keycard',
             'doom_type': 13,
             'episode': 1,
             'map': 2},
    350004: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Nuclear Plant (E1M2) - Computer area map',
             'doom_type': 2026,
             'episode': 1,
             'map': 2},
    350005: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Toxin Refinery (E1M3)',
             'doom_type': -1,
             'episode': 1,
             'map': 3},
    350006: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Toxin Refinery (E1M3) - Yellow keycard',
             'doom_type': 6,
             'episode': 1,
             'map': 3},
    350007: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Toxin Refinery (E1M3) - Blue keycard',
             'doom_type': 5,
             'episode': 1,
             'map': 3},
    350008: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Toxin Refinery (E1M3) - Computer area map',
             'doom_type': 2026,
             'episode': 1,
             'map': 3},
    350009: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Command Control (E1M4)',
             'doom_type': -1,
             'episode': 1,
             'map': 4},
    350010: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Command Control (E1M4) - Yellow keycard',
             'doom_type': 6,
             'episode': 1,
             'map': 4},
    350011: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Command Control (E1M4) - Blue keycard',
             'doom_type': 5,
             'episode': 1,
             'map': 4},
    350012: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Command Control (E1M4) - Computer area map',
             'doom_type': 2026,
             'episode': 1,
             'map': 4},
    350013: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Phobos Lab (E1M5)',
             'doom_type': -1,
             'episode': 1,
             'map': 5},
    350014: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Phobos Lab (E1M5) - Blue keycard',
             'doom_type': 5,
             'episode': 1,
             'map': 5},
    350015: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Phobos Lab (E1M5) - Yellow keycard',
             'doom_type': 6,
             'episode': 1,
             'map': 5},
    350016: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Phobos Lab (E1M5) - Computer area map',
             'doom_type': 2026,
             'episode': 1,
             'map': 5},
    350017: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Central Processing (E1M6)',
             'doom_type': -1,
             'episode': 1,
             'map': 6},
    350018: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Central Processing (E1M6) - Blue keycard',
             'doom_type': 5,
             'episode': 1,
             'map': 6},
    350019: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Central Processing (E1M6) - Red keycard',
             'doom_type': 13,
             'episode': 1,
             'map': 6},
    350020: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Central Processing (E1M6) - Yellow keycard',
             'doom_type': 6,
             'episode': 1,
             'map': 6},
    350021: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Central Processing (E1M6) - Computer area map',
             'doom_type': 2026,
             'episode': 1,
             'map': 6},
    350022: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Computer Station (E1M7)',
             'doom_type': -1,
             'episode': 1,
             'map': 7},
    350023: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Computer Station (E1M7) - Yellow keycard',
             'doom_type': 6,
             'episode': 1,
             'map': 7},
    350024: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Computer Station (E1M7) - Blue keycard',
             'doom_type': 5,
             'episode': 1,
             'map': 7},
    350025: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Computer Station (E1M7) - Red keycard',
             'doom_type': 13,
             'episode': 1,
             'map': 7},
    350026: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Computer Station (E1M7) - Computer area map',
             'doom_type': 2026,
             'episode': 1,
             'map': 7},
    350027: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Phobos Anomaly (E1M8)',
             'doom_type': -1,
             'episode': 1,
             'map': 8},
    350028: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Phobos Anomaly (E1M8) - Computer area map',
             'doom_type': 2026,
             'episode': 1,
             'map': 8},
    350029: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Military Base (E1M9)',
             'doom_type': -1,
             'episode': 1,
             'map': 9},
    350030: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Military Base (E1M9) - Yellow keycard',
             'doom_type': 6,
             'episode': 1,
             'map': 9},
    350031: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Military Base (E1M9) - Red keycard',
             'doom_type': 13,
             'episode': 1,
             'map': 9},
    350032: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Military Base (E1M9) - Blue keycard',
             'doom_type': 5,
             'episode': 1,
             'map': 9},
    350033: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Military Base (E1M9) - Computer area map',
             'doom_type': 2026,
             'episode': 1,
             'map': 9},
    350034: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Deimos Anomaly (E2M1)',
             'doom_type': -1,
             'episode': 2,
             'map': 1},
    350035: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Deimos Anomaly (E2M1) - Blue keycard',
             'doom_type': 5,
             'episode': 2,
             'map': 1},
    350036: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Deimos Anomaly (E2M1) - Red keycard',
             'doom_type': 13,
             'episode': 2,
             'map': 1},
    350037: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Deimos Anomaly (E2M1) - Computer area map',
             'doom_type': 2026,
             'episode': 2,
             'map': 1},
    350038: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Containment Area (E2M2)',
             'doom_type': -1,
             'episode': 2,
             'map': 2},
    350039: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Containment Area (E2M2) - Blue keycard',
             'doom_type': 5,
             'episode': 2,
             'map': 2},
    350040: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Containment Area (E2M2) - Yellow keycard',
             'doom_type': 6,
             'episode': 2,
             'map': 2},
    350041: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Containment Area (E2M2) - Red keycard',
             'doom_type': 13,
             'episode': 2,
             'map': 2},
    350042: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Containment Area (E2M2) - Computer area map',
             'doom_type': 2026,
             'episode': 2,
             'map': 2},
    350043: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Refinery (E2M3)',
             'doom_type': -1,
             'episode': 2,
             'map': 3},
    350044: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Refinery (E2M3) - Blue keycard',
             'doom_type': 5,
             'episode': 2,
             'map': 3},
    350045: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Refinery (E2M3) - Computer area map',
             'doom_type': 2026,
             'episode': 2,
             'map': 3},
    350046: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Deimos Lab (E2M4)',
             'doom_type': -1,
             'episode': 2,
             'map': 4},
    350047: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Deimos Lab (E2M4) - Blue keycard',
             'doom_type': 5,
             'episode': 2,
             'map': 4},
    350048: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Deimos Lab (E2M4) - Yellow keycard',
             'doom_type': 6,
             'episode': 2,
             'map': 4},
    350049: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Deimos Lab (E2M4) - Computer area map',
             'doom_type': 2026,
             'episode': 2,
             'map': 4},
    350050: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Command Center (E2M5)',
             'doom_type': -1,
             'episode': 2,
             'map': 5},
    350051: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Command Center (E2M5) - Computer area map',
             'doom_type': 2026,
             'episode': 2,
             'map': 5},
    350052: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Halls of the Damned (E2M6)',
             'doom_type': -1,
             'episode': 2,
             'map': 6},
    350053: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Halls of the Damned (E2M6) - Blue skull key',
             'doom_type': 40,
             'episode': 2,
             'map': 6},
    350054: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Halls of the Damned (E2M6) - Yellow skull key',
             'doom_type': 39,
             'episode': 2,
             'map': 6},
    350055: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Halls of the Damned (E2M6) - Red skull key',
             'doom_type': 38,
             'episode': 2,
             'map': 6},
    350056: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Halls of the Damned (E2M6) - Computer area map',
             'doom_type': 2026,
             'episode': 2,
             'map': 6},
    350057: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Spawning Vats (E2M7)',
             'doom_type': -1,
             'episode': 2,
             'map': 7},
    350058: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Spawning Vats (E2M7) - Red keycard',
             'doom_type': 13,
             'episode': 2,
             'map': 7},
    350059: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Spawning Vats (E2M7) - Yellow keycard',
             'doom_type': 6,
             'episode': 2,
             'map': 7},
    350060: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Spawning Vats (E2M7) - Blue keycard',
             'doom_type': 5,
             'episode': 2,
             'map': 7},
    350061: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Spawning Vats (E2M7) - Computer area map',
             'doom_type': 2026,
             'episode': 2,
             'map': 7},
    350062: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Tower of Babel (E2M8)',
             'doom_type': -1,
             'episode': 2,
             'map': 8},
    350063: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Tower of Babel (E2M8) - Computer area map',
             'doom_type': 2026,
             'episode': 2,
             'map': 8},
    350064: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Fortress of Mystery (E2M9)',
             'doom_type': -1,
             'episode': 2,
             'map': 9},
    350065: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Fortress of Mystery (E2M9) - Blue skull key',
             'doom_type': 40,
             'episode': 2,
             'map': 9},
    350066: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Fortress of Mystery (E2M9) - Red skull key',
             'doom_type': 38,
             'episode': 2,
             'map': 9},
    350067: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Fortress of Mystery (E2M9) - Yellow skull key',
             'doom_type': 39,
             'episode': 2,
             'map': 9},
    350068: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Fortress of Mystery (E2M9) - Computer area map',
             'doom_type': 2026,
             'episode': 2,
             'map': 9},
    350069: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Hell Keep (E3M1)',
             'doom_type': -1,
             'episode': 3,
             'map': 1},
    350070: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Hell Keep (E3M1) - Computer area map',
             'doom_type': 2026,
             'episode': 3,
             'map': 1},
    350071: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Slough of Despair (E3M2)',
             'doom_type': -1,
             'episode': 3,
             'map': 2},
    350072: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Slough of Despair (E3M2) - Blue skull key',
             'doom_type': 40,
             'episode': 3,
             'map': 2},
    350073: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Slough of Despair (E3M2) - Computer area map',
             'doom_type': 2026,
             'episode': 3,
             'map': 2},
    350074: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Pandemonium (E3M3)',
             'doom_type': -1,
             'episode': 3,
             'map': 3},
    350075: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Pandemonium (E3M3) - Blue skull key',
             'doom_type': 40,
             'episode': 3,
             'map': 3},
    350076: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Pandemonium (E3M3) - Computer area map',
             'doom_type': 2026,
             'episode': 3,
             'map': 3},
    350077: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'House of Pain (E3M4)',
             'doom_type': -1,
             'episode': 3,
             'map': 4},
    350078: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'House of Pain (E3M4) - Blue skull key',
             'doom_type': 40,
             'episode': 3,
             'map': 4},
    350079: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'House of Pain (E3M4) - Yellow skull key',
             'doom_type': 39,
             'episode': 3,
             'map': 4},
    350080: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'House of Pain (E3M4) - Red skull key',
             'doom_type': 38,
             'episode': 3,
             'map': 4},
    350081: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'House of Pain (E3M4) - Computer area map',
             'doom_type': 2026,
             'episode': 3,
             'map': 4},
    350082: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Unholy Cathedral (E3M5)',
             'doom_type': -1,
             'episode': 3,
             'map': 5},
    350083: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Unholy Cathedral (E3M5) - Blue skull key',
             'doom_type': 40,
             'episode': 3,
             'map': 5},
    350084: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Unholy Cathedral (E3M5) - Yellow skull key',
             'doom_type': 39,
             'episode': 3,
             'map': 5},
    350085: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Unholy Cathedral (E3M5) - Computer area map',
             'doom_type': 2026,
             'episode': 3,
             'map': 5},
    350086: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Mt. Erebus (E3M6)',
             'doom_type': -1,
             'episode': 3,
             'map': 6},
    350087: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Mt. Erebus (E3M6) - Blue skull key',
             'doom_type': 40,
             'episode': 3,
             'map': 6},
    350088: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Mt. Erebus (E3M6) - Computer area map',
             'doom_type': 2026,
             'episode': 3,
             'map': 6},
    350089: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Limbo (E3M7)',
             'doom_type': -1,
             'episode': 3,
             'map': 7},
    350090: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Limbo (E3M7) - Blue skull key',
             'doom_type': 40,
             'episode': 3,
             'map': 7},
    350091: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Limbo (E3M7) - Red skull key',
             'doom_type': 38,
             'episode': 3,
             'map': 7},
    350092: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Limbo (E3M7) - Yellow skull key',
             'doom_type': 39,
             'episode': 3,
             'map': 7},
    350093: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Limbo (E3M7) - Computer area map',
             'doom_type': 2026,
             'episode': 3,
             'map': 7},
    350094: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Dis (E3M8)',
             'doom_type': -1,
             'episode': 3,
             'map': 8},
    350095: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Dis (E3M8) - Computer area map',
             'doom_type': 2026,
             'episode': 3,
             'map': 8},
    350096: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Warrens (E3M9)',
             'doom_type': -1,
             'episode': 3,
             'map': 9},
    350097: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Warrens (E3M9) - Blue skull key',
             'doom_type': 40,
             'episode': 3,
             'map': 9},
    350098: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Warrens (E3M9) - Red skull key',
             'doom_type': 38,
             'episode': 3,
             'map': 9},
    350099: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Warrens (E3M9) - Computer area map',
             'doom_type': 2026,
             'episode': 3,
             'map': 9},
    350100: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Shotgun',
             'doom_type': 2001,
             'episode': -1,
             'map': -1},
    350101: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Rocket launcher',
             'doom_type': 2003,
             'episode': -1,
             'map': -1},
    350102: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Plasma gun',
             'doom_type': 2004,
             'episode': -1,
             'map': -1},
    350103: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Chainsaw',
             'doom_type': 2005,
             'episode': -1,
             'map': -1},
    350104: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Chaingun',
             'doom_type': 2002,
             'episode': -1,
             'map': -1},
    350105: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'BFG9000',
             'doom_type': 2006,
             'episode': -1,
             'map': -1},
    350106: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Backpack',
             'doom_type': 8,
             'episode': -1,
             'map': -1},
    350107: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Armor',
             'doom_type': 2018,
             'episode': -1,
             'map': -1},
    350108: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Mega Armor',
             'doom_type': 2019,
             'episode': -1,
             'map': -1},
    350109: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Berserk',
             'doom_type': 2023,
             'episode': -1,
             'map': -1},
    350110: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Invulnerability',
             'doom_type': 2022,
             'episode': -1,
             'map': -1},
    350111: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Partial invisibility',
             'doom_type': 2024,
             'episode': -1,
             'map': -1},
    350112: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Supercharge',
             'doom_type': 2013,
             'episode': -1,
             'map': -1},
    350113: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Medikit',
             'doom_type': 2012,
             'episode': -1,
             'map': -1},
    350114: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Box of bullets',
             'doom_type': 2048,
             'episode': -1,
             'map': -1},
    350115: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Box of rockets',
             'doom_type': 2046,
             'episode': -1,
             'map': -1},
    350116: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Box of shotgun shells',
             'doom_type': 2049,
             'episode': -1,
             'map': -1},
    350117: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Energy cell pack',
             'doom_type': 17,
             'episode': -1,
             'map': -1},
    350118: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Hangar (E1M1) - Complete',
             'doom_type': -2,
             'episode': 1,
             'map': 1},
    350119: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Nuclear Plant (E1M2) - Complete',
             'doom_type': -2,
             'episode': 1,
             'map': 2},
    350120: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Toxin Refinery (E1M3) - Complete',
             'doom_type': -2,
             'episode': 1,
             'map': 3},
    350121: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Command Control (E1M4) - Complete',
             'doom_type': -2,
             'episode': 1,
             'map': 4},
    350122: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Phobos Lab (E1M5) - Complete',
             'doom_type': -2,
             'episode': 1,
             'map': 5},
    350123: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Central Processing (E1M6) - Complete',
             'doom_type': -2,
             'episode': 1,
             'map': 6},
    350124: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Computer Station (E1M7) - Complete',
             'doom_type': -2,
             'episode': 1,
             'map': 7},
    350125: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Phobos Anomaly (E1M8) - Complete',
             'doom_type': -2,
             'episode': 1,
             'map': 8},
    350126: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Military Base (E1M9) - Complete',
             'doom_type': -2,
             'episode': 1,
             'map': 9},
    350127: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Deimos Anomaly (E2M1) - Complete',
             'doom_type': -2,
             'episode': 2,
             'map': 1},
    350128: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Containment Area (E2M2) - Complete',
             'doom_type': -2,
             'episode': 2,
             'map': 2},
    350129: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Refinery (E2M3) - Complete',
             'doom_type': -2,
             'episode': 2,
             'map': 3},
    350130: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Deimos Lab (E2M4) - Complete',
             'doom_type': -2,
             'episode': 2,
             'map': 4},
    350131: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Command Center (E2M5) - Complete',
             'doom_type': -2,
             'episode': 2,
             'map': 5},
    350132: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Halls of the Damned (E2M6) - Complete',
             'doom_type': -2,
             'episode': 2,
             'map': 6},
    350133: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Spawning Vats (E2M7) - Complete',
             'doom_type': -2,
             'episode': 2,
             'map': 7},
    350134: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Tower of Babel (E2M8) - Complete',
             'doom_type': -2,
             'episode': 2,
             'map': 8},
    350135: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Fortress of Mystery (E2M9) - Complete',
             'doom_type': -2,
             'episode': 2,
             'map': 9},
    350136: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Hell Keep (E3M1) - Complete',
             'doom_type': -2,
             'episode': 3,
             'map': 1},
    350137: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Slough of Despair (E3M2) - Complete',
             'doom_type': -2,
             'episode': 3,
             'map': 2},
    350138: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Pandemonium (E3M3) - Complete',
             'doom_type': -2,
             'episode': 3,
             'map': 3},
    350139: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'House of Pain (E3M4) - Complete',
             'doom_type': -2,
             'episode': 3,
             'map': 4},
    350140: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Unholy Cathedral (E3M5) - Complete',
             'doom_type': -2,
             'episode': 3,
             'map': 5},
    350141: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Mt. Erebus (E3M6) - Complete',
             'doom_type': -2,
             'episode': 3,
             'map': 6},
    350142: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Limbo (E3M7) - Complete',
             'doom_type': -2,
             'episode': 3,
             'map': 7},
    350143: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Dis (E3M8) - Complete',
             'doom_type': -2,
             'episode': 3,
             'map': 8},
    350144: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Warrens (E3M9) - Complete',
             'doom_type': -2,
             'episode': 3,
             'map': 9},
}


item_name_groups: Dict[str, Set[str]] = {
    'Ammos': {'Box of bullets', 'Box of rockets', 'Box of shotgun shells', 'Energy cell pack', },
    'Keys': {'Central Processing (E1M6) - Blue keycard', 'Central Processing (E1M6) - Red keycard', 'Central Processing (E1M6) - Yellow keycard', 'Command Control (E1M4) - Blue keycard', 'Command Control (E1M4) - Yellow keycard', 'Computer Station (E1M7) - Blue keycard', 'Computer Station (E1M7) - Red keycard', 'Computer Station (E1M7) - Yellow keycard', 'Containment Area (E2M2) - Blue keycard', 'Containment Area (E2M2) - Red keycard', 'Containment Area (E2M2) - Yellow keycard', 'Deimos Anomaly (E2M1) - Blue keycard', 'Deimos Anomaly (E2M1) - Red keycard', 'Deimos Lab (E2M4) - Blue keycard', 'Deimos Lab (E2M4) - Yellow keycard', 'Fortress of Mystery (E2M9) - Blue skull key', 'Fortress of Mystery (E2M9) - Red skull key', 'Fortress of Mystery (E2M9) - Yellow skull key', 'Halls of the Damned (E2M6) - Blue skull key', 'Halls of the Damned (E2M6) - Red skull key', 'Halls of the Damned (E2M6) - Yellow skull key', 'House of Pain (E3M4) - Blue skull key', 'House of Pain (E3M4) - Red skull key', 'House of Pain (E3M4) - Yellow skull key', 'Limbo (E3M7) - Blue skull key', 'Limbo (E3M7) - Red skull key', 'Limbo (E3M7) - Yellow skull key', 'Military Base (E1M9) - Blue keycard', 'Military Base (E1M9) - Red keycard', 'Military Base (E1M9) - Yellow keycard', 'Mt. Erebus (E3M6) - Blue skull key', 'Nuclear Plant (E1M2) - Red keycard', 'Pandemonium (E3M3) - Blue skull key', 'Phobos Lab (E1M5) - Blue keycard', 'Phobos Lab (E1M5) - Yellow keycard', 'Refinery (E2M3) - Blue keycard', 'Slough of Despair (E3M2) - Blue skull key', 'Spawning Vats (E2M7) - Blue keycard', 'Spawning Vats (E2M7) - Red keycard', 'Spawning Vats (E2M7) - Yellow keycard', 'Toxin Refinery (E1M3) - Blue keycard', 'Toxin Refinery (E1M3) - Yellow keycard', 'Unholy Cathedral (E3M5) - Blue skull key', 'Unholy Cathedral (E3M5) - Yellow skull key', 'Warrens (E3M9) - Blue skull key', 'Warrens (E3M9) - Red skull key', },
    'Levels': {'Central Processing (E1M6)', 'Command Center (E2M5)', 'Command Control (E1M4)', 'Computer Station (E1M7)', 'Containment Area (E2M2)', 'Deimos Anomaly (E2M1)', 'Deimos Lab (E2M4)', 'Dis (E3M8)', 'Fortress of Mystery (E2M9)', 'Halls of the Damned (E2M6)', 'Hangar (E1M1)', 'Hell Keep (E3M1)', 'House of Pain (E3M4)', 'Limbo (E3M7)', 'Military Base (E1M9)', 'Mt. Erebus (E3M6)', 'Nuclear Plant (E1M2)', 'Pandemonium (E3M3)', 'Phobos Anomaly (E1M8)', 'Phobos Lab (E1M5)', 'Refinery (E2M3)', 'Slough of Despair (E3M2)', 'Spawning Vats (E2M7)', 'Tower of Babel (E2M8)', 'Toxin Refinery (E1M3)', 'Unholy Cathedral (E3M5)', 'Warrens (E3M9)', },
    'Powerups': {'Armor', 'Berserk', 'Invulnerability', 'Mega Armor', 'Partial invisibility', 'Supercharge', },
    'Weapons': {'BFG9000', 'Chaingun', 'Chainsaw', 'Plasma gun', 'Rocket launcher', 'Shotgun', },
}
