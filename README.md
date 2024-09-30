## Setting the Context
This project was under a collaborative effort of [Aneesh](https://github.com/lhcee3) and [Hemanth](https://github.com/hemanth-yasaswi) for the Hackathon Hosted at Lords Insitutute of Technology, Hyderabad on the 8th and 9th of June, 2024.

![IMG-20240610-WA0004](https://github.com/user-attachments/assets/65a92902-3634-4fa8-b04b-7a3e03e8743d)

# Weapon Detection Streamlit App

This project demonstrates a real-time weapon detection application using Streamlit and OpenCV. Users can log in with a username and password (plain text for demonstration, not recommended for production) to access the live video stream with weapon detection functionality.

**Features:**

- Login functionality (username and password)
- Real-time weapon detection from a webcam stream (using a pre-trained classifier)
- Live video display with bounding boxes around detected weapons

**Prerequisites:**

- Python 3.12.3
- Streamlit library (`pip install streamlit`)
- OpenCV library (`pip install opencv-python`)
- imutils library (`pip install imutils`)
- numpy library (`pip install numpy`)

**Instructions:**

1. **Clone or Download the Repository:**
   - Clone the repository to your local machine using Git (recommended):
     ```bash
     git clone https://github.com/lhcee3/Weapon-Detection-Opencv.git
     ```
   

2. **Set Up the Environment:**
   - Create a virtual environment to isolate project dependencies (recommended):
     ```bash
     python -m venv venv  
     source venv/bin/activate  # Activate the virtual environment (Linux/macOS)
     venv\Scripts\activate.bat  # Activate on Windows
     ```
   - Install the required libraries:
     ```bash
     pip install streamlit opencv-python imutils numpy
     ```

3. **Replace Classifier File Path (Optional):**
   - The code assumes a weapon classifier file named `cascade.xml`. If you have a pre-trained classifier, replace the path in the code:
     ```python
     gun_cascade = cv2.CascadeClassifier('path/to/your/cascade.xml')  # Update the path
     ```
   - Be cautious when downloading pre-trained classifiers, as their accuracy and limitations vary. Consider evaluating them for your specific use case.

4. **Run the Application:**
   - Open a terminal or command prompt and navigate to your project directory.
   - Activate your virtual environment if you created one (see step 2).
   - Run the application using:
     ```bash
     streamlit run check.py  
     ```
   - Access the application in your web browser at http://localhost:8501.

**Disclaimer:**

- This project is for demonstration purposes only.
- Pre-trained weapon classifiers might have limitations and inaccuracies. Evaluate their performance on your specific use case before relying on them for critical applications.
- Using plain text passwords in the code is highly discouraged for real-world deployments. Implement secure password hashing and storage if required.

**Further Considerations:**

- For production deployment, consider using a cloud platform like Heroku or Google Cloud Run. These platforms offer streamlined deployment processes and web hosting capabilities.
- Secure your deployed application by implementing user authentication and authorization mechanisms.
- Regularly update your dependencies to address security vulnerabilities and ensure compatibility with the latest Streamlit and OpenCV versions.
