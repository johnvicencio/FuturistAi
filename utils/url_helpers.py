from flask import url_for
import os
from urllib.parse import urljoin

def override_url_for():
    """Context processor to make dated_url_for available in templates"""
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    """
    Custom URL generator that:
    - Uses GitHub's media CDN in production
    - Uses local static files in development
    """
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            # Use GitHub media CDN in production
            if os.environ.get('FLASK_ENV') == 'production':
                return urljoin(
                    'https://media.githubusercontent.com/media/johnvicencio/FuturistAi/main/',
                    f'static/{filename}'
                )
    
    # Default Flask behavior for all other cases
    return url_for(endpoint, **values)