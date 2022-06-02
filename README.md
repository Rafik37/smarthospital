
# Smart Hospital
---
## Screenshots 
### Homepage
![homepage snap](https://github.com/Rafik37/hospitalmanagement/blob/master/static/screenshots/homepage.png?raw=true)
### Homepage Cards
![homepage snap](https://github.com/Rafik37/hospitalmanagement/blob/master/static/screenshots/homepage1.PNG?raw=true)
### Admin Login
![admin login](https://github.com/Rafik37/hospitalmanagement/blob/master/static/screenshots/adminlogin.PNG?raw=true)
====================================================================================================================
### Admin Dashboard
![dashboard admin](https://github.com/Rafik37/hospitalmanagement/blob/master/static/screenshots/admin_dashboard.png?raw=true)
=======
### Admin Doctor pannel
![doctor snap](https://github.com/Rafik37/hospitalmanagement/blob/master/static/screenshots/admin_doctor.png?raw=true)
### Doctor list
![doctor snap](https://github.com/Rafik37/hospitalmanagement/blob/master/static/screenshots/admin_doctor1.png?raw=true)
---
## Functions
### Admin
- Signup then login.
- Can add/view/approve/reject/delete doctor (approve those doctor who applied for job in their hospital).
- Can add/view/approve/reject/discharge patient.
- Can Generate/Download Invoice pdf.
- Can view/book/approve Appointment.

### Doctor
- Apply for job in hospital. Then Login (Approval required by hospital admin, Then only doctor can login).
- Can only view their patient details (symptoms, name, mobile ) assigned to that doctor by admin.
- Can view their discharged(by admin) patient list.
- Can view their Appointments, booked by admin.
- Can delete their Appointment, when doctor attended their appointment.

### Patient
- Create account for admit in hospital. Then Login (Approval required by hospital admin, Then only patient can login).
- Can view assigned doctor's details like ( specialization, mobile, address).
- Can view their booked appointment status (pending/confirmed by admin).
- Can book appointments.(approval required by admin)
- Can view/download Invoice pdf (Only when that patient is discharged by admin).

---

## HOW TO RUN THIS PROJECT
- Install Python(3.7.6) (Dont Forget to Tick Add to Path while installing Python)
- Open Terminal and Execute Following Commands :
```
pip install django==3.0.5
pip install django-widget-tweaks
pip install xhtml2pdf
```
- Download This Project Zip Folder and Extract it
- Move to project folder in Terminal. Then run following Commands :
```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
- Now enter following URL in Your Browser Installed On Your Pc
```
http://127.0.0.1:8000/
```
