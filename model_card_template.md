# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This is a Random Forest Classifier trained to predict whether an individual’s annual income exceeds $50K using the U.S. Census dataset (census.csv). The model uses both categorical and continuous features, with categorical features one-hot encoded.

Categorical features used:

workclass

education

marital-status

occupation

relationship

race

sex

native-country

Continuous features include age, hours-per-week, and other numeric columns.

## Intended Use
This model is intended for educational purposes, specifically for demonstrating a machine learning pipeline, model training, inference, and evaluation on structured tabular data.

It is not intended for real-world financial or employment decision-making, as the dataset is simplified and the model has known limitations in performance and fairness.

## Training Data
The model was trained on the Census Income Dataset, split into 80% training and 20% testing data. The training data contains a mixture of categorical and numeric features representing demographics, employment, and work-related information.

## Evaluation Data
The test set consists of the 20% holdout portion of the Census dataset, which was not seen during training. Model performance was evaluated using overall metrics and metrics computed on slices of categorical features.

## Metrics
The following metrics were used:

Precision: Measures the proportion of predicted positives that are truly positive.

Recall: Measures the proportion of actual positives that were correctly predicted.

F1 Score: Harmonic mean of precision and recall, balancing the two.

Overall metrics on the test set:

Precision: 0.7419

Recall: 0.6384

F1: 0.6863

Performance on selected categorical slices (examples from slice_output.txt):

Workclass slices:

Private (4,578 samples): Precision 0.7376 | Recall 0.6404 | F1 0.6856

Federal-gov (191 samples): Precision 0.7971 | Recall 0.7857 | F1 0.7914

Self-emp-not-inc (498 samples): Precision 0.7064 | Recall 0.4904 | F1 0.5789

Education slices:

Bachelors (1,053 samples): Precision 0.7523 | Recall 0.7289 | F1 0.7404

Masters (369 samples): Precision 0.8271 | Recall 0.8551 | F1 0.8409

HS-grad (2,085 samples): Precision 0.6594 | Recall 0.4377 | F1 0.5261

Native-country slices:

United-States (5,870 samples): Precision 0.7392 | Recall 0.6321 | F1 0.6814

India (21 samples): Precision 0.8750 | Recall 0.8750 | F1 0.8750

Germany (32 samples): Precision 0.8462 | Recall 0.8462 | F1 0.8462

## Ethical Considerations
The dataset contains sensitive demographic information, including race, sex, and nationality.

Model predictions may reflect biases present in the data.

Special caution should be taken to avoid unfair treatment of underrepresented groups or minority categories.

This model is not intended for high-stakes decisions in employment, finance, or social services.

## Caveats and Recommendations
The model shows varying performance across slices; some rare categories (e.g., education: 1st-4th) have very few samples, which may lead to unstable predictions.

Accuracy, precision, and recall may differ on real-world populations.

Future improvements could include additional data preprocessing, hyperparameter tuning, and bias mitigation techniques.

Use this model primarily for educational purposes and controlled experimentation.