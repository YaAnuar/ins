import aiohttp
import asyncio

async def write_json_to_file(key, url):
	lock = asyncio.Lock()
	async with lock:
	    async with aiohttp.ClientSession() as session:
	    	async with session.get(url) as response:
	            with open("file.txt", key) as city:
	            	city.write(str(await response.json()))	
	            	city.write('\n')
	            	city.write('\n')
	            	city.write('\n')



async def main():
	await write_json_to_file('w','http://samples.openweathermap.org/data/2.5/forecast?id=2643743&appid=b1b15e88fa797225412429c1c50c122a1')
	await write_json_to_file('a','http://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1')
	await write_json_to_file('a','http://samples.openweathermap.org/data/2.5/forecast?id=1526384&appid=b1b15e88fa797225412429c1c50c122a1')

loop = asyncio.get_event_loop()
loop.run_until_complete(main())