class Artwork:
    def __init__(self, title, artist, date_of_creation, historical_significance, location):
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.historical_significance = historical_significance
        self.location = location


class Exhibition:
    def __init__(self, name, duration, location):
        self.name = name
        self.duration = duration
        self.location = location
        self.artworks = []  # Aggregation

    def add_artwork(self, artwork):
        self.artworks.append(artwork)


class Visitor:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.tickets = []  # Aggregation

    def purchase_ticket(self, ticket):
        self.tickets.append(ticket)


class Ticket:
    def __init__(self, ticket_id, purchase_date, event_date, event_location, price):
        self.ticket_id = ticket_id
        self.purchase_date = purchase_date
        self.event_date = event_date
        self.event_location = event_location
        self.price = price


class Tour:
    def __init__(self, tour_date, guide, group_size):
        self.tour_date = tour_date
        self.guide = guide
        self.group_size = group_size
        self.tickets = []  # Composition

    def add_ticket(self, ticket):
        self.tickets.append(ticket)


class SpecialEvent:
    def __init__(self, event_name, event_date, duration, location, ticket_price):
        self.event_name = event_name
        self.event_date = event_date
        self.duration = duration
        self.location = location
        self.ticket_price = ticket_price
        self.tickets = []  # Composition

    def add_ticket(self, ticket):
        self.tickets.append(ticket)