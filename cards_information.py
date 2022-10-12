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

witch_curses = 0.5
witch_essence = 1
leaf_value = 3
enemy_resource_multiplier = 2
shard_multiplier_centaur = 37.5
shard_multiplier_vilecreature = 50
shard_multiplier_airelemental = 62.5
shard_multiplier_sparkbubble = 75
relic_dmg_terrors = 35
relic_dmg_superterror = 40
relic_dmg_energyguard = 45
blower_enemy_dmg = 0.1995
slap_multiplier = 0.05


def stat(stat, tier):

	if tier == 'Common':
		return
		
	elif tier == 'Uncommon':
		return stat*2.25

	elif tier == 'Rare':
		for x in range(3):
			if x == 0:
				continue
			else:
				stat = stat*2.25
		return f'{stat:.2f}'

	elif tier == 'Epic':
		for x in range(4):
			if x == 0:
				continue
			else:
				stat = stat*2.25
		return f'{stat:.2f}'

	elif tier == 'Mythical':
		for x in range(5):
			if x == 0:
				continue
			else:
				stat = stat*2.25
		return f'{stat:.2f}'

	elif tier == 'Legendary':
		for x in range(6):
			if x == 0:
				continue
			else:
				stat = stat*2.25
		return f'{stat:.2f}'


def card_inf(tier):

	if tier == 'Common':
		common_cards = [

		#Bosses
		{
			'Name':'Witch',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Leaf Value Multiplier':'3%',
			'Witch curses':'+0.5',
			'Witch Essence':'1%',
			'Location':'Cursed Kokkaupunki',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029423643169669160/1029423789613785119/witch_card_common.png'
		},
		{
			'Name':'Centaur',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Leaf Value Multiplier':'3%',
			'Enemy Shards Multiplier':'37,5%',
			'Location':'The Exalted Bridge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029432843035742261/1029432879664599070/centaur_card_common.png'
		},
		{
			'Name':'Vile Creature',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Leaf Value Multiplier':'3%',
			'Enemy Shards Multiplier':'50%',
			'Location':'Vilewood Cemetary',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029436982541176882/1029437326360846346/vilecreature_card_common.png'
		},
		{
			'Name':'Air Elemental',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Leaf Value Multiplier':'3%',
			'Enemy Shards Multiplier':'62,5%',
			'Location':'The Lone Tree',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437012039708804/1029437353456041994/airelemental_card_common.png'
		},
		{
			'Name':'Spark Bubble',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Leaf Value Multiplier':'3%',
			'Enemy Shards Multiplier':'75%',
			'Location':'Spark Bubble',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437036916117607/1029437375119638628/sparkbubble_card_common.png'
		},
		{
			'Name':'Terror Blue',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Leaf Value Multiplier':'3%',
			'Relic Damage Multiplier':'35%',
			'Location':'Blue Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437069124190339/1029437390214930583/blueterror_card_common.png'
		},
		{
			'Name':'Terror Green',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Leaf Value Multiplier':'3%',
			'Relic Damage Multiplier':'35%',
			'Location':'Green Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437116662415380/1029437409865244712/greenterror_card_common.png'
		},
		{
			'Name':'Terror Red',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Leaf Value Multiplier':'3%',
			'Relic Damage Multiplier':'35%',
			'Location':'Red Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437141119410176/1029437429721079899/redterror_card_common.png'
		},
		{
			'Name':'Terror Purple',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Leaf Value Multiplier':'3%',
			'Relic Damage Multiplier':'35%',
			'Location':'Purple Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437162044788858/1029437440575942746/purpleterror_card_common.png'
		},
		{
			'Name':'Super Terror',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Leaf Value Multiplier':'3%',
			'Relic Damage Multiplier':'40%',
			'Location':'Black Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437179203686400/1029437456744992839/superterror_card_common.png'
		},
		{
			'Name':'Energy Guard',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Leaf Value Multiplier':'3%',
			'Relic Damage Multiplier':'45%',
			'Location':'Energy Singularity',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437205036404747/1029798460565762148/unknown.png'
		}
		]
		return common_cards


	elif tier == 'Uncommon':

		uncommon_cards = [

		#Bosses
		{
			'Name':'Witch',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}%',
			'Enemy Resource Multiplier':'4.5%',
			'Witch curses':f'+{stat(witch_curses, tier)}',
			'Witch Essence':f'{stat(witch_essence, tier)}%',
			'Location':'Cursed Kokkaupunki',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029423643169669160/1029423788619735110/witch_card_uncommon.png'
		},
		{
			'Name':'Centaur',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}%',
			'Enemy Resource Multiplier':'4.5%',
			'Enemy Shards Multiplier':f'{stat(shard_multiplier_centaur, tier)}%',
			'Location':'The Exalted Bridge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029432843035742261/1029779273873113108/centaur_card_uncommon.png'
		},
		{
			'Name':'Vile Creature',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':'4.5%',
			'Enemy Shards Multiplier':f'{stat(shard_multiplier_vilecreature, tier)}%',
			'Location':'Vilewood Cemetary',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029436982541176882/1029782423313063946/vilecreature_card_uncommon.png'
		},
		{
			'Name':'Air Elemental',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':'4.5%',
			'Enemy Shards Multiplier':f'{stat(shard_multiplier_airelemental, tier)}%',
			'Location':'The Lone Tree',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437012039708804/1029776366289309716/airelemental_card_uncommon.png'
		},
		{
			'Name':'Spark Bubble',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':'4.5%',
			'Enemy Shards Multiplier':f'{stat(shard_multiplier_sparkbubble, tier)}%',
			'Location':'Spark Bubble',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437036916117607/1029784796743880704/unknown.png'
		},
		{
			'Name':'Terror Blue',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':'4.5%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_terrors, tier)}%',
			'Location':'Blue Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437069124190339/1029787772891975781/unknown.png'
		},
		{
			'Name':'Terror Green',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':'4.5%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_terrors, tier)}%',
			'Location':'Green Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437116662415380/1029789752251138128/unknown.png'
		},
		{
			'Name':'Terror Red',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':'4.5%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_terrors, tier)}%',
			'Location':'Red Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437141119410176/1029792906954952715/unknown.png'
		},
		{
			'Name':'Terror Purple',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':'4.5%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_terrors, tier)}%',
			'Location':'Purple Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437162044788858/1029795020439568384/unknown.png'
		},
		{
			'Name':'Super Terror',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':'4.5%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_superterror, tier)}%',
			'Location':'Black Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437179203686400/1029796830730526740/unknown.png'
		},
		{
			'Name':'Energy Guard',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':'4.5%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_energyguard, tier)}%',
			'Location':'Energy Singularity',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437205036404747/1029798460972601374/unknown.png'
		}
		]
		return uncommon_cards


	elif tier == 'Rare':

		rare_cards = [

		#Bosses
		{
			'Name':'Witch',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Blower Enemy DMG':'1.01%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}%',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Witch curses':f'+{stat(witch_curses, tier)}',
			'Witch Essence':f'{stat(witch_essence, tier)}%',
			'Location':'Cursed Kokkaupunki',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029423643169669160/1029427103747293194/witch_card_rare.png'
		},
		{
			'Name':'Centaur',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Blower Enemy DMG':'1.01%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}%',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Enemy Shards Multiplier':f'{stat(shard_multiplier_centaur, tier)}%',
			'Location':'The Exalted Bridge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029432843035742261/1029779273545957396/centaur_card_rare.png'
		},
		{
			'Name':'Vile Creature',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Blower Enemy DMG':'1.01%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Enemy Shards Multiplier':f'{stat(shard_multiplier_vilecreature, tier)}%',
			'Location':'Vilewood Cemetary',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029436982541176882/1029782422990094346/vilecreature_card_rare.png'
		},
		{
			'Name':'Air Elemental',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Blower Enemy DMG':'1.01%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Enemy Shards Multiplier':f'{stat(shard_multiplier_airelemental, tier)}%',
			'Location':'The Lone Tree',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437012039708804/1029776365936984184/airelemental_card_rare.png'
		},
		{
			'Name':'Spark Bubble',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Blower Enemy DMG':'1.01%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Enemy Shards Multiplier':f'{stat(shard_multiplier_sparkbubble, tier)}%',
			'Location':'Spark Bubble',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437036916117607/1029784796399943770/unknown.png'
		},
		{
			'Name':'Terror Blue',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Blower Enemy DMG':'1.01%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_terrors, tier)}%',
			'Location':'Blue Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437069124190339/1029787772472533112/unknown.png'
		},
		{
			'Name':'Terror Green',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Blower Enemy DMG':'1.01%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_terrors, tier)}%',
			'Location':'Green Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437116662415380/1029789751869448302/unknown.png'
		},
		{
			'Name':'Terror Red',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Blower Enemy DMG':'1.01%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_terrors, tier)}%',
			'Location':'Red Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437141119410176/1029792906468392990/unknown.png'
		},
		{
			'Name':'Terror Purple',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Blower Enemy DMG':'1.01%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_terrors, tier)}%',
			'Location':'Purple Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437162044788858/1029795020045295728/unknown.png'
		},
		{
			'Name':'Super Terror',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Blower Enemy DMG':'1.01%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_superterror, tier)}%',
			'Location':'Black Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437179203686400/1029796830223028385/unknown.png'
		},
		{
			'Name':'Energy Guard',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Blower Enemy DMG':'1.01%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_energyguard, tier)}%',
			'Location':'Energy Singularity',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437205036404747/1029798461358477342/unknown.png'
		}
		]
		return rare_cards


	elif tier == 'Epic':

		epic_cards = [

		#Bosses
		{
			'Name':'Witch',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}%',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Witch curses':f'+{stat(witch_curses, tier)}',
			'Witch Essence':f'{stat(witch_essence, tier)}%',
			'Location':'Cursed Kokkaupunki',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029423643169669160/1029427103202017400/witch_card_epic.png'
		},
		{
			'Name':'Centaur',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}%',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Enemy Shards Multiplier':f'{stat(shard_multiplier_centaur, tier)}%',
			'Location':'The Exalted Bridge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029432843035742261/1029779274372219001/centaur_card_epic.png'
		},
		{
			'Name':'Vile Creature',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Enemy Shards Multiplier':f'{stat(shard_multiplier_vilecreature, tier)}%',
			'Location':'Vilewood Cemetary',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029436982541176882/1029782421849243749/vilecreature_card_epic.png'
		},
		{
			'Name':'Air Elemental',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Enemy Shards Multiplier':f'{stat(shard_multiplier_airelemental, tier)}%',
			'Location':'The Lone Tree',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437012039708804/1029776364640931871/airelemental_card_epic.png'
		},
		{
			'Name':'Spark Bubble',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Enemy Shards Multiplier':f'{stat(shard_multiplier_sparkbubble, tier)}%',
			'Location':'Spark Bubble',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437036916117607/1029784796009873418/unknown.png'
		},
		{
			'Name':'Terror Blue',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_terrors, tier)}%',
			'Location':'Blue Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437069124190339/1029787772082462790/unknown.png'
		},
		{
			'Name':'Terror Green',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_terrors, tier)}%',
			'Location':'Green Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437116662415380/1029789751424852108/unknown.png'
		},
		{
			'Name':'Terror Red',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_terrors, tier)}%',
			'Location':'Red Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437141119410176/1029792907391139870/unknown.png'
		},
		{
			'Name':'Terror Purple',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_terrors, tier)}%',
			'Location':'Purple Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437162044788858/1029795019676209183/unknown.png'
		},
		{
			'Name':'Super Terror',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_superterror, tier)}%',
			'Location':'Black Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437179203686400/1029796829719699586/unknown.png'
		},
		{
			'Name':'Energy Guard',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_energyguard, tier)}%',
			'Location':'Energy Singularity',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437205036404747/1029798461790490694/unknown.png'
		}
		]
		return epic_cards


	elif tier == 'Mythical':

		mythical_cards = [

		#Bosses
		{
			'Name':'Witch',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}%',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Witch curses':f'+{stat(witch_curses, tier)}',
			'Witch Essence':f'{stat(witch_essence, tier)}%',
			'Location':'Cursed Kokkaupunki',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029423643169669160/1029427102493200534/witch_card_mythical.png'
		},
		{
			'Name':'Centaur',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}%',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Enemy Shards Multiplier':f'{stat(shard_multiplier_centaur, tier)}%',
			'Location':'The Exalted Bridge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029432843035742261/1029779273155870770/centaur_card_mythical.png'
		},
		{
			'Name':'Vile Creature',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Enemy Shards Multiplier':f'{stat(shard_multiplier_vilecreature, tier)}%',
			'Location':'Vilewood Cemetary',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029436982541176882/1029782422608412703/vilecreature_card_mythical.png'
		},
		{
			'Name':'Air Elemental',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Enemy Shards Multiplier':f'{stat(shard_multiplier_airelemental, tier)}%',
			'Location':'The Lone Tree',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437012039708804/1029776365446238248/airelemental_card_mythical.png'
		},
		{
			'Name':'Spark Bubble',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Enemy Shards Multiplier':f'{stat(shard_multiplier_sparkbubble, tier)}%',
			'Location':'Spark Bubble',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437036916117607/1029784793380048936/unknown.png'
		},
		{
			'Name':'Terror Blue',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_terrors, tier)}%',
			'Location':'Blue Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437069124190339/1029787771679809556/unknown.png'
		},
		{
			'Name':'Terror Green',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_terrors, tier)}%',
			'Location':'Green Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437116662415380/1029789751047372940/unknown.png'
		},
		{
			'Name':'Terror Red',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_terrors, tier)}%',
			'Location':'Red Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437141119410176/1029792906036396172/unknown.png'
		},
		{
			'Name':'Terror Purple',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_terrors, tier)}%',
			'Location':'Purple Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437162044788858/1029795019340660766/unknown.png'
		},
		{
			'Name':'Super Terror',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_superterror, tier)}%',
			'Location':'Black Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437179203686400/1029796829199601765/unknown.png'
		},
		{
			'Name':'Energy Guard',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_energyguard, tier)}%',
			'Location':'Energy Singularity',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437205036404747/1029798462159589458/unknown.png'
		}
		]
		return mythical_cards


	elif tier == 'Legendary':

		legendary_cards = [

		#Bosses
		{
			'Name':'Witch',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}%',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Witch curses':f'+{stat(witch_curses, tier)}',
			'Witch Essence':f'{stat(witch_essence, tier)}%',
			'Location':'Cursed Kokkaupunki',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029423643169669160/1029427101973102663/witch_card_legendary.png'
		},
		{
			'Name':'Centaur',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}%',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Enemy Shards Multiplier':f'{stat(shard_multiplier_centaur, tier)}%',
			'Location':'The Exalted Bridge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029432843035742261/1029779274783268934/centaur_card_legendary.png'
		},
		{
			'Name':'Vile Creature',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Enemy Shards Multiplier':f'{stat(shard_multiplier_vilecreature, tier)}%',
			'Location':'Vilewood Cemetary',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029436982541176882/1029782422172205146/vilecreature_card_legendary.png'
		},
		{
			'Name':'Air Elemental',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Enemy Shards Multiplier':f'{stat(shard_multiplier_airelemental, tier)}%',
			'Location':'The Lone Tree',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437012039708804/1029776365014237224/airelemental_card_legendary.png'
		},
		{
			'Name':'Spark Bubble',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Enemy Shards Multiplier':f'{stat(shard_multiplier_sparkbubble, tier)}%',
			'Location':'Spark Bubble',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437036916117607/1029784792809619526/unknown.png'
		},
		{
			'Name':'Terror Blue',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_terrors, tier)}%',
			'Location':'Blue Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437069124190339/1029787771151339642/unknown.png'
		},
		{
			'Name':'Terror Green',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_terrors, tier)}%',
			'Location':'Green Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437116662415380/1029789750720204892/unknown.png'
		},
		{
			'Name':'Terror Red',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_terrors, tier)}%',
			'Location':'Red Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437141119410176/1029792907793793024/unknown.png'
		},
		{
			'Name':'Terror Purple',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_terrors, tier)}%',
			'Location':'Purple Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437162044788858/1029795018896068718/unknown.png'
		},
		{
			'Name':'Super Terror',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_superterror, tier)}%',
			'Location':'Black Planet Edge',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437179203686400/1029796828813729862/unknown.png'
		},
		{
			'Name':'Energy Guard',
			'Boss card Spawn chance':'0.1%',
			'Additional Enemy DMG':'2.5%',
			'Slap DMG':f'{stat(slap_multiplier, tier)}%',
			'Blower Enemy DMG':f'{stat(blower_enemy_dmg, tier)}%',
			'Leaf Value Multiplier':f'{stat(leaf_value, tier)}',
			'Enemy Resource Multiplier':f'{stat(enemy_resource_multiplier, tier)}%',
			'Relic Damage Multiplier':f'{stat(relic_dmg_energyguard, tier)}%',
			'Location':'Energy Singularity',
			'thumbnail':'https://cdn.discordapp.com/attachments/1029437205036404747/1029798462889394176/unknown.png'
		}
		]
		return legendary_cards

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
