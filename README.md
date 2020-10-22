# ControllExpenses
Web app to track expenses of a person as well as their income

## **Requirements**
* python 3.0 or greater
* Django

## **Installing**
1. clone this project
```
   git clone https://github.com/HectorCaAc/ControllExpenses.git 
```
2. 
```
    cd ControllExpenses
```
3. **Optional**
It is a good idea to create an individual enviorement to prevent any depency issue. It is recommend to use conda for this
```
    conda create --name ControllExpenses python=3.6
```
4. 
```
    pip -r requirements.txt
```
*if python 2 is installed on the computer then download any version of python >= 3.0 and instead of using pip use pip3*

5. 
```
    python manage.py migrate
```

6. **Optional**
Create a super user, It is possible to find how to do that doing a quickly google search

## Run

0. If it is required to activate the enviorement do it
```
    conda activate ControllExpenses
```
1. 
```
    python manage.py runserver
``` 
2. 
If you want to deploy this application on heroku it is required to download heroku package for it using pip, and ucomment the django_heroku on settings

## TODO
1. [ ] Add a filter functionality to entries pages.
3. [ ] Be able to sort the income for the next that should appear.
4. [ ] The borders of different elements of the dashboard do not show a current event.s
8. [ ] To if exists a lot of entries or at the moment of query those it will be a good idead to use the overflow
9. [ ] Add test for the models (I have the feeling that the Income and the functionality to enter new income is not workig)
11. [ ] the Model of entry and the form have a werid _init_, for an example check the fucntion form_valid from expesnses views personData to see it.
12. [ ] Make the function to run schedule tasks.
13. [ ] The proxy attribute is not working for the package json 
14. [ ] The summary page hte income is not showing the right information
15. [ ] Make the task run to know how much money avaiable there are.
16. [ ] When a category is created the amount Avaiable is 0
17. [ ] Show if the user overspend of spend the right amount.
18. [ ] Be sure that one user can not read data from other users
19. [ ] Add more functionalities to the category body.
    - Notes of the user
    - Receipts
    - Number of times the budget has over spend
    - Should the category still count to the budget
    - Number of entries for the past 30 days.
20. [ ] Integrate wellsfargo api into the project if it is possible
21. [ ] Inside of the category add graphs at the bottom to make it look better or some table
22. [ ] Required to add category option, then start to add the other options to the category 
        (modify category, and export category)

 ## TODAY TASKS
- [ ] make the modify and export functionality to work..
- [ ] Add 30 days pie diagram.
- [ ] fixt space of the left bar.(navbar\)
- [ ] Add income and spending of the user pannel.