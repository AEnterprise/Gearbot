from random import randint
import asyncio

from Other.Handlers import SocketNamespace

from Other import BackendUtils

class BotStats(SocketNamespace):
    async def on_connect(self, sid, environ):
        pass

    async def on_disconnect(self, sid):
        pass
    
    async def on_get(self, sid, data):
        # Temporary until guilds work
        verified_status = await self.verify_client(data)
        await self.emit("api_response",
            # Format is [uptime(s), commandCount, messageCount, guildCount, 
            # errorCount, totalUserCount, uniqueUserCount, tacoTime]
            data = ["0 Days, 5 Hours, 6 Minutes, 24 Seconds", 35, 45, 55, 65, 75, 37, 8500000]
        )
        # Testing liveness code
        while True:
            await self.emit("api_response", 
                data = ["0 Days, 5 Hours, 6 Minutes, 24 Seconds", randint(0, 100),
                    randint(0, 1000000), randint(0, 100), randint(0, 100), randint(0, 10), randint(0, 100), randint(0, 1000000)]
            )
            await asyncio.sleep(2)