from re import compile , match
from os.path import exists

from pydub import AudioSegment

r_mp3 = compile(r"(?P<file_name>.+)+.mp3")


def convert_mp3_to_wav(file_name):
    assert exists(file_name), FileExistsError("Not existing mp3 file %s", file_name)
    assert match(r_mp3, file_name), ValueError("Not mp3 file %s", file_name)

    mp3_file_name = match(r_mp3, file_name).groupdict()['file_name']
    if exists( mp3_file_name+ '.wav'):
        return 0



    try:
        sound = AudioSegment.from_mp3(file_name)
        sound.export(mp3_file_name + '.wav', format="wav")
    except:
        print("Fail to conver to wave file")
        return -1
    return 0



