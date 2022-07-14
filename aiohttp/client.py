import aiohttp
import asyncio
import json

async def main():
    async with aiohttp.ClientSession() as session:
    	async with session.get('http://samples.openweathermap.org/data/2.5/forecast?id=2643743&appid=b1b15e88fa797225412429c1c50c122a1') as response:
            with open("London.txt", "w") as london:
            	london.write(str(await response.json()))
    async with aiohttp.ClientSession() as session:
        async with session.get('http://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1') as response:
            with open("Moscow.txt", "w") as Moscow:
            	Moscow.write(str(await response.json()))
    async with aiohttp.ClientSession() as session:
        async with session.get('http://samples.openweathermap.org/data/2.5/forecast?id=1526384&appid=b1b15e88fa797225412429c1c50c122a1') as response:
            with open("Almaty.txt", "w") as Almaty:
            	Almaty.write(str(await response.json()))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())