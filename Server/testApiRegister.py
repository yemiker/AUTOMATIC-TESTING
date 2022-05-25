import requests

class TestRegister:
    def testRegister_valid(self):
        url = "https://trip-yoetz.herokuapp.com/auth/register"
        body = {"name":"alam","lastName":"mangist","birthDate":"2004-01-01","email":"aaa@walla.com","password":"ahruah123"}
        response = requests.post(url,json=body)
        print(response.json())
        res = response.json()
        assert res['message'] == "user added successfully"
        assert response.status_code == 200


    def testRegister_Invalid_When_FirstName_IsNull(self):
        url = "https://trip-yoetz.herokuapp.com/auth/register"
        body = {"name":"","lastName":"mangist","birthDate":"2004-01-01","email":"dsgadsa@walla.com","password":"ahruah123"}
        response = requests.post(url,json=body)
        print(response.json())
        res = response.json()
        assert res['message'] == 'User validation failed: name: Path `name` is required.'
        assert response.status_code == 500

    def testRegister_Invalid_When_LastName_IsNull(self):
        url = "https://trip-yoetz.herokuapp.com/auth/register"
        body = {"name":"alaaam","lastName":"","birthDate":"2004-01-01","email":"dsgadssssa@walla.com","password":"ahruah123"}
        response = requests.post(url,json=body)
        print(response.json())
        res = response.json()
        assert res['message'] == 'User validation failed: lastName: Path `lastName` is required.'
        assert response.status_code == 500

    def testRegister_Invalid_When_BirthDate_IsNull(self):
        url = "https://trip-yoetz.herokuapp.com/auth/register"
        body = {"name":"alaaam","lastName":"aaa","birthDate":"","email":"dsad@walla.com","password":"ahruah123"}
        response = requests.post(url,json=body)
        print(response.json())
        res = response.json()
        assert res['message'] == 'User validation failed: birthDate: Path `birthDate` is required.'
        assert response.status_code == 500

    def testRegister_Invalid_When_Email_IsNull(self):
        url = "https://trip-yoetz.herokuapp.com/auth/register"
        body = {"name":"alaaam","lastName":"aaa","birthDate":"2004-01-01","email":" ","password":"ahruah123"}
        response = requests.post(url,json=body)
        print(response.json())
        res = response.json()
        assert res['message'] == 'User validation failed: email: Path `email` is invalid ( ).'
        assert response.status_code == 500

    def testRegister_Invalid_When_password_IsNull(self):
        url = "https://trip-yoetz.herokuapp.com/auth/register"
        body = {"name":"alaaam","lastName":"aaa","birthDate":"2004-01-01","email":"ds@walla.com","password":" "}
        response = requests.post(url,json=body)
        print(response.json())
        res = response.json()
        assert res['message'] == 'User validation failed: password: Path `password` is required.'
        assert response.status_code == 500



