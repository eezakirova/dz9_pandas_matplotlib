import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Этап 1. Чтение данных из JSON-файла
with open("events.json", encoding="utf-8") as f:
    events_json = json.load(f)

# Преобразование списка событий в DataFrame
events_df = pd.DataFrame(events_json["events"])

# Этап 2. Анализ данных
# Выделяем тип события (первое слово в поле signature)
events_df["event_type"] = events_df["signature"].str.split().str[0]

# Подсчет количества событий каждого типа
type_stats = events_df.groupby("event_type").size().sort_values(ascending=False)

print("Статистика по типам событий информационной безопасности:")
print(type_stats)

# Этап 3. Визуализация результатов
plt.figure(figsize=(10, 6))
sns.countplot(
    data=events_df,
    x="event_type",
    hue="event_type",
    dodge=False,
    palette="Set2",
    legend=False
)

plt.title("Распределение событий информационной безопасности по типам")
plt.xlabel("Тип события")
plt.ylabel("Количество событий")
plt.tight_layout()
plt.show()
