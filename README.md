# Vendor Management System

This is a Django-based Vendor Management System that allows users to manage products and vendors.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd Vendor-Management-System
    ```

2. Create a virtual environment:
    ```sh
    python -m venv envsmart
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        .\envsmart\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source envsmart/bin/activate
        ```

4. Install the dependencies:
    ```sh
    pip install -r requierment.txt
    ```

5. Apply migrations:
    ```sh
    python vendor_project/manage.py migrate
    ```

6. Run the development server:
    ```sh
    python vendor_project/manage.py runserver
    ```

## Project Structure

- [`vendor_project/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2FVendor-Management-System%2Fvendor_project%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\satya\OneDrive\Desktop\Vendor-Management-System\vendor_project\"): Contains the main Django project.
    - `manage.py`: Django's command-line utility for administrative tasks.
    - `db.sqlite3`: SQLite database file.
    - `templates/`: Contains HTML templates.
        - [`base.html`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2FVendor-Management-System%2Fvendor_project%2Ftemplates%2Fbase.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\satya\OneDrive\Desktop\Vendor-Management-System\vendor_project\templates\base.html"): Base template for the project.
        - [`add_product.html`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2FVendor-Management-System%2Fvendor_project%2Ftemplates%2Fadd_product.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\satya\OneDrive\Desktop\Vendor-Management-System\vendor_project\templates\add_product.html"): Template for adding a product.
        - [`edit_product.html`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2FVendor-Management-System%2Fvendor_project%2Fvendor_app%2Fviews.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A64%2C%22character%22%3A4%7D%5D "vendor_project/vendor_app/views.py"): Template for editing a product.
        - [`confirm_delete.html`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2FVendor-Management-System%2Fvendor_project%2Ftemplates%2Fconfirm_delete.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\satya\OneDrive\Desktop\Vendor-Management-System\vendor_project\templates\confirm_delete.html"): Template for confirming product deletion.
        - [`register.html`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2FVendor-Management-System%2Fvendor_project%2Ftemplates%2Fregister.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\satya\OneDrive\Desktop\Vendor-Management-System\vendor_project\templates\register.html"): Template for user registration.
        - [`login.html`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2FVendor-Management-System%2Fvendor_project%2Ftemplates%2Flogin.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\satya\OneDrive\Desktop\Vendor-Management-System\vendor_project\templates\login.html"): Template for user login.

    - `vendor_app/`: Contains the main application code.
        - [`models.py`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2FVendor-Management-System%2Fvendor_project%2Fvendor_app%2Fmodels.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A0%2C%22character%22%3A0%7D%5D "vendor_project/vendor_app/models.py"): Defines the database models.
        - `urls.py`: URL routing for the application.
        - [`views.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2FVendor-Management-System%2Fvendor_project%2Fvendor_app%2Fviews.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\satya\OneDrive\Desktop\Vendor-Management-System\vendor_project\vendor_app\views.py"): Contains the view functions.
        - `tests.py`: Contains the test cases.
    - [`vendor_project/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2FVendor-Management-System%2Fvendor_project%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\satya\OneDrive\Desktop\Vendor-Management-System\vendor_project\"): Contains project settings and URLs.
        - `settings.py`: Django settings for the project.
        - `urls.py`: URL routing for the project.

## Authentication

The application uses authentication to ensure that users cannot access certain functionalities without logging in. Users must register and log in to add, edit, or delete products. The following views are protected and require authentication:

- [`add_product`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2FVendor-Management-System%2Fvendor_project%2Fvendor_app%2Fviews.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A53%2C%22character%22%3A4%7D%5D "vendor_project/vendor_app/views.py")
- [`edit_product`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2FVendor-Management-System%2Fvendor_project%2Fvendor_app%2Fviews.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A64%2C%22character%22%3A4%7D%5D "vendor_project/vendor_app/views.py")
- [`delete_product`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2FVendor-Management-System%2Fvendor_project%2Fvendor_app%2Fviews.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A76%2C%22character%22%3A4%7D%5D "vendor_project/vendor_app/views.py")

These views are defined in [`vendor_app/views.py`](command:_github.copilot.openSymbolInFile?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fsatya%2FOneDrive%2FDesktop%2FVendor-Management-System%2Fvendor_project%2Fvendor_app%2Fviews.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22vendor_app%2Fviews.py%22%5D "c:\Users\satya\OneDrive\Desktop\Vendor-Management-System\vendor_project\vendor_app\views.py") and use the `@login_required` decorator to enforce authentication.