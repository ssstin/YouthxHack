# i-Connect

i-Connect is an innovative software solution developed to strengthen **Social Defence** in Singapore by overcoming communication barriers faced by the elderly and hearing-impaired communities. In a diverse, multi-racial, and multi-lingual society like Singapore, fostering understanding and connection among different communities is crucial for peace, progress, and resilience. i-Connect helps bridge language and communication gaps between elderly residents who speak various dialects and volunteers or caregivers who primarily speak English, as well as between hearing-impaired individuals and the broader community.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Acknowledgements](#acknowledgements)

## Introduction

In Singapore's multi-cultural society, **Social Defence** involves building trust, understanding, and harmony among people of different races, languages, and backgrounds. However, vulnerable groups, such as the elderly who only speak dialects like Hokkien, Cantonese, or Hakka, often face language barriers that limit their participation in community networks and access to essential services. Similarly, hearing-impaired individuals encounter challenges in daily communication, leading to social isolation.

**i-Connect** aims to address these challenges by providing a seamless communication tool that empowers volunteers, caregivers, and community members to interact more effectively with these groups. By breaking down language barriers and enabling smoother communication, i-Connect contributes to the larger goal of Social Defence—ensuring that all Singaporeans, regardless of language or physical ability, are included, understood, and supported, especially during times of crisis.

## Features

- **Speech-to-Text Translation**: Converts spoken dialects (Hokkien, Cantonese, Hakka) to English text.
- **Text-to-Speech Translation**: Converts English text input from volunteers to spoken dialects.
- **Sign Language Detection**: Recognizes hand motions and translates them to English text.
- **Sign Language Generation**: Converts English text input from volunteers to animated sign language.

## Directory
<pre>
Directory
│   .gitignore
│   README.md
│   requirements.txt
│   
├───.vscode
│       launch.json
│       
├───myenv
└───src
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
</pre>
## Installation (MacOS)

To run i-Connect locally, follow these steps:

1. Clone the repository into a directory of your choice, and navigate to its root directory.
```ssh
git clone https://github.com/ssstin/YouthxHack.git <repo_name>
```
```ssh
cd <repo_name>
```

2. Open the root directory of the repository using VSCode.
```ssh
code .
```

3. Open a terminal in VSCode and create the virtual environment using Python.

```ssh
python3 -m venv myenv
```

4. Run the created environment.
```ssh
source myenv/bin/activate
```

5. Ensure that there are no dependencies in your environment by running this line. The output should be empty.
```ssh
pip freeze
```

6. Install the required dependencies for the application.
```ssh
pip install -r requirements.txt
```

7. Check that your environment now has only the dependencies specified in `requirements.txt`.
```ssh
pip freeze
```

## Usage 

1. Navigate to the `Run and Debug` tab in VSCode, select `Python Debugger (Flask)` and click the run button.

## Acknowledgements

- The Lions Befrienders Service Association for their support and inspiration.
- Volunteers and community groups dedicated to bridging communication gaps in Singapore.
- YouthxHack 2024 and Dell for providing the platform and motivation to create solutions for social good.
- This project makes use of the pretrained model provided by [kinivi](https://github.com/kinivi) for hand gesture recognition, which is available on GitHub at [https://github.com/kinivi/hand-gesture-recognition-mediapipe](https://github.com/kinivi/hand-gesture-recognition-mediapipe).
- This project makes use of a few language translation models, which are cited below:
    1. Cantonese to English: [CAiRE/wav2vec2-large-xlsr-53-cantonese](https://huggingface.co/CAiRE/wav2vec2-large-xlsr-53-cantonese)
    2. English to Cantonese [facebook/m2m100_418M](https://huggingface.co/facebook/m2m100_418M)
    3. Translation Model [Helsinki-NLP/opus-mt-zh-en](https://huggingface.co/Helsinki-NLP/opus-mt-zh-en)


## Citations
1. **ASCEND: A Spontaneous Chinese-English Dataset for Code-switching in Multi-turn Conversation**  
*Holy Lovenia, Samuel Cahyawijaya, Genta Indra Winata, Peng Xu, Xu Yan, Zihan Liu, Rita Frieske, Tiezheng Yu, Wenliang Dai, Elham J. Barezi, and others*  
Proceedings of the 13th Language Resources and Evaluation Conference (LREC), 2022.

2. **Beyond English-Centric Multilingual Machine Translation**  
*Angela Fan, Shruti Bhosale, Holger Schwenk, Zhiyi Ma, Ahmed El-Kishky, Siddharth Goyal, Mandeep Baines, Onur Celebi, Guillaume Wenzek, Vishrav Chaudhary, Naman Goyal, Tom Birch, Vitaliy Liptchinsky, Sergey Edunov, Edouard Grave, Michael Auli, Armand Joulin*  
*arXiv preprint* arXiv:2010.11125, 2020.

3. **OPUS-MT — Building open translation services for the World**  
*Jörg Tiedemann and Santhosh Thottingal*  
*Proceedings of the 22nd Annual Conference of the European Association for Machine Translation (EAMT)*, 2020, Lisbon, Portugal.
