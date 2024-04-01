from Asg2_Louvre import Artwork, Exhibition, Visitor, Ticket, Tour, SpecialEvent

def test_add_artwork_to_museum():
    artwork = Artwork("Mona Lisa", "Leonardo da Vinci", "1503", "Iconic portrait", "Permanent galleries")
    if artwork.title == "Mona Lisa":
        print("Artwork successfully added to the museum.")
    else:
        print("Failed to add artwork to the museum.")

def test_open_exhibition_or_event():
    exhibition = Exhibition("Modern Art Exhibition", "2024-04-01", "Exhibition Hall 1")
    if exhibition.name == "Modern Art Exhibition":
        print("Exhibition successfully opened at the museum.")
    else:
        print("Failed to open exhibition at the museum.")

def test_purchase_tickets():
    ticket = Ticket(1, "2024-04-01", "2024-04-05", "Exhibition Hall 1", 63)
    if ticket.ticket_id == 1:
        print("Ticket successfully purchased.")
    else:
        print("Failed to purchase ticket.")

def test_display_payment_receipts():
    ticket1 = Ticket(1, "2024-04-01", "2024-04-05", "Exhibition Hall 1", 63)
    ticket2 = Ticket(2, "2024-04-02", "2024-04-06", "Exhibition Hall 2", 75)
    total_price = ticket1.price + ticket2.price
    receipt = f"Ticket ID: {ticket1.ticket_id}, Purchase Date: {ticket1.purchase_date}, " \
              f"Event Date: {ticket1.event_date}, Event Location: {ticket1.event_location}, " \
              f"Price: {ticket1.price} AED\n" \
              f"Ticket ID: {ticket2.ticket_id}, Purchase Date: {ticket2.purchase_date}, " \
              f"Event Date: {ticket2.event_date}, Event Location: {ticket2.event_location}, " \
              f"Price: {ticket2.price} AED\n" \
              f"Total Price: {total_price} AED"
    print("Payment Receipts:")
    print(receipt)

if __name__ == '__main__':
    test_add_artwork_to_museum()
    test_open_exhibition_or_event()
    test_purchase_tickets()
    test_display_payment_receipts()