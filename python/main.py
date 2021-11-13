# pip install google-cloud-translate
# Python 3.8

import os
from google.cloud import translate_v2 as translate


def main():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"solar-center-332017-e36ffd47e8aa.json"

    translate_client = translate.Client()

    text = input("Enter a message you want to translate: ")
    target = input("Enter the language you want to translate into: ")
    # Target takes a ISO-639-1 Code for the language you want to translate into
    # All codes supported: https://cloud.google.com/translate/docs/languages

    output = translate_client.translate(values=text,
                                        target_language=target,
                                        model="nmt")

    print(output['translatedText'])
    # print(output)


if __name__ == '__main__':
    main()
