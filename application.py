import streamlit as st
import pandas as pd
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline
import os
from Prediction.batch import BatchPrediction
from src.logger import logging
from src.components.data_transformation import DataTransformationConfig
from src.config.configuration import *
from src.pipeline.training_pipeline import Train
from werkzeug.utils import secure_filename
import base64

feature_engineering_file_path = FEATURE_ENG_OBJ_PATH
transformer_file_path = PREPROCESSING_OBJ_PATH
model_file_path = MODEL_FILE_PATH

UPLOAD_FOLDER = 'batch_prediction/Uploaded_CSV_FILE'
#predicted_file_path = 'batch_prediction/Predicted_CSV_FILE/predicted_results.csv'


# Set the title of the Streamlit app
st.title("Store Sales Prediction App")

ALLOWED_EXTENSIONS = {'csv'}

# Streamlit sidebar
st.sidebar.header("Navigation")
selected_page = st.sidebar.radio("Select a Page", ["Home", "Predict", "Batch Prediction", "Train"])

if selected_page == "Home":
    st.header("Home Page")
    st.write("Welcome to the Store Sales Prediction App!")
    st.write("Use the sidebar to navigate to different pages.")

elif selected_page == "Predict":
    st.header("Single Data Point Prediction")
    
    # Create input form
    st.subheader("Enter Data for Prediction")
    item_fat_content = st.selectbox("Item Fat Content", ["Low Fat", "Regular"])
    item_visibility = st.number_input("Item Visibility", min_value=0.0, format="%.2f")
    item_type = st.selectbox("Item Type",['Fruits and Vegetables','Snack Foods','Household','Frozen Foods','Dairy','Canned','Baking Goods'
                                           'Health and Hygiene','Soft Drinks','Meat','Breads','Hard Drinks','Others','Starchy Foods',
                                           'Breakfast','Seafood'])
    item_mrp = st.number_input("Item MRP", min_value=0.0, format="%.2f")
    outlet_identifier = st.selectbox("Outlet Identifier",['OUT010','OUT013','OUT017','OUT018','OUT019','OUT027','OUT035','OUT045','OUT046','OUT049'])
    outlet_establishment_year = st.number_input("Outlet Establishment Year", min_value=0, format="%d")
    outlet_location_type = st.selectbox("Outlet Location Type", ["Tier 1", "Tier 2", "Tier 3"])
    outlet_type = st.selectbox("Outlet Type", ["Grocery Store", "Supermarket Type1", "Supermarket Type2", "Supermarket Type3"])
    
    # Make a prediction
    if st.button("Predict"):
        data = CustomData(
            Item_Fat_Content=item_fat_content,
            Item_Visibility=item_visibility,
            Item_Type=item_type,
            Item_MRP=item_mrp,
            Outlet_Identifier=outlet_identifier,
            Outlet_Establishment_Year=outlet_establishment_year,
            Outlet_Location_Type=outlet_location_type,
            Outlet_Type=outlet_type
        )
        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_new_data)
        result = int(pred[0])
        st.success(f"Predicted Store Sales is: {result}")

elif selected_page == "Batch Prediction":
    st.header("Batch Prediction")

    # Create a file uploader
    st.subheader("Upload a CSV File")
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file is not None:
        # Save the uploaded file
        file_path = os.path.join(UPLOAD_FOLDER, secure_filename(uploaded_file.name))
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())
        
        logging.info("CSV received and Uploaded")

        # Perform batch prediction using the uploaded file
        batch = BatchPrediction(file_path, model_file_path, transformer_file_path, feature_engineering_file_path)
        batch.start_batch_prediction()

        # # Define the function to create a download link
        # def get_binary_file_downloader_html(file_path):
        #     with open(file_path, 'rb') as file:
        #         contents = file.read()
        #     encoded_file = base64.b64encode(contents).decode()
        #     return f'<a href="data:file/csv;base64,{encoded_file}" download="predicted_results.csv">Download Predicted File</a>'


        # # Define a variable to store the path to the predicted file after batch prediction
        # predicted_file_path = 'batch_prediction/Prediction_CSV/prediction.csv'


        # After batch prediction and displaying the success message, add a download button for the predicted file
        output = "Batch Prediction Done"
        st.success(output)

        # # Add a download button for the predicted file
        # if st.button("Download Predicted File"):
        #     st.markdown(get_binary_file_downloader_html(predicted_file_path), unsafe_allow_html=True)

# ... The rest of your code ...
elif selected_page == "Train":
    st.header("Model Training")

    if st.button("Train Model"):
        try:
            pipeline = Train()
            pipeline.main()
            st.success("Training complete")
        except Exception as e:
            logging.error(f"{e}")
            st.error(f"Error during training: {str(e)}")

# Run the Streamlit app
if __name__ == '__main__':
    st.sidebar.title("My Streamlit App")
    st.title("Main Content")