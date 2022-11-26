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
def genrid(n):
    url="https://files.api.edvora.me/upload/record?no_of_files="+str(n)
    rslt=requests.post(url,headers={'authorization':auth,'classroom-id':c_cid}).json()
    return rslt['record_id']

def uploadurl():
    rid=genrid(1)
    rslt=requests.post(f"https://files.api.edvora.me/upload/url/new?record_id={rid}&no_of_files=1",headers={'authorization':auth,'classroom-id':c_cid},json={"url":"https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg","type":"others","classroom_id":c_cid})
    return rslt.json()

username="stress15"
password='00'
auth=login(username,password)
c_cid="6378f4f95d5f9e3e7a2ee26d"
header={'authorization':auth,'classroom-id':c_cid}
# for i in range(1,101):
#     d=uploadurl()
#     data={"content":"scheduled post "+str(i),"attachments":[d['file_key']],"scheduled_at":1672032960}
#     rslt=requests.post("https://classrooms.api.edvora.me/classroom/feed?record_id="+d['record_id'],headers=header,json=data)
#     print(rslt)


# for i in range(1,101):
#     d=uploadurl()
#     data={"title":"scheduled note "+str(i),"description":"scheduled note "+str(i),"attachments":[d['file_key']],"scheduled_at":1672032960}
#     print(data)
#     rslt=requests.post("https://classrooms.api.edvora.me/classroom/materials/note?record_id="+d['record_id'],headers=header,json=data)
#     print(rslt)

# for i in range(1,101):
#     d=uploadurl()
#     data={"title":"scheduled syllabus "+str(i),"description":"scheduled syllabus "+str(i),"attachments":[d['file_key']],"scheduled_at":1672032960}
#     print(data)
#     rslt=requests.post("https://classrooms.api.edvora.me/classroom/materials/syllabus?record_id="+d['record_id'],headers=header,json=data)
#     print(rslt)

for i in range(1,101):
    d=uploadurl()
    data={"title":"scheduled assignment "+str(i),"description":"scheduled assignment "+str(i),"due_date":1700978700,"points":{"grading_type":"overall","points":"99"},"attachments":[d['file_key']],"scheduled_at":1672032960}
    print(data)
    rslt=requests.post("https://classrooms.api.edvora.me/classroom/assignments?record_id="+d['record_id'],headers=header,json=data)
    print(rslt)
