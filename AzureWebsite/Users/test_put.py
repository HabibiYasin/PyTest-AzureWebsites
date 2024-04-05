import requests

# Fungsi untuk mengirim permintaan PUT ke API
def update_user_info(user_id, new_data):
    url = f"https://fakerestapi.azurewebsites.net/api/v1/Users/{user_id}"
    headers = {
        "accept": "*/*",
        "Content-Type": "application/json; v=1.0"
    }
    response = requests.put(url, json=new_data, headers=headers)
    return response

# Tes untuk metode PUT API
def test_update_user_info():
    user_id = 1  # ID pengguna yang ingin diperbarui
    new_data = {
        "id": 1,
        "userName": "habibi99",
        "password": "valid123"
    }  # Data baru untuk pengguna

    response = update_user_info(user_id, new_data)

    # Periksa bahwa permintaan berhasil dengan status kode 200
    assert response.status_code == 200

    # Periksa bahwa informasi pengguna telah diperbarui dengan benar
    updated_user_info = response.json()
    assert updated_user_info["id"] == new_data["id"]
    assert updated_user_info["userName"] == new_data["userName"]
    assert updated_user_info["password"] == new_data["password"]
