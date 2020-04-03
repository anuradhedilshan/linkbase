from .models import posts
import datetime

def updatePost():
    des_set  = []


    dbQuery = posts.objects.order_by('id')[:10:-1]
    for i in range(len(dbQuery)):
        if len(dbQuery[i].quickdes) < 60 :
            lenth = len(dbQuery[i].quickdes)
            description  = dbQuery[i].quickdes
            ldes = description + "  _  "*(30-lenth) 
        else:
            ldes = dbQuery[i].quickdes
        des_set.append([ldes,dbQuery[i].image,dbQuery[i].title,dbQuery[i].id])
        
    return des_set


def showCase(cat):
    dbQuery =  posts.objects.filter(catagorye=cat)[:5]
    return dbQuery


