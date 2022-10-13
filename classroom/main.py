import requests
import base64
import json,random,string

auth=""
c_cid=""
aut_api = "https://auth.api.edvora.me/"
class_api = "https://classrooms.api.edvora.me/"
def login(username,password):
    print("Logging in...")
    req = requests.post(aut_api + 'login', json={'username': username, 'password': password})
    return base64.b64encode(req.content).decode('utf-8')
def create_classroom(cname):
    print("Creating a classroom...")
    data={"classroom_name":cname,"section":"d","subject_code":"d","cover":{"logo":0,"color":"#9002B4"}}
    resp= (requests.post(class_api + 'classrooms', headers={'Authorization': auth}, json=data)).json()
    return resp["_id"]

def create_feeds(data):
    print("Creating a feed...")
    return requests.post(class_api + 'classroom/feed', headers={'Authorization': auth, 'Classroom-Id': c_cid}, json=data)

def create_materials(data):
    print("Creating a material...")
    return requests.post(class_api + 'classroom/materials/syllabus', headers={'Authorization': auth, 'Classroom-Id': c_cid}, json=data)

def create_assignments(data):
    print("Creating an assignment...")
    return requests.post(class_api + 'classroom/assignments', headers={'Authorization': auth, 'Classroom-Id': c_cid}, json=data)

def create_polls(data):
    print("Creating a poll...")
    return requests.post(class_api + 'classroom/polls', headers={'Authorization': auth, 'Classroom-Id': c_cid}, json=data)


auth=login("classrm","00")
c_cid=create_classroom("classssss")
print("Classroom created with id: "+c_cid)
print("creating 600 feed posts")
for i in range(0,600):
    data={"content": ''.join(random.choices(string.ascii_letters, k=1000))}
    create_feeds(data)
    print("feed post "+str(i)+" created")

arr=["note","syllabus"]
arr2=[True,False]
for i in range(0,600):
    data={"title": ''.join(random.choices(string.ascii_letters, k=100)),"type":random.choice(arr),"description": ''.join(random.choices(string.ascii_letters, k=1000)),"post_to_feed":random.choice(arr2)}
    create_materials(data)
    print("material "+str(i)+" created")

for i in range(0,600):
    data={"title": ''.join(random.choices(string.ascii_letters, k=100)),"description": ''.join(random.choices(string.ascii_letters, k=1000)),"due_date":1698777000,"points":{"grading_type":"overall","points":100},"post_to_feed":random.choice(arr2)}
    create_assignments(data)
    print("assignment "+str(i)+" created")

for i in range(0,600):
    data={"title": "".join(random.choices(string.ascii_letters, k=100)),"is_live":True,"questions":[{"question":"".join(random.choices(string.ascii_letters, k=100)),"options":["".join(random.choices(string.ascii_letters, k=100)),"".join(random.choices(string.ascii_letters, k=100)),"".join(random.choices(string.ascii_letters, k=100)),"".join(random.choices(string.ascii_letters, k=100))]},{"question":"".join(random.choices(string.ascii_letters, k=100)),"options":["".join(random.choices(string.ascii_letters, k=100)),"".join(random.choices(string.ascii_letters, k=100)),"".join(random.choices(string.ascii_letters, k=100)),"".join(random.choices(string.ascii_letters, k=100))]}],"post_to_feed":random.choice(arr2)}
    create_polls(data)
    print("poll "+str(i)+" created")







