class Agency():

    def __init__(self, agency_data: dict):
        self.agency_id = agency_data['agency_id']
        self.agency_name = agency_data['agency_name']
        self.agency_url = agency_data['agency_url']
        self.agency_timezone = agency_data['agency_timezone']
        self.agency_lang = agency_data['agency_lang']
        self.agency_phone = agency_data['agency_phone']
        self.agency_fare_url = agency_data['agency_fare_url']

    def __repr__(self):
        return f'Agency: {self.agency_name}'

    def __str__(self):
        return f'Agency: {self.agency_name}'
