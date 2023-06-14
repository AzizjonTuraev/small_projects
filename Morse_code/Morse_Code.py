# To run the code fully with sounds please use Windows OS


import time
import winsound

freq = 600 
dotLength = 60 
dashLength = dotLength * 4
pauseWords = dotLength * 8





def beep(dur):
    """
    makes noise for specific duration.
    :param dur: duration of beep in milliseconds
    """
    winsound.Beep(freq, dur)

def pause(dur):
    """
    pauses audio for dur milliseconds
    :param dur: duration of pause in milliseconds
    """
    time.sleep(dur / 1000)

def morseaudio(morse):
    """
    plays audio conversion of morse string using inbuilt windows module.
    :param morse: morse code string.
    """
    for char in morse:
        if char == ".":
            beep(dotLength)
        elif char == "-":
            beep(dashLength)
        elif char == "/":
            pause(pauseWords)
        else:
            # char is blank space
            pause(dashLength)




MORSE_CODE_DICT = {'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".",
                'f': "..-.", 'g': "--.", 'h': "....", 'i': "..", 'j': ".---", 'k': "-.-",
                'l': ".-..", 'm': "--", 'n': "-.", 'o': "---", 'p': ".--.", 'q': "--.-",
                'r': ".-.", 's': "...", 't': "-", 'u': "..-", 'v': "...-", 'w': ".--",
                'x': "-..-", 'y': "-.--", 'z': "--..",
                '1': ".----", '2': "..---", '3': "...--", '4': "....-", '5': ".....",
                '6': "-....", '7': "--...", '8': "---..", '9': "----.", '0': "-----",
                ' ': ".......", '.': ".-.-.-", ',': "--..--", '?': "..--..", "'": ".----.",
                '@': ".--.-.", '-': "-....-", '"': ".-..-.", ':': "---...", ';': "---...",
                '=': "-...-", '!': "-.-.--", '/': "-..-.", '(': "-.--.", ')': "-.--.-",
                'á': ".--.-", 'é': "..-.."}




def to_morse(text):
    
    """ A function that translates english words into Morse code.
    
    An argument takes only a word
    
    """
    
    
    try:

        chunk = []
        for char in text:
        
            chunk.append(MORSE_CODE_DICT[char.lower()])
            chunk.append(' ')
    
        answer = ''.join(chunk).strip()
        morseaudio(answer)
        
        return answer
    
    except:
        
        return print('Check for your input. It may include a sign that is not in Morse Code')






def to_english(word):
    
    """ A function that translates Morse code into english words.
    
        An argument takes Morse code that is equivalent to a single word in English
    
    """


    try:
    
        chunk = []
    
        for each in word.split():
            
            letter = list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(each)]
            chunk.append(letter)
        
        answer = ''.join(chunk)
    
        return answer
    
    except:
        
        return print('Check for your input. It may include a sign that is not in Morse Code')




def test_case1():
     assert to_morse('Hello World!') == '.... . .-.. .-.. --- ....... .-- --- .-. .-.. -.. -.-.--'



def test_case2():
     assert to_english('.... . .-.. .-.. --- ....... .-- --- .-. .-.. -.. -.-.--') == 'hello world!'



def test_case3():
    assert to_morse('This is a test code') == '- .... .. ... ....... .. ... ....... .- ....... - . ... - ....... -.-. --- -.. .'