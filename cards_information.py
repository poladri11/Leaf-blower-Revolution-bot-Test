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

tier_powers = {
	'Common': 0,
	'Uncommon': 1,
	'Rare': 2,
	'Epic': 3,
	'Mythical': 4,
	'Legendary': 5
}

common_timer_boss_stats = {
	'Leaf Value Multiplier': {
		'base': leaf_value,
		'min_tier': 'Common',
		'format': '{:2g}%'
	},
	'Blower Enemy DMG': {
		'base': blower_enemy_dmg,
		'min_tier': 'Rare',
		'format': '{:2g}%'
	},
	'Slap DMG': {
		'base': slap_multiplier,
		'min_tier': 'Epic',
		'format': '{:2g}%'
	},
	'Enemy Resource Multiplier': {
		'base': enemy_resource_multiplier,
		'min_tier': 'Uncommon',
		'format': '{:2g}%'
	}
}

minor_terror_tier_stats = {
	'Relic Damage Multiplier': {
		'base': relic_dmg_terrors,
		'min_tier': 'Common',
		'format': '{:2g}%'
	},
	**common_timer_boss_stats
}

base_card_information = [
	{
		'Name': 'Witch',
		'Boss card Spawn chance': '0.1%',
		'Additional Enemy DMG': '2.5%',
		'Location': 'Cursed Kokkaupunki',
		'thumbnail': 'https://cdn.discordapp.com/attachments/1029423643169669160/1029423789613785119/witch_card_common.png',
		'Tier Stats': {
			'Witch curses': {
				'base': witch_curses,
				'min_tier': 'Common',
				'format': '+{:2g}'
			},
			'Witch Essence': {
				'base': witch_essence,
				'min_tier': 'Common',
				'format': '{:2g}%'
			},
			**common_timer_boss_stats
		}
	},
	{
		'Name': 'Centaur',
		'Boss card Spawn chance': '0.1%',
		'Additional Enemy DMG': '2.5%',
		'Location': 'The Exalted Bridge',
		'thumbnail': 'https://cdn.discordapp.com/attachments/1029432843035742261/1029432879664599070/centaur_card_common.png',
		'Tier Stats': {
			'Enemy Shards Multiplier': {
				'base': shard_multiplier_centaur,
				'min_tier': 'Uncommon',
				'format': '{:2g}%'
			},
			**common_timer_boss_stats
		}
	},
	{
		'Name': 'Vile Creature',
		'Boss card Spawn chance': '0.1%',
		'Additional Enemy DMG': '2.5%',
		'Location': 'Vilewood Cemetary',
		'thumbnail': 'https://cdn.discordapp.com/attachments/1029436982541176882/1029437326360846346/vilecreature_card_common.png',
		'Tier Stats': {
			'Enemy Shards Multiplier': {
				'base': shard_multiplier_vilecreature,
				'min_tier': 'Uncommon',
				'format': '{:2g}%'
			},
			**common_timer_boss_stats
		}
	},
	{
		'Name': 'Air Elemental',
		'Boss card Spawn chance': '0.1%',
		'Additional Enemy DMG': '2.5%',
		'Location': 'The Lone Tree',
		'thumbnail': 'https://cdn.discordapp.com/attachments/1029437012039708804/1029437353456041994/airelemental_card_common.png',
		'Tier Stats': {
			'Enemy Shards Multiplier': {
				'base': shard_multiplier_airelemental,
				'min_tier': 'Uncommon',
				'format': '{:2g}%'
			},
			**common_timer_boss_stats
		}
	},
	{
		'Name': 'Spark Bubble',
		'Boss card Spawn chance': '0.1%',
		'Additional Enemy DMG': '2.5%',
		'Location': 'Spark Bubble',
		'thumbnail': 'https://cdn.discordapp.com/attachments/1029437036916117607/1029437375119638628/sparkbubble_card_common.png',
		'Tier Stats': {
			'Enemy Shards Multiplier': {
				'base': shard_multiplier_sparkbubble,
				'min_tier': 'Uncommon',
				'format': '{:2g}%'
			},
			**common_timer_boss_stats
		}
	},
	{
		'Name': 'Terror Blue',
		'Boss card Spawn chance': '0.1%',
		'Additional Enemy DMG': '2.5%',
		'Location': 'Blue Planet Edge',
		'thumbnail': 'https://cdn.discordapp.com/attachments/1029437069124190339/1029437390214930583/blueterror_card_common.png',
		'Tier Stats': minor_terror_tier_stats
	},
	{
		'Name': 'Terror Green',
		'Boss card Spawn chance': '0.1%',
		'Additional Enemy DMG': '2.5%',
		'Location': 'Green Planet Edge',
		'thumbnail': 'https://cdn.discordapp.com/attachments/1029437116662415380/1029437409865244712/greenterror_card_common.png',
		'Tier Stats': minor_terror_tier_stats
	},
	{
		'Name': 'Terror Red',
		'Boss card Spawn chance': '0.1%',
		'Additional Enemy DMG': '2.5%',
		'Location': 'Red Planet Edge',
		'thumbnail': 'https://cdn.discordapp.com/attachments/1029437141119410176/1029437429721079899/redterror_card_common.png',
		'Tier Stats': minor_terror_tier_stats
	},
	{
		'Name': 'Terror Purple',
		'Boss card Spawn chance': '0.1%',
		'Additional Enemy DMG': '2.5%',
		'Location': 'Purple Planet Edge',
		'thumbnail': 'https://cdn.discordapp.com/attachments/1029437162044788858/1029437440575942746/purpleterror_card_common.png',
		'Tier Stats': minor_terror_tier_stats
	},
	{
		'Name': 'Super Terror',
		'Boss card Spawn chance': '0.1%',
		'Additional Enemy DMG': '2.5%',
		'Leaf Value Multiplier': '3%',
		'Relic Damage Multiplier': '40%',
		'Location': 'Black Planet Edge',
		'thumbnail': 'https://cdn.discordapp.com/attachments/1029437179203686400/1029437456744992839/superterror_card_common.png',
		'Tier Stats': {
			'Relic Damage Multiplier': {
				'base': relic_dmg_superterror,
				'min_tier': 'Common',
				'format': '{:2g}%'
			},
			**common_timer_boss_stats
		}
	},
	{
		'Name': 'Energy Guard',
		'Boss card Spawn chance': '0.1%',
		'Additional Enemy DMG': '2.5%',
		'Leaf Value Multiplier': '3%',
		'Relic Damage Multiplier': '45%',
		'Location': 'Energy Singularity',
		'thumbnail': 'https://cdn.discordapp.com/attachments/1029437205036404747/1029798460565762148/unknown.png',
		'Tier Stats': {
			'Relic Damage Multiplier': {
				'base': relic_dmg_energyguard,
				'min_tier': 'Common',
				'format': '{:2g}%'
			},
			**common_timer_boss_stats
		}
	}
]


def stat(stat_value, tier):
	stat_value = stat_value * 2.25 ** tier_powers[tier]

	return f'{stat_value:.2f}'


def flatten_tier_stats(card_info, tier):
	tier_stats = card_info['Tier Stats']
	tier_power = tier_powers[tier]

	mapped_stats = {}
	for name, info in tier_stats:
		if tier_power < tier_powers[info['min_tier']]:
			continue

		value = stat(info['base'], tier)
		formatted_value = info['format'].format(value)
		mapped_stats[name] = formatted_value

	result = mapped_stats
	result.update(card_info)
	del result['Tier Stats']

	return result


def card_inf(tier):
	return [flatten_tier_stats(card_info, tier) for card_info in base_card_information]


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
