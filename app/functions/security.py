# Functions for security

from argon2 import PasswordHasher

ph = PasswordHasher()

def hash_password(password):
    """
    Hashes a password
    
    Args:
        password: str
        
    Returns:
        str
    """
    return ph.hash(password)

def verify_password(hashed_password, password):
    """
    Verifies a password against a hashed password
    
    Args: 
        hashed_password: str
        password: str
    
    Returns:
        bool
    """
    try:
        ph.verify(hashed_password, password)
        return True
    except:
        return False

