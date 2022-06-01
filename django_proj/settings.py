"""
This file is present for adding all the applications and the middleware application present.
Also, it has information about templates and databases.
Overall, this is the main file of my Django web application.
"""
from app.models.portfolio_data import DataStructureAndAnalysis


class DesignAndLayout(DataStructureAndAnalysis):
    """
    Front-end part of the flow, that will rely on the data retrieved from
    the DataStructureAndAnalysis class, and present it accordingly on the web
    page.
    """
    ...
