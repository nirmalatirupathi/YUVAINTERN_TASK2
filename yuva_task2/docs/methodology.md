# EDA Methodology

## 1. Dataset Intake
Load the approved dataset and record its source, observation period, row count, column count and access constraints.

## 2. Structural Profiling
Inspect `shape`, column names, data types, sample rows, unique values and candidate identifiers. Verify that the churn target has a clear definition.

## 3. Data Quality
Measure missingness, duplicate rows, impossible values, inconsistent categories and suspicious identifiers. Preserve a record of each data-quality decision.

## 4. Univariate Analysis
For numeric variables, inspect distributions, central tendency, spread, skewness and potential outliers. For categorical variables, inspect frequency and rare categories.

## 5. Bivariate Analysis
Compare important predictors with churn and examine relationships between pairs of predictors. Suitable visuals include boxplots, grouped bars and scatter plots.

## 6. Multivariate Analysis
Use correlation analysis, segmented views and selected interaction plots to identify combined patterns and redundancy among variables.

## 7. Missing Values
Distinguish structural missingness from accidental missingness. Candidate approaches include median imputation for suitable numeric variables and an explicit `Unknown` category for suitable categorical variables. Decisions must be made using business context.

## 8. Outliers
Use IQR rules, boxplots, robust statistics and domain thresholds. Do not remove an observation solely because it is statistically unusual. Possible treatments are retain, cap, transform, correct or exclude, with a documented reason.

## 9. Modeling Implications
Record potential predictors, leakage risks, transformations, class imbalance and variables requiring special treatment. Preprocessing used for modeling must be fit only on training data.

## 10. Reproducibility
Keep analysis code modular and rerunnable. Record package versions and analysis dates. Separate exploratory observations from confirmed business conclusions.
