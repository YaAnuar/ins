import aiohttp
import asyncio
import json

async def write_json_to_file(url):
    async with aiohttp.ClientSession() as session:
    	async with session.get(url) as response:
            with open("London.txt", "w") as london:
            	london.write(str(await response.json()))	


async def main():
	await write_json_to_file('http://samples.openweathermap.org/data/2.5/forecast?id=2643743&appid=b1b15e88fa797225412429c1c50c122a1')
	await write_json_to_file('http://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1')
	await write_json_to_file('http://samples.openweathermap.org/data/2.5/forecast?id=1526384&appid=b1b15e88fa797225412429c1c50c122a1')

loop = asyncio.get_event_loop()
loop.run_until_complete(main())