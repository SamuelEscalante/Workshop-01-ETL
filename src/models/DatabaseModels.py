"""
SQLAlchemy Table Definition 

This script defines two model classes to represent tables in a database using SQLAlchemy.

Defined Classes:
- Candidates: Represents the 'Candidates' table with fields related to candidates.
- SuccessfulApplicants: Represents the 'SuccessfulApplicants' table with additional fields specific to successful candidates.

Common Attributes:
- id: Unique identifier for each record.
- FirstName: Candidate's first name.
- LastName: Candidate's last name.
- Email: Candidate's email address.
- ApplicationDate: Date of the candidate's application.
- Country: Candidate's country of residence.
- YOE: Years of experience of the candidate.
- Seniority: Candidate's seniority level.
- Technology: Technology related to the application.
- CodeChallengeScore: Score in the code challenge.
- TechnicalInterviewScore: Score in the technical interview.

Additional Attributes (Only in SuccessfulApplicants):
- Continent: Continent of the successful candidate.
- CategoryOfTechnology: Specific category of technology.
- Hired: Indicator of whether the candidate was hired (1 if hired, 0 if not).

Additionally, both classes have a special __str__ method that provides a string representation of the associated table.
"""

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

BASE = declarative_base()

class Candidates(BASE):
    __tablename__ = 'Candidates'
    id = Column(Integer, primary_key=True, autoincrement=True)
    FirstName = Column(String(100), nullable=False)
    LastName = Column(String(100), nullable=False)
    Email = Column(String(100), nullable=False)
    ApplicationDate = Column(Date, nullable=False)
    Country = Column(String(100), nullable=False)
    YOE = Column(Integer, nullable=False)
    Seniority = Column(String(100), nullable=False)
    Technology = Column(String(100), nullable=False)
    CodeChallengeScore = Column(Integer, nullable=False)
    TechnicalInterviewScore = Column(Integer, nullable=False)
    
    def __str__ (self):
        return f" Table -> {self.Candidates.__table__}"
    
class SuccessfulApplicants(BASE):
    __tablename__ = 'SuccessfulApplicants'
    id = Column(Integer, primary_key=True, autoincrement=True)
    FirstName = Column(String(100), nullable=False)
    LastName = Column(String(100), nullable=False)
    Email = Column(String(100), nullable=False)
    ApplicationDate = Column(Date, nullable=False)
    Country = Column(String(100), nullable=False)
    Continent = Column(String(100), nullable=False)
    YOE = Column(Integer, nullable=False)
    Seniority = Column(String(100), nullable=False)
    Technology = Column(String(100), nullable=False)
    CodeChallengeScore = Column(Integer, nullable=False)
    TechnicalInterviewScore = Column(Integer, nullable=False)
    CategoryOfTechnology = Column(String(100), nullable=False)
    Hired = Column(Integer, nullable=False)
    
    def __str__(self):
        return f" Table -> {SuccessfulApplicants.__table__}"