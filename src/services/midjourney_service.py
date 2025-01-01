from .discord_service import DiscordService

class MidjourneyService:
    def __init__(self, discord_service: DiscordService):
        self.discord = discord_service

    async def generate_image(self, prompt, channel_id):
        """Generate image using Midjourney"""
        command = f'/imagine {prompt}'
        return await self.discord.send_command(command, channel_id)

    async def upscale_image(self, message_id, index, channel_id):
        """Upscale a specific image variation"""
        command = f'/up {message_id} {index}'
        return await self.discord.send_command(command, channel_id)

    async def vary_image(self, message_id, index, channel_id):
        """Create variation of a specific image"""
        command = f'/vary {message_id} {index}'
        return await self.discord.send_command(command, channel_id)