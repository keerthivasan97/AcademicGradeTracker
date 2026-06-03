import json 
import os


def add_user(username,email,password):
    file_name = 'students.json'
    if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
        with open(file_name, 'w') as f:
            json.dump({}, f)

    with open(file_name, 'r') as f:
        obj = json.load(f)

    if username in obj:
        print("username already exists")
        return False
    else:
        obj[username] = {
            'email': email,
            'password': password,
            'semesters': {}
        }

        with open(file_name, 'w') as f:
            json.dump(obj, f, indent=4)

        print("successfully added the user")
        return True
    

def login_user(username,password):
    file_name = 'students.json'
    if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
        print("No users found. Please sign up first.")
        return False

    with open(file_name, 'r') as f:
        obj = json.load(f)

    if username in obj and obj[username]['password'] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False
    

def add_sem(arr,username):
    file_name = 'students.json'
    with open(file_name, 'r') as f:
        obj = json.load(f)
    if username in obj:
        obj[username]['semesters'].update(arr)

    with open(file_name, 'w') as f:
        json.dump(obj, f, indent=4)

    print("successfully added the semester data")
    return True


def get_user_data(username):
    file_name = 'students.json'
    if not os.path.exists(file_name) or os.path.getsize(file_name) ==0:
        return {}
    try:
        with open(file_name,'r') as f:
            obj = json.load(f)
            if isinstance(obj,dict):
                return obj.get(username,{})
    except json.JSONDecodeError:
        return {}
    return {}