

class Route():

    def __init__(self, route_data: dict):
        self.route_id = route_data['route_id']
        self.agency_id = route_data['agency_id']
        self.route_short_name = route_data['route_short_name']
        self.route_long_name = route_data['route_long_name']
        self.route_desc = route_data['route_desc']
        self.route_type = route_data['route_type']
        self.route_url = route_data['route_url']
        self.route_color = route_data['route_color']
        self.route_text_color = route_data['route_text_color']

    def __repr__(self):
        return f'Route: {self.route_long_name}'

    def __str__(self):
        return f'Route: {self.route_long_name}'