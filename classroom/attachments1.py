import requests
import base64
import json,random,string,datetime,time

auth="eyJ0b2tlbiI6ImM0ZmFmYTQ5LTBkMDktNGExMy1hMzc5LTVlMTI2NjgxODI3MiIsInVzZXJuYW1lIjoiaGVsbG9wMjEiLCJvcmdhbml6YXRpb25faWQiOiIxMDEiLCJzZXNzaW9uX2lkIjoiZDI1ZGUzMzktNTQxNC00YTdhLWEyMjMtMjE2ZWY5OWVlNTIzIiwicm9sZV9pZCI6IjYyMDExMDUyYWFkYmNjMTQ0MmI0YjE1OSJ9"
c_cid="634ed7794938e6a5a5b232b9"
aut_api = "https://auth.api.edvora.me/"
class_api = "https://classrooms.api.edvora.me/"

timstmp=1666194600


def add_attachment(nfs=1):
    nrid=requests.post(f"https://files.api.edvora.me/upload/record?no_of_files={nfs}", headers={'Authorization': auth})
    print(nrid.content)
    print(nrid.status_code)    
    print(nrid.json())
    print("========================")
    nrid=nrid.json()["record_id"]

    nflid=requests.post(f"https://files.api.edvora.me/upload/local/new?record_id={nrid}&no_of_files={nfs}", headers={'Authorization': auth},json={"classroom_id":c_cid,"filename":"rtimeline7.png","filesize": 59782,"mimetype":"image/png","type":"feed"})
    print(nflid.content)
    print(nflid.status_code)    
    print(nflid.json())
    presurl=nflid.json()["presigned_url"]
    nflid1=nflid.json()["filekey"]
    print("=========================")

    aws=requests.put(presurl)
    print(aws.content)
    print(aws.status_code)
    print("=========================")
    complt=requests.post(f"https://files.api.edvora.me/upload/local/complete?key={nflid1}&record_id={nrid}",headers={'Authorization': auth})
    # print(complt)
    print(complt.content)
    print(complt.status_code)
    print(complt.json())
    print("=========================")
    rslt=[]
    rslt.append(nrid)
    rslt.append(nflid1)
    return rslt
def create_user(typ):
    username=''.join(random.choices(string.ascii_letters, k=20))
    arr=["62011052aadbcc1442b4b159","6201106aaadbcc1442b4b15a"]
    data={
    "username": username,
    "full_name": username,
    "date_of_birth": 5695889,
    "gender": "male",
    "email_address": f"{username}@fgdre.team",
    "mobile_number": username+"12",
    "nationality": "Edvorian",
    "address": "Edvora HQ",
    "password": "00",
    "when_accepted_terms": 5695889,
    "profile_key": "6755941390055587",
    "role_id": arr[typ],
    "organization_id": "101"
}
    return requests.post(aut_api + 'register', json=data)


def login(username,password):
    print("Logging in.."+username)
    req = requests.post(aut_api + 'login', json={'username': username, 'password': password})
    return base64.b64encode(req.content).decode('utf-8')
    # return req.json()

def create_classroom(cname):
    print("Creating a classroom...")
    data={"classroom_name":cname,"section":"d","subject_code":"d","cover":{"logo":0,"color":"#9002B4"}}
    resp= (requests.post(class_api + 'classrooms', headers={'Authorization': auth}, json=data)).json()
    return resp["_id"]

def add_members(data):
    print("Adding members...")
    return requests.post(class_api + 'classroom/members', headers={'Authorization': auth, 'Classroom-Id': c_cid}, json=data)
def create_feeds(data):
    print("Creating a feed...")
    return requests.post(class_api + 'classroom/feed', headers={'Authorization': auth, 'Classroom-Id': c_cid}, json=data)

def create_materials(data):
    print("Creating a material...")
    return requests.post(class_api + 'classroom/materials/syllabus', headers={'Authorization': auth, 'Classroom-Id': c_cid}, json=data)

def create_assignments(data):
    print("Creating an assignment...")
    return requests.post(class_api + 'classroom/assignments', headers={'Authorization': auth, 'Classroom-Id': c_cid}, json=data)

# usersdata=[]
# usersdata.append(create_user(0).json())
# auth=login(usersdata[0]["username"],"00")
file=open("classroom/response1"+".txt","w")
# file.write("Username: "+usersdata[0]["username"]+"\nPassword: 00\n")
# file.write("Auth: "+auth+"\n")
# #create 10 student accounts
# c_cid=create_classroom(''.join(random.choices(string.ascii_letters, k=20)))
# print("Classroom created with id: "+c_cid)
# file.write("Classroom id: "+c_cid+"\n")

# # add members to classroom
# usernames=[]
# for i in range(1,len(usersdata)):
#     usernames.append(usersdata[i]["username"])
# add_members({"members":usernames})

# create 600 feed
succs=0
failed=0
for i in range(0,1):
    abc=add_attachment()
    fids=[]
    fids.append(abc[1])
    data={"attachments":fids,"content": ''.join(random.choices(string.ascii_letters, k=1000)),"record_id": abc[0]}
    stats=create_feeds(data)
    if(stats.status_code==200):
        succs+=1
    else:
        failed+=1
        file.write("Failed to create feed post: "+str(stats.content)+"\n")
file.write("Successfully Created "+str(succs)+" feed posts\n")
file.write("=======================================================\n")


file.close()






