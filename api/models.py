from bson.objectid import ObjectId
from pymongo import *
client = MongoClient("mongodb+srv://rishijha1709:rishijha1709@cluster0.2lkrw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.nurture_advisory




class object():

    def getaobject(self,data,coll):
        return coll.find_one(data)
    def insertaobject(self,data,coll):
        ins = coll.insert_one(data)
        return ins.inserted_id
    def getallobject(self,coll):
        res = []
        for doc in coll.find():
            res.append(doc)
        return res

    def updateaobject(self,coll,pdata,ndata):
        id = coll.update_one(pdata,{"$set":ndata})
        return "ok"
    def deleteaobject(self,id,coll):
        coll.delete_one({"_id":id})
    def todict(self):
        return self.__dict__

class Advisor(object):
    coll = db["advisor"]
    def __init__(self,ad_name:str,purl:str):
        self.advisor_name = ad_name
        self.photo_url = purl
    
    def advisorispresent(self,id):
        sizes = self.getallobject(self.coll)
        res = False
        for i in sizes:
            if i["_id"] == ObjectId(id):
                res =True
                break
            continue
        return res

    def listalladvisor(self):
        p = []
        pi ={}
        pizzas = self.getallobject(self.coll)
        for i in pizzas:
            for j in i :
                if j =="_id":
                    pi["id"] =str(i[j])
                else:
                    pi[j] = i[j]
            p.append(pi)
            pi= {}
        return p 



class user(object):
    coll = db["user"]
    def __init__(self,name,email,password):
        self.name = name
        self.password= password
        self.email= email
    
    def userispresent(self,id):
        sizes = self.getallobject(self.coll)
        res = False
        for i in sizes:
            if i["_id"] == ObjectId(id):
                res =True
                break
            continue
        return res

class booking(object):
    coll = db["booking"]
    def __init__(self,advisor:str,user:str,time:str):
        self.advisor= advisor
        self.user = user
        self.bookingtime =time
