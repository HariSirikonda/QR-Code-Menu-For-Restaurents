# QR Code Menu Generator

QR Code Menu Generator is a web application designed to help restaurant owners create QR codes for their menu cards. By providing the restaurant name and a Google Drive link to a PDF of the menu, the application generates a downloadable QR code image. This QR code can be printed and placed on tables, enabling customers to easily scan and access the restaurant menu.

---

## Features

### 1. **Simple User Interface**
- A clean and intuitive design to ensure a seamless user experience.
- Users only need to input their restaurant name and menu URL.

### 2. **QR Code Generation**
- Automatically converts the provided URL into a QR code.
- Displays the QR code on the screen immediately after generation.

### 3. **Downloadable QR Code**
- Users can easily download the QR code image.
- The downloaded QR code image is ready for printing and use.

### 4. **Practical for Restaurants**
- Reduces the need for physical menus, making operations more hygienic and cost-effective.
- QR codes can be printed and placed on tables, improving the customer experience.

---

## How It Works

1. **Input Restaurant Details**:
   - Enter the restaurant name.
   - Provide a Google Drive link to the PDF menu.

2. **Generate QR Code**:
   - Click the **Generate QR Code** button.
   - The application generates a unique QR code for the provided URL.

3. **Download and Use**:
   - Download the generated QR code image.
   - Print and place it on tables for customers to scan and access the menu.

---

## Advantages

### For Restaurants:
- **Cost Efficiency**: Eliminates the need for frequent reprints of physical menus.
- **Hygiene**: Enhances hygiene by reducing the need for shared physical menus.
- **Convenience**: Allows customers to access menus directly on their smartphones.

### For Customers:
- **Ease of Access**: No need to wait for a physical menu.
- **Modern Experience**: Offers a tech-savvy and professional impression.

### For the Environment:
- **Eco-Friendly**: Reduces paper usage, contributing to sustainable practices.

---

## Application Workflow

1. Launch the web application.
2. Fill in the required details (restaurant name and menu URL).
3. Generate the QR code.
4. Download the QR code and print it.
5. Place the QR code at tables in the restaurant for customer use.

---

## Technologies Used

- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Django (Python)
- **QR Code Generation**: Python's `qrcode` library

---

## How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/HariSirikonda/QR-Code-Menu-For-Restaurents.git
   ```

2. Navigate to the project directory:
   ```bash
   cd qr-code-menu-generator
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the server:
   ```bash
   python manage.py runserver
   ```

5. Open your browser and go to:
   ```
   http://127.0.0.1:8000/
   ```

---

## Future Enhancements

- **Custom QR Code Styles**: Add options to customize QR code colors and designs.
- **Database Integration**: Store restaurant information for future edits and retrieval.
- **Analytics**: Provide statistics on QR code scans and customer activity.

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute the application as needed.

---

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request with your improvements or suggestions.

---

## Contact

For queries or feedback, please contact:
- **Email**: [harisirikonda22@gmail.com]
- **GitHub**: [https://github.com/HariSirikonda]

---

Thank you for using the QR Code Menu Generator! Happy coding! 🎉
