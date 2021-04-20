from flask import Blueprint

campaign = Blueprint('campaign', __name__)

from app.apis.campaign.campaign_apis import *