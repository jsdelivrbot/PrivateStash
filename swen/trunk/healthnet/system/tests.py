from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from .models import *
from django.core.urlresolvers import reverse
import datetime

# Create your tests here.

class ExceptionTest(TestCase):
    #not done yet
    def test_registrationOutOfDate(self):
        admin=User.objects.create_superuser('admin','1800notAreal@email.com','p@ssWord')
        c=Client()
        loggedin=c.login(username=admin.username,password='p@ssWord')
        #date of birth should be in the past or today
        #dont let the user date of birth be in the future
        reg=Registration(admin,role='AD',date_of_birth=datetime.date(year=3111,month=2,day=2),phone_number='1111111111',mail_address='mail')
        status=''
        if reg.date_of_birth.year>datetime.datetime.now().year:
            status='birthday in range'
        else:
            status='birthday out of range'
        self.assertEquals(status,'birthday out of range')

    def test_ageIncorrect(self):  
        admin=User.objects.create_superuser('admin','1800notAreal@email.com','p@ssWord')
        c=Client()
        loggedin=c.login(username=admin.username,password='p@ssWord')
        #unreasonable date of birth
        #dont let me do this
        reg2=Registration(admin,role='AD',date_of_birth=datetime.date(year=1111,month=2,day=2),phone_number='1111111111',mail_address='mail')
        status=''
        timediff=datetime.datetime.now().year-reg2.date_of_birth.year
        self.assertIs(timediff>150,False)


    
    def test_appointmentCreatedInFuture(self):  
        admin=User.objects.create_superuser('admin','1800notAreal@email.com','p@ssWord')
        c=Client()
        loggedin=c.login(username=admin.username,password='p@ssWord')
        #create an appointment in the future
        reg2=Appointment(admin,date_scheduled=datetime.datetime.now()+datetime.timedelta(days=1))
        timediff=datetime.datetime.now().day-reg2.date_scheduled.day
        self.assertIs(timediff<0,True)



    def test_appointmentCreatedInPast(self):  
        admin=User.objects.create_superuser('admin','1800notAreal@email.com','p@ssWord')
        c=Client()
        loggedin=c.login(username=admin.username,password='p@ssWord')
        #create an appointment in the past
        reg2=Appointment(admin,date_scheduled=datetime.datetime.now()-datetime.timedelta(days=1))
        timediff=datetime.datetime.now().day-reg2.date_scheduled.day
        self.assertIs(timediff>0,False)


    def test_PrescriptionMedicine(self):  
        admin=User.objects.create_superuser('admin','1800notAreal@email.com','p@ssWord')
        c=Client()
        loggedin=c.login(username=admin.username,password='p@ssWord')
        #testing description
        reg2=Prescription(admin, medicine='It was the best of times, it was the worst of times, it was the age of wisdom',dosage="According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground.",doctors_note='UUDDLRLRBAUUDDLRLRBA',pharmacy="Electrode, Diglett, Nidoran, Mankey, Venusaur, Rattata, Fearow, Pidgey, Seaking, Jolteon, Dragonite, Gastly, Ponyta, Vaporeon, Poliwrath, Butterfree")
        self.assertEquals(reg2.medicine,'It was the best of times, it was the worst of times, it was the age of wisdom')

    def test_PrescriptionDosage(self):  
        admin=User.objects.create_superuser('admin','1800notAreal@email.com','p@ssWord')
        c=Client()
        loggedin=c.login(username=admin.username,password='p@ssWord')
        #testing description
        reg2=Prescription(admin, medicine='It was the best of times, it was the worst of times, it was the age of wisdom',dosage='According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground.',doctors_note='UUDDLRLRBAUUDDLRLRBA',pharmacy='Electrode, Diglett, Nidoran, Mankey, Venusaur, Rattata, Fearow, Pidgey, Seaking, Jolteon, Dragonite, Gastly, Ponyta, Vaporeon, Poliwrath, Butterfree')
        self.assertEquals(reg2.dosage,'According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground.')

    def test_PrescriptionDoctorsNote(self):  
        admin=User.objects.create_superuser('admin','1800notAreal@email.com','p@ssWord')
        c=Client()
        loggedin=c.login(username=admin.username,password='p@ssWord')
        #testing description
        reg2=Prescription(admin, medicine='It was the best of times, it was the worst of times, it was the age of wisdom',dosage='According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground.',doctors_note='UUDDLRLRBAUUDDLRLRBA',pharmacy='Electrode, Diglett, Nidoran, Mankey, Venusaur, Rattata, Fearow, Pidgey, Seaking, Jolteon, Dragonite, Gastly, Ponyta, Vaporeon, Poliwrath, Butterfree')
        self.assertEquals(reg2.doctors_note,'UUDDLRLRBAUUDDLRLRBA')

    def test_PrescriptionPharmacy(self):  
        admin=User.objects.create_superuser('admin','1800notAreal@email.com','p@ssWord')
        c=Client()
        loggedin=c.login(username=admin.username,password='p@ssWord')
        #testing description
        reg2=Prescription(admin, medicine='It was the best of times, it was the worst of times, it was the age of wisdom',dosage='According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground.',doctors_note='UUDDLRLRBAUUDDLRLRBA',pharmacy='Electrode, Diglett, Nidoran, Mankey, Venusaur, Rattata, Fearow, Pidgey, Seaking, Jolteon, Dragonite, Gastly, Ponyta, Vaporeon, Poliwrath, Butterfree')
        self.assertEquals(reg2.pharmacy,'Electrode, Diglett, Nidoran, Mankey, Venusaur, Rattata, Fearow, Pidgey, Seaking, Jolteon, Dragonite, Gastly, Ponyta, Vaporeon, Poliwrath, Butterfree')

    def test_Record(self):
        admin=User.objects.create_superuser('admin','1800notAreal@email.com','p@ssWord')
        c=Client()
        loggedin=c.login(username=admin.username,password='p@ssWord')
        #testing record
        reg2=Record(admin, record_type='HR',doctors_note='Every time im running Im feeling like I gotta get away, get away,get away Better know that I wont and I wont ever stop Cause you know that I gotta win everyday,day')
        self.assertEquals(reg2.doctors_note,'Every time im running Im feeling like I gotta get away, get away,get away Better know that I wont and I wont ever stop Cause you know that I gotta win everyday,day')

    def test_Activity(self):  
        admin=User.objects.create_superuser('admin','1800notAreal@email.com','p@ssWord')
        c=Client()
        loggedin=c.login(username=admin.username,password='p@ssWord')
        #testing description
        reg2=Activity(admin, activity_type='RG',description='Ladies and gentlemen, this is Chris and Im your chief flight attendant. On behalf of Captain Chris and the entire crew, welcome aboard SWEN Airlines flight f261-14d, non-stop service from R1 to an A. Our flight time will be 12 minutes.')
        self.assertEquals(reg2.description,'Ladies and gentlemen, this is Chris and Im your chief flight attendant. On behalf of Captain Chris and the entire crew, welcome aboard SWEN Airlines flight f261-14d, non-stop service from R1 to an A. Our flight time will be 12 minutes.')

    def test_ActivityRedirect(self):
        c=Client()
        response=c.get(reverse('system:dashboard'),follow=True)
        admin=User.objects.create_superuser('admin','1800notAreal@email.com','p@ssWord')
        login=c.login(username=admin.username,password='p@ssWord')
        lastUrl,status=response.redirect_chain[-1]
        self.assertRedirects(response,lastUrl,status_code=302,target_status_code=200,host=None,msg_prefix='',fetch_redirect_response=True)

    def test_message(self):  
        admin=User.objects.create_superuser('admin','1800notAreal@email.com','p@ssWord')
        reciever=User.objects.create_user('reciever','1800notAreal@gmail.com','pass@word@2')
        c=Client()
        loggedin=c.login(username=admin.username,password='p@ssWord')
        #create an appointment in the future
        reg2=Message(admin,reciever,text='The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [beep] A single lap should be completed each time you hear this sound. [ding] Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start.')

        self.assertEquals(reg2.text,'The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [beep] A single lap should be completed each time you hear this sound. [ding] Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start.')


