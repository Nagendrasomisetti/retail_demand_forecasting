
# 🛒 Retail Demand Forecasting

This project predicts **Weekly Sales** for a retail store using a machine learning model trained on historical sales data.

## Features

- Trains a Linear Regression model using historical sales data.
- Simple Streamlit web app for making predictions.
- Input fields for Store, Dept, Date, and IsHoliday (all label-encoded).

## Project Structure

```
.
├── app.py              # Streamlit web app for predictions
├── train_model.py      # Script to train and save the model
├── model.pkl           # Saved trained model
├── requirements.txt    # Python dependencies
└── render.yaml         # (Optional) Deployment config
```

## Getting Started

## 1. Clone the repository

```sh
git clone https://github.com/<your-username>/<your-repo>.git
cd retail_demand_forecasting
```

### 2. Install dependencies

```sh
pip install -r requirements.txt
```

### 3. Train the model

Make sure your dataset (`sales data-set.csv`) is in the correct path as specified in `train_model.py`.

```sh
python train_model.py
```

### 4. Run the Streamlit app

```sh
streamlit run app.py
```

Open the provided URL in your browser to use the app.
## Usage

- Enter the **Store**, **Dept**, **Date**, and **IsHoliday** values as integer labels.
- Click **Predict Sales** to see the predicted weekly sales.

## Notes

- The model expects label-encoded values for all inputs.
- You can modify `train_model.py` to use different features or models as needed.

## License

This project is for educational purposes.
