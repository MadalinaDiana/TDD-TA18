import requests


def test_wrong_login():
    api_login_url = "https://api.jules.app/login"
    payload = {'email': "df@yahoo.com", 'password': "fdf"}
    headers = {'content-type': 'application/json'}
    response = requests.post(api_login_url, data=payload, headers=headers)
    print(response.text)


def test_contacts_postman_api():
    contacts_url = "https://thinking-tester-contact-list.herokuapp.com/contacts"
    bearer_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MzcwYzlmZWQ4OGRmZTAwMTVlMzA1ZGQiLCJpYXQiOjE2NjgzNDI4Mjl9.TndW-lcs1e1vzqvSoxgcxviK0Xe1zU12L78lKrJ3DWU"
    headers = {
        'Authorization': f'Bearer {bearer_token}'
    }
    response = requests.get(contacts_url, headers=headers)

    assert response.status_code == 200
    assert len(response.json()) == 1
    my_contact = response.json()[0]
    assert my_contact['firstName'] == 'Adela'
    assert my_contact['lastName'] == 'Neascu'


def test_add_contacts():
    contacts_url = "https://thinking-tester-contact-list.herokuapp.com/contacts"
    bearer_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9" \
                   ".eyJfaWQiOiI2MzZhOWJhYTZlOTNmMTAwMTUyNjA1MmUiLCJpYXQiOjE2Njc5MzEwNTB9" \
                   ".Oa8tyBk9KkLKAhNsq8v6Y1Lm7jJbXEsp30Flb3M5NmA "
    headers = {
        'Authorization': f'Bearer {bearer_token}'
    }
    payload = {  # nu functioneaza
        'firstName': 'John',
        'lastName': 'Doe',
        "birthdate": "1970-01-01",
        "email": "jdoe@fake.com",
        "phone": "8005555555",
        "street1": "1 Main St.",
        "street2": "Apartment A",
        "city": "Anytown",
        "stateProvince": "KS",
        "postalCode": "12345",
        "country": "USA"
    }

    response = requests.post(contacts_url, data=payload, headers=headers)
    print(response.text)
