API Authentication using Django and Token-Based Authentication

This project implements basic authentication using Django's built-in authentication system with token-based authentication.It allows users to log in and obtain a token, which can be used to authenticate subsequent requests.

Created a new token.py file to enable the user to generate token for authentication.

Then to the views.py i implemented LoginView which takes ObtainAuthToken as a parameter. This enusures that user get a token key.
The logout view was implemented for user who wishes to logout. This also destroy the token.

Finally, those views were added to the app's urls.
POST /login/
POST /logout/

I used postman to test its functionality. Any user who login get a token for authentication. 

This is the whole process.