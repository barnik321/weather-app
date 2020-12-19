from flask import request
import requests


def retrieve_local_ip_adress():
    """Return IP address of our computer."""
    response = requests.get('https://api.ipify.org')

    return response.text


def get_client_ip_address():
    """Return ip address of the client"""
    return request.headers['X-Forwarded-For']