import requests
import base64
import json,random,string,datetime,time

auth=""
c_cid=""
aut_api = "https://auth.api.edvora.me/"
class_api = "https://classrooms.api.edvora.me/"

timstmp=1666194600


def add_attachment(nfs):
    file.write("adding attachment : "+str(nfs)+"\n")
    nrid=requests.post(f"https://files.api.edvora.me/upload/record?no_of_files={nfs}", headers={'Authorization': auth})
    nrid=nrid.json()["record_id"]
    nflid1=[]

    nflid=["5a15d31d-dc1f-4637-9bb2-067ca2acf0c0","d9d25115-9017-4010-8b97-a0a7cfc87949","7c411e0d-2b5b-4635-87c9-9d660eb7e1ee","fd4193b0-9436-40ca-a6f9-b787c4c9f2a8","1d1bc0f4-369d-41a4-8898-c6c90af369a1","66b486fc-ab67-48d3-be52-85bc4d7fcf2a","2c025a70-fc08-4193-9a2d-af9e0e46cab9","a867a3ea-1a5e-45a7-b8d9-87b57c07e829","2492deb0-700a-4250-b0ef-b395467e10e0","0b95eb14-a868-4723-877d-2011d7694d8b"]
    for i in range(nfs):
        nflid1.append(nflid[i])
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
def gen_opts():
    opts=[]
    for i in range(0,random.randint(2,8)):
        opts.append(''.join(random.choices(string.ascii_letters, k=100)))
    return opts
def gen_ques():
    ques=[]
    for i in range(0,random.randint(1,10)):
        file.write("adding question : "+str(i)+"\n")
        abc=add_attachment(random.randint(0,10))
        ques.append({"question":''.join(random.choices(string.ascii_letters, k=100)),"options":gen_opts(),"attachments":abc[1],"record_id": abc[0]})
    return ques

def create_polls(data):
    print("Creating a poll...")
    return requests.post(class_api + 'classroom/polls', headers={'Authorization': auth, 'Classroom-Id': c_cid}, json=data)
pollss=[]

#comment this section if you want to use pre-existing user
usersdata=[]
usersdata.append(create_user(0).json())
auth=login(usersdata[0]["username"],"00")
file=open("classroom/response2"+".txt","w")
file.write("Username: "+usersdata[0]["username"]+"\nPassword: 00\n")
file.write("Auth: "+auth+"\n")
#create 10 student accounts
c_cid=create_classroom(''.join(random.choices(string.ascii_letters, k=20)))
print("Classroom created with id: "+c_cid)
file.write("Classroom id: "+c_cid+"\n")


#uncomment this section to use pre-existing accounts
usrname="hellop24"
passwrd="00"

c_cid="634ed7794938e6a5a5b232b9"


auth=login(usrname,passwrd)
file=open(usrname+".txt","w")


file.write("Classroom id: "+c_cid+"\n")


##############################################

# create 600 feed
succs=0
failed=0
for i in range(0,2):
    file.write("Creating feed "+str(i)+"\n")
    abc=add_attachment(random.randint(1,10))
    
    data={"attachments":abc[1],"content": ''.join(random.choices(string.ascii_letters, k=1000)),"record_id": abc[0]}
    stats=create_feeds(data)
    if(stats.status_code==200):
        succs+=1
    else:
        failed+=1
        file.write("Failed to create feed post: "+str(stats.content)+"\n")
file.write("Successfully Created "+str(succs)+" feed posts\n")
file.write("=======================================================\n")

succs=0
failed=0
arr=["note","syllabus"]
arr2=[True,False]
for i in range(0,2):
    file.write("Creating material "+str(i)+"...\n")
    abc=add_attachment(random.randint(1,10))
    data={"attachments":abc[1],"record_id": abc[0],"title": ''.join(random.choices(string.ascii_letters, k=100)),"type":random.choice(arr),"description": ''.join(random.choices(string.ascii_letters, k=100)),"post_to_feed":random.choice(arr2)}
    stats=create_materials(data)
    if(stats.status_code==200):
        succs+=1
    else:
        failed+=1
        file.write("Failed to create material: "+str(stats.content)+"\n")
file.write("Successfully Created "+str(succs)+" materials\n")
file.write("=======================================================\n")

# create 600 assignments
assigns=[]
succs=0
failed=0
for i in range(0,2):
    file.write("Creating assignment "+str(i)+"...\n")
    abc=add_attachment(random.randint(1,10))
    data={"attachments":abc[1],"record_id": abc[0],"title": ''.join(random.choices(string.ascii_letters, k=100)),"description": ''.join(random.choices(string.ascii_letters, k=1000)),"due_date":int(datetime.datetime.now().timestamp())+random.randint(99999,9999999),"points":{"grading_type":"overall","points":100},"post_to_feed":random.choice(arr2)}
    stats=create_assignments(data)
    if(stats.status_code==200):
        assigns.append(stats.json())
        succs+=1
    else:
        failed+=1
        file.write("Failed to create assignment: "+str(stats.content)+"\n")
file.write("Successfully Created "+str(succs)+" assignments\n")
file.write("=======================================================\n")

#create 600 polls
succs=0
failed=0
for i in range(0,2):
    file.write("Creating poll "+str(i)+"...\n")
    data={"title": "".join(random.choices(string.ascii_letters, k=100)),"questions":gen_ques(),"post_to_feed":random.choice(arr2)}
    stats=create_polls(data)
    if(stats.status_code==200):
        pollss.append(stats.json())
        succs+=1
    else:
        failed+=1
        file.write("Failed to create poll: "+str(stats.content)+"\n")
file.write("Successfully Created "+str(succs)+" polls\n")


file.close()






