import datetime
import random
import string
import pyttsx3
from pydub import AudioSegment
from langdetect import detect


def engine_settings(engine):
	voices = engine.getProperty('voices')
	engine.setProperty('rate', 185)  # Выставляем скорость чтения голоса
	for voice in voices:
		if voice.name == 'Aleksander':
			return engine.setProperty('voice', voice.id)  # Выбираем подходящий голос


def get_mp3_file(file_name, article_text, article_lang):
	engine = pyttsx3.init()
	engine_settings(engine)  # Применение настроек голоса
	engine.save_to_file(article_text, file_name)  # Сохранение текста статьи в аудиофайл
	engine.runAndWait()
	convert_file_to_mp3(file_name)  # Конвертация в mp3 формат


def convert_file_to_mp3(file_name):
	converter = AudioSegment
	converter_file = converter.from_file(file_name)
	converter_file.export(file_name, format="mp3")


def get_file_name():
	file_name = ''
	for _ in range(8):
		file_name += random.choice(string.ascii_letters)
	file_name += '_' + str(datetime.datetime.now().date())
	file_name += '.mp3'  # Сохраняем файл изначально в mp3 формате
	return file_name


def get_article_language(article_text):
	lang_dict = {'en': ['EN', ['en_GB']],
	             'ru': ['RU', ['ru_RU']]}
	try:
		language = detect(article_text)  # Определяем язык статьи
	except TypeError:
		return False
	return lang_dict.get(language, False)
