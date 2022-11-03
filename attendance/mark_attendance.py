import string
import requests,base64,random

auth=""
c_cid=""
aut_api = "https://auth.api.edvora.me/"
a_url="https://timetable.api.edvora.me/attendance"
mem_url="https://classrooms.api.edvora.me/classroom/members/by_roles"
eves_url="http://timetable.api.edvora.me/timetables/classroom"

def login(username,password):
    print("Logging in.."+username)
    req = requests.post("https://auth.api.edvora.me/login", json={'username': username, 'password': password})
    return base64.b64encode(req.content).decode('utf-8')

def create_classroom(cname):
    print("Creating a classroom...")
    data={"classroom_name":cname,"section":"d","subject_code":"d","cover":{"logo":0,"color":"#9002B4"}}
    resp= (requests.post("https://classroom.api.edvora.me/" + 'classrooms', headers={'Authorization': auth}, json=data)).json()
    return resp["_id"]

def get_mems(cid):
    resp= (requests.get(mem_url, headers={'authorization': auth,"classroom-id": cid})).json()
    usrnams=[]
    for i in resp:
        x=i["members"]
        for j in x:
            usrnams.append(j["username"])
    return usrnams

def get_att():
    mems=get_mems(c_cid)
    att=[]
    apll=[0,1,2,3]
    remark=[''.join(random.choices(string.ascii_letters, k=100)),None]
    for i in mems:
        att.append({"username":i,"state": random.choice(apll),"remark": remark[random.randint(0,1)]})
    # print(att)
    return (att)
def mark_att(id,dtt):
    print("Marking attendance...")
    print("classroom id: "+id+"\ndate: "+str(dtt)+"\nevent id: "+id)
    resp= (requests.post(a_url, headers={'authorization': auth}, json={"event_id": id,"participants": get_att(),"date": dtt}))
    return resp

def fetch_only_non_recuring_events(time1,time2):
    print("Fetching events...")
    resp= (requests.get(eves_url+f"/{c_cid}?start_date={time1}&end_date={time2}", headers={'authorization': auth})).json()
    # print(resp)
    eves={}
    for i in resp:
        if i["rrule"]==None:
            eves[i["_id"]]=i["start_datetime"]
    return eves


auth=login("hellop19","00")
c_cid="635dca1030d8e11765990329"
eves=fetch_only_non_recuring_events(1667241000,1669746600)
for i in eves:
    resp=mark_att(i,eves[i])
    print(f"response for marking event {i} : "+str(resp.status_code))
# 
