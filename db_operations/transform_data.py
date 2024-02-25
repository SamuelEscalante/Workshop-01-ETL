"""
transform_data.py

This module contains the TransformData class, which provides methods for processing and transforming data
from a CSV file. It includes functions to rename columns, insert an 'id' column, determine 'Hired' status, and
create a 'CategoryOfTechnology' column based on a mapping.
"""

import pandas as pd

class TransformData:
    """
    TransformData class for processing and transforming data.

    Parameters
    ----------
    file : str
        The path to the CSV file.

    Attributes
    ----------
    df : pandas.DataFrame
        The DataFrame to hold the data.

    Methods
    -------
    rename_columns()
        Rename specific columns in the DataFrame.

    insertar_id()
        Insert an 'id' column in the DataFrame.

    agregar_contratados()
        Add a 'Hired' column based on specified conditions.

    group_by_category()
        Create a 'CategoryOfTechnology' column based on a mapping.

    """
    def __init__(self, file):
        self.df = pd.read_csv(file, sep=';', encoding='utf-8')
        """
        Initialize the TransformData object.

        Parameters
        ----------
        file : str
            The path to the CSV file.
        """
    
    def rename_columns(self) -> None:
        """
        Rename specific columns in the DataFrame.

        Returns
        -------
        None
        """        
        self.df.rename(columns={            
            "First Name": "FirstName",
            "Last Name": "LastName",
            "Application Date": "ApplicationDate",
            "Code Challenge Score": "CodeChallengeScore",
            "Technical Interview Score": "TechnicalInterviewScore"}, inplace=True)

    def insertar_id(self) -> None:
        """
        Insert an 'id' column in the DataFrame.

        Returns
        -------
        None
        """
        self.df.insert(0, 'id', range(1, len(self.df) + 1))

    def agregar_contratados(self) -> None:
        """
        Add a 'Hired' column based on specified conditions.

        Returns
        -------
        None
        """     
        self.df["Hired"] = self.df.apply(lambda row: 1 if row["CodeChallengeScore"] >= 7 and row["TechnicalInterviewScore"] >= 7 else 0, axis=1)

    def group_by_category(self) -> None:
        """
        Create a 'CategoryOfTechnology' column based on a mapping.

        Returns
        -------
        None
        """
        self.technology_to_category = {
    'Development - CMS Backend': 'Development',
    'Development - CMS Frontend': 'Development',
    'Development - FullStack': 'Development',
    'Development - Frontend': 'Development',
    'Development - Backend': 'Development',
    'Game Development': 'Development',
    'DevOps': 'Development',
    'Adobe Experience Manager': 'Development',
    'QA Automation': 'Quality Assurance',
    'QA Manual': 'Quality Assurance',
    'System Administration': 'Security',
    'Security Compliance': 'Security',
    'Security': 'Security',
    'Database Administration': 'Data & Analytics',
    'Data Engineer': 'Data & Analytics',
    'Business Intelligence': 'Data & Analytics',
    'Business Analytics / Project Management': 'Data & Analytics',
    'Salesforce': 'Sales and Business',
    'Sales': 'Sales and Business',
    'Client Success': 'Sales and Business',
    'Social Media Community Management': 'Marketing and Communication',
    'Mulesoft': 'Marketing and Communication',
    'Technical Writing': 'Marketing and Communication',
    'Design': 'Design',
}
        self.df['CategoryOfTechnology'] = self.df['Technology'].map(self.technology_to_category)