import httpx
import asyncio
import time
import base64

file=open("responseccr.json","w")
async def get_async(url):
    async with httpx.AsyncClient() as client:
        return await client.post("https://classrooms.api.edvora.me/classrooms", headers={"Authorization":url},json=cons)

urls = ["eyJ0b2tlbiI6IjU0NzBiMDkwLWE4MmYtNDIxNi04Yjc2LWM0NDc1MWRkNWVkYyIsInVzZXJuYW1lIjoiaGVsbG9wMCIsIm9yZ2FuaXphdGlvbl9pZCI6IjEwMSIsInNlc3Npb25faWQiOiJlMTEwODI0Yy1hZjM4LTRlNDEtODJlYi1kYzJjODVkMzFhOTUiLCJyb2xlX2lkIjoiNjIwMTEwNTJhYWRiY2MxNDQyYjRiMTU5In0=","eyJ0b2tlbiI6IjgzZWI1NjQ1LTFjMjktNDRjYy1iYThiLTU1ODdiZDk0NDZjOCIsInVzZXJuYW1lIjoiaGVsbG9wMSIsIm9yZ2FuaXphdGlvbl9pZCI6IjEwMSIsInNlc3Npb25faWQiOiJiZGJkZmZiYi1lNmY5LTQ0MDUtYjg1MC1jMTgwOGY0ODQ1YzgiLCJyb2xlX2lkIjoiNjIwMTEwNTJhYWRiY2MxNDQyYjRiMTU5In0=","eyJ0b2tlbiI6ImE2MGFhZWI4LTQ3NDMtNDIwNS1hNTA4LThmYTZkYzI5Mzg0ZCIsInVzZXJuYW1lIjoiaGVsbG9wMiIsIm9yZ2FuaXphdGlvbl9pZCI6IjEwMSIsInNlc3Npb25faWQiOiJhMDA4MDdmNy0xYzczLTQyM2UtOGQ4Ni01MmYxMDA3ZjIxOGQiLCJyb2xlX2lkIjoiNjIwMTEwNTJhYWRiY2MxNDQyYjRiMTU5In0=","eyJ0b2tlbiI6IjE4ZDYwMzBjLTFiNjktNDRjZS05ODYwLWFmMzBkYzk4ZGU1NiIsInVzZXJuYW1lIjoiaGVsbG9wMyIsIm9yZ2FuaXphdGlvbl9pZCI6IjEwMSIsInNlc3Npb25faWQiOiIzZjI0Y2JjNy1hMjYxLTQwNzUtODE2OC0yMWJiMGU3YWZhY2UiLCJyb2xlX2lkIjoiNjIwMTEwNTJhYWRiY2MxNDQyYjRiMTU5In0=","eyJ0b2tlbiI6ImZmZjI1ZDQzLTZlYmEtNDUxZS05NTcwLTFkYTgyZDg1YjRhOSIsInVzZXJuYW1lIjoiaGVsbG9wNCIsIm9yZ2FuaXphdGlvbl9pZCI6IjEwMSIsInNlc3Npb25faWQiOiI0YTVkZjRjOC1lY2ZmLTRiZDQtODAzZS1jNWNiNDQxMmFjMTciLCJyb2xlX2lkIjoiNjIwMTEwNTJhYWRiY2MxNDQyYjRiMTU5In0=","eyJ0b2tlbiI6ImI2ODk4N2NhLTIzMGYtNGExZC04NGM5LTFmNDRiZWFjYmU2NyIsInVzZXJuYW1lIjoiaGVsbG9wNSIsIm9yZ2FuaXphdGlvbl9pZCI6IjEwMSIsInNlc3Npb25faWQiOiI3NDc5OTA4My1iODI4LTQyZWItYTFiOS0wOGIyZWY1MmRiNGMiLCJyb2xlX2lkIjoiNjIwMTEwNTJhYWRiY2MxNDQyYjRiMTU5In0=","eyJ0b2tlbiI6IjNjYTc3ZGExLWYyOTQtNDRhMy04MjU3LTVlZjMxN2VmMmI1ZSIsInVzZXJuYW1lIjoiaGVsbG9wNiIsIm9yZ2FuaXphdGlvbl9pZCI6IjEwMSIsInNlc3Npb25faWQiOiJiOWZhMTE5Zi05OGFmLTRmYzEtOTAwOC02MWE5YmFiOWE2NDEiLCJyb2xlX2lkIjoiNjIwMTEwNTJhYWRiY2MxNDQyYjRiMTU5In0="]
cons={"classroom_name":"asdkkje","section":"d","subject_code":"d","cover":{"logo":0,"color":"#9002B4"}}
async def launch():

    resps = await asyncio.gather(*map(get_async, urls))
    data = [resp.json() for resp in resps]
    data2 = [resp for resp in resps]
    file.write(str(data))
    file.close()
    
    for status_code in data2:
        print(status_code)

tm1 = time.perf_counter()

asyncio.run(launch())

tm2 = time.perf_counter()
print(f'Total time elapsed: {tm2-tm1:0.2f} seconds')