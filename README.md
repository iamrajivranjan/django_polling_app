# django_polling_app
Polling app just for learning purpose

##Installation
1. First create folder<FolderName> and create Virtual environment using (venv -> which is standard inbuil in python3) 

2. git clone this project in <FolderName>
'''python
git clone <url>
'''

3. Activate virtual env from the <FolderName> which contains bin folder and the project which you cloned.
'''bash
source bin/activate
'''

4. Install the requirements
'''bash
pip install -r requirements.txt
'''

5. go to the cloned folder which contains manage.py and run server 
'''bash 
python3 manage.py runserver 
'''

## Admin Setup
1. makemigrations -> for all the models 
'''bash 
python3 manage.py makemigrations
'''

2. migrate -> to create table in database
'''bash
python3 manage.py migrate
'''

3. create superuser -> from the cloned folder
'''bash
python3 manage.py createsuperuser
'''

4. Runserver as above
