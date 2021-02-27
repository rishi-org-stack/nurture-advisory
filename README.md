# pizaa-api

COMMANDS:
  1 To Run: python manage.py runserve
  2 important::: pip install pymongo[srv] //run this command

  
APIs:
1 regular/ == will create a pizza of type "regular" and will insert it into database if size is already present in database 

2 square/== will create a pizza of type "square" and insert it into database it size is already present in ur database 

3  square/size/listall/ == will list all square pizza of thate particular size

4  regular/size/listall/ == will list all regular pizza of thate particular size

5 size/ == will add  asize in database

6 update/typeof/id/size/ == will update size of  pizza with that id and type

7 delete/id/ == delete will delete pizza with that id
Disclaimer 

api/models.py 
Change that string inside mongoclient("your cluster")
