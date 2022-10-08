import requests
import base64
import json

from random import randint, randrange

request = requests.Session()

aut_api = "https://auth.api.edvora.me/"
class_api = "https://classrooms.api.edvora.me/"
files_api = "https://files.api.edvora.me/"
timetable_api = "https://timetable.api.edvora.me/"

team = ["Dhruv","Shivani","Ritik","Ciddarth","Baraka","Muzammil","Samuel","Sahil","Naren","Rahul","Pushpit","Michelle","Lohith","Samish","Shivani0","Rohan","Pushpender","Yash","naren", "Ashita", "Amernath", "JayShree", "Prasanth", "Praveen"]

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. Why do we use it?It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).Where does it come from?Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32."
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/800px-Image_created_with_a_mobile_phone.png"

def requesttojson(request):
    return json.loads(request._content)

def createuserData(name, email):
    return {
        "username": name,
        "full_name": str(name).strip(),
        "date_of_birth": 5545454,
        "gender": "male",
        "email_address": str(email).strip(),
        "mobile_number": str(randint(100000000, 9999999999)),
        "nationality": "testing",
        "address": "weDonthave",
        "password": "00",
        "profile_key": "0909s090909",
        "role_id": "62011052aadbcc1442b4b159",
        "organization_id": "101"
    }

def registerUser(name, email):
    data = createuserData(name, email)
    r = requests.post("https://auth.api.edvora.me/register", json=data)
    if (r.status_code == 200):
        return r
    else:
        return False

def login(username, password):
    req = request.post(aut_api + 'login', json={'username': username, 'password': password})
    return base64.b64encode(req.content).decode('utf-8')

def createClass(auth, i):
    return request.post(class_api + 'classrooms', headers={'Authorization': auth}, json={
        "classroom_name": "Classroom - " + str(i),
        "section": "B" + str(i),
        "subject_code": "CH" + str(i),
        "cover": {
            "logo": 2,
            "color": "#FA53CB"
        }
    })

def joinClass(auth, c_id, users = []):
	return request.post(class_api + 'classroom/members', headers={'Authorization': auth, 'Classroom-Id': c_id}, json={'members': users})

def imageAttach(auth, c_id, type):
    attachment = []
    for x in range(0, 10):
        data = requesttojson(request.post(files_api + 'upload/url/new', headers={'Authorization': auth}, json={'url': image_url, 'classroom_id': c_id, 'type': type}))
        attachment.append(data["file_key"])
    return attachment

def createFeed(auth, c_id, i=0):
    body = str(i) + text
    attachment = imageAttach()
    return request.post(class_api + 'classroom/feed', headers={'Authorization': auth, 'Classroom-Id': c_id}, json={'content': body, 'attachments': attachment})

def createComment(auth, c_id, p_id, i=0):
	body = str(i) + text
	return request.post(class_api + 'classroom/feed/' + p_id + '/comment', headers={'Authorization': auth, 'Classroom-Id': c_id}, json={'content': body})

def createSyllabus(auth, c_id, i=0):
    body = str(i) + text
    attachment = imageAttach()
    return request.post(class_api + 'classroom/materials/syllabus', headers={'Authorization': auth, 'Classroom-Id': c_id}, json={'title': body, "description": body, 'attachments': attachment})

def createNotes(auth, c_id, i=0):
    body = str(i) + text
    # attachment = imageAttach()
    return request.post(class_api + 'classroom/materials/note', headers={'Authorization': auth, 'Classroom-Id': c_id}, json={'title': body, "description": body, 'attachments': ["4c7c0d48-0692-415d-8be4-a57f729130d0", "1cbda2bb-41df-4bae-bec8-39b8848db970", "0985484c-d8ba-4d4d-99b0-4706b479c84d"]})

def getAllClass(auth):
    return request.get(class_api + 'classrooms', headers={'Authorization': auth})

def driver1000():
    # create users
    for i in range(0, 10):
        registerUser('joyyy'+str(i), 'joyy'+str(i)+"email@gmail.com")
        print('registered user:', i)
        # login with registered user
        auth = login('alpha'+str(i), '00')
        # create classess
        for c in range(0, 10):
            c_data = requesttojson(createClass(auth, c))
            print('created class', i, c)
            # create feed/syllabus/notes
            for f in range(0, 10):
                # create feed
                f_data = requesttojson(createFeed(auth, c_data["_id"], f))
                # create comment
                for cm in range(0, 10):
                    createComment(auth, c_data["_id"], f_data["_id"], cm)
                # create syallbus
                createSyllabus(auth, c_data["_id"], f)
                # create notes
                createNotes(auth, c_data["_id"], f)
                print('created feed/syllabus/notes', i, c, f)


from datetime import datetime, timedelta

def generate_dates(event_duration):
    list_of_dates = []
    start_date= datetime(year = 2022, month = 9, day = 17, hour = 9, minute = 0, second = 0)
    target = start_date+ timedelta(days = 190)
    start_day = start_date
    while start_date < target:
        for i in range(8):
            end_day=start_day + timedelta(hours=1)
            list_of_dates.append([int(start_day.timestamp()),int(end_day.timestamp())])
            start_day = end_day
        start_date += timedelta(days=1)
    return list_of_dates

def createEventNonRrule(auth,c_id):
    duration= 60 
    events = generate_dates(duration) 
    i =0
    for event in events:
        input_dict = {
            "classroom_id": c_id,
            "description": f"Testing the event no{i}",
            "location": "Delhi",
            "title": f"Test event{i}",
            "start_datetime": event[0],
            "end_datetime": event[1],
            "participants_count": 0,
            "participants": [],
            "meetlink": "",
            "extlink": "",
            "labels": [
                "test"
            ],
            "event_duration": {
                "duration": duration,
                "unit": "minutes"
            },
            "remind_me": [
                {
                    "duration": 3,
                    "unit": "minutes"
                }
            ],
            "priority_fields": 2
        }
        i+=1
        response = requesttojson(request.post(timetable_api + 'timetables', headers={'Authorization':auth},json=input_dict))
        print(response)
    return "success"

def driver():
    auth = login("rd", "rd")
    for x in range(0, 500):
        createClass(auth, '63286a6c190b14f5f571bd79', x)
        print(x)

def teamReg():
    # Create team users
    for name in team:
        registerUser(name, name +"email@gmail.com")

    # login one of the account
    auth = login("Dhruv", "00")
    # create a class
    classData = createClass(auth, 0)
    # load data in json
    data = json.loads(classData._content)
    # add all team user account in class
    joinClass(auth, data["_id"], team)

driver()
