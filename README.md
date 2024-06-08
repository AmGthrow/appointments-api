# Installation and Setup

Create a virtual environment

```
python -m venv venv
```

Activate the virtual environment

```
source venv/bin/activate    # For Linux
venv/Scripts/activate       # For Windows
```

Install dependencies. If installation fails, please ensure you have Python 3.10.

```
pip install -r requirements.txt
```

Run a local instance of the backend server

```
cd technical_assessment
python manage.py runserver
```

# Usage

There are currently two apps being used

- `appointments` - handles CRUD for actual appointments
- `patients` - handles CRUD for patients (mostly just their names)

## Appointments

### Model

![image](https://github.com/AmGthrow/appointments-api/assets/54239564/53adbcf9-5e4b-443c-b27a-bbec0410126d)

The Appointment object contains 4 fields:

- `start_time` - a `DateTimeField()` for when the appointment will start
- `end_time` - a `DateTimeField()` for when the appointment will end
- `patients` - a `ManyToManyField()` linking to the patients included in the appointment
- `comments` - a `TextField()` containing comments for the appointment

### API Endpoints

![image](https://github.com/AmGthrow/appointments-api/assets/54239564/a3bb4f81-e01d-45b6-8e23-5f2329d80af8)

- `GET /appointments/` - list out the appointments that currently exist
  - Query parameters:
    - `start_date` - a date of the format `YYYY-MM-DD`. Only appointments on or later than this date will be included
    - `end_date` - a date of the format `YYYY-MM-DD`. Only appointments on or earlier than this date will be included
- `POST /appointments/` - create a new appointment
- `GET /appointments/{id}/` - retrieve details for one specific appointment
- `PUT /appointments/{id}/` - update an existing appointment with new data
- `DELETE /appointments/{id}/` - delete an existing appointment

## Patients

### Model

![image](https://github.com/AmGthrow/appointments-api/assets/54239564/89c0bd16-8a17-4b56-ae79-ecd650c8a29e)

The Patient object contains 1 field:

- `name` - a `CharField()` representing the patient's name

### API Endpoints

![image](https://github.com/AmGthrow/appointments-api/assets/54239564/40344368-15ad-44a3-9496-e50f0869691b)

- `GET /patients/` - list out the patients that currently exist
- `POST /patients/` - create a new patient
- `GET /patients/{id}/` - retrieve details for one specific patient
- `PUT /patients/{id}/` - update an existing patient with new data
- `DELETE /patients/{id}/` - delete an existing patient
