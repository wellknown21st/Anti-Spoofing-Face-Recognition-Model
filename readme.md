Project Overview
This repository contains scripts for:

Face detection using YOLO and CVzone modules

Face liveness/fakeness detection (binary classification: “real” or “fake”)

Face recognition to identify known users with attendance marking

Dataset collection and data splitting for training/validation/testing

Model training using Ultralytics YOLO

Directory Structure
dataCollection.py: Collects labeled face data and saves images/labels with liveness classification

splitData.py: Splits the collected data into train/val/test sets and generates a YAML config

train.py: Trains a YOLO model using the formatted split data

main.py: Runs live detection (YOLO-based) for "real" vs "fake" faces

main2.py: Runs live detection and also performs face recognition-based attendance marking

faceDetectorTest.py: Tests face detection using CVzone

yoloTest.py: Tests YOLO detection model

tempCodeRunnerFile.py, textFileTest.py: Temporary/debug scripts

Getting Started
1. Clone the Repository
bash
git clone <your-repo-url>
cd <repo-directory>
2. Environment Setup
It is recommended to use Python 3.8 or higher.

bash
python -m venv venv
source venv/bin/activate         # Linux/macOS
venv\Scripts\activate            # Windows
3. Install Dependencies
bash
pip install -r requirements.txt
4. Prepare Dataset
Use dataCollection.py to collect and classify face images.

Split you dataset using splitData.py.

Train your YOLO model with train.py.

5. Model Inference & Attendance
Run main.py for real/fake detection.

Run main2.py for recognition and attendance marking.

Customize the YAML and model paths in your scripts as needed.

Notes
Ensure your webcam or video source is configured correctly.

Change model paths appropriately for your environment.

For CUDA support, install corresponding PyTorch and CUDA versions.

The scripts expect data formats compatible with YOLO and face_recognition.

requirements.txt
text
