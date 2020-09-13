org $279700
KeyDoorOffset:
;      0     1     2     3     4     5     6     7     8     9     a     b     c     d     e     f --Offset Ruler
dw $0000,$0001,$0003,$0000,$0006,$0000,$000b,$0000,$0000,$0000,$000c,$000d,$0010,$0011,$0012,$0000
dw $0000,$0015,$0018,$001c,$001e,$0025,$0027,$0000,$0000,$002b,$002d,$0033,$0035,$0038,$0039,$003d
dw $003f,$0040,$0043,$0045,$0047,$0000,$004f,$0000,$0053,$0000,$0055,$005b,$0000,$0000,$005f,$0000
dw $0060,$0062,$0064,$0065,$0066,$0068,$006e,$0074,$007a,$007c,$007e,$0081,$0000,$0082,$0086,$0088
dw $0089,$008a,$0000,$008b,$008e,$0092,$0096,$0000,$0000,$0099,$009d,$00a2,$00a5,$00a6,$00a8,$00aa
dw $00ab,$00ad,$00af,$00b2,$0000,$0000,$00b5,$00b9,$00bf,$00c5,$00c9,$00ca,$00cc,$00ce,$00d1,$00d5
dw $00d6,$00dc,$00e3,$00e9,$00ec,$00ed,$00ee,$00f2,$00f5,$0000,$00f7,$00f8,$00fc,$00ff,$0102,$0000
dw $0000,$0103,$0106,$0107,$010a,$010c,$010e,$0112,$0000,$0000,$0000,$0114,$0117,$011b,$011e,$0121
dw $0000,$0123,$0000,$0124,$0127,$0128,$0000,$012c,$0000,$0000,$0000,$012e,$0133,$0139,$013e,$0000
dw $013f,$0140,$0141,$0146,$0000,$0149,$014b,$014d,$014f,$0150,$0000,$0153,$0156,$015a,$015d,$0161
dw $0163,$0164,$0166,$016a,$016c,$016d,$0000,$0000,$0170,$0176,$017c,$0182,$0184,$0000,$0185,$0186
dw $0188,$018b,$018f,$0197,$019c,$019d,$019e,$01a3,$01a4,$01a6,$01aa,$01ad,$01b3,$0000,$01bb,$01be
dw $01bf,$01c2,$01ca,$01d2,$01d9,$01da,$01dd,$01e3,$01e6,$01e7,$0000,$01ec,$01ed,$0000,$01f0,$0000
dw $01f1,$01f3,$01f7,$0000,$0000,$01f8,$01fa,$0000,$01fd,$0200,$0203,$0204,$0206,$0000,$0000,$0000
dw $0207


org $279E00
SpiralOffset:
;    0   1   2   3   4   5   6   7   8   9   a   b   c   d   e   f --Offset Ruler
db $00,$01,$02,$00,$03,$00,$00,$04,$00,$05,$07,$00,$08,$00,$0b,$00
db $00,$0c,$00,$00,$00,$0d,$0e,$0f,$00,$00,$11,$00,$13,$14,$15,$00
db $00,$00,$00,$00,$00,$00,$16,$19,$1b,$00,$00,$00,$00,$00,$00,$00
db $00,$1c,$00,$00,$1f,$00,$00,$00,$20,$00,$21,$00,$00,$00,$00,$22
db $23,$24,$25,$00,$00,$26,$00,$00,$00,$00,$27,$00,$29,$2a,$2b,$00
db $00,$00,$00,$2c,$2d,$00,$00,$00,$00,$00,$00,$00,$2e,$2f,$00,$30
db $00,$00,$00,$35,$36,$00,$37,$00,$00,$00,$38,$3a,$3b,$00,$3c,$00
db $3d,$40,$41,$00,$00,$00,$42,$45,$00,$00,$00,$00,$00,$00,$00,$49
db $4a,$00,$00,$00,$00,$00,$00,$4b,$00,$00,$00,$00,$4f,$00,$53,$00
db $00,$54,$00,$55,$00,$00,$00,$56,$57,$58,$00,$00,$00,$00,$59,$00
db $5a,$00,$5b,$00,$00,$5c,$5d,$00,$00,$00,$00,$5e,$00,$00,$5f,$00
db $60,$00,$00,$00,$00,$63,$64,$00,$00,$00,$00,$00,$65,$00,$66,$00
db $67,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00
db $6a,$6d,$6e,$00,$00,$00,$00,$00,$00,$00,$6f,$00,$00,$00,$00,$00
db $70

org $279F00
DoorOffset:
db $00,$01,$02,$00,$03,$00,$04,$00,$00,$00,$00,$00,$9A,$05,$99,$00
db $00,$06,$07,$08,$09,$0A,$0B,$00,$00,$0C,$0D,$0E,$00,$0F,$10,$11
db $12,$13,$14,$15,$16,$00,$17,$00,$98,$00,$18,$19,$00,$00,$1A,$00
db $1B,$00,$1C,$1D,$1E,$1F,$20,$21,$22,$23,$24,$25,$00,$26,$27,$00
db $96,$28,$97,$29,$2A,$2B,$2C,$00,$00,$2D,$2E,$2F,$30,$31,$32,$00
db $33,$34,$35,$36,$00,$00,$37,$38,$39,$3A,$3B,$3C,$3D,$3E,$3F,$40
db $41,$42,$43,$A0,$00,$00,$44,$45,$46,$00,$47,$48,$49,$4A,$4B,$00
;    0   1   2   3   4   5   6   7   8   9   a   b   c   d   e   f --Offset Ruler
db $00,$4C,$00,$00,$00,$4D,$4E,$9E,$00,$00,$00,$4F,$50,$51,$52,$53
db $00,$54,$00,$9C,$9D,$55,$00,$00,$00,$00,$00,$56,$57,$58,$59,$00
db $5A,$5B,$5C,$5D,$00,$5E,$5F,$00,$9B,$60,$00,$61,$62,$63,$64,$65
db $66,$67,$68,$69,$6A,$6B,$00,$00,$6C,$6D,$6E,$6F,$70,$00,$71,$72
db $00,$73,$74,$75,$76,$77,$78,$79,$7A,$7B,$7C,$7D,$7E,$00,$7F,$80
db $00,$81,$82,$83,$84,$85,$86,$87,$88,$89,$00,$8A,$8B,$00,$8C,$00
db $00,$8D,$8E,$00,$00,$8F,$90,$00,$91,$92,$93,$94,$95,$00,$00,$00
db $9f

org $27A000
DoorTable:
;; NW 00  N  01  N  02  WN 00  W  01  WS 02  SW 00  S  01  SE 02  EN 00  E  01  ES 02 - Door ruler
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Default/Garbage row
dw $0003, $0003, $0003, $0450, $0003, $0003, $0003, $0003, $0003, $0452, $0003, $0003 ; HC Back Hall (x01)
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Sewer Switches (x02)
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Crystaroller
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Arghus
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Aga 2
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Sewer Secret Room
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Sanc
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; TR Pokey
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; TR Lava Pipe
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; TR Pipes n Ledge
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Swap Canal
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Pod dark Maze
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Pod Bridge
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Pod Eye Statue
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; GT Pre Aga
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Ice Cross
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Ice BK
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; x20 Aga1
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Sewer Key Rat
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Sewer Waters
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; TR Eye Entrance
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; TR Chest Entrance
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Swamp Statue
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; PoD Arena (x2a)
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; PoD Statue (x2b)
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Ice Compass
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; x30 Aga's Altar
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Dark Cross
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Lanmolas
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Swamp West Wing
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Flooded Key
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Swamp Main Hub (x36)
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Swamp Hammer Time
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Swamp First Basement
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Drop to the Moth
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Pod 3 Catwalks
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Pod Conveyor
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; GT Minihelma
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Ice Conveyor
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Sewers
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Desert Torches
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; TT Big Chest
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; TT Cellblock
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Swamp Compass Loop
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Skull3 Torches
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Pod Entrance
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Pod Mimics 1
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; GT Conveyor Ice
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; GT Moldorm
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; IPBJ
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0401, $0003, $0003 ; HC West Hall (x50)
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; HC Throne Room (x51)
dw $0003, $0003, $0003, $0401, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; HC East Hall (x52)
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Desert Tiles 1
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Skull 2 Left Entrance
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Skull 2 Right Entrance
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Skull 1 Entrance
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Skull 3 Entrance
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Helmasaur
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; GT Spike Switch
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; GT Cannonball
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Gauntlet 1
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Ice Choice Cross
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Iced U
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; HC West Lobby (x60)
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; HC Main Lobby (x61)
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; HC East Lobby (x62)
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; x66 Swamp Waterfall
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; x67 Skull 1 Left Drop
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; x68 Skull 1 Pinball
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; x6a Pod Rupees
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; x6b GT Mimics
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; x6c GT Lanmolas
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; x6d Gauntlet 2
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; x6e Ice Gators
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; HC Armory
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Desert BK Chest
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Swamp Flooded Chests
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; GT DM's Tile
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; GT Randoroom
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; GT Warp Maze
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Ice Freezors
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Ice Hookpit
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; HC Catawalk
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Desert Right Entrance
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; GT Left
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; GT Hopeful Torch
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; GT Right
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Ice Lonely Freezor
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Vitreous (x90)
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Mire Rain
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Mire Dark Crystals
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Mire Blockswitch
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; GT Fallbridge
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; GT Torch Cross
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Eastern Darkness
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; GT Warp Maze 2
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; GT Invis Bridge
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; GT Compass Room
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Ice Big Chests
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Icy Pots
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Mire Pre-Vitreous (xa0)
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Mire Fishbone
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Mire Bridges
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Mire Corner
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Trinexx (xa4)
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; GT Wizzrobes
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Eastern Compass (xa8)
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Eastern Courtyard (xa9)
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Eastern Map (xaa)
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; TT Switch
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Blind
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Iced T
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Ice Slipway
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Mire Warpzone
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Mire ????
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Mire Spikes
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; TR Refill
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; TR Dark Maze
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; TR Chainchomp
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; TR Rollers
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Eastern Big Key
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Easter Cannonball
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Eastern Dark Circle
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; TT Hellway
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; TT Bossway
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Ice Blockswitch
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Ice Backtracker
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Mire Tiles
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Mire Main Hub
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Mire Big Chest
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; TR Switch Maze
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; TR Narrow
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; TR Early Hub
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; TR Floating Torches
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Armos
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Eastern Entrance
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; TT NW Quad
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; TT NE Quad
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Ice Boss Drop
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Mire BK
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Mire 2
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; TR Laser Bridge
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; TR Main Entrance
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Eastern Eyegores
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Eastern Attic Switches
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Eastern Attic Start
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; TT Entrance Quad
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; TT SE Quad
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Aga 6F
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Sewers Rope
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Swamp Lobby
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Ice Lobby
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; GT Lobby
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Mire Lobby
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Desert West Lobby
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Desert Main Lobby
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Hera Lobby
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Tower Lobby
dw $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003, $0003 ; Desert Back Lobby
; this should end at 27AF18 about (160 * 24 bytes =  3840 or F18)
; some values you can hardcode for spirals
;dw $0070, $36a0 ; ->HC Stairwell
;dw $0072, $4ff8 ; ->HC Map Room
;dw $0080, $1f50 ; ->zelda's cellblock

org $27B000
SpiralTable: ;113 4 byte entries - should end at 27B44C
dw $0203, $8080 ;null row
dw $0203, $8080 ;HC Backhallway
dw $0203, $8080 ;Sewer Pull
dw $0203, $8080 ;Crystaroller
dw $0203, $8080 ;Moldorm
dw $0203, $8080, $0203, $8080 ;Pod Basement
dw $0203, $8080 ;Pod Stalfos
dw $0203, $8080, $0203, $8080, $0203, $8080 ;GT Entrance
dw $0203, $8080 ;Ice Entrance
dw $0203, $8080 ;Escape
dw $0203, $8080 ;TR Pipe Ledge
dw $0203, $8080 ;Swamp Way
dw $0203, $8080, $0203, $8080 ;Hera Fallplace
dw $0203, $8080, $0203, $8080 ;PoD Bridge
dw $0203, $8080 ;GT Ice
dw $0203, $8080 ;GT F8
dw $0203, $8080 ;Ice Cross
dw $0203, $8080, $0203, $8080, $0203, $8080 ;Swamp Statue
dw $0203, $8080, $0203, $8080 ;Hera Big
dw $0203, $8080 ;Swamp Ent
dw $0203, $8080, $0203, $8080, $0203, $8080 ;Hera Startiles (middle value unused)
dw $0203, $8080 ;West Swamp
dw $0203, $8080 ;Swamp Basement
dw $0203, $8080 ;Pod Drops
dw $0203, $8080 ;Ice Hammer
dw $0203, $8080 ;Aga Guards
dw $0203, $8080 ;Sewer Begin
dw $0203, $8080 ;Sewer Rope
dw $0203, $8080 ;TT Cellblock
dw $0203, $8080, $0203, $8080 ;Pod Entrance
dw $0203, $8080 ;GT Icespike
dw $0203, $8080 ;GT Moldorm
dw $0203, $8080 ;IPBJ
dw $0203, $8080 ;Desert Prep
dw $0203, $8080 ;Swamp Attic
dw $0203, $8080 ;GT Cannonball
dw $0203, $8080 ;GT Gauntlet1
dw $0203, $8080, $0203, $8080, $0203, $8080, $0203, $8080, $0203, $8080 ;Ice U (1st three values unused)
dw $0203, $8080 ;Desert Back
dw $0203, $8080 ;TT Attic L
dw $0203, $8080 ;Swamp Waterf
dw $0203, $8080 ;Pod Rupees
dw $0203, $8080 ;Pod Rupees
dw $0203, $8080 ;GT Mimics
dw $0203, $8080 ;GT Lanmo
dw $0203, $8080 ;Ice Gators
dw $0203, $8080, $0203, $8080, $0203, $8080 ;HC Tiny (first value placeholder)
dw $0203, $8080 ;HC Boomer
dw $0203, $8080 ;HC Pits1
dw $0203, $8080, $0203, $8080, $0203, $8080 ;Swamp Sunken
dw $0203, $8080, $0203, $8080, $0203, $8080, $0203, $8080 ;Hera Entrance (first value unused)
dw $0203, $8080 ;Ice Hookshot
dw $0203, $8080 ;HC Cellblock
dw $0203, $8080, $0203, $8080, $0203, $8080, $0203, $8080 ;Hera Basement (first and third values unused)
dw $0203, $8080, $0203, $8080, $0203, $8080, $0203, $8080 ;GT Circle (third value unused)
dw $0203, $8080 ;Ice Last Freeze
dw $0203, $8080 ;Mire Drops
dw $0203, $8080 ;Mire Block
dw $0203, $8080 ;Mire Attic
dw $0203, $8080 ;Mire Entrance
dw $0203, $8080 ;East Dark
dw $0203, $8080 ;Ice Big
dw $0203, $8080 ;Mire Previtreous
dw $0203, $8080 ;Mire Bridges
dw $0203, $8080 ;GT Wizzrobes
dw $0203, $8080 ;GT Spikepit
dw $0203, $8080 ;TT Switch
dw $0203, $8080 ;Ice T
dw $0203, $8080, $0203, $8080, $0203, $8080 ;Tower Usains (2nd value unused)
dw $0203, $8080 ;TR PlatMaze
dw $0203, $8080 ;TR Chainchomp
dw $0203, $8080 ;TT Bossway
dw $0203, $8080 ;Ice FallZone
dw $0203, $8080, $0203, $8080, $0203, $8080 ;Tower Dark2 (2nd value unused)
dw $0203, $8080, $0203, $8080, $0203, $8080 ;Tower Dark1 (2nd value unused)
dw $0203, $8080 ;Mire BK Thang
dw $0203, $8080 ;Mire2
dw $0203, $8080 ;East Attic Start
dw $0203, $8080 ;Tower Entrance


org $27C000 ;ends around 27C418
PairedDoorTable:
dw $0000 ; the bad template
dw $0000,$0000
dw $0000,$0000,$0000
dw $0000,$0000,$0000,$0000,$0000
dw $0000
dw $0000
dw $0000,$0000,$0000
dw $0000
dw $0000
dw $0000,$0000,$0000

dw $0000,$0000,$8021
dw $0000,$0000,$0000,$0000
dw $4014,$0000
dw $8024,$8013,$0000,$0000,$0000,$0000,$0000
dw $0000,$0000
dw $0000,$0000,$0000,$0000
dw $201a,$401a
dw $0000,$4019,$8019,$402a,$0000,$0000
dw $0000,$0000
dw $0000,$0000,$0000
dw $0000
dw $0000,$0000,$0000,$0000
dw $0000,$0000

dw $0000
dw $2011,$0000,$0000
dw $8032,$0000
dw $0000,$0000
dw $8014,$0000,$0000,$0000,$0000,$0000,$0000,$0000
dw $4036,$0000,$0000,$0000
dw $0000,$0000
dw $0000,$101a,$402b,$0000,$0000,$0000
dw $0000,$202a,$0000,$0000
dw $0000

dw $0000,$0000
dw $0000,$0000
dw $8022
dw $0000
dw $0000,$0000
dw $2036,$0000,$0000,$0000,$0000,$0000
dw $8037,$8026,$8035,$0000,$0000,$0000
dw $8036,$8038,$0000,$4038,$0000,$0000
dw $4037,$1037
dw $0000,$0000
dw $204a,$0000,$0000
dw $0000
dw $0000,$0000,$804d,$0000
dw $0000,$404e
dw $0000

dw $0000
dw $0000
dw $0000,$0000,$2053
dw $0000,$0000,$0000,$0000
dw $0000,$0000,$0000,$0000
dw $0000,$0000,$0000
dw $0000,$0000,$8059,$0000
dw $0000,$0000,$803a,$0000,$0000
dw $0000,$0000,$0000
dw $0000
dw $203d,$0000
dw $0000,$403e
dw $0000 ; this is the odd extra room - shouldn't be used

dw $0000,$0000
dw $0000,$0000
dw $0000,$0000,$0000
dw $0000,$0000,$2043
dw $0000,$0000,$0000,$0000
dw $0000,$0000,$4058,$0000,$0000,$0000
dw $0000,$2057,$4068,$0000,$0000,$0000
dw $2049,$0000,$0000,$0000
dw $0000
dw $806b,$0000
dw $0000,$0000
dw $0000,$0000,$0000
dw $805f,$0000,$0000,$0000
dw $805e

dw $0000,$0000,$0000,$0000,$0000,$0000
dw $0000,$0000,$0000,$0000,$0000,$0000,$0000
dw $0000,$0000,$0000,$0000,$0000,$0000
dw $0000,$0000,$0000
dw $0000
dw $0000
dw $0000,$0000,$0000,$0000
dw $0000,$0000,$0000
dw $0000,$2058
dw $0000
dw $805b,$0000,$0000,$0000
dw $0000,$0000,$0000
dw $0000,$0000,$0000
dw $0000

dw $0000,$0000,$0000
dw $0000
dw $0000,$0000,$0000
dw $0000,$0000
dw $0000,$0000
dw $0000,$0000,$0000,$0000
dw $0000,$0000
dw $0000,$207c,$0000
dw $0000,$407d,$407b,$0000
dw $0000,$407c,$0000
dw $808e,$0000,$0000
dw $0000,$0000

dw $0000
dw $0000,$0000,$0000
dw $0000
dw $0000,$0000,$0000,$0000
dw $0000,$0000
dw $0000,$0000,$0000,$0000,$0000
dw $0000,$0000,$0000,$0000,$0000,$0000
dw $0000,$0000,$0000,$0000,$0000
dw $807e

dw $0000
dw $0000
dw $0000,$0000,$0000,$0000,$0000
dw $0000,$0000,$0000
dw $0000,$0000
dw $0000,$0000
dw $0000,$0000
dw $0000
dw $0000,$20a9,$0000
dw $0000,$0000,$0000
dw $0000,$0000,$0000,$0000
dw $0000,$0000,$0000
dw $0000,$0000,$0000,$0000
dw $0000,$0000

dw $0000
dw $40b1,$0000
dw $80b2,$0000,$0000,$0000
dw $0000,$0000
dw $0000
dw $0000,$0000,$0000
dw $0000,$0000,$80b8,$0000,$0000,$0000
dw $0000,$0000,$4099,$0000,$0000,$0000
dw $0000,$0000,$0000,$0000,$0000,$0000
dw $0000,$0000
dw $0000
dw $0000
dw $0000,$0000

dw $0000,$0000,$0000
dw $0000,$80a1,$0000,$0000
dw $80a2,$0000,$0000,$0000,$0000,$0000,$0000,$0000
dw $0000,$0000,$0000,$0000,$0000
dw $0000
dw $0000
dw $0000,$0000,$80c6,$0000,$0000
dw $0000
dw $20a8,$0000
dw $80ba,$0000,$0000,$0000
dw $80b9,$0000,$0000
dw $0000,$0000,$0000,$0000,$0000,$0000
dw $0000,$80cc,$0000,$40cc,$0000,$0000,$0000,$0000
dw $0000,$80bf,$0000
dw $40be

dw $0000,$0000,$0000
dw $0000,$40c2,$0000,$0000,$0000,$0000,$0000,$0000
dw $80c3,$40c1,$0000,$0000,$0000,$0000,$0000,$0000
dw $80c2,$0000,$0000,$0000,$0000,$0000,$0000
dw $80c5
dw $80c4,$0000,$0000
dw $20b6,$0000,$0000,$0000,$0000,$0000
dw $0000,$0000,$0000
dw $0000
dw $0000,$0000,$0000,$0000,$0000
dw $20cc
dw $40bc,$10bc,$80cb
dw $0000

dw $0000,$0000
dw $0000,$0000,$0000,$0000
dw $0000
dw $0000,$0000
dw $0000,$0000,$0000
dw $0000,$0000,$0000
dw $0000,$0000,$0000
dw $0000
dw $0000,$0000
dw $0000
dw $0000,$0000,$0000,$0000
dw $ffff ; indicates the end - we can drop this

; Edge Transition Table (Target Room, Flags, MultiDiv ratio for edges)
org $27C500 ;ends around 27C5F(9) 4 bytes would be 27C649
;I kind of want to split the 3rd byte into two
NorthOpenEdge:
db $00,$80,$11, $00,$80,$11, $00,$80,$11, $00,$80,$11
db $00,$80,$11, $00,$80,$11, $00,$80,$11, $00,$80,$11
db $00,$80,$11, $00,$80,$11, $00,$80,$11
SouthOpenEdge:
db $00,$80,$11, $00,$80,$11, $00,$80,$11, $00,$80,$11
db $00,$80,$11, $00,$80,$11, $00,$80,$11, $00,$80,$11
db $00,$80,$11, $00,$80,$11, $00,$80,$11
WestOpenEdge:
db $00,$80,$11, $00,$80,$11, $00,$80,$11
db $00,$80,$11, $00,$80,$11, $00,$80,$11
db $00,$80,$11, $00,$80,$11, $00,$80,$11
EastOpenEdge:
db $00,$80,$11, $00,$80,$11, $00,$80,$11
db $00,$80,$11, $00,$80,$11, $00,$80,$11
db $00,$80,$11, $00,$80,$11, $00,$80,$11
; Edge Info Table (Midpoint, Width, Min Coord)
; I kind of want to add a fourth byte to help indicate quadrant info on min coord
NorthEdgeInfo:
db $a8,$10,$a0, $2c,$08,$28 ;HC
db $b8,$20,$a8 ; DP West Wing
db $38,$20,$28, $f8,$a0,$a8, $b8,$20,$a8 ; DP Main
db $78,$20,$68 ; DP East Wing
db $f8,$10,$f0, $7c,$18,$70 ; TT Lobby
db $74,$18,$68, $f8,$10,$f0 ; TT Compass
SouthEdgeInfo:
db $a8,$10,$a0, $2c,$08,$28 ; HC
db $b8,$20,$a8 ; DP Sandworm
db $38,$20,$28, $f8,$a0,$a8, $b8,$20,$a8 ; DP North Hall & Dead End
db $78,$20,$68 ; DP Arrow Pot
db $f8,$10,$f0, $7c,$18,$70 ; TT Ambush
db $74,$18,$68, $f8,$10,$f0 ; TT BK Corner
WestEdgeInfo:
db $78,$30,$60 ; TT Attic
db $40,$20,$30 ; DP North Hall
db $40,$20,$30 ; DP Arrow Pot
db $84,$18,$78, $68,$10,$60 ; HC South
db $a0,$a0,$50 ; DP East Wing
db $58,$50,$30, $98,$50,$70 ; TT BK Corner
db $58,$50,$30 ; TT Compass
EastEdgeInfo:
db $78,$30,$60 ; TT Attic
db $40,$20,$30 ; DP Sandworm
db $40,$20,$30 ; DP North Hall
db $68,$10,$60, $84,$18,$78 ; HC Guards
db $a0,$a0,$50 ; DP Main Lobby
db $58,$50,$30, $98,$50,$70 ; TT Ambush
db $58,$50,$30 ; TT Nook
MultDivInfo: ; (1, 2, 3, 4, 5, 6, 10, 20)
db $01, $02, $03, $04, $05, $06, $0a, $14
; indices: 0-7


; dungeon tables
;   HC   HC   EP   DP   AT   SP   PD   MM   SW   IP   TH   TT   TR   GT
org $27f000
CompassBossIndicator:
dw $0000, $0000, $0000, $0000, $0000, $0000, $0000, $0000, $0000, $0000, $0000, $0000, $0000, $0000
TotalKeys: ;27f01c
db $04, $04, $02, $04, $04, $06, $06, $06, $05, $06, $01, $03, $06, $08
ChestKeys: ;27f02a
db $01, $01, $00, $01, $02, $01, $06, $03, $03, $02, $01, $01, $04, $04
BigKeyStatus: ;27f038 (status 2 indicate BnC guard)
dw $0002, $0002, $0001, $0001, $0000, $0001, $0001, $0001, $0001, $0001, $0001, $0001, $0001, $0001
DungeonReminderTable: ;27f054
dw $2D50, $2D50, $2D51, $2D52, $2D54, $2D56, $2D55, $2D5A, $2D57, $2D59, $2D53, $2D58, $2D5B, $2D5C
TotalLocationsLow: ;27f070
db $08, $08, $06, $06, $02, $00, $04, $08, $08, $08, $06, $08, $02, $07
TotalLocationsHigh: ;27f07e
db $00, $00, $00, $00, $00, $01, $01, $00, $00, $00, $00, $00, $01, $02
;27F08C

; Vert 0,6,0 Horz 2,0,8
org $27f090
CoordIndex: ; Horizontal 1st
db 2, 0 ; Coordinate Index $20-$23
OppCoordIndex:
db 0, 2 ; Swapped coordinate Index $20-$23 (minor optimization)
CameraIndex: ; Horizontal 1st
db 0, 6 ; Camera Index $e2-$ea
CamQuadIndex: ; Horizontal 1st
db 8, 0 ; Camera quadrants $600-$60f
ShiftQuadIndex:
db 2, 1 ; see ShiftQuad func (relates to $a9,$aa)
CamBoundIndex: ; Horizontal 1st
db 0, 4 ; Camera Bounds $0618-$61f
OppCamBoundIndex: ; Horizontal 1st
db 4, 0 ; Camera Bounds $0618-$61f
CamBoundBaseLine: ; X camera stuff is 1st column todo Y camera needs more testing
dw $007f, $0077 ; Left/Top camera bounds when at edge or layout frozen
dw $0007, $000b ; Left/Top camera bounds when not frozen + appropriate low byte $22/$20 (preadj. by #$78/#$6c)
dw $00ff, $010b ; Right/Bot camera bounds when not frozen + appropriate low byte $20/$22
dw $017f, $0187 ; Right/Bot camera bound when at edge or layout frozen
;27f0ae next free byte

org $27f100
TilesetTable:
;    0   1   2   3   4   5   6   7   8   9   a   b   c   d   e   f --Offset Ruler
db $13,$04,$04,$06,$0d,$ff,$08,$05,$06,$07,$07,$07,$0e,$0e,$0b,$ff
db $13,$04,$04,$0d,$0d,$0d,$08,$05,$06,$07,$07,$07,$0e,$0e,$0b,$0b
db $04,$04,$04,$0d,$0d,$ff,$08,$05,$08,$09,$07,$07,$06,$ff,$0b,$06
db $04,$05,$04,$12,$08,$08,$08,$08,$08,$09,$07,$07,$06,$0e,$0b,$0b
db $04,$04,$04,$12,$0a,$0a,$08,$ff,$ff,$09,$07,$07,$0e,$0e,$0b,$0b
db $04,$04,$04,$12,$08,$01,$09,$09,$09,$09,$07,$0e,$0e,$0e,$0b,$0b
db $04,$04,$04,$12,$0a,$0a,$08,$09,$09,$ff,$07,$0e,$0e,$0e,$0b,$ff
db $04,$04,$04,$12,$12,$12,$08,$05,$ff,$ff,$ff,$0e,$0e,$0e,$0b,$0b
db $04,$04,$04,$12,$12,$12,$ff,$05,$ff,$05,$ff,$0e,$0e,$0e,$0b,$ff
db $0c,$0c,$0c,$0c,$ff,$0e,$0e,$0c,$0c,$05,$ff,$0e,$0e,$0e,$0b,$0b
db $0c,$0c,$0c,$0c,$0d,$0e,$0e,$05,$05,$05,$05,$0a,$0a,$ff,$0b,$0b
db $04,$0c,$0c,$0c,$0d,$0d,$0d,$0d,$05,$05,$05,$0a,$0a,$ff,$0b,$0b
db $04,$0c,$0c,$0c,$0d,$0d,$0d,$0d,$05,$05,$ff,$0a,$0a,$ff,$0b,$ff
db $04,$0c,$0c,$ff,$ff,$0d,$0d,$ff,$05,$05,$05,$0a,$0a,$ff,$0b,$06
db $04,$06,$06,$06,$06,$06,$06,$06,$06,$ff,$06,$06,$ff,$06,$06,$06
db $06,$06,$03,$03,$03,$03,$ff,$ff,$06,$06,$06,$06,$ff,$06,$06,$06

;27f200
PaletteTable:
db $21,$00,$00,$07,$00,$08,$00,$00,$07,$00,$00,$00,$00,$00,$00,$21
db $21,$00,$00,$00,$00,$00,$00,$00,$07,$00,$00,$00,$00,$00,$00,$00
db $00,$00,$00,$00,$00,$00,$00,$00,$00,$0e,$00,$00,$07,$00,$00,$07
db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$07,$00,$00,$00
db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$13
db $00,$00,$00,$00,$00,$01,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00
db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00
db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00
db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00
db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00
;    0   1   2   3   4   5   6   7   8   9   a   b   c   d   e   f --Offset Ruler
db $00,$00,$00,$00,$00,$00,$00,$06,$00,$00,$00,$00,$00,$00,$00,$00
db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00
db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00
db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$14,$20
db $00,$07,$20,$20,$07,$07,$07,$07,$07,$20,$20,$07,$20,$20,$20,$20
db $07,$07,$02,$02,$02,$02,$07,$07,$07,$20,$20,$07,$20,$20,$20,$07

;27f300
