
import speech_recognition
import os
import random
import webbrowser
sr = speech_recognition.Recognizer()
cmd_list = {
    'functions': {
        'create_task': ['задача', "заметка", "создать задачу", "создать заметку", "создай задачу", "создай заметку"],
        'greeting': ['лифт', "привет"],
        "play_music": ['дискотека', "поставь музыку", "музыка"],
        "browser": ['поищи', "браузер", "поиск"],
        'open_program': ['открой телеграм', "открой telegram", "запусти телеграм", "запусти telegram"],
        'open_site': ['открой сайт']
    }
    

}
def greeting():
    return "Здравствуйте!"


def listen():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
            print('[...]')
            return query
    except speech_recognition.UnknownValueError as e:
        print("I DONT UNDERSTAND YOU")

def create_task():
    
    print('Что записать?')
    query = listen()
    with open('tasks.txt', 'a') as file:
        file.write(f'{query}\n')
    return "SUCCESS"

def play_music():
    files = os.listdir('music')
    random_file = f'music/{random.choice(files)}'
    os.system(f'xdg-open {random_file}')
    return f'{random_file}'
    
def browser():
    print('[...]')
    print('Что ищем?')
    
    query = listen()
    webbrowser.open(f'www.google.com/search?q={query}')
    print(query)



def open_program():
    os.system('telegram-desktop')

def open_site():
    print('Site: ')
    query= listen()
    print(f'{query} opening')
    webbrowser.open(f'www.{query}.com')  
def main():
    query = listen()
    for k,v in cmd_list['functions'].items():
        if query in v:
            print(globals()[k]())
    
if __name__ == '__main__':
    main()





