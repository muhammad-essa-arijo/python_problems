"""
Problem: Create a formatted event ticket using f-string alignment and width formatting.
"""

event = "OpenHack25 Conference"
venue = "MUET SZAB Campus"
attendee = "Essa Arijo"
ticket_id = "TKT-9021"

print("*" * 40)
# The <20 means left-align with 20 spaces, >15 means right-align with 15 spaces
print(f"* {event:<25} {ticket_id:>9} *")
print(f"* Venue: {venue:<28} *")
print(f"* Attendee: {attendee:<25} *")
print("*" * 40)