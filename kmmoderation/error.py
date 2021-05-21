import discord
from discord.ext import commands
import traceback
import asyncio
import sys



class CommandErrorHandler(commands.Cog, name="Command Backend Helper"):
    """The backend helper for the Pogmas Base."""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """The event triggered when an error is raised while invoking a command.
        Parameters
        ------------
        ctx: commands.Context
            The context used for command invocation.
        error: commands.CommandError
            The Exception raised.
        """

        # This allows us to call the default error handler at any time
        async def ee():
            try:
                cog_name = ctx.cog.qualified_name
            except Exception as e:
                cog_name = "None"
            print(f'Ignoring exception in command {ctx.command}:', file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
            py_error = traceback.format_exception(type(error), error, error.__traceback__)
            py_error = ''.join(py_error)
            embed = discord.Embed(title="⚠ حدث خطأ.", colour=discord.Colour.red(), description="لازم يكون معك رولات ._.")
            await ctx.send(embed=embed)

        # This prevents any commands with local handlers being handled here in on_command_error.
        if hasattr(ctx.command, 'on_error'):
            return

        # This prevents any cogs with an overwritten cog_command_error being handled here.
        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        ignored = (commands.CommandNotFound)

        # Allows us to check for original exceptions raised and sent to CommandInvokeError.
        # If nothing is found. We keep the exception passed to on_command_error.
        error = getattr(error, 'original', error)

        # Anything in ignored will return and prevent anything happening.
        if isinstance(error, ignored):
            return

        # For this error example we check to see where it came from...


        elif isinstance(error, discord.ext.commands.DisabledCommand):
            await ctx.send("فشل تنفيذ الأمر: الأمر معطل ولا يمكن تشغيله ، معذرةً.")

        elif isinstance(error, discord.ext.commands.CommandOnCooldown):
            await ctx.send(f"واو هناك {ctx.author.name}, أنت تسير بسرعة كبيرة. حاول مرة أخرى في: {int(ctx.command.get_cooldown_retry_after(ctx))}s.")

        elif isinstance(error, discord.ext.commands.MaxConcurrencyReached):
            if ctx.command.qualified_name in ('cut'):
                await ctx.send("فشل تنفيذ الأمر: كل يدي مشغولة الآن ؛ يمكنني فقط الإعجاب بـ 3 تخفيضات لكل خادم في وقت واحد!")



        elif isinstance(error, discord.ext.commands.MissingRequiredArgument):
            await ctx.send("فشل تنفيذ الأمر:  مفقودة! الاستخدام الصحيح:")
            await ctx.send_help(ctx.command)


        elif isinstance(error, discord.Forbidden):
            await ctx.send("فشل تنفيذ الأمر: لا أستطيع أن أفعل ما تريد مني أن أفعله لأنني لا أمتلك أذونات. أعطني أذونات وحاول مرة أخرى.")

        elif isinstance(error, discord.NotFound):
            await ctx.send("فشل تنفيذ الأمر: يبدو أنني لا أجد ذلك. تأكد من صحة المعرف وحاول مرة أخرى.")

        elif isinstance(error, asyncio.TimeoutError):
            await ctx.message.add_reaction('⌛')
        else:
            # All other Errors not returned come here. And we can just print the default TraceBack.
            await ee()


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))