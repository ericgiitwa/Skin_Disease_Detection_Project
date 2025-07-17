# Skin_Disease_Detection_Project

# About the Dataset:
This dataset is a collection of images representing various skin diseases, categorized into 20  classes. It provides an invaluable resource for image classification tasks, particularly in the fields of dermatology and medical diagnostics.

### Skin Diseases:
Acne, Actinic Carcinoma, Atopic Dermatitis, Bullous Disease, Cellulitis, Eczema, Drug Eruptions, Herpes HPV, Light Diseases, Lupus, Melanoma, Poison IVY, Psoriasis, Benign Tumors, Systemic Disease, Ringworm, Urticarial Hives, Vascular Tumors, Vasculitis, Viral Infections.

## Why this project
Skin diseases affect millions globally, ranging from benign conditions like acne to life-threatening conditions like melanoma. Early and accurate diagnosis is critical but access to dermatologists is limited and expensive, especially in underserved regions like Kenya.  

Our project is an Innovative solution that will be implemented to improve healthcare access in rural areas. Telemedicine such as our project are being used to bring healthcare services directly to remote communities. These initiatives leverage technology to connect patients with healthcare professionals who can provide diagnosis, treatment, and advice remotely. 

Healthcare systems in Kenya vary greatly across the counties, with some counties having well-developed systems while others struggle to provide even basic healthcare services.  

### Challenges facing healthcare in Kenya: 

* Lack of funding. 
* Shortage of healthcare professionals. 
* Limited access to medical supplies and equipment.  
* Poverty
  
#### Providing healthcare in rural areas of Kenya presents unique challenges: 
Many rural communities are located far from medical facilities, making it difficult for residents to access healthcare services.

Poor infrastructure, including lack of roads and transportation options, further exacerbates this issue. 

## Objectives:
* Is it possible to upload images to our deployed model to identify the skin disease?
* Improve diagnostic efficiency by automating skin condition  diagnosis and cutting down on delays.
* Expand access by enabling mobile diagnosis tools for rural areas.
* Reduce costs to minimize unnecessary trips to doctors and biopsies.
* Enhance patient outcomes by  supporting early detection of serious conditions like skin cancer.

## Stakeholders
* Patients in rural areas
* Local clinics and hospitals
* Health workers
* Ministry of Health
* NGOs and health orgs

#### SOURCES: 
https://www.africansahara.org/african-healthcare-systems-and-challenges/ 

https://pmc.ncbi.nlm.nih.gov/articles/PMC10149786/#s3 

https://aho.afro.who.int/ind/af?dim=133&dom=Funding%20of%20health

https://www.macrotrends.net/global-metrics/countries/ken/kenya/healthcare-spending

# MODELING
##  Skin Disease Classification with CNN

In this project we developed and evaluated a Convolutional Neural Network (CNN) for multi-class skin disease classification. The modeling process involved building a baseline model and then applying several fine-tuning techniques to improve performance

### 🔹 Base Model Summary

The base model was a simple CNN architecture with three convolutional layers each followed by max pooling, a dropout layer for regularization and a dense layer for final classification. It was designed to learn hierarchical patterns in skin lesion images and predict one of 19 disease classes

- **Convolutional Layers**: Extracted features from images at increasing complexity levels
- **MaxPooling Layers**: Reduced spatial dimensions and helped with overfitting
- **Dropout Layer**: Prevented overfitting by randomly disabling neurons
- **Dense Layers**: Learned higher-level representations for decision-making
- **Softmax Output**: Used for multi-class probability distribution

###  Model Compilation and Training

The model was compiled using:
- **Categorical Crossentropy** as the loss function (suitable for multi-class problems)
- **Adam optimizer** with a small learning rate
- **Accuracy** as the evaluation metric

To address data imbalance, class weights were applied. Early stopping was used to halt training when validation performance stopped improving

### Fine-Tuning Strategy

To enhance performance, the following adjustments were made in the tuned model:
- Increased the number of neurons in the dense layer
- Applied dropout regularization to reduce overfitting
- Used `ReduceLROnPlateau` to lower the learning rate when validation loss plateaued
- Maintained class weighting and early stopping to stabilize training

### Observations

- The base model achieved low training (~11%) and validation (~6%) accuracy, indicating underfitting
- Even after tuning the accuracy improvement was marginal
- Confusion matrix and classification reports showed poor class-level performance often predicting dominant classes only

### Conclusion

Despite implementing regularization and learning rate adjustments, both the base and tuned models struggled to generalize well. The limited performance may be due to high class imbalance, data complexity or insufficient training data. Future improvements could involve using more advanced architectures (Like transfer learning) or enriching the dataset with better quality and quantity of images

