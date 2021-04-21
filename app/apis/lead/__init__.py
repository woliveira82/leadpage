from flask import Blueprint

lead = Blueprint('lead', __name__)

from app.apis.lead.lead_apis import *

