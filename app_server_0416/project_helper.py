from flask import *
from helper_function import *
from extensions import connect_to_database
import os
import error_handler
#import pdb

def get_project_info(projectid):
	project_info = get_project_basic_info(projectid)
	picture_list = get_pic_list(projectid)
	print(picture_list)
	content = get_project_content(projectid)
	print(content)
	publication_list = get_project_pubcs(projectid)
	print(publication_list)
	project_info['pic'] = picture_list #list of dict
	project_info['content'] = content #string
	project_info['publications'] = publication_list #list of dict
	# pdb.set_trace()
	return project_info

def get_project_basic_info(projectid):
	db = connect_to_database()
	cur = db.cursor()
	projectid = int(projectid)
	command = "SELECT Topic, Abstract, Website FROM Project WHERE Projectid ="+projectid+""
	cur.execute(command)
	project_info_dict = cur.fetchall()[0]
	print(project_info_dict)
    #pdb.set_trace()
	return project_info_dict

def get_pic_list(projectid):
    #pdb.set_trace()
	db = connect_to_database()
	cur = db.cursor()
	projectid = int(projectid)
	command = "SELECT Picture.Pictureid AS Pictureid, Picture.format AS format FROM Picture JOIN PictureContain ON Picture.Pictureid = PictureContain.Pictureid WHERE PictureContain.Projectid = "+projectid+""
	cur.execute(command)
    #pdb.set_trace()
	pic = cur.fetchall() #dict
	if len(pic)>0:
		return pic[0]
	else:
		return False



def get_project_content(projectid):
	db = connect_to_database()
	cur = db.cursor()
	projectid = int(projectid)
	command = "SELECT Content.Contentid AS Contentid, Content.Paragraph As Paragraph FROM Content JOIN ContentContain ON Content.Contentid = ContentContain.Contentid WHERE ContentContain.Projectid = "+projectid+""
	cur.execute(command)
	content = cur.fetchall()
	if len(content)>0:
		real_content = content[0]['Paragraph'] #string
	else:
		real_content = ""
	return real_content

def get_project_pubcs(projectid):
	db = connect_to_database()
	cur = db.cursor()
	projectid = int(projectid)
	command1 = "SELECT Publication.Publicationid, Publication.Pubname, Publication.Pubtime, Publication.Information,Publication.People FROM Publication JOIN PublicationContain ON PublicationContain.Publicationid = Publication.Publicationid WHERE PublicationContain.Projectid = "+projectid+""
	cur.execute(command1)
	pubs_list = cur.fetchall() #list of dict
	return pubs_list

def add_publication(pubname,pubtime,information,projectid,people):
	db = connect_to_database()
	cur = db.cursor()
	command1 = "INSERT INTO Publication(Pubname,Pubtime,Information,People) VALUES('"+pubname+"','"+pubtime+"','"+information+"','"+people+"')"
	cur.execute(command1)
	command2 = "SELECT Publicationid FROM Publication WHERE Pubname = '"+pubname+"'"
	Publicationid = str(cur.execute(command2))
	projectid = int(projectid)
	command3 = "INSERT INTO PublicationContain(Publicationid, Projectid) VALUES("+Publicationid+","+projectid+")"
	print('===line 75 command3=======')
	print(command3)
	status = cur.execute(command3)
	print('proj_help status  line 78' + str(status))

	return True

def delete_publication(publicationid,projectid):
	db = connect_to_database()
	cur = db.cursor()
	command1 = "DELETE FROM Publication WHERE Publicationid ="+publicationid+""
	cur.execute(command1) #don't need to delete from the publicationcontain table because it is on delete cascade    
	return True

def delete_picture(pictureid,projectid):
	db = connect_to_database()
	cur = db.cursor()
	command1 = "DELETE FROM Picture WHERE Pictureid ='"+pictureid+"'"
	cur.execute(command1) #don't need to delete from the publicationcontain table because it is on delete cascade    
	return True

	

