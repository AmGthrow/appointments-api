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

Install dependencies

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

The Appointment object contains 4 fields:

- `start_time` - a `DateTimeField()` for when the appointment will start
- `end_time` - a `DateTimeField()` for when the appointment will end
- `patients` - a `ManyToManyField()` linking to the patients included in the appointment
- `comments` - a `TextField()` containing comments for the appointment

### API Endpoints

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

The Patient object contains 1 field:

- `name` - a `CharField()` representing the patient's name

### API Endpoints

- `GET /patients/` - list out the patients that currently exist
- `POST /patients/` - create a new patient
- `GET /patients/{id}/` - retrieve details for one specific patient
- `PUT /patients/{id}/` - update an existing patient with new data
- `DELETE /patients/{id}/` - delete an existing patient
