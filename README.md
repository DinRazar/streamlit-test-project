# CIFAR-3 Image Classification API

## Описание проекта
Проект посвящён сравнению моделей классификации изображений на основе CIFAR-10 с использованием трёх классов:
- airplane
- ship
- truck

После сравнения моделей по метрикам accuracy, precision, recall и F1-score была выбрана лучшая модель и развёрнуто API на FastAPI, а также создан веб-интерфейс на Streamlit.

## Используемые классы
- 0 — airplane
- 1 — ship
- 2 — truck

## Файлы проекта
- `main.py` — API на FastAPI
- `streamlit_app.py` — веб-интерфейс на Streamlit
- `requirements.txt` — зависимости
- `best_classification_model.h5` — сохранённая модель

## Локальный запуск API
```bash
uvicorn main:app --reload
```

## Локальный запуск Streamlit
```bash
streamlit run streamlit_app.py
```

## API endpoint
POST `/predict`

## Пример ответа
```json
{
  "predicted_class": "ship",
  "confidence": 0.9821
}
```

## Ссылки
- GitHub: сюда вставишь позже
- API: сюда вставишь позже
- Streamlit: сюда вставишь позже