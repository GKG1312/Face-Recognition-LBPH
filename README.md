# Face Recognition Based Attendance System

A modern, robust, and efficient automated attendance management system leveraging Local Binary Patterns Histograms (LBPH) for facial recognition. Built with Python, OpenCV, and Tkinter, this system provides a seamless experience for student registration and real-time attendance tracking.

## 🌟 Features

-   **Seamless Registration**: Capture and process facial images to create student profiles.
-   **LBPH Recognition**: High-performance face identification using the LBPH algorithm.
-   **Real-Time Tracking**: Instantaneous face detection and recognition from live webcam feeds.
-   **Automated Logging**: Attendance is automatically recorded in time-stamped CSV files.
-   **Secure Management**: Password-protected administrative actions (Saving Profiles, Changing Passwords).
-   **Rich UI**: A clean, responsive dashboard with a live clock and registration counters.

## 🛠️ Tech Stack

-   **Language**: Python 3.x
-   **Computer Vision**: OpenCV (`opencv-contrib-python`)
-   **GUI Framework**: Tkinter / ttk
-   **Data Processing**: Pandas, NumPy
-   **Image Processing**: Pillow (PIL)

## 📁 Project Structure

```text
face-recognition-LBPH/
├── main.py                 # Application entry point
├── src/                    # Source code directory
│   ├── auth.py             # Authentication & password management
│   ├── logic.py            # Face detection, training, & tracking logic
│   ├── ui.py               # Tkinter GUI implementation
│   ├── utils.py            # Path & file validation utilities
│   └── __init__.py         # Package initialization
├── Attendance/             # Generated daily attendance logs (CSV)
├── StudentDetails/         # Master student database (CSV)
├── TrainingImage/          # Raw images captured during registration
├── TrainingImageLabel/     # Trained LBPH model (YAML)
└── haarcascade_frontalface_default.xml # Haar Cascade for face detection
```

## 🚀 Getting Started

### Prerequisites

-   Python 3.13+ installed.
-   A working webcam.

### Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd face-recognition-LBPH
    ```

2.  **Set up Virtual Environment** (Optional but recommended):
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Windows: .venv\Scripts\activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install opencv-contrib-python pandas pillow numpy
    ```

4.  **Haarcascade File**: Ensure `haarcascade_frontalface_default.xml` is present in the root directory.

### Running the Application

```bash
python main.py
```

## 📖 Usage

### 1. New Registration
1.  Enter the **Roll Number** and **Name** of the student.
2.  Click **Take Images**. The system will capture 50 samples from the webcam.
3.  Click **Save Profile**. Enter the administrative password (default prompt if first time) to train the model.

### 2. Taking Attendance
1.  Click **Take Attendance**.
2.  The webcam feed will open. Once a face is recognized, a rectangular box with the student's name will appear.
3.  Press **'q'** to stop the process.
4.  The attendance table on the dashboard will refresh automatically with the updated records.

## 🔒 Security
-   The default password for "Save Profile" is requested during the first use if not already set.
-   Passwords can be modified via the **Help -> Change Password** menu.

---
*Developed as a Minor Project at Government Engineering College, Jagdalpur.*
