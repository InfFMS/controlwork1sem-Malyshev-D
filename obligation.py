# Задача: Расчет доходности облигации с учетом комиссии и налогов
# -----------------------------------------------------------------------------
# Введение:
# Облигация — это долговая ценная бумага, которая приносит доход в виде процентов
# (купонов) или разницы между ценой покупки и ценой погашения.
#
# Ваши вложения в облигацию могут быть уменьшены за счет:
# 1. Комиссии брокера при покупке облигации.
# 2. Подоходного налога (13%) на полученный доход.
#
# Ваша задача — написать программу, которая рассчитает ЧИСТУЮ доходность облигации
# с учетом этих факторов.
# -----------------------------------------------------------------------------
#
# Условия:
# Пользователь вводит данные:
# 1. Цена покупки облигации.
# 2. Цена погашения облигации.
# 3. Сумму разовой купонной выплаты.
# 4. Периодичность выплаты купонов (в месяцах).
# 5. Комиссию брокера (в процентах) — применяется только при покупке облигации.
# 6. Период до погашения облигации (в месяцах).
#
# Формулы:
# 1. Комиссия на покупку:
#    Комиссия на покупку = Цена покупки × (Комиссия / 100)
#
# 2. Полная цена покупки:
#    Полная цена покупки = Цена покупки + Комиссия на покупку
#
# 3. Общий купонный доход:
#    Общий купонный доход = Сумма купона × (Период до погашения / Периодичность купонов)
#
# 4. Общий доход до налогообложения:
#    Общий доход = Цена погашения + Общий купонный доход - Полная цена покупки
#
# 5. Налог на доход:
#    Налог = Общий доход × 13%, если доход > 0, иначе налог = 0
#
# 6. Чистая доходность (в процентах):
#    Чистая доходность (%) = (Общий доход - Налог) / Чистая цена покупки × 100
#
# -----------------------------------------------------------------------------
# Напишите программу ниже:
