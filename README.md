
# vantage API 
  AWS Cognito authenticator module / datalink to sharepoint database. <h2>
  # Get Started 

Create a SETUP.py file on Auth/ directory; 
Place the following strings with your credentials and server informations inside brackets and remove the brackets;


email = ['youremail@work.com'] <br>
passPhrase = ['yourpassphrase']<br>
client_id = ['yourAWSClientID']<br>
region_name = ['Your AWS server Region like us-east-1']<br>
AuthFlow = ['Flow you use to auth like USER_PASSWORD_AUTH']<br>
auth_data = { 'USERNAME':email , 'PASSWORD':passPhrase }


Remember to install boto3 and requests packages (pip install)

Thx!! 
