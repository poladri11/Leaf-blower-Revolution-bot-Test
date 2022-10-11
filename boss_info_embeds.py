import discord
from discord import app_commands
from discord.app_commands import Choice



boss_choices = [
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
    Choice(name='Energy Guard', value='Energy Guard')
    ]

boss_data = [{
	"name":"Witch",
	"location":"Cursed Kokkaupunki",
	"health":"1e30",
	"drop":"<:cosmicessence:1028011185670475876> x5 <:earthessence:1028011187142664202> x5\n<:leafessence:1028011188568739870> x5 <:wateressence:1028011190045130772> x5\n222 curses",
	"dmg":"2e25 Blowing DMG + Wind + Gravity Ball\n1e27 Blowing DMG AFK",
	"thumbnail":"https://cdn.discordapp.com/attachments/751835340482019458/1028009480392278036/witch_2.png",
	"type":"Regular"
},
{
	"name":"Centaur",
	"location":"The Exalted Bridge",
	"health":"3e41",
	"drop":"<:ancient:1029137273779925022> > 1e9\n<:shard:1029136850339758091> 3-6\n0-1 <:commonrelic:1029136848989208667> / <:uncommonrelic:1029136851707101264> Relic",
	"dmg":"2.2e41 Slap Damage\n4.5e38 Blowing DMG + Gravity Ball",
	"thumbnail":"https://cdn.discordapp.com/attachments/751835340482019458/1029141769851502612/centaur.png",
	"type":"Regular"
},
{
	"name":"Vile Creature",
	"drop":"<:ancient:1029137273779925022> > 1e13\n<:sacred:1029166830448816220> > 1e5\n<:shard:1029136850339758091> 10-20\n0-1 <:commonrelic:1029136848989208667> / <:uncommonrelic:1029136851707101264> / <:rarerelic:1029166829131800586> Relic",
	"location":"Vilewood Cemetery",
	"health":"3e44",
	"dmg":"2.2e44 Slap Damage",
	"thumbnail":"https://cdn.discordapp.com/attachments/751835340482019458/1029165678416105482/vilecreature.png",
	"type":"Regular"
},
{
	"name":"Air Elemental",
	"drop":"<:ancient:1029137273779925022> > 1e15\n<:sacred:1029166830448816220> > 1e7\n<:shard:1029136850339758091> 30-40\n0-1 <:uncommonrelic:1029136851707101264> / <:rarerelic:1029166829131800586> / <:epicrelic:1029411851819286549> Relic",
	"location":"The Lone Tree",
	"health":"3e49",
	"dmg":"2.2e49 Slap Damage",
	"thumbnail":"https://cdn.discordapp.com/attachments/751835340482019458/1029165676746784798/airelemental.png",
	"type":"Regular"
},
{
	"name":"Spark Bubble",
	"drop":"<:shard:1029136850339758091> 50-60\n0-1 <:rarerelic:1029166829131800586> / <:epicrelic:1029411851819286549> / <:mythicalrelic:1029411853383774299> Relic",
	"location":"Spark Bubble",
	"health":"1e57",
	"dmg":"1.8e56 Slap Damage",
	"thumbnail":"https://cdn.discordapp.com/attachments/751835340482019458/1029165677434638428/sparkbubble.png",
	"type":"Exotic"
},
{
	"name":"Terror Blue",
	"drop":"<:shard:1029136850339758091> 70-100\n0-1 <:epicrelic:1029411851819286549> / <:mythicalrelic:1029411853383774299> Relic\n0-1(10%) L1 Leafcension",
	"location":"Blue Planet Edge",
	"health":"1e68",
	"dmg":"7.15e66 Slap Damage\nWeak against Exotic, Gold and Platinum DMG type",
	"thumbnail":"https://cdn.discordapp.com/attachments/751835340482019458/1029165678097346560/terror.png",
	"type":"Ice"
},
{
	"name":"Terror Green",
	"drop":"<:shard:1029136850339758091> 70-100\n0-1 <:epicrelic:1029411851819286549> / <:mythicalrelic:1029411853383774299> Relic\n0-1(10%) L1 Leafcension",
	"location":"Green Planet Edge",
	"health":"1e68",
	"dmg":"7.15e66 Slap Damage\nWeak against Lava and Exotic DMG type",
	"thumbnail":"https://cdn.discordapp.com/attachments/751835340482019458/1029165678097346560/terror.png",
	"type":"Platinum"
},
{
	"name":"Terror Red",
	"drop":"<:shard:1029136850339758091> 70-100\n0-1 <:epicrelic:1029411851819286549> / <:mythicalrelic:1029411853383774299> Relic\n0-1(10%) L1 Leafcension",
	"location":"Red Planet Edge",
	"health":"1e68",
	"dmg":"7.15e66 Slap Damage\nWeak against Ice and Cosmic DMG type",
	"thumbnail":"https://cdn.discordapp.com/attachments/751835340482019458/1029165678097346560/terror.png",
	"type":"Lava"
},
{
	"name":"Terror Purple",
	"drop":"<:shard:1029136850339758091> 70-100\n0-1 <:epicrelic:1029411851819286549> / <:mythicalrelic:1029411853383774299> Relic\n0-1(10%) L1 Leafcension",
	"location":"Purple Planet Edge",
	"health":"1e68",
	"dmg":"7.15e66 Slap Damage\nWeak against Cosmic and Lava DMG type",
	"thumbnail":"https://cdn.discordapp.com/attachments/751835340482019458/1029165678097346560/terror.png",
	"type":"Gold"
},
{
	"name":"Super Terror",
	"drop":"<:shard:1029136850339758091> 100-125\n<:ascensionshard:1029417793176748124> 1-3 (10%)\n<:fusionshard:1029417794862850068> 1-3 (10%)\n<:transformationshard:1029417796112752721> 1-3 (10%)\n0-1 <:mythicalrelic:1029411853383774299> Relic\n2-3(10%) L1 Leafcension",
	"location":"Black Planet Edge",
	"health":"1e73",
	"dmg":"7.15e71 Slap Damage\nWeak against Platinum, Ice and Lava DMG type",
	"thumbnail":"https://cdn.discordapp.com/attachments/751835340482019458/1029165677761806386/superterror.png",
	"type":"Cosmic"
},
{
	"name":"Energy Guard",
	"drop":"<:shard:1029136850339758091> 150-200\n<:ascensionshard:1029417793176748124> 2-3 (10%)\n<:fusionshard:1029417794862850068> 2-3 (10%)\n<:transformationshard:1029417796112752721> 2-3 (10%)\n0-1 <:mythicalrelic:1029411853383774299> Relic\n2-3(10%) L2 Leafcension",
	"location":"Energy Singularity",
	"health":"1e80",
	"dmg":"7.15e78 Slap Damage",
	"thumbnail":"https://cdn.discordapp.com/attachments/751835340482019458/1029165677073936456/energyguard.png",
	"type":"Cursed"
}
]


# Embed for the boss information
def embed(x):
	embed_info = discord.Embed(colour=discord.Colour(0xc30cc1))

	embed_info.set_thumbnail(url=f"{x['thumbnail']}")
	embed_info.set_author(name=f"{x['name']} | Information")
	embed_info.add_field(name="Basic drop", value=f"{x['drop']}", inline=True)
	embed_info.add_field(name="Total Health", value=f"{x['health']}", inline=True)
	embed_info.add_field(name="Location", value=f"{x['location']}", inline=True)
	embed_info.add_field(name="Damage required", value=f"{x['dmg']}", inline=True)
	embed_info.add_field(name="Type", value=f"{x['type']}", inline=True)

	return embed_info