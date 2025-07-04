# -*- coding: utf-8 -*-

from utils import item_types, update_backstage_quality, update_brie_quality,update_conjured_quality, update_normal_quality, update_sulfuras_quality

class GildedRose(object):

    def __init__(self, items: list):
        self.items = items


    def update_quality(self):
        for item in self.items:
            item_type = item_types.get(item.name.lower(), "")
            match item_type:
                case 'brie':
                    update_brie_quality(item)
                    continue
                case 'back':
                    update_backstage_quality(item)
                    continue
                case 'sulf':
                    update_sulfuras_quality(item)
                    continue
                case 'conj':
                    update_conjured_quality(item)
                    continue
                case _:
                    update_normal_quality(item)
                    continue


