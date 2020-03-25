# A test backend for making login pages in flutter

Documentation on how to use this:



### Admin interface for creating / editing users with a gui : 
https://knk.magnum.wtf/admin/login/?next=/admin/
Username: PussySlayer69
Password: kps


### Create new user

POST https://knk.magnum.wtf/api/register/

params = {
  "name":----,
  "user":-----,
  "pass":-----,
}


### Login with an existing user

POST https://knk.magnum.wtf/api/login

params = {
  "user":-----,
  "pass":-----,
}

_If your login details are correct, you will receive an authentication token. Save this. You will need this later to check whether the user is already logged in._

### Check whether a user is logged in


POST https://knk.magnum.wtf/api/authorize

params = {
  "token":-----,
}

### Logout a user

POST https://knk.magnum.wtf/api/logout

params = {
  "token":-----,
}
