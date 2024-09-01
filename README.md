# I-Translate

I-Translate is an innovative software solution developed to strengthen **Social Defence** in Singapore by overcoming communication barriers faced by the elderly and hearing-impaired communities. In a diverse, multi-racial, and multi-lingual society like Singapore, fostering understanding and connection among different communities is crucial for peace, progress, and resilience. I-Translate helps bridge language and communication gaps between elderly residents who speak various dialects and volunteers or caregivers who primarily speak English, as well as between hearing-impaired individuals and the broader community.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Acknowledgements](#acknowledgements)

## Introduction

In Singapore's multi-cultural society, **Social Defence** involves building trust, understanding, and harmony among people of different races, languages, and backgrounds. However, vulnerable groups, such as the elderly who only speak dialects like Hokkien, Cantonese, or Hakka, often face language barriers that limit their participation in community networks and access to essential services. Similarly, hearing-impaired individuals encounter challenges in daily communication, leading to social isolation.

**I-Translate** aims to address these challenges by providing a seamless communication tool that empowers volunteers, caregivers, and community members to interact more effectively with these groups. By breaking down language barriers and enabling smoother communication, I-Translate contributes to the larger goal of Social Defence—ensuring that all Singaporeans, regardless of language or physical ability, are included, understood, and supported, especially during times of crisis.

## Features

- **Speech-to-Text Translation**: Converts spoken dialects (Hokkien, Cantonese, Hakka) to English text.
- **Text-to-Speech Translation**: Converts English text input from volunteers to spoken dialects.
- **Sign Language Detection**: Recognizes hand motions and translates them to English text.
- **Sign Language Generation**: Converts English text input from volunteers to animated sign language.

## Directory

│   .DS_Store
│   .gitignore
│   README.md
│   requirements.txt
│   
├───.vscode
│       launch.json
│       
├───myenv
└───src
    │   .DS_Store
    │   main.py
    │   
    ├───cv
    │   │   app.py
    │   │   keypoint_classification.ipynb
    │   │   keypoint_classification_EN.ipynb
    │   │   point_history_classification.ipynb
    │   │   
    │   ├───.ipynb_checkpoints
    │   │       keypoint_classification-checkpoint.ipynb
    │   │       keypoint_classification_EN-checkpoint.ipynb
    │   │       
    │   ├───model
    │   │   │   __init__.py
    │   │   │   
    │   │   ├───keypoint_classifier
    │   │   │   │   keypoint.csv
    │   │   │   │   keypoint_classifier.hdf5
    │   │   │   │   keypoint_classifier.keras
    │   │   │   │   keypoint_classifier.py
    │   │   │   │   keypoint_classifier.tflite
    │   │   │   │   keypoint_classifier_label.csv
    │   │   │           
    │   │   ├───point_history_classifier
    │   │   │   │   point_history.csv
    │   │   │   │   point_history_classifier.hdf5
    │   │   │   │   point_history_classifier.py
    │   │   │   │   point_history_classifier.tflite
    │   │   │   │   point_history_classifier_label.csv
    │   │   │   
    │   │   └───__pycache__
    │   │           __init__.cpython-311.pyc
    │   │           
    │   └───utils
    │       │   cvfpscalc.py
    │       │   __init__.py
    │       │   
    │       └───__pycache__
    │               cvfpscalc.cpython-311.pyc
    │               __init__.cpython-311.pyc
    │               
    ├───webpage
    │   │   __init__.py
    │   │   
    │   ├───static
    │   │   │   .DS_Store
    │   │   │   styles.css
    │   │   │   
    │   │   └───image
    │   │           microphone.png
    │   │           tablet.png
    │   │           translate.png
    │   │           
    │   ├───templates
    │   │   │   base.html
    │   │   │   _navigation.html
    │   │   │   
    │   │   └───pages
    │   │           about.html
    │   │           home.html
    │   │           translate.html
        

            



## Installation

To run I-Translate locally, follow these steps:

1. TBC

## Usage 

TBC

## Acknowledgements

- The Lions Befrienders Service Association for their support and inspiration.
- Volunteers and community groups dedicated to bridging communication gaps in Singapore.
- YouthxHack 2024 and Dell for providing the platform and motivation to create solutions for social good.
- This project makes use of the pretrained model provided by [kinivi](https://github.com/kinivi) for hand gesture recognition, which is available on GitHub at [https://github.com/kinivi/hand-gesture-recognition-mediapipe](https://github.com/kinivi/hand-gesture-recognition-mediapipe).