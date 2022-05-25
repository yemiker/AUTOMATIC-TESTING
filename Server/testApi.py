import requests
"""Trip yoetz web """

class Test_login:

    def test_LoginValid(self):
        #api url of web
        url = "https://trip-yoetz.herokuapp.com/auth/login"
        # get request payload
        body = {"email":"chris@gamil.com","password":"ahruah123"}
        response = requests.post(url, json=body)
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 20
        assert (response.json()['message']) == 'login successful'


    def test_Login_Invalid_When_Email_Invalid(self):
        # api url of web
        url = "https://trip-yoetz.herokuapp.com/auth/login"
        # get request payload
        body = {"email": "22@gamil.com", "password": "ahruah123"}
        response = requests.post(url, json=body)
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 40
        assert response.json()['message'] == "no user found"

    def test_Login_Invalid_When_Password_Invalid(self):
        # api url of web
        url = "https://trip-yoetz.herokuapp.com/auth/login"
        # get request payload
        body = {"email": "chris@gamil.com", "password": "1234"}
        response = requests.post(url, json=body)
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 40
        assert response.json()['message'] == "password or email incorrect"

    def test_Login_Invalid_When_Email_field_Null(self):
        # api url of web
        url = "https://trip-yoetz.herokuapp.com/auth/login"
        # get request payload
        body = {"email":"","password":"ahruah123"}
        response = requests.post(url, json=body)
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 40
        assert response.json()['message'] == "password or email incorrect"

    def test_Login_Invalid_When_Password_field_Null(self):
        # api url of web
        url = "https://trip-yoetz.herokuapp.com/auth/login"
        # get request payload
        body = {"email":"chris@gamil.com"}
        response = requests.post(url, json=body)
        assert response.status_code == 500
        assert response.elapsed.total_seconds() < 40
        assert response.json()['message']=='Illegal arguments: undefined, string'

    def test_Login_Invalid_When_All_fields_Null(self):
        # api url of web
        url = "https://trip-yoetz.herokuapp.com/auth/login"
        # get request payload
        body = {}
        response = requests.post(url, json=body)
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 40
        assert response.json()['message'] == "no user found"






