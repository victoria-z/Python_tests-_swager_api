import unittest
import requests
import random

random_user_id=random.randint(1,20)
user_ind=random.randint(1,1000)
user_login=('User'+ str(user_ind))
user_email=('User'+str(user_ind)+'@mailinator.com')
url = "https://petstore.swagger.io/v2"
SUCCESS_CODE = 200
NOT_FOUND_CODE=404


class TestPets(unittest.TestCase):


    # # create a new user - проблема с передачей айдишника, не могу понять как правильно подставить данные в id
    # def test1_create_user(self):
    #     user_id=random_user_id
    #     print(user_login)
    #     print(user_email)
    #     body='{"id": user_id, "username": "user_login","firstName":"Test", "lastName": "User","email":"user_email","password": "1qaz2wsx","phone": "1234567","userStatus": 0}'
    #     headers = {'accept': 'application/json','Content-Type': 'application/json'}
    #     r=requests.post(url+"/user", headers=headers, data=body)
    #     self.assertEqual(r.status_code, SUCCESS_CODE)

 # create a new user
    def test1_create_user(self):
        user_id=random_user_id
        print(user_login)
        print(user_email)
        body='{"id": 1, "username": "user_login","firstName":"Test", "lastName": "User","email":"user_email","password": "1qaz2wsx","phone": "1234567","userStatus": 0}'
        headers = {'accept': 'application/json','Content-Type': 'application/json'}
        r=requests.post(url+"/user", headers=headers, data=body)
        self.assertEqual(r.status_code, SUCCESS_CODE)

# User login with correct data
    def test2_find_pet_by_id(self):
        params={'username':'user_login', 'password':'1qaz2wsx'}
        r = requests.get(url + "/user/login", params=params)
        self.assertEqual(r.status_code, SUCCESS_CODE)

# User login with incorrect data - похоже поля ввода принимают абсолютно любые даные
    def test3_find_pet_by_id(self):
        params="{'username':'user_login', 'password':''}"
        r = requests.get(url + "/user/login", params=params)
        self.assertEqual(r.status_code, NOT_FOUND_CODE)

#Get user by user name
    def test4_find_pet_by_id(self):
        r = requests.get(url + "/user/" +"user_login")
        print(r)
        self.assertEqual(r.status_code, SUCCESS_CODE)


if __name__ == "__main__":
    unittest.main()