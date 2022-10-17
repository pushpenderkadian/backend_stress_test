import requests
import base64
import json,random,string,datetime,time

auth=""
c_cid=""
aut_api = "https://auth.api.edvora.me/"
class_api = "https://classrooms.api.edvora.me/"

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
    print("Logging in...")
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

def submit_assignment(id):
    print("Submitting assignment...")
    requests.post(f"https://classrooms.api.edvora.me/classroom/assignments/{id}/submission", headers={'Authorization': auth, 'Classroom-Id': c_cid}, json={"attachments":[]})
    return requests.post(f"https://classrooms.api.edvora.me/classroom/assignments/{id}/submit", headers={'Authorization': auth, 'Classroom-Id': c_cid},json={})

def gen_opts():
    opts=[]
    for i in range(0,random.randint(2,8)):
        opts.append(''.join(random.choices(string.ascii_letters, k=100)))
    return opts
def gen_ques():
    ques=[]
    for i in range(0,random.randint(1,10)):
        ques.append({"question":''.join(random.choices(string.ascii_letters, k=100)),"options":gen_opts()})
    return ques

def launch_poll(id):
    return requests.post(f"https://classrooms.api.edvora.me/classroom/polls/{id}/launch", headers={'Authorization': auth, 'Classroom-Id': c_cid}, json={})
pollss=[]

def gen_ans(n):
    arr=[]
    for i in range(0,n):
        arr.append(random.randint(0,1))
    return arr

def submit_poll(id,ques):
    return requests.post(f"https://classrooms.api.edvora.me/classroom/polls/{id}/submit", headers={'Authorization': auth, 'Classroom-Id': c_cid}, json={"answers":gen_ans(ques)})

def create_polls(data):
    print("Creating a poll...")
    return requests.post(class_api + 'classroom/polls', headers={'Authorization': auth, 'Classroom-Id': c_cid}, json=data)

usersdata=[]
usersdata.append(create_user(0).json())
auth=login(usersdata[0]["username"],"00")

#create 10 student accounts
for i in range(10):
    usersdata.append(create_user(1).json())

c_cid=create_classroom(''.join(random.choices(string.ascii_letters, k=20)))
print("Classroom created with id: "+c_cid)

print(usersdata)
# add members to classroom
usernames=[]
for i in range(1,len(usersdata)):
    usernames.append(usersdata[i]["username"])
add_members({"members":usernames})

# create 600 feed
print("creating 600 feed posts")
for i in range(0,600):
    data={"content": ''.join(random.choices(string.ascii_letters, k=1000))}
    create_feeds(data)
    print("feed post "+str(i)+" created")

# create 600 materials
arr=["note","syllabus"]
arr2=[True,False]
for i in range(0,600):
    data={"title": ''.join(random.choices(string.ascii_letters, k=100)),"type":random.choice(arr),"description": ''.join(random.choices(string.ascii_letters, k=1000)),"post_to_feed":random.choice(arr2)}
    create_materials(data)
    print("material "+str(i)+" created")

# create 600 assignments
assigns=[]
for i in range(0,600):
    data={"title": ''.join(random.choices(string.ascii_letters, k=100)),"description": ''.join(random.choices(string.ascii_letters, k=1000)),"due_date":int(datetime.datetime.now().timestamp())+random.randint(99999,9999999),"points":{"grading_type":"overall","points":100},"post_to_feed":random.choice(arr2)}
    assigns.append(create_assignments(data).json())
    print("assignment "+str(i)+" created")

# submit assignments
for i in range(1,len(usersdata)):
    auth=login(usersdata[i]["username"],"00")
    for j in assigns:
        submit_assignment(j["_id"])
        print("assignment submitted by "+usersdata[i]["username"])
auth=login(usersdata[0]["username"],"00")


#create 600 polls
for i in range(0,600):
    data={"title": "".join(random.choices(string.ascii_letters, k=100)),"questions":gen_ques(),"post_to_feed":random.choice(arr2)}
    pollss.append(create_polls(data).json())
    print("poll "+str(i)+" created")

#publish polls

for i in pollss:
    launch_poll(i["_id"])

#submit polls
for i in range(1,len(usersdata)):
    auth=login(usersdata[i]["username"],"00")
    for j in pollss:
        print(submit_poll(j["_id"],len(j["questions"])))
        print("Poll submitted by "+usersdata[i]["username"])
auth=login(usersdata[0]["username"],"00")






