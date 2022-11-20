

import requests
import json
# mention url
url = "https://www.fast2sms.com/dev/bulkV2"



# create a dictionary


# create a dictionary
headers = {
	'authorization': 'QqbHW076SFDTledzUu4yhiYNIK2tf3LEnkc9Br5ZasOjp1VwxMLsyMZXA8IUPcEbdB6GJgvnDhwFfV2a',
	'Content-Type': "application/x-www-form-urlencoded",
	'Cache-Control': "no-cache"
}


my_data = {
	    # Your default Sender ID
	    'sender_id': 'FTWSMS',
	
	    # Put your message here!
	    'message': 'Argent.....There is a demand for your blood group. We request you to donate your blood in your nearby BloodBank connect with our Organization.',
	
	    'language': 'english',
	    'route': 'p',
	
	    # You can send sms to multiple numbers
	    # separated by comma.
        
	     'numbers': '9345123560'
        }
response = requests.request("POST",
							url,
							data = my_data,
							headers = headers)
        #load json data from sourc
returned_msg = json.loads(response.text)

        # print the send message
print(returned_msg['message'])






















# import os
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail


# message = Mail(from_email='rishiragul26@gmail.com',
#                 to_emails='rishiragul26@gmail.com',
#                 subject='Sending with SendGrid is Fun',
#                 html_content='<strong> Hello World</strong>')


# # sg = SendGridAPIClient("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")
# # response = sg.send(message)
# # print(response.status_code, response.body)
# try:
#     sg = SendGridAPIClient(os.environ.get('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'))
#     response = sg.send(message)

#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except Exception as e:
#     print(e.message)




# # from_email = Email("aks.praveenkumar2002@gmail.com")
# # to_email = To("aks.praveen2002@gmail.com")
# # subject = "Sending with SendGrid is Fun"
# # content = Content("text/plain", "and easy to do anywhere, even with Python")
# # mail = Mail(from_email, to_email, subject, content)
# # response = sg.client.mail.send.post(request_body=mail.get())
# # print(response.status_code)
# # print(response.body)
# # print(response.headers)