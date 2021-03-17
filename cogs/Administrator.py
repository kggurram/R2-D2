#import libraries
from discord.ext import commands
import discord

#Admin commands class
class Administrator(commands.Cog):
    def __init__(self, r2d2):
        self.r2d2 = r2d2
    
    #kick command (only for Admin, Mod, or Bot roles)
    @commands.command()
    @commands.has_any_role("Supreme Leaders, Emperor, Administrator, Admin, Moderator, Bot") #if user has given role
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason) #kick
    
    #ban command (only for Admin, Mod, or Bot roles)
    @commands.command()
    @commands.has_any_role("Supreme Leaders, Emperor, Administrator, Admin, Moderator, Bot") #if user has given role
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason) #ban
        await ctx.send(f"{member.mention}, twee-vwoop ZZT! >:(") #R2-D2 sends an angry message

    #unban command (only for Admin, Mod, or Bot roles)
    @commands.command()
    @commands.has_any_role("Supreme Leaders, Emperor, Administrator, Admin Moderator, Bot") #if user has given role
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans() #list of banned members
        member_name, member_discriminator = member.split("#") #splits characters around hashtag ie. XXXXX#12345 --> name = XXXXXX, discriminator = 12345

        for ban_entry in banned_users: #for each entry in list of banned members
            user = ban_entry.user

            if(user.name, user.discriminator) == (member_name, member_discriminator): #if given name matches entry,
                await ctx.guild.unban(user) #unban
                await ctx.send(f"{user.mention}, zzt beep :/") #R2-D2 is reluctant on welcoming them back
                return

#required setup def
def setup(r2d2):
    r2d2.add_cog(Administrator(r2d2))