import string
import requests,base64,random

auth=""
c_cid=""
aut_api = "https://auth.api.edvora.me/"
a_url="https://timetable.api.edvora.me/attendance"
mem_url="https://classrooms.api.edvora.me/classroom/members/by_roles"
eves_url="http://timetable.api.edvora.me/timetables/classroom"
all_att={}

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
    patt=get_att()
    print("classroom id: "+id+"\ndate: "+str(dtt)+"\nevent id: "+id)
    resp= (requests.post(a_url, headers={'authorization': auth}, json={"event_id": id,"participants": patt,"date": dtt}))
    if(resp.status_code==202):
        for i in all_att:
            if i["event_id"]==id and i["start_datetime"]==dtt:
                print("Attendance already marked for this event\nupdating attendance...")
                resp=(requests.patch("https://timetable.api.edvora.me/attendance/"+i["attendance_id"], headers={'authorization': auth}, json={"participants": patt}))

    return resp

def fetch_all_attendance(time1,time2):
    resp= (requests.get(f"https://timetable.api.edvora.me/fetchattendance/classroom/{c_cid}?&from_date={time1}&until={time2}", headers={'authorization': auth})).json()
    return resp

def fetch_all_events(time1,time2):
    print("Fetching events...")
    resp= (requests.get(eves_url+f"/{c_cid}?start_date={time1}&end_date={time2}", headers={'authorization': auth})).json()
    eves={}
    for i in resp:
        if i["rrule"]==None:
            x=[i["start_datetime"]]
            eves[i["_id"]]=x
        if i["rrule"]!=None:
            eves[i["_id"]]=i["rrule"]
    globals().update(all_att=fetch_all_attendance(time1,time2))
    return eves


auth=login("hellop19","00")
c_cid="635dca1030d8e11765990329"
eves=fetch_all_events(1667241000,1669746600)
# print(eves)
for i in eves:
    for j in eves[i]:
        resp=mark_att(i,j)
        print(f"response for marking event {i} : "+str(resp.status_code))
