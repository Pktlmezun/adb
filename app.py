from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Optional
from datetime import date, time
import os
from models import Base, User, Caregiver, Member, Address, Job, JobApplication, Appointment
from models import GenderEnum, CaregivingTypeEnum, AppointmentStatusEnum

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost/caregivers_platform")
# Fix for psycopg (v3) - replace postgresql:// with postgresql+psycopg://
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+psycopg://", 1)
elif DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+psycopg://", 1)

engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables if they don't exist (for first deployment)
# Wrap in try-except to handle initial connection issues
try:
    Base.metadata.create_all(bind=engine)
except Exception as e:
    print(f"Warning: Could not create tables on startup: {e}")
    print("Tables will be created on first database access")

app = FastAPI(title="Caregivers Platform")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_enum_from_value(enum_class, value):
    for member in enum_class:
        if member.value == value:
            return member
    raise ValueError(f"No enum member found for value: {value}")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/users", response_class=HTMLResponse)
async def list_users(request: Request):
    db = next(get_db())
    users = db.query(User).all()
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.post("/users/create")
async def create_user(
    email: str = Form(...),
    given_name: str = Form(...),
    surname: str = Form(...),
    city: str = Form(...),
    phone_number: str = Form(...),
    profile_description: str = Form(""),
    password: str = Form(...)
):
    db = next(get_db())
    user = User(
        email=email,
        given_name=given_name,
        surname=surname,
        city=city,
        phone_number=phone_number,
        profile_description=profile_description,
        password=password
    )
    db.add(user)
    db.commit()
    return RedirectResponse(url="/users", status_code=303)


@app.post("/users/update/{user_id}")
async def update_user(
    user_id: int,
    email: str = Form(...),
    given_name: str = Form(...),
    surname: str = Form(...),
    city: str = Form(...),
    phone_number: str = Form(...),
    profile_description: str = Form(""),
    password: str = Form(...)
):
    db = next(get_db())
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.email = email
    user.given_name = given_name
    user.surname = surname
    user.city = city
    user.phone_number = phone_number
    user.profile_description = profile_description
    user.password = password

    db.commit()
    return RedirectResponse(url="/users", status_code=303)


@app.post("/users/delete/{user_id}")
async def delete_user(user_id: int):
    db = next(get_db())
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return RedirectResponse(url="/users", status_code=303)


@app.get("/caregivers", response_class=HTMLResponse)
async def list_caregivers(request: Request):
    db = next(get_db())
    caregivers = db.query(Caregiver).join(User).all()
    users_without_caregiver = db.query(User).outerjoin(Caregiver).filter(Caregiver.caregiver_user_id == None).all()
    return templates.TemplateResponse("caregivers.html", {
        "request": request,
        "caregivers": caregivers,
        "available_users": users_without_caregiver,
        "genders": ["Male", "Female", "Other"],
        "caregiving_types": ["babysitter", "caregiver for elderly", "playmate for children"]
    })


@app.post("/caregivers/create")
async def create_caregiver(
    caregiver_user_id: int = Form(...),
    photo: str = Form(""),
    gender: str = Form(...),
    caregiving_type: str = Form(...),
    hourly_rate: float = Form(...)
):
    db = next(get_db())
    caregiver = Caregiver(
        caregiver_user_id=caregiver_user_id,
        photo=photo,
        gender=gender,
        caregiving_type=caregiving_type,
        hourly_rate=hourly_rate
    )
    db.add(caregiver)
    db.commit()
    return RedirectResponse(url="/caregivers", status_code=303)


@app.post("/caregivers/update/{caregiver_user_id}")
async def update_caregiver(
    caregiver_user_id: int,
    photo: str = Form(""),
    gender: str = Form(...),
    caregiving_type: str = Form(...),
    hourly_rate: float = Form(...)
):
    db = next(get_db())
    caregiver = db.query(Caregiver).filter(Caregiver.caregiver_user_id == caregiver_user_id).first()
    if not caregiver:
        raise HTTPException(status_code=404, detail="Caregiver not found")

    caregiver.photo = photo
    caregiver.gender = gender
    caregiver.caregiving_type = caregiving_type
    caregiver.hourly_rate = hourly_rate

    db.commit()
    return RedirectResponse(url="/caregivers", status_code=303)


@app.post("/caregivers/delete/{caregiver_user_id}")
async def delete_caregiver(caregiver_user_id: int):
    db = next(get_db())
    caregiver = db.query(Caregiver).filter(Caregiver.caregiver_user_id == caregiver_user_id).first()
    if not caregiver:
        raise HTTPException(status_code=404, detail="Caregiver not found")

    db.delete(caregiver)
    db.commit()
    return RedirectResponse(url="/caregivers", status_code=303)


@app.get("/members", response_class=HTMLResponse)
async def list_members(request: Request):
    db = next(get_db())
    members = db.query(Member).join(User).all()
    users_without_member = db.query(User).outerjoin(Member).filter(Member.member_user_id == None).all()
    return templates.TemplateResponse("members.html", {
        "request": request,
        "members": members,
        "available_users": users_without_member
    })


@app.post("/members/create")
async def create_member(
    member_user_id: int = Form(...),
    house_rules: str = Form(""),
    dependent_description: str = Form("")
):
    db = next(get_db())
    member = Member(
        member_user_id=member_user_id,
        house_rules=house_rules,
        dependent_description=dependent_description
    )
    db.add(member)
    db.commit()
    return RedirectResponse(url="/members", status_code=303)


@app.post("/members/update/{member_user_id}")
async def update_member(
    member_user_id: int,
    house_rules: str = Form(""),
    dependent_description: str = Form("")
):
    db = next(get_db())
    member = db.query(Member).filter(Member.member_user_id == member_user_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")

    member.house_rules = house_rules
    member.dependent_description = dependent_description

    db.commit()
    return RedirectResponse(url="/members", status_code=303)


@app.post("/members/delete/{member_user_id}")
async def delete_member(member_user_id: int):
    db = next(get_db())
    member = db.query(Member).filter(Member.member_user_id == member_user_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")

    db.delete(member)
    db.commit()
    return RedirectResponse(url="/members", status_code=303)


@app.get("/addresses", response_class=HTMLResponse)
async def list_addresses(request: Request):
    db = next(get_db())
    addresses = db.query(Address).join(Member).join(User).all()
    members_without_address = db.query(Member).outerjoin(Address).filter(Address.member_user_id == None).all()
    return templates.TemplateResponse("addresses.html", {
        "request": request,
        "addresses": addresses,
        "available_members": members_without_address
    })


@app.post("/addresses/create")
async def create_address(
    member_user_id: int = Form(...),
    house_number: str = Form(...),
    street: str = Form(...),
    town: str = Form(...)
):
    db = next(get_db())
    address = Address(
        member_user_id=member_user_id,
        house_number=house_number,
        street=street,
        town=town
    )
    db.add(address)
    db.commit()
    return RedirectResponse(url="/addresses", status_code=303)


@app.post("/addresses/update/{member_user_id}")
async def update_address(
    member_user_id: int,
    house_number: str = Form(...),
    street: str = Form(...),
    town: str = Form(...)
):
    db = next(get_db())
    address = db.query(Address).filter(Address.member_user_id == member_user_id).first()
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")

    address.house_number = house_number
    address.street = street
    address.town = town

    db.commit()
    return RedirectResponse(url="/addresses", status_code=303)


@app.post("/addresses/delete/{member_user_id}")
async def delete_address(member_user_id: int):
    db = next(get_db())
    address = db.query(Address).filter(Address.member_user_id == member_user_id).first()
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")

    db.delete(address)
    db.commit()
    return RedirectResponse(url="/addresses", status_code=303)


@app.get("/jobs", response_class=HTMLResponse)
async def list_jobs(request: Request):
    db = next(get_db())
    jobs = db.query(Job).join(Member).join(User).all()
    members = db.query(Member).join(User).all()
    return templates.TemplateResponse("jobs.html", {
        "request": request,
        "jobs": jobs,
        "members": members,
        "caregiving_types": ["babysitter", "caregiver for elderly", "playmate for children"]
    })


@app.post("/jobs/create")
async def create_job(
    member_user_id: int = Form(...),
    required_caregiving_type: str = Form(...),
    other_requirements: str = Form(""),
    date_posted: str = Form(...)
):
    db = next(get_db())
    job = Job(
        member_user_id=member_user_id,
        required_caregiving_type=required_caregiving_type,
        other_requirements=other_requirements,
        date_posted=date.fromisoformat(date_posted)
    )
    db.add(job)
    db.commit()
    return RedirectResponse(url="/jobs", status_code=303)


@app.post("/jobs/update/{job_id}")
async def update_job(
    job_id: int,
    member_user_id: int = Form(...),
    required_caregiving_type: str = Form(...),
    other_requirements: str = Form(""),
    date_posted: str = Form(...)
):
    db = next(get_db())
    job = db.query(Job).filter(Job.job_id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    job.member_user_id = member_user_id
    job.required_caregiving_type = required_caregiving_type
    job.other_requirements = other_requirements
    job.date_posted = date.fromisoformat(date_posted)

    db.commit()
    return RedirectResponse(url="/jobs", status_code=303)


@app.post("/jobs/delete/{job_id}")
async def delete_job(job_id: int):
    db = next(get_db())
    job = db.query(Job).filter(Job.job_id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    db.delete(job)
    db.commit()
    return RedirectResponse(url="/jobs", status_code=303)


@app.get("/applications", response_class=HTMLResponse)
async def list_applications(request: Request):
    db = next(get_db())
    applications = db.query(JobApplication).join(Caregiver).join(User).all()
    caregivers = db.query(Caregiver).join(User).all()
    jobs = db.query(Job).all()
    return templates.TemplateResponse("applications.html", {
        "request": request,
        "applications": applications,
        "caregivers": caregivers,
        "jobs": jobs
    })


@app.post("/applications/create")
async def create_application(
    caregiver_user_id: int = Form(...),
    job_id: int = Form(...),
    date_applied: str = Form(...)
):
    db = next(get_db())
    application = JobApplication(
        caregiver_user_id=caregiver_user_id,
        job_id=job_id,
        date_applied=date.fromisoformat(date_applied)
    )
    db.add(application)
    db.commit()
    return RedirectResponse(url="/applications", status_code=303)


@app.post("/applications/update/{caregiver_user_id}/{job_id}")
async def update_application(
    caregiver_user_id: int,
    job_id: int,
    date_applied: str = Form(...)
):
    db = next(get_db())
    application = db.query(JobApplication).filter(
        JobApplication.caregiver_user_id == caregiver_user_id,
        JobApplication.job_id == job_id
    ).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")

    application.date_applied = date.fromisoformat(date_applied)

    db.commit()
    return RedirectResponse(url="/applications", status_code=303)


@app.post("/applications/delete/{caregiver_user_id}/{job_id}")
async def delete_application(caregiver_user_id: int, job_id: int):
    db = next(get_db())
    application = db.query(JobApplication).filter(
        JobApplication.caregiver_user_id == caregiver_user_id,
        JobApplication.job_id == job_id
    ).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")

    db.delete(application)
    db.commit()
    return RedirectResponse(url="/applications", status_code=303)


@app.get("/appointments", response_class=HTMLResponse)
async def list_appointments(request: Request):
    db = next(get_db())
    appointments = db.query(Appointment).all()
    caregivers = db.query(Caregiver).join(User).all()
    members = db.query(Member).join(User).all()
    return templates.TemplateResponse("appointments.html", {
        "request": request,
        "appointments": appointments,
        "caregivers": caregivers,
        "members": members,
        "statuses": ["pending", "accepted", "declined"]
    })


@app.post("/appointments/create")
async def create_appointment(
    caregiver_user_id: int = Form(...),
    member_user_id: int = Form(...),
    appointment_date: str = Form(...),
    appointment_time: str = Form(...),
    work_hours: int = Form(...),
    status: str = Form(...)
):
    db = next(get_db())
    appointment = Appointment(
        caregiver_user_id=caregiver_user_id,
        member_user_id=member_user_id,
        appointment_date=date.fromisoformat(appointment_date),
        appointment_time=time.fromisoformat(appointment_time),
        work_hours=work_hours,
        status=status
    )
    db.add(appointment)
    db.commit()
    return RedirectResponse(url="/appointments", status_code=303)


@app.post("/appointments/update/{appointment_id}")
async def update_appointment(
    appointment_id: int,
    caregiver_user_id: int = Form(...),
    member_user_id: int = Form(...),
    appointment_date: str = Form(...),
    appointment_time: str = Form(...),
    work_hours: int = Form(...),
    status: str = Form(...)
):
    db = next(get_db())
    appointment = db.query(Appointment).filter(Appointment.appointment_id == appointment_id).first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    appointment.caregiver_user_id = caregiver_user_id
    appointment.member_user_id = member_user_id
    appointment.appointment_date = date.fromisoformat(appointment_date)
    appointment.appointment_time = time.fromisoformat(appointment_time)
    appointment.work_hours = work_hours
    appointment.status = status

    db.commit()
    return RedirectResponse(url="/appointments", status_code=303)


@app.post("/appointments/delete/{appointment_id}")
async def delete_appointment(appointment_id: int):
    db = next(get_db())
    appointment = db.query(Appointment).filter(Appointment.appointment_id == appointment_id).first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    db.delete(appointment)
    db.commit()
    return RedirectResponse(url="/appointments", status_code=303)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

