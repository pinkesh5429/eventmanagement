Step-1 Require Software
	1) Visual Studio Code require for Edit the Code
	2) Anaconda Prompt for Run the Project
	3) Require python setup for django framework


Step-2 Require Module
	1)xhtml2pdf
	  -pip install xhtml2pdf
	
Step-3 Some Changes Require for Run This Project
	1) for paytm integration you need to provide your merchant id and merchant key
	  in event folder goto views.py file and add the merchant key at line no. 39 and and mid at line no. 436
	2) for SMTP you need to add your email id and password in eventmangement folder goto settings.py and add your email id and password at line no. 138 and 142

Step-4 Now you can run the program
	Start the anaconda prompt and goto project folder using "cd" command
	Then write the syntax as mention as below
		-python manage.py runserver
	Then goto browser and copy the URL which is provided by anaconda prompt  