# college_mgnt
Steps for running web application

1. Creating virtual envinronment
Type following command in you command prompt to create virtual env(This is one time steup no need to do this every time) -> python -m virtualenv env

2. Install packages virtual envinronment
(This is one time steup no need to do this every time) -> pip install -r requirements.txt

3. Activate virtual envinronment
(This is to be done every time when you are running project) -> source env/bin/activate ( for linux) -> .\env\Scripts\activate ( for windows)
  note: (To go back on the previous page type) -> cd ..
4. Starting server
->cd college_mgnt\college_mgnt optional
-> cd college_mgnt -> python manage.py runserver