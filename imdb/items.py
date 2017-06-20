# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class MovieItem(scrapy.Item):
    Title = Field()
    Rating = Field()
    Ranking = Field()  # this is the number it is in the list
    ReleaseDate = Field()
    MainPageUrl = Field()

        # extra detials
    Director = Field()
    Writers = Field()
    Runtime = Field()
    Sinopsis = Field()
    Genres = Field()
    MpaaRating = Field()
    Budget = Field()
    Language = Field()
    Country = Field()

        # technical details
    GrossProfit = Field()
    OpeningWeekendProfit = Field()
    AspectRatio = Field()
    SoundMix = Field()
    Color = Field()

    CastMembers = Field()


class CastItem(Item):
    ActorName = Field()
    CharacterName = Field()
    # this is howmany down they are from the top of the cast list.
    Ranking = Field()
