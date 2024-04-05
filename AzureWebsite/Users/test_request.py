import requests

# Tes untuk mendapatkan informasi semua pengguna
def test_get_list_of_users():
    url = "https://fakerestapi.azurewebsites.net/api/v1/Users"
    headers = {"accept": "text/plain; v=1.0"}  # Define your headers here
    response = requests.get(url, headers=headers)
    assert response.status_code == 200


# Fungsi untuk mendapatkan informasi pengguna dari API
def get_user_info(user_id):
    url = f"https://fakerestapi.azurewebsites.net/api/v1/Users/{user_id}"
    headers = {"accept": "*/*"}  # Header opsional, tergantung kebutuhan
    response = requests.get(url, headers=headers)
    return response

# Tes untuk mendapatkan informasi pengguna pertama
def test_get_first_user():
    response = get_user_info(1)
    assert response.status_code == 200
    user_info = response.json()
    assert user_info["id"] == 1

# Tes untuk mendapatkan informasi pengguna terakhir
def test_get_last_user():
    response = get_user_info(10)
    assert response.status_code == 200
    user_info = response.json()
    assert user_info["id"] == 10

# Tes untuk mendapatkan informasi pengguna yang tidak ada
def test_get_nonexistent_user():
    response = get_user_info(11)
    assert response.status_code == 404