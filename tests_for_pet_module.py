import unittest
import requests
import random

random_order_id=random.randint(1,5)
random_pet_id=random.randint(1,100)
SUCCESS_CODE = 200
url = "https://petstore.swagger.io/v2"
exist_pet_id = 5
NOT_FOUND_CODE=404
order_id=random_order_id
pet_id = random_pet_id

class TestPets(unittest.TestCase):

#test add pet to store

    def test1_add_pet_to_store(self):
        print(random_pet_id)
        body='{"id": '+str(pet_id)+',"category": {"id": 5 ,"name" : "category"},"name": "pet_name","photoUrls": [    "string"  ],  "tags": [    {      "id": 1,      "name": "tag_name"    }  ],  "status": "available"}'
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
             }
        r=requests.post(url+"/pet", headers=headers, data=body)
        self.assertEqual(r.status_code, SUCCESS_CODE)
        r = requests.get(url + "/pet/"+ str(pet_id))
        self.assertEqual(r.status_code, SUCCESS_CODE)

# Find Pet by ID

    def test2_find_pet_by_id(self):
        r = requests.get(url + "/pet/"+ str(pet_id))
        self.assertEqual(r.status_code, SUCCESS_CODE)

# Find Pet by ID negative

    def test3_find_pet_by_id_negative(self):
        negative_list=[99999999999999, "asd", 0, " "]
        for i in negative_list:
            r = requests.get(url + "/pet/"+ str(i))
            print(i)
            self.assertEqual(r.status_code, NOT_FOUND_CODE)

# Place an order for a pet

    def test4_place_order_for_pet(self):
        pet_id = random_pet_id
        print(order_id)
        body='{"id": '+str(order_id)+',"petId": '+str(pet_id)+',"quantity": 1,"shipDate": "2020-03-23T19:07:21.602Z","status": "placed","coplete": true}'
        headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'}
        r=requests.post(url+"/store"+"/order", headers=headers, data=body)
        self.assertEqual(r.status_code, SUCCESS_CODE)

#find order by ID

    def test5_find_purchase_order_by_id(self):
        print(order_id)
        r=requests.get(url+'/store'+'/order/'+ str(order_id))
        self.assertEqual(r.status_code,SUCCESS_CODE)

#find order by not existing ID

    def test6_find_purchase_order_by_id_negative(self):
        negative_order_list=[99, " ", "@@", "vv"]
        for i in negative_order_list:
            r=requests.get(url+'/store'+'/order/'+str(i))
            print(i)
        self.assertEqual(r.status_code, NOT_FOUND_CODE)

# delete purchase order by id
    def test7_delete_order_by_id(self):
        headers = {'accept': 'application/json'}
        r=requests.delete(url+'/store'+'/order/'+ str(order_id),headers=headers)
        self.assertEqual(r.status_code,SUCCESS_CODE)

        #chek that the order was deleted
        r=requests.get(url+'/store'+'/order/'+ str(order_id))
        self.assertEqual(r.status_code,NOT_FOUND_CODE)

if __name__ == "__main__":
    unittest.main()