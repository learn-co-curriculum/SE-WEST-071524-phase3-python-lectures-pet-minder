# Stretch Goal: Build Out Corresponding Owner Members

# Owner Attributes: 
# name: string 
# phone: string 
# email: string 
# address: string

import sqlite3

CONN = sqlite3.connect('lib/resources.db')
CURSOR = CONN.cursor()

class Owner:
    
    pass