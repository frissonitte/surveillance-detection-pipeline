# Real-Time Surveillance Object Detection Pipeline

This project is a high-performance computer vision pipeline framework designed to perform real-time object detection by processing video streams from security cameras.
[ShanghaiTech Campus dataset](https://svip-lab.github.io/dataset/campus_dataset.html) used in this initial version.

## Key Features

- **NVIDIA CUDA Optimization:** Millisecond-level inference times achieved through GPU-based parallel processing.
- **Lean Architecture:** A modular structure designed for future integration with anomaly detection, zone intrusion monitoring, and alarm systems.
- **Edge-Computing Ready:** Targets high FPS even on low-resource hardware by utilizing the lightweight YOLOv8 architecture.

## Tech Stack

- **Language:** Python
- **Framework:** PyTorch & Ultralytics (YOLOv8)
- **Image Processing:** OpenCV
- **Hardware Acceleration:** NVIDIA CUDA

## Roadmap

- [x] Phase 1: CUDA Integration and Static Image/Video Testing
- [ ] Phase 2: Live Camera Stream (RTSP) Protocol Integration
- [ ] Phase 3: Implementation of Zone Intrusion Detection Logic
- [ ] Phase 4: Logging and Notification/Alarm Service
