def find_common_participants(group1, group2, separator=','):
    # Разделяем строки на участники с помощью указанного разделителя
    participants1 = set(group1.split(separator))
    participants2 = set(group2.split(separator))

    # Находим общих участников
    common_participants = participants1.intersection(participants2)

    # Возвращаем отсортированный список общих участников
    return sorted(common_participants)


# Пример использования
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Находим общих участников
common_participants = find_common_participants(participants_first_group, participants_second_group, separator='|')

# Выводим результат
print(common_participants)