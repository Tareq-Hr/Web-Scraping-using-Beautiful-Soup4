import requests
from bs4 import BeautifulSoup
from tkinter import *
import webbrowser
from PIL import ImageTk, Image
from tkinter.ttk import *


def createNewWindow2():
 fenetre = Tk()
 fenetre.title("Results")
 fenetre.iconbitmap("job.jpg")
 scrollbar = Scrollbar(fenetre)
 scrollbar.pack(side=RIGHT, fill=Y)
 job_title = e1.get()
 job_ville = e2.get().lower()

 #############################################################################################################
 marocannonce = 'https://www.marocannonces.com/maroc'
 indeed = 'https://ma.indeed.com/emplois?q=developpeur&l='+job_ville.capitalize()+'&advn=4401717887588522&vjk=84f8d93edcda6f86'
 indeed2 = 'https://ma.indeed.com/emplois?q=developer&l='+job_ville.capitalize()+'&advn=4401717887588522&vjk=84f8d93edcda6f86'
 indeed3 = 'https://ma.indeed.com/emplois?q=informatique&l='+job_ville.capitalize()+'&advn=4401717887588522&vjk=84f8d93edcda6f86'
 #rekrute = 'https://www.rekrute.com/offres-emploi-maroc.html'
 #rekrute = 'https://www.rekrute.com/offres.html?st=d&keywordNew=1&keyword='+job_ville+'&filterLogo=&filterLogo='
 rekrute = 'https://www.rekrute.com/offres.html?s=1&p=2&o=1&keyword='+job_ville
 rekrute2 = 'https://www.rekrute.com/offres.html?s=&p=2&o=1&keyword='+job_ville
 rekrute3 = 'https://www.rekrute.com/offres.html?s=3&p=3&o=1&keyword='+job_ville
 rekrute4 = 'https://www.rekrute.com/offres.html?s=3&p=4&o=1&keyword='+job_ville
 #############################################################################################################

 page_marocannonce = requests.get(marocannonce)
 page_indeed = requests.get(indeed)
 page_indeed2 = requests.get(indeed2)
 page_indeed3 = requests.get(indeed3)
 page_rekrute = requests.get(rekrute)
 page_rekrute2 = requests.get(rekrute2)
 page_rekrute3 = requests.get(rekrute3)
 page_rekrute4 = requests.get(rekrute4)
 #############################################################################################################

 # get html code
 soup_marocannonce = BeautifulSoup(page_marocannonce.content, 'html.parser')
 soup_indeed = BeautifulSoup(page_indeed.content, 'html.parser')
 soup_indeed2 = BeautifulSoup(page_indeed2.content, 'html.parser')
 soup_indeed3 = BeautifulSoup(page_indeed3.content, 'html.parser')
 soup_rekrute = BeautifulSoup(page_rekrute.content, "html.parser")
 soup_rekrute2 = BeautifulSoup(page_rekrute2.content, "html.parser")
 soup_rekrute3 = BeautifulSoup(page_rekrute3.content, "html.parser")
 soup_rekrute4 = BeautifulSoup(page_rekrute4.content, "html.parser")
 #############################################################################################################

 # --------print only elements which have a specific id---------
 id_marocannonce = soup_marocannonce.find(id='content')
 id_indeed = soup_indeed.find(id='resultsCol')
 id_indeed2 = soup_indeed2.find(id='resultsCol')
 id_indeed3 = soup_indeed3.find(id='resultsCol')
 id_rekrute = soup_rekrute.find(id="fortopscroll")
 id_rekrute2 = soup_rekrute2.find(id="fortopscroll")
 id_rekrute3 = soup_rekrute3.find(id="fortopscroll")
 id_rekrute4 = soup_rekrute4.find(id="fortopscroll")
 #############################################################################################################

 #filter more our results
 ul_marocannonce = id_marocannonce.find('ul', class_='cars-list')
 section_indeed = id_indeed.find_all('div', class_='title')
 section_indeed2 = id_indeed2.find_all('div', class_='title')
 section_indeed3 = id_indeed3.find_all('div', class_='title')
 jobs_Rekrute = id_rekrute.find_all('h2')
 jobs_Rekrute2 = id_rekrute2.find_all('h2')
 jobs_Rekrute3 = id_rekrute3.find_all('h2')
 jobs_Rekrute4 = id_rekrute4.find_all('h2')
 #############################################################################################################

 # filter more our results
 jobs_marocannonce = ul_marocannonce.find_all('h3')
 #jobs_marocannonce2 = ul_marocannonce.find('h3')
 #jobs_Rekrute = div_rekrute.find_all('h2')
 #jobs_ville = jobs_marocannonce.find('span', class_='location')

 #############################################################################################################

 fenetre.option_add('*font', ('', 15), priority=40)
 mylist = Text(fenetre, yscrollcommand=scrollbar.set , bd=20, width=100, height=100,
               highlightcolor="black")

 #############################################################################################################
 length_marocannonce  = len(jobs_marocannonce)
 length_indeed  = len(section_indeed)
 length_indeed2  = len(section_indeed2)
 length_indeed3  = len(section_indeed3)
 length_rekrute  = len(jobs_Rekrute)
 length_rekrute2  = len(jobs_Rekrute2)
 length_rekrute3  = len(jobs_Rekrute3)
 length_rekrute4  = len(jobs_Rekrute4)
 #############################################################################################################

 i = 0
 j = 0
 l = 0
 l2 = 0
 l3 = 0
 l4 = 0
 c2 = 0
 c1 = 0
 #############################################################################################################

 k=100
 k2=200
 k3 = 300
 k4 = 400
 r2 = 500
 r3 = 600
 r4 = 700
 #############################################################################################################

 link1 = []
 link2 = []
 link3 = []
 link4 = []
 link5 = []
 link6 = []
 link7 = []
 link8 = []

 #############################################################################################################

 # test in console
 print(length_marocannonce,length_indeed, length_rekrute)
 #############################################################################################################

#Results from Maroc Annonce
 def web(i,link):
     link.append("www.marocannonces.com/" + job.find('a')['href'])
     button = Button(fenetre, text="click")
     if job_title.lower() in job.text.strip().lower():
        if job_ville in job.text.strip().lower():
         # label1_marocannonce = Label(fenetre, text="Résultats depuis maroc annonce :",bg="yellow")
         # label2_marocannonce = Label(fenetre, text=job.text.strip())
         # label3_marocannonce = Label(fenetre, text=f"Apply here: {link}\n")
         mylist.tag_config(i + 1, foreground="blue")
         mylist.tag_config(0, foreground="green")
         mylist.insert(END, "Offer from : ",0)
         mylist.insert(END, "marocannonce.com :\n")
         mylist.insert(END, "Job Title : ",0)
         mylist.insert(END, job.text.strip() + "\n")
         # mylist.insert(END, f"Apply here: {link}\n")
         #mylist.insert(END, "Check the offre now ==> :")
         mylist.insert(END, "Check the offer NOW !", i + 1)
         mylist.tag_bind(i + 1, "<Button-1>", lambda e: webbrowser.open(link[i], new=0, autoraise=True))
         mylist.insert(END, "\n\n")
         # label1_marocannonce.pack()
         # label2_marocannonce.pack()
         # label3_marocannonce.pack()
         #print(
            # "*************************************Résultats depuis maroc annonce*****************************************")
         #print(job.text.strip())
        # print(f"Apply here: {link[i]}\n")
 #############################################################################################################

#Results from Indded
 def web2(i, k, link):
    link.append(job.find('a')['href'])
    if job_title.lower() in job.text.strip().lower():
     # label1_indeed = Label(fenetre, text="Résultats depuis indeed",bg="red")
     # label2_indeed = Label(fenetre, text=job.text.strip())
     # label3_indeed = Label(fenetre, text=f"Apply here : {link}\n")
     mylist.tag_config(k + 1, foreground="blue")
     mylist.tag_config(0, foreground="green")
     mylist.insert(END, "offer from : ",0)
     mylist.insert(END, "ma.indeed.com\n")
     mylist.insert(END, "Job Title : ",0)
     mylist.insert(END, job.text.strip()+"\n")
     #mylist.insert(END, "Check the offer NOW !")
     mylist.insert(END, "Check the offer NOW !", k + 1)
     mylist.tag_bind(k + 1, '<Button-1>', lambda e: webbrowser.open("https://ma.indeed.com"+link[i], new=0, autoraise=True))
     mylist.tag_config(0, foreground="green")
     mylist.insert(END, "\n\n")
     # label1_indeed.pack()
     # label2_indeed.pack()
     # label3_indeed.pack()
     # print("****************************************Résultats depuis indeed********************************************")
     # print(job.text.strip())
     #print(f"Apply here: {link}\n")
#############################################################################################################

 def web3(i, k, link):
    link.append("https://www.rekrute.com"+job.find('a')['href'])
    if job_title.lower() in job.text.strip().lower():
     # label1_indeed = Label(fenetre, text="Résultats depuis indeed",bg="red")
     # label2_indeed = Label(fenetre, text=job.text.strip())
     # label3_indeed = Label(fenetre, text=f"Apply here : {link}\n")
     mylist.tag_config(0, foreground="green")
     mylist.insert(END, "offer from : ",0)
     mylist.insert(END, "www.rekrute.com\n")
     mylist.tag_config(k + 1, foreground="blue")
     mylist.insert(END, "Job Title : ",0)
     mylist.insert(END,job.text.strip()+"\n")
     #mylist.insert(END, "Check the offer NOW !")
     mylist.insert(END, "Check the offer NOW !", k + 1)
     mylist.tag_bind(k + 1, '<Button-1>', lambda e: webbrowser.open(link[i], new=0, autoraise=True))
     mylist.insert(END, "\n\n")
     # label1_indeed.pack()
     # label2_indeed.pack()
     # label3_indeed.pack()
     # print("****************************************Résultats depuis indeed********************************************")
     # print(job.text.strip())
     # print(f"Apply here: {link}\n")
 #############################################################################################################

 for job in section_indeed:
    if length_indeed != 0:
        length_indeed-=1
        web2(i,k,link1)
        i+=1
        k+=1
 #############################################################################################################
 for job in section_indeed2:
    if length_indeed2 != 0:
        length_indeed2-=1
        web2(c1,k3,link4)
        i+=1
        k3+=1
 #############################################################################################################
 for job in section_indeed3:
    if length_indeed3 != 0:
        length_indeed3-=1
        web2(c2,k4,link5)
        c2 +=1
        k4+=1
 #############################################################################################################

 for job in jobs_Rekrute:
    if length_rekrute != 0:
        length_rekrute-=1
        web3(l,k2,link3)
        l+=1
        k2+=1
#############################################################################################################

 for job in jobs_Rekrute2:
    if length_rekrute2 != 0:
        length_rekrute2-=1
        web3(l2,r2,link6)
        l2+=1
        r2+=1
#############################################################################################################

 for job in jobs_Rekrute3:
    if length_rekrute3 != 0:
        length_rekrute3-=1
        web3(l3,r3,link7)
        l3+=1
        r3+=1
#############################################################################################################

 for job in jobs_Rekrute4:
    if length_rekrute4 != 0:
        length_rekrute4-=1
        web3(l4,r4,link8)
        l4+=1
        r4+=1
 #############################################################################################################

 for job in jobs_marocannonce:
    if length_marocannonce != 0:
        length_marocannonce-=1
        web(j,link2)
        j+=1


 #############################################################################################################


 '''**************************Second Interface TKinter*********************************'''
 mylist.pack(fill = BOTH, expand=True)
 scrollbar.config( command = mylist.yview )
 #fermer la fenetre
 fenetre.mainloop()
 #############################################################################################################

 '''**************************First Interface TKinter*********************************'''
fenetre = Tk()
fenetre.option_add('*font', ('', 15), priority=40)

search = PhotoImage(file = r"search2.jpg")
img = search.subsample(3,3)

exit = PhotoImage(file = r"exit2.jpg")
img_exit1 = exit.subsample(3,3)
img_exit = img_exit1.subsample(3)
#image2=Label(fenetre, image=search, justify=RIGHT, width="40", height="40")

buttonExample = Button(fenetre,text="Search for a job", image=img,
                       compound=LEFT ,command=createNewWindow2, cursor="hand2")

e1 = Entry(fenetre)
e2 = Entry(fenetre)
label = Label(fenetre, text="Create your skills Below : ", width="23", justify=RIGHT)
ville = Label(fenetre, text="City : ", justify=CENTER, width="23")
vid=Label(fenetre, text=" ")
vid2=Label(fenetre,text=" ")
vid3=Label(fenetre,text=" ")
vid4=Label(fenetre,text=" ")
bouton = Button(fenetre, text="Exit", image=img_exit, compound=LEFT, command=fenetre.quit,  cursor="hand2")

img2 = ImageTk.PhotoImage(Image.open("job.jpg"))
image=Label(fenetre, image=img2, width="700", justify=RIGHT)


#label.pack()
#e1.pack()
#buttonExample.pack()
fenetre.title("WebScraping Using BeautifulSoup4")
fenetre.rowconfigure(0, weight=5)
fenetre.columnconfigure(0, weight=5)
vid2.pack()
label.pack()
e1.pack()
vid3.pack()
ville.pack()
e2.pack()
vid4.pack()
buttonExample.pack()
bouton.pack()
image.pack()

vid.pack()
fenetre.mainloop()
#############################################################################################################