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
	await write_json_to_file('a','http://samples.openweathermap.org/data/2.5/forecast?id=2643743&appid=b1b15e88fa797225412429c1c50c122a1')
	await write_json_to_file('a','http://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1')
	await write_json_to_file('a','http://samples.openweathermap.org/data/2.5/forecast?id=1526384&appid=b1b15e88fa797225412429c1c50c122a11')
	# correct way
	#await write_json_to_file('w','https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid=d9d3c1fda92985791ef7d4d5b9fe5d88')
	#await write_json_to_file('a','https://api.openweathermap.org/data/3.0/onecall?lat=55.75&lon=37.61&exclude=hourly,daily&appid=d9d3c1fda92985791ef7d4d5b9fe5d88')
	#await write_json_to_file('w','https://api.openweathermap.org/data/3.0/onecall?lat=43.23&lon=76.88&exclude=hourly,daily&appid=d9d3c1fda92985791ef7d4d5b9fe5d88')



loop = asyncio.get_event_loop()
loop.run_until_complete(main())