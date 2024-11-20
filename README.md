# Contact Manager Application

The **Contact Manager Application** is a user-friendly Python and Tkinter-based software designed to manage client details and streamline the billing process. It allows saving client information, generating UPI QR codes for payments, and viewing additional support and policy details.

## Features

1. **Main Page**:
   - Displays the application logo on the left.
   - Three interactive buttons:
     - **Contact & Billing**: Opens a page to manage client details and billing.
     - **About**: Provides customer support, team guidelines, and privacy policy information.
     - **Exit**: Closes the application.

2. **Contact & Billing Page**:
   - Input fields for:
     - Full Name
     - Phone Number
     - Email Address
     - Billing Price
   - **Save Information**: Saves client data locally in a folder named `User Information`.
   - **QR Code Generation**: Creates a UPI payment QR code for easy transactions.
   - **Navigate Back**: Returns to the main page.

3. **About Page**:
   - **Customer Support**: Displays contact details for assistance.
   - **Team Guidelines**: Includes instructions for effective use and collaboration.
   - **Privacy Policy**: Ensures data security and user privacy.
   - **Navigate Back**: Returns to the main page.

## Installation & Usage

1. **Prerequisites**:
   - Python 3.x installed on your system.
   - Required modules: `tkinter`, `qrcode`, `os`.
   - Install the `qrcode` module using:
     ```bash
     pip install qrcode
     ```

2. **Steps**:
   - Clone or download the repository.
   - Place your logo image in the root directory and name it `logo.png`.
   - Run the application:
     ```bash
     python contact_manager.py
     ```

3. **How to Use**:
   - Open the application and use the Main Page to navigate.
   - Save client information and automatically store it in the `User Information` folder.
   - Generate UPI QR codes for billing and share with clients.

## Directory Structure

```plaintext
ContactManager/
├── contact_manager.py   # Main application file
├── logo.png             # Application logo
├── User Information/    # Directory for saved client data
├── payment_qr.png       # Temporary generated QR code
```
## Customization

- **Logo**: Replace `logo.png` with your own logo image.
- **Payment UPI**: Update the UPI ID in the `save_user_data` method to your own.
- **Theme**: Adjust background colors, button styles, and font styles in the application's UI design.

## Future Enhancements

- Add database integration for better data management.
- Implement advanced price calculations, including discounts and taxes.
- Add user authentication for secure access to the application.
- Provide export options for saved data (e.g., CSV or PDF files).

## License

This project is licensed under the MIT License. Feel free to modify and distribute it according to your requirements.
