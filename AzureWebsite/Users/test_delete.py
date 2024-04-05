import requests

# Fungsi untuk mengirim permintaan DELETE ke API
def delete_user(user_id):
    url = f"https://fakerestapi.azurewebsites.net/api/v1/Users/{user_id}"
    headers = {
        "accept": "*/*"
    }
    response = requests.delete(url, headers=headers)
    return response

# Tes untuk metode DELETE API
def test_delete_user():
    user_id = 1  # ID pengguna yang ingin dihapus

    response = delete_user(user_id)

    # Periksa bahwa permintaan berhasil dengan status kode 200
    assert response.status_code == 200

    # Periksa bahwa pengguna telah dihapus dari sistem
    # Untuk sumber daya yang telah dihapus, respons biasanya kosong
    assert response.text == ""
