import requests

# Base URL
base_url = "http://localhost:8000/profiles/"

# GET isteği örneği
def get_profile(profile_id):
    response = requests.get(base_url + str(profile_id))
    print(response.json())

# PUT isteği örneği
def update_profile(profile_id, data):
    response = requests.put(base_url + str(profile_id) , json=data)
    print(response.json())

# DELETE isteği örneği
def delete_profile(profile_id):
    response = requests.delete(base_url + str(profile_id))
    print(response.status_code)

# Profil oluşturmak için veri
new_profile_data = {
    "first_name": "Turahan",
    "last_name": "Korna",
    "nickname": "tKorna",
    "email": "TurahanKorna@gmail.com"
}

# Profil ID'si
profile_id = 4

# # GET isteği örneği
# get_profile(profile_id)

# PUT isteği örneği
update_profile(profile_id, new_profile_data)

# # DELETE isteği örneği
# delete_profile(profile_id)
