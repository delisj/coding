import requests
def get_chucknorris_joke (category =""):
    if category == "celebrity":
        url = "https://api.chucknorris.io/jokes/random?category=celebrity"
    else: 
        url = "https://api.chucknorris.io/jokes/random"



    r = requests.get(url)
    data = r.json()
    return(data['value'])
print ("Celebrity: " + get_chucknorris_joke("celebrity"))
print ("Random: " + get_chucknorris_joke())
