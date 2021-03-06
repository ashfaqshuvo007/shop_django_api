## User Registration Flow

A user is signed up. Therefore self created. A signup request is automatically followed up by the system with a verification email sending. The verification email contains a link to activate the account. After the activation link is clicked, user will need to login to the system.

## Necessary APIs

### To register a new user

**API URL:** `/users/`

**Method:** POST

**Headers:** 
* Content-Type: application/json

**Sample body:**
```json
    {
        "username": "halum1",
        "password": "halum",
        "first_name": "Halum",
        "last_name": "Mama",
        "email": "hal1um@gmail.com",
        "user_type": 2,
        "contact_number": "+8801705360381",
        "company_name": "Field Buzz",
        "address": "Baridhara, Dhaka"
    }
```

**Sample Response:**
```json
{
    "username": "halum1",
    "first_name": "Halum",
    "last_name": "Mama",
    "email": "hal1um@gmail.com",
    "user_type": 2,
    "verification_status": 1,
    "contact_number": "+8801705360381",
    "company_name": "Field Buzz",
    "address": "Baridhara, Dhaka"
}
```
Note that:
* verification_status = 0: Unverified user
* verification_status = 1: Verification status sent via email
* verification_status = 2: User is verified

*NB:* Currently console backend is being used as email backend. Therefore actual email is not sent to user, but it can be seen from Django server's console output.


### To verify user:

**Sample URL:** `/users/user-verification/07e4e3e3-bade-4ef9-a29b-085efde1b394/`

**Method:** GET

**Headers:** 
* Content-Type: application/json

**Sample Response:**
```json
{
    "user_id": 6,
    "message": "Verification successful",
    "success": true
}
```


### To login:

**Sample URL:** `/users/login/`

**Method:** POST

**Headers:** 
* Content-Type: application/json

**Sample Request Body:**
```json
{
    "username": "halum",
    "password": "halum"
}
```

**Sample Response:**
```json
{
    "token": "de66e029ba673e0fdd32229d7d35685dffc1c587",
    "user": 5,
    "first_name": "Halum",
    "last_name": "Mama",
    "verification_status": 2,
    "success": true
}
```