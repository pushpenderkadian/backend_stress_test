
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

def createuserData(name):
    return {
        "username": name,
        "password": "00",
    }

def registerUser(name):
    data = createuserData(name)
    r = requests.post("https://auth.api.edvora.me/login", json=data)
    if (r.status_code == 200):
        return r.json()
    else:
        return False

def driver():
    
    # for i in range(0, 100):
    rslt=registerUser("hellop88")
    
    file=open("hellop88.txt", 'w')
    file.write(str(rslt))
        # login with registered user
driver()
        