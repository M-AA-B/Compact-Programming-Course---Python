# Task 5 — Dortmund events

# Create a dictionary containing event names and their dates
events = {
    "Dortmund Night of Museums": "19 September 2026",
    "Event 2": "19 September 2026",
    "Event 3": "19 September 2026"
}

# Go through each event in the dictionary
for event, date in events.items():

    # Check if the event was running on 19 September 2026
    if date == "19 September 2026":

        # Print the name of the event
        print(event)