"""
Run this script to manually create database tables.
Usage: python create_tables.py
"""
import os
from sqlalchemy import create_engine
from models import Base

# Get database URL from environment or use default
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost/caregivers_platform")

# Fix for psycopg (v3)
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+psycopg://", 1)
elif DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+psycopg://", 1)

print(f"Connecting to database...")
engine = create_engine(DATABASE_URL)

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("✓ Tables created successfully!")
