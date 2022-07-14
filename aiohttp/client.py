import aiohttp
import asyncio

async def write_json_to_file(key, url):
	lock = asyncio.Lock()
	async with lock:
	    async with aiohttp.ClientSession() as session:
	    	async with session.get(url) as response:
	            with open("cities.txt", key) as city:
	            	city.write(str(await response.json()))	
	            	city.write('\n\n\n')



async def main():
	await write_json_to_file('w','http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=d9d3c1fda92985791ef7d4d5b9fe5d88')
	await write_json_to_file('a','http://api.openweathermap.org/data/2.5/weather?q=Moscow,ru&APPID=d9d3c1fda92985791ef7d4d5b9fe5d88')
	await write_json_to_file('a','http://api.openweathermap.org/data/2.5/weather?q=Almaty,kz&APPID=d9d3c1fda92985791ef7d4d5b9fe5d88')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())