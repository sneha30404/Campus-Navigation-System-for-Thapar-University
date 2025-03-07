# Campus-Navigation-System-for-Thapar-University

The **Campus Navigation System** is designed to make campus navigation in Thapar Institute of Engineering and Technology effortless. Whether you're a new student, visitor, or faculty member, this application ensures you can find your way around the campus with ease. 

---

## Features
- **Indoor and Outdoor Navigation**: Navigate confidently within buildings and across campus grounds.
- **Search Functionality**: Quickly locate buildings, rooms, or landmarks.
- **User-Friendly Interface**: A sleek and intuitive design ensures smooth interaction.

**Technology Stack**:
- **Backend**: Python (Flask)
- **Database**: MySQL
- **Frontend**: HTML, CSS, JavaScript

---

## Prerequisites
Before you begin, make sure you have the following installed on your system:
- Python 3.8 or later
- MySQL server
- pip (Python package installer)

---

## Installation and Setup
Follow these simple steps to get started:

### Clone the Repository
Run the following commands in your terminal:
```bash
git clone <https://github.com/sneha30404/Campus-Navigation-System-for-Thapar-University>
cd <Campus-Navigation-System-for-Thapar-University>
```

### Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### Setup the Database
- Create a new MySQL database for the project.
- In map.html file, add your API key here:
  <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_SECRETKEY_HERE&libraries=places"></script>
- Import the provided SQL file to set up the required tables:
  ```bash
  mysql -u <username> -p <database_name> < database_setup.sql
  ```
- Update the database connection details in `config.py`.

### Run the Application
Start the Flask server:
```bash
python app.py
```

### Access the Application
Open your browser and navigate to:
```bash
http://127.0.0.1:5000
```

---

## Usage
We have not yet integrated the outdoor and indoor navigation system, as it is in pilot phase. Please Refer to this link for outdoor system.
Link:
- Use the **Search** feature to find locations quickly.
- Explore the **Map** to navigate across campus easily.
- Enjoy a seamless navigation experience tailored to your needs!

---

## Contributing
We welcome contributions to enhance the Campus Navigation System! Here's how you can contribute:
1. **Fork the repository**.
2. **Create a new branch** for your feature or bug fix.
3. **Commit your changes** and submit a pull request.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact
For any questions or support, feel free to reach out:
- **Name**: Sneha
- **Email**: sneha30404@gmail.com

Thank you for using the Campus Navigation System! 🚶‍♂️

