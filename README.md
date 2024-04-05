# Testing API with pytest

This project aims to test the web API at https://fakerestapi.azurewebsites.net/. The testing is done using pytest.

## Technologies Used
- Language: Python
- Code Editor: Visual Studio Code

## Test Result
![Test Result](https://github.com/HabibiYasin/PyTest-AzureWebsites/blob/main/hasil_test_pytest.jpg)

## How to Use
1. Clone the repository.
2. Open Visual Studio Code.
3. Make sure to have `requests` installed. If not, install it using pip:
    ```
    pip install requests
    ```
4. Open the terminal in Visual Studio Code and navigate to the project directory.
5. Run the following command to execute the tests:
    ```
    python -m pytest AzureWebsite/Users
    ```

This command will run the pytest tests for the API located in the `AzureWebsite/Users` directory.
