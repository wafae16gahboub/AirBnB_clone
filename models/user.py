#!/usr/bin/python3
"""User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
