import random

welcome_msg = ("Добро пожаловать в наш магазин эзотерики! 🔮\n"
               "Ты сможешь найти здесь всё, что пригодится для знакомства с потусторонним миром! 👻\n"
               "Выбирай, что хочешь приобрести:")

def get_magic_ball_phrase():
    """Возвращает случайную фразу магического шара"""
    phrases = [
        "Бесспорно",
        "Купи шар",
        "Никаких сомнений",
        "Определённо да",
        "Можешь быть уверен(а) в этом",
        "Мне кажется — «тебе стоит купить шар»",
        "Вероятнее всего",
        "Хорошие перспективы",
        "Знаки говорят — «купи шар»",
        "Да, тебе стоит купить шар",
        "Пока не ясно, попробуй снова",
        "Купи шар и спроси позже",
        "Лучше не рассказывать",
        "Сейчас нельзя предсказать",
        "Купи шар и спроси опять",
        "Даже не думай",
        "Мой ответ — «нет»",
        "Перспективы не очень хорошие, но ты всегда можешь купить шар",
        "Весьма сомнительно"
    ]
    return random.choice(phrases)
