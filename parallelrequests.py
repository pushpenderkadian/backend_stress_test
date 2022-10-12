import httpx
import asyncio
import time
import base64

file=open("responses.json","w")
file2=open("authtokens.json","w")
async def get_async(url):
    async with httpx.AsyncClient() as client:
        return await client.post("https://auth.api.edvora.me/login", json=url)

# urls = ["http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata","http://worldtimeapi.org/api/timezone/Asia/Kolkata"]
urls = [{"username": "hellop0", "password": "00"},{"username": "hellop1", "password": "00"},{"username": "hellop2", "password": "00"},{"username": "hellop3", "password": "00"},{"username": "hellop4", "password": "00"},{"username": "hellop5", "password": "00"},{"username": "hellop6", "password": "00"}]
# urls=[{"username": "hellop0", "password": "00"}]
async def launch():

    resps = await asyncio.gather(*map(get_async, urls))
    data = [resp for resp in resps]
    data2 = [resp for resp in resps]
    file.write(str(data))
    file.close()
    for i in data:
        if("<Response [200 OK]>" in str(data2[data.index(i)])):
            file2.write("\""+base64.b64encode(i.content).decode('utf-8')+ "\",")
            file2.write("\n")
    
    for status_code in data2:
        print(status_code)

tm1 = time.perf_counter()

asyncio.run(launch())

tm2 = time.perf_counter()
print(f'Total time elapsed: {tm2-tm1:0.2f} seconds')