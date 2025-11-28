# Hello World Databricks App 👋

A simple Hello World application built with Streamlit for deployment on Databricks Apps.

## 📁 Project Structure

```
hello-world-cursor/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── app.yaml           # Databricks App configuration
└── README.md          # This file
```

## 🚀 Deploying to Databricks Apps

### Prerequisites
- Access to a Databricks workspace
- Databricks CLI installed (optional, for CLI deployment)

### Deployment Steps

#### Option 1: Deploy via Databricks UI

1. **Log into your Databricks workspace**

2. **Navigate to Apps**
   - Click on "Apps" in the left sidebar
   - Click "Create App" or "New App"

3. **Upload your application**
   - Upload or link your app files (`app.py`, `requirements.txt`, `app.yaml`)
   - Or connect to a Git repository containing these files

4. **Configure the app**
   - The `app.yaml` file will automatically configure the app to run Streamlit
   - Set any necessary environment variables if needed

5. **Deploy**
   - Click "Deploy" or "Start App"
   - Wait for the app to build and start
   - Access your app via the provided URL

#### Option 2: Deploy via Databricks CLI

```bash
# Install Databricks CLI
pip install databricks-cli

# Configure authentication
databricks configure --token

# Deploy the app
databricks apps deploy <app-name> --source-directory .
```

## 🧪 Running Locally

To test the app locally before deploying:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

The app will be available at `http://localhost:8501`

## 📝 Features

- Simple and clean Hello World interface
- Interactive user input
- Streamlit-based for easy development
- Ready to deploy on Databricks Apps

## 🛠️ Customization

You can customize the app by modifying `app.py`:
- Add more Streamlit components
- Connect to Databricks data sources
- Add data visualizations
- Integrate with MLflow models

## 📚 Resources

- [Databricks Apps Documentation](https://docs.databricks.com/en/dev-tools/databricks-apps/index.html)
- [Streamlit Documentation](https://docs.streamlit.io/)

## 📄 License

See LICENSE file for details.
