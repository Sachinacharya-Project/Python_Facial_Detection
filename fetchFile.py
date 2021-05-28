from tkinter import Tk, filedialog

root = Tk()
root.title('Fetching Image/Video')
root.withdraw()
root.attributes('-topmost', True)

def FetchFile(fileType='image'):
    if fileType == 'image':
        file = filedialog.askopenfilename(title='Choose Image', filetypes=(('JPEG', ('.jpg', '.jpeg')), ('PNG', '.png'), ('All Images', '.*')))
    else:
        file = filedialog.askopenfilename(title='Choose Video', filetypes=(('mp4', ('.mp4')), ('mkv', '.mkv'), ('All Images', '.*')))
    return file