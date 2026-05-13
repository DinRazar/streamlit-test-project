import streamlit as st
import requests

st.set_page_config(page_title="CIFAR-3 Classifier", layout="centered")

st.title("Классификация изображений")
st.write("Загрузи изображение самолёта, корабля или грузовика.")

uploaded_file = st.file_uploader("Выбери изображение", type=["jpg", "jpeg", "png"])

api_url = "https://streamlit-test-project.onrender.com/predict"

if uploaded_file is not None:
    st.image(uploaded_file, caption="Загруженное изображение", use_container_width=True)

    if st.button("Предсказать"):
        files = {
            "file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)
        }

        response = requests.post(api_url, files=files)

        if response.status_code == 200:
            result = response.json()
            st.success(f"Предсказанный класс: {result['predicted_class']}")
            st.info(f"Уверенность модели: {result['confidence']:.4f}")
        else:
            st.error("Ошибка при обращении к API")