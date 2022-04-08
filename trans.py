def translate_text(text):
	"""Translates text into the target language.

	Target must be an ISO 639-1 language code.
	See https://g.co/cloud/translate/v2/translate-reference#supported_languages
	"""
	import six
	from google.cloud import translate_v2 as translate
	import os
	os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="abc.json"
	translate_client = translate.Client()

	if isinstance(text, six.binary_type):
	    text = text.decode("utf-8")

	# Text can also be a sequence of strings, in which case this method
	# will return a sequence of results for each text.
	result = translate_client.translate(text, target_language = "vi")

	print(u"Text: {}".format(result["input"]))
	print(u"Translation: {}".format(result["translatedText"]))
	print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))
	return result['translatedText']
# print(translate_text("hello world"))