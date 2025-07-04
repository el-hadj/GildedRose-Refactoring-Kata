from item import Item


MAX_QUALITY = 50
MIN_QUALITY = 0

item_types = {
    "aged brie": "brie",
    "backstage passes to a tafkal80etc concert": "back",
    "sulfuras, hand of ragnaros": "sulf",
    "conjured mana cake": "conj"
}


def update_brie_quality(item: Item):
    item.sell_in -= 1
    if item.quality < MAX_QUALITY:
        item.quality += 1
        if item.sell_in < 0 and item.quality < MAX_QUALITY:
            item.quality += 1

def update_backstage_quality(item: Item):
    item.sell_in -=1
    if item.sell_in < 0:
        item.quality = 0
    elif item.sell_in <= 5:
        item.quality = min(item.quality + 3, MAX_QUALITY)
    elif item.sell_in <= 10:
        item.quality = min(item.quality + 2, MAX_QUALITY)
    else:
        item.quality = min(item.quality + 1, MAX_QUALITY)

def update_sulfuras_quality(item: Item):
    pass

def update_normal_quality(item: Item):
    item.sell_in -=1
    if item.quality > MIN_QUALITY:
        item.quality -=1
        if item.sell_in < 0 and item.quality > MIN_QUALITY:
            item.quality -=1

def update_conjured_quality(item: Item):
    item.sell_in -=1
    if item.quality > MIN_QUALITY:
        item.quality -= 2

    if item.sell_in < 0 and item.quality > MIN_QUALITY:
        item.quality -= 2

    if item.quality < MIN_QUALITY:
        item.quality = 0