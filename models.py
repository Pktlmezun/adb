"""
CSCI 341 Assignment 3 - Part 2
ORM Models for Caregivers Platform Database
Using SQLAlchemy ORM
"""

from sqlalchemy import Column, Integer, String, Text, Date, Time, DECIMAL, Enum, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
import enum

Base = declarative_base()


# Enum classes for controlled values
class GenderEnum(str, enum.Enum):
    Male = "Male"
    Female = "Female"
    Other = "Other"


class CaregivingTypeEnum(str, enum.Enum):
    babysitter = "babysitter"
    caregiver_for_elderly = "caregiver for elderly"
    playmate_for_children = "playmate for children"


class AppointmentStatusEnum(str, enum.Enum):
    pending = "pending"
    accepted = "accepted"
    declined = "declined"


# ORM Models
class User(Base):
    __tablename__ = 'USER'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), nullable=False, unique=True)
    given_name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    phone_number = Column(String(20), nullable=False)
    profile_description = Column(Text)
    password = Column(String(255), nullable=False)

    # Relationships
    caregiver = relationship("Caregiver", back_populates="user", uselist=False, cascade="all, delete-orphan")
    member = relationship("Member", back_populates="user", uselist=False, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(id={self.user_id}, name={self.given_name} {self.surname})>"


class Caregiver(Base):
    __tablename__ = 'CAREGIVER'

    caregiver_user_id = Column(Integer, ForeignKey('USER.user_id', ondelete='CASCADE'), primary_key=True)
    photo = Column(String(255))
    gender = Column(String(50), nullable=False)
    caregiving_type = Column(String(50), nullable=False)
    hourly_rate = Column(DECIMAL(10, 2), nullable=False)

    # Relationships
    user = relationship("User", back_populates="caregiver")
    job_applications = relationship("JobApplication", back_populates="caregiver", cascade="all, delete-orphan")
    appointments = relationship("Appointment", back_populates="caregiver", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Caregiver(id={self.caregiver_user_id}, type={self.caregiving_type.value})>"


class Member(Base):
    __tablename__ = 'MEMBER'

    member_user_id = Column(Integer, ForeignKey('USER.user_id', ondelete='CASCADE'), primary_key=True)
    house_rules = Column(Text)
    dependent_description = Column(Text)

    # Relationships
    user = relationship("User", back_populates="member")
    address = relationship("Address", back_populates="member", uselist=False, cascade="all, delete-orphan")
    jobs = relationship("Job", back_populates="member", cascade="all, delete-orphan")
    appointments = relationship("Appointment", back_populates="member", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Member(id={self.member_user_id})>"


class Address(Base):
    __tablename__ = 'ADDRESS'

    member_user_id = Column(Integer, ForeignKey('MEMBER.member_user_id', ondelete='CASCADE'), primary_key=True)
    house_number = Column(String(20), nullable=False)
    street = Column(String(255), nullable=False)
    town = Column(String(100), nullable=False)

    # Relationships
    member = relationship("Member", back_populates="address")

    def __repr__(self):
        return f"<Address(member_id={self.member_user_id}, street={self.street})>"


class Job(Base):
    __tablename__ = 'JOB'

    job_id = Column(Integer, primary_key=True, autoincrement=True)
    member_user_id = Column(Integer, ForeignKey('MEMBER.member_user_id', ondelete='CASCADE'), nullable=False)
    required_caregiving_type = Column(String(50), nullable=False)
    other_requirements = Column(Text)
    date_posted = Column(Date, nullable=False)

    # Relationships
    member = relationship("Member", back_populates="jobs")
    job_applications = relationship("JobApplication", back_populates="job", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Job(id={self.job_id}, type={self.required_caregiving_type.value})>"


class JobApplication(Base):
    __tablename__ = 'JOB_APPLICATION'

    caregiver_user_id = Column(Integer, ForeignKey('CAREGIVER.caregiver_user_id', ondelete='CASCADE'), primary_key=True)
    job_id = Column(Integer, ForeignKey('JOB.job_id', ondelete='CASCADE'), primary_key=True)
    date_applied = Column(Date, nullable=False)

    # Relationships
    caregiver = relationship("Caregiver", back_populates="job_applications")
    job = relationship("Job", back_populates="job_applications")

    def __repr__(self):
        return f"<JobApplication(caregiver={self.caregiver_user_id}, job={self.job_id})>"


class Appointment(Base):
    __tablename__ = 'APPOINTMENT'

    appointment_id = Column(Integer, primary_key=True, autoincrement=True)
    caregiver_user_id = Column(Integer, ForeignKey('CAREGIVER.caregiver_user_id', ondelete='CASCADE'), nullable=False)
    member_user_id = Column(Integer, ForeignKey('MEMBER.member_user_id', ondelete='CASCADE'), nullable=False)
    appointment_date = Column(Date, nullable=False)
    appointment_time = Column(Time, nullable=False)
    work_hours = Column(Integer, nullable=False)
    status = Column(String(50), nullable=False)

    # Relationships
    caregiver = relationship("Caregiver", back_populates="appointments")
    member = relationship("Member", back_populates="appointments")

    def __repr__(self):
        return f"<Appointment(id={self.appointment_id}, status={self.status.value})>"

