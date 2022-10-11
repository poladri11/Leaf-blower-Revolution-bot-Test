import discord
from discord import app_commands
from discord.app_commands import Choice

cards_tiers = [
    Choice(name='Common', value='Common'),
    Choice(name='Uncommon', value='Uncommon'),
    Choice(name='Rare', value='Rare'),
    Choice(name='Epic', value='Epic'),
    Choice(name='Mythical', value='Mythical'),
    Choice(name='Legendary', value='Legendary'),
    ]

def card_inf(tier):

	if tier == 'Common':
		common_cards = [{
			'Name':'Witch',
			'Boss card Spawn chance':'0,1%',
			'Additional Enemy DMG':'2,5%',
			'Leaf Value Multiplier':'3%',
			'Witch curses':'+0.5',
			'Witch Essence':'1%',
			'Location':'Cursed Kokkaupunki',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029423643169669160/1029423789613785119/witch_card_common.png'
		},
		{
			'Name':'Centaur',
			'Boss card Spawn chance':'0,1%',
			'Additional Enemy DMG':'2,5%',
			'Leaf Value Multiplier':'3%',
			'Enemy Shards Multiplier':'37,5%',
			'Location':'The Exalted Bridge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029432843035742261/1029432879664599070/centaur_card_common.png'
		},
		{
			'Name':'Vile Creature',
			'Boss card Spawn chance':'0,1%',
			'Additional Enemy DMG':'2,5%',
			'Leaf Value Multiplier':'3%',
			'Enemy Shards Multiplier':'50%',
			'Location':'Vilewood Cemetary',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029436982541176882/1029437326360846346/vilecreature_card_common.png'
		},
		{
			'Name':'Air Elemental',
			'Boss card Spawn chance':'0,1%',
			'Additional Enemy DMG':'2,5%',
			'Leaf Value Multiplier':'3%',
			'Enemy Shards Multiplier':'62,5%',
			'Location':'The Lone Tree',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437012039708804/1029437353456041994/airelemental_card_common.png'
		},
		{
			'Name':'Spark Bubble',
			'Boss card Spawn chance':'0,1%',
			'Additional Enemy DMG':'2,5%',
			'Leaf Value Multiplier':'3%',
			'Enemy Shards Multiplier':'75%',
			'Location':'Spark Bubble',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437036916117607/1029437375119638628/sparkbubble_card_common.png'
		},
		{
			'Name':'Terror Blue',
			'Boss card Spawn chance':'0,1%',
			'Additional Enemy DMG':'2,5%',
			'Leaf Value Multiplier':'3%',
			'Relic Damage Multiplier':'35%',
			'Location':'Blue Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437069124190339/1029437390214930583/blueterror_card_common.png'
		},
		{
			'Name':'Terror Green',
			'Boss card Spawn chance':'0,1%',
			'Additional Enemy DMG':'2,5%',
			'Leaf Value Multiplier':'3%',
			'Relic Damage Multiplier':'35%',
			'Location':'Green Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437116662415380/1029437409865244712/greenterror_card_common.png'
		},
		{
			'Name':'Terror Red',
			'Boss card Spawn chance':'0,1%',
			'Additional Enemy DMG':'2,5%',
			'Leaf Value Multiplier':'3%',
			'Relic Damage Multiplier':'35%',
			'Location':'Red Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437141119410176/1029437429721079899/redterror_card_common.png'
		},
		{
			'Name':'Terror Purple',
			'Boss card Spawn chance':'0,1%',
			'Additional Enemy DMG':'2,5%',
			'Leaf Value Multiplier':'3%',
			'Relic Damage Multiplier':'35%',
			'Location':'Purple Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437162044788858/1029437440575942746/purpleterror_card_common.png'
		},
		{
			'Name':'Super Terror',
			'Boss card Spawn chance':'0,1%',
			'Additional Enemy DMG':'2,5%',
			'Leaf Value Multiplier':'3%',
			'Relic Damage Multiplier':'40%',
			'Location':'Black Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437179203686400/1029437456744992839/superterror_card_common.png'
		},
		{
			'Name':'Energy Guard',
			'Boss card Spawn chance':'0,1%',
			'Additional Enemy DMG':'2,5%',
			'Leaf Value Multiplier':'3%',
			'Relic Damage Multiplier':'45%',
			'Location':'Energy Singularity',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029432843035742261/1029432879664599070/centaur_card_common.png'
		}
		]
		return common_cards
	elif tier == 'Uncommon':

		uncommon_cards = [{

		}]
		return uncommon_cards



cards_choices = [
    Choice(name='Witch', value='Witch'),
    Choice(name='Centaur', value='Centaur'),
    Choice(name='Vile Creature', value='Vile Creature'),
    Choice(name='Air Elemental', value='Air Elemental'),
    Choice(name='Spark Bubble', value='Spark Bubble'),
    Choice(name='Terror Blue', value='Terror Blue'),
    Choice(name='Terror Green', value='Terror Green'),
    Choice(name='Terror Red', value='Terror Red'),
    Choice(name='Terror Purple', value='Terror Purple'),
    Choice(name='Super Terror', value='Super Terror'),
    Choice(name='Energy Guard', value='Energy Guard'),
    ]