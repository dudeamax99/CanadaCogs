import discord
import asyncio
from redbot.core import commands
from redbot.core.bot import Red
from redbot.core import Config, checks, commands
from discord.ext.commands import Bot
from datetime import datetime, timedelta

#Made by Dudeamax99#4646

class NeverHaveIEver(commands.Cog):
    def __init__(self, bot: Red):
        self.bot = bot

    @commands.command()
    async def NeverHaveIEver(self, ctx, *, word: str):
        try:
            wordi = word
            wordi = wordi.replace("<@","").replace("!","").replace(">","")
            try:
                message = await ctx.send(f"Never Have I Ever**{word}**.")
                pass
            try:
                await message.add_reaction("thumbsup")
            except:
                await ctx.send("I was unable to react. Please give me permission before using this command.")
                await message.delete()
                return
            users = []
            def check(reaction, user):
                return str(reaction) == "thumbsup" and user not in users and not user.bot and reaction.message.id == message.id
            while (ctx.message.created_at.timestamp() + 10) > datetime.utcnow().timestamp():
                try:
                    reaction, user = await self.bot.wait_for("reaction_add", check=check, timeout=5)
                    users.append(user)
                    await ctx.send(f"**{user.name}** has never**{word}**.")
                except:
                    pass
            if len(users) == 0:
                try:
                    await ctx.send(f"Everyone has **{word}**.")
            elif len(users) == 1:
                try:
                    await ctx.send(f"{len(users)} person has never **{word}**.")
            else:
                try:
                    await ctx.send(f"{len(users)} people have never **{word}**.")
        except Exception as e:
            print(e)
            pass
