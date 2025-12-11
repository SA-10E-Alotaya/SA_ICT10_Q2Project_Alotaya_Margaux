from pyscript import display, document

# Define club information using dictionaries
club_info =  {
            "basketball": {
                "name": "Basketball Club",
                "description": "A club for Basketball enthusiasts of all skill levels.",
                "meeting_time": "Every Wednesday 3:30-5:00 PM",
                "location": "Quadrangle",
                "advisor": "Mr. Mariano",
                "members": 16,
                "category": "Special Subjects"
            },
            "drama": {
                "name": "Drama Club",
                "description": "For students interested in theater, acting, and stage production.",
                "meeting_time": "Every Monday and Thursday 4:00-6:00 PM",
                "location": "MM Hall",
                "advisor": "Ms. Evangelista",
                "members": 19,
                "category": "Arts"
            },
            "dance": {
                "name": "Dance Club",
                "description": "Socialize and have fun dancing to your own beat.",
                "meeting_time": "Every Tuesday 3:45-5:30 PM",
                "location": "Music Room",
                "advisor": "Mr. Nixon",
                "members": 18,
                "category": "Special Subjects"
            },
            "math": {
                "name": "Math Club",
                "description": "Develop quick solving skills.",
                "meeting_time": "Every Friday 3:30-5:00 PM",
                "location": "Room 507",
                "advisor": "Ms. Mondejar",
                "members": 12,
                "category": "Academic"
            },
            "art": {
                "name": "Art Club",
                "description": "Explore various art mediums and techniques.",
                "meeting_time": "Every Wednesday 3:45-5:15 PM",
                "location": "Art Room",
                "advisor": "Mr. Balajadia",
                "members": 2420,
                "category": "Arts"
            },
            "": {
                "name": "",
                "description": "",
                "meeting_time": "",
                "location": "",
                "advisor": "",
                "members": "",
                "category": ""
            }
        }
        
def show_club_info(e):
    document.getElementById('club-info').innerHTML = " "
    selected_club = document.getElementById("club-select").value
    info = club_info.get(selected_club, club_info[""])
            
    output = f"""
            {info['name']}
            Description:{info['description']}
            Meeting Time: {info['meeting_time']}
            Location: {info['location']}
            Advisor: {info['advisor']}
            Number of Members: {info['members']}
            Category: {info['category']}
            """
    display(output, target="club-info")