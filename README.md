# MyJournal

> A simple flask application developed by Christine Ritah Nagadya for the Andela Kenya Cohort XVI bootcamp project,as a prequisite for the Andela Fellowship. The MyJournal App is an online journal that enables user(s) to create , view and also modify personal events. 

###### (Proposed) Application Functionalities
- [x] User signup / login
- [x] Create and Save a journal entry comprising of three sections: Date;Journal (body) and ~~Tags~~
- [x] View all personal journey entries listed in the order of journal's date.
- [x] Edit/update old journals
- [ ] Search through all personal journal articles by key-words (tags) or text within the journal.

###### User Guide
1. To access the app, a user needs to:
 1. Clone or download a version of the app to his / her local machine 
 2. Install all the app dependencies listed in the requirements.txt file by running the commandline:
 ```
 pip install -r requirements.txt
 ```
 And then executing the run.py file using:
 ```
python run.py
```
 3. Launch the app in the browser using [link](http://127.0.0.1:5000/login) 
2. At the login in page, the user will be required to click the **_Yahoo_** for authorization using his / her yahoo email address before clicking the **_Sign In_** button
**Note:**  New users are automatically added to the system as long as the **_Yahoo_** credentials are correct.
3. After logging in, the user will be redirected to a page showing journal articles, _if any_ listed in the order they were created.
4. To edit and article, the user simply needs to hover the mouse over that particular article. An **_Edit_** button will be displaced at the top right of the article. The user can then edit the article in question by clicking this button.
5. To create a new article, the user should click the **_Create Article_** link at the top right of the page, enter the necessary information and then click the **_Add Article_**  button.
6. Similarly, to logout out of the app, the user should click the **_Logout**_ link at the top right of the page. He / she will be required to login again to access the app in future.