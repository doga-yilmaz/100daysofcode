capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Turkey": "Istanbul",
    "England": "London"
}

travel_log = {
    "France": {"cities_visited": ["Paris", "Lile", "Dijon"], "total_visits" : 12 },
    "Canada": {"cities_lives": ["Ottowa","Vancouver", "Toronto"], "total_years": 17},
    "UK": {"pubs_drink": ["London", "Bristol", "Manchester", "Liverpool"], "total_pubs": 258}  
}

#Nesting Dictionary in a List

travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lile", "Dijon"], 
        "total_visits" : 12 
    },
    {
        "country": "Germany", 
        "cities_lives": ["Ottowa","Vancouver", "Toronto"], 
        "total_years": 17
    },
    {
        "country": "UK", 
        "pubs_drink": ["London", "Bristol", "Manchester", "Liverpool"], 
        "total_pubs": 258
    }
]

print(travel_log[1])
