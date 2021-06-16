1.Install Python in your machine. Python >=3.5
2. Install MongoDB in your machine.
3. Check Requirements.txt file for dependecies needed. 
4.Run cmd (pip install requirements.txt) to install dependencies.

How to Run:

1. Open cmd in current directory. 
2. Run command python manage.py runserver
3. Goto http://localhost:8000/ in your browser.

Urls:- 
CRUD stands for Create Read Update Delete

1. http://localhost:8000/Bank :- This url is used to CRUD the bank information.
2. http://localhost:8000/Branch :- This url is used to CRUD the branch information.
3. http://localhost:8000/BankBranch :- This url is used to view information of bank with their branches information.

How to search through city,ifsc,bank_name in http://localhost:8000/BankBranch
Ex:-  http://localhost:8000/BankBranch/?city=MUMBAI&bank_name=Bank of india&ifsc=A01232324E
