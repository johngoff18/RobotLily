from pathlib import Path
import os
import sf2_loader as sf


from datetime import date, timedelta
from datetime import datetime
import time


# Utility Classes : for Various Tasks such as file name handling and job progress completion percentage


def remove_ext(fileName):
   filename = Path(fileName)
   return filename.with_suffix('')


def percentage(part, whole):
 return 100 * float(part)/float(whole)


def iterate(n):
   n += 1
   return n


# Main render Functions : bread and butter of the application.  Utilizes the sf2_loader to render midi files to wav format in the designated soundfont and instrument specified


def midi_to_wav(midiFile):
   loader = sf.sf2_loader('./soundfonts/lyle.sf2')
   # Gets file name from the posix object.
   fileName = os.path.basename(midiFile)
   loader.export_midi_file(midiFile, name="export/hymnal/"+ fileName + "lyle.wav", format='wav',track=[0], frame_rate=44100)


# Main render test Function: bread and butter test of the application.  Utilizes the sf2_loader to play midi files in the designated soundfont and instrument specified


def play_midi_file(midiFile):
   loader = sf.sf2_loader('soundfonts/essential.sf2')
   loader.play_midi_file(midiFile, instruments= [59,59,59,32])


# Loops of the Application : functions designed to take files, instruments, or other lists and repeat the main render functions in batch processing


#loops through presets by number
def convert_into_all():
   for x in range (1,59):
       robotlilyDriver(x)


#loops through all midi files in library directory
def loop_songs():
   pathlist = Path('library/').glob('**/*.mid')
   for path in pathlist:
       # because path is PosixPath not string
       play_midi_file(path)
       # print(path_in_str)
       print(path)


#loops through all midi files in library directory
def loop_production_voices():
   for subdir, dirs, files in os.walk(r'https://www.https://www.productionvoices.com/wp-content/uploads/'):
       for filename in files:
           filepath = subdir + os.sep + filename
           if filepath.endswith(".rar") or filepath.endswith(".wav"):
               print (filepath)




#basic information function used to test sf2_loader current configuration
def get_loader_information():
   loader = sf.sf2_loader('soundfonts/essential.sf2')
   loader.change_preset('Ch Grand+ChamberStr')
   all_instruments = loader.get_all_instrument_names()
   current_instrument = loader.get_current_instrument()
   sfidList = loader.sfid_list
   print(all_instruments)
   print(current_instrument)
   print(sfidList)


#Method for retrieveing track information takes (sf2_loader,posixpath) arguments
def track_and_instrument_information(loader,midiFile):
   current_midi_file = sf.mp.read(midiFile, mode='all', to_piece=True, get_off_drums=False)
   print(current_midi_file.instruments_list)
   print(current_midi_file.channels)
   print(current_midi_file.instruments_numbers)
   print(loader.get_instrument_name(track=None,
                         sfid=None,
                         bank_num=None,
                         preset_num=None,
                         num=0))


#main executing function of program : loops through midi files, sets the configuration of sf2_loader then it renders each midi file as a wav file and displays the name of the completed render in the terminal for progress tracking.
def robotlilyDriver():
   pathlist = Path('library/').glob('**/*.mid')
   pathlist1 = Path('library/').glob('**/*.mid')


   process_start_time = datetime.now()


   iteration = 1
   number_of_project_files = 0


   for path in pathlist:
       number_of_project_files += 1
       print(str(number_of_project_files) + " : " + os.path.basename(path))
      
   current_date_time = datetime.now()
   duration_of_task = current_date_time - process_start_time
   seconds = duration_of_task.total_seconds()
   print("Operation completed in " + str(seconds) + " seconds")
  
   process_start_time = datetime.now()


   for path in pathlist1:
       progress = percentage(float(iteration),float(number_of_project_files))
       # because path is PosixPath not string
       midi_to_wav(path)
       # print(path_in_str)
       out_of_total = str(iteration) + "/" + str(number_of_project_files)
       print("Progress : " + out_of_total + " " + str(progress) + "% " + os.path.basename(path))
       iteration += 1






       current_date_time = datetime.now()
       duration_of_task = current_date_time - process_start_time
       seconds = duration_of_task.total_seconds()
       print("Operation duration so-far is " + str(seconds) + " seconds")
       print("Estimated time remaining: " + str(duration_of_task*(number_of_project_files-iteration)))
       # break


   print("Operation completed in " + str(seconds) + " seconds")


if __name__ == "__main__":
   robotlilyDriver()
   # loop_songs()
   # loop_production_voices()
  
  
   # {0: {
   # 0: 'Yamaha C5 Grand',
   # 1: 'Large Concert Grand',
   # 2: 'Mellow C5 Grand',
   # 3: 'Bright C5 Grand',
   # 4: 'Upright Piano',
   # 5: 'Chateau Grand',
   # 6: 'Mellow Chateau Grand',
   # 7: 'Dark Chateau Grand',
   # 8: 'Rhodes EP', 9: 'DX7 EP',
   # 10: 'Rhodes Bell EP',
   # 11: 'Rotary Organ',
   # 12: 'Small Pipe Organ',
   # 13: 'Pipe Organ Full',
   # 14: 'Small Plein-Jeu',
   # 15: 'Flute Sml Plein-Jeu',
   # 16: 'FlutePad Sml Plein-J',
   # 17: 'Plein-jeu Organ Lge',
   # 18: 'Pad Plein-Jeu Large',
   # 19: 'Warm Pad',
   # 20: 'Synth Strings',
   # 21: 'Voyager-8',
   # 22: 'Full Strings Vel',
   # 23: 'Full Orchestra',
   # 24: 'Chamber Strings 1',
   # 25: 'Chamber Str 2 (SSO)',
   # 26: 'Violin (all around)',
   # 27: 'Two Violins',
   # 28: 'Cello 1',
   # 29: 'Cello 2 (SSO)',
   # 30: 'Trumpet',
   # 31: 'Trumpet+8 Vel',
   # 32: 'Tuba', 33: 'Oboe',
   # 34: 'Tenor Sax', 3
   # 35: 'Alto Sax',
   # 36: 'Flute Expr+8 (SSO)',
   # 37: 'Flute 2',
   # 38: 'Timpani',
   # 39: 'Banjo 5 String',
   # 40: 'Steel Guitar',
   # 41: 'Nylon Guitar',
   # 42: 'Spanish Guitar',
   # 43: 'Spanish V Slide',
   # 44: 'Clean Guitar',
   # 45: 'LP Twin Elec Gtr',
   # 46: 'LP Twin Dynamic',
   # 47: 'Muted LP Twin',
   # 48: 'Jazz Guitar',
   # 49: 'Chorus Guitar',
   # 50: 'YamC5 + Pad',
   # 51: 'YamC5+LowStrings',
   # 52: 'YamC5+ChamberStr',
   # 53: 'YamC5+Strings',
   # 54: 'Chateau Grand+Pad',
   # 55: 'Ch Grand+LowStrings',
   # 56: 'Ch Grand+ChamberStr',
   # 57: 'Ch Grand+Strings',
   # 58: 'DX7+Pad',
   # 59: 'DX7+LowStrings'}}
from pathlib import Path
import os
import sf2_loader as sf


from datetime import date, timedelta
from datetime import datetime
import time


# Utility Classes : for Various Tasks such as file name handling and job progress completion percentage


def remove_ext(fileName):
   filename = Path(fileName)
   return filename.with_suffix('')


def percentage(part, whole):
 return 100 * float(part)/float(whole)


def iterate(n):
   n += 1
   return n


# Main render Functions : bread and butter of the application.  Utilizes the sf2_loader to render midi files to wav format in the designated soundfont and instrument specified


def midi_to_wav(midiFile):
   loader = sf.sf2_loader('./soundfonts/lyle.sf2')
   # Gets file name from the posix object.
   fileName = os.path.basename(midiFile)
   loader.export_midi_file(midiFile, name="export/hymnal/"+ fileName + "lyle.wav", format='wav',track=[0], frame_rate=44100)


# Main render test Function: bread and butter test of the application.  Utilizes the sf2_loader to play midi files in the designated soundfont and instrument specified


def play_midi_file(midiFile):
   loader = sf.sf2_loader('soundfonts/essential.sf2')
   loader.play_midi_file(midiFile, instruments= [59,59,59,32])


# Loops of the Application : functions designed to take files, instruments, or other lists and repeat the main render functions in batch processing


#loops through presets by number
def convert_into_all():
   for x in range (1,59):
       robotlilyDriver(x)


#loops through all midi files in library directory
def loop_songs():
   pathlist = Path('library/').glob('**/*.mid')
   for path in pathlist:
       # because path is PosixPath not string
       play_midi_file(path)
       # print(path_in_str)
       print(path)


#loops through all midi files in library directory
def loop_production_voices():
   for subdir, dirs, files in os.walk(r'https://www.https://www.productionvoices.com/wp-content/uploads/'):
       for filename in files:
           filepath = subdir + os.sep + filename
           if filepath.endswith(".rar") or filepath.endswith(".wav"):
               print (filepath)




#basic information function used to test sf2_loader current configuration
def get_loader_information():
   loader = sf.sf2_loader('soundfonts/essential.sf2')
   loader.change_preset('Ch Grand+ChamberStr')
   all_instruments = loader.get_all_instrument_names()
   current_instrument = loader.get_current_instrument()
   sfidList = loader.sfid_list
   print(all_instruments)
   print(current_instrument)
   print(sfidList)


#Method for retrieveing track information takes (sf2_loader,posixpath) arguments
def track_and_instrument_information(loader,midiFile):
   current_midi_file = sf.mp.read(midiFile, mode='all', to_piece=True, get_off_drums=False)
   print(current_midi_file.instruments_list)
   print(current_midi_file.channels)
   print(current_midi_file.instruments_numbers)
   print(loader.get_instrument_name(track=None,
                         sfid=None,
                         bank_num=None,
                         preset_num=None,
                         num=0))


#main executing function of program : loops through midi files, sets the configuration of sf2_loader then it renders each midi file as a wav file and displays the name of the completed render in the terminal for progress tracking.
def robotlilyDriver():
   pathlist = Path('library/').glob('**/*.mid')
   pathlist1 = Path('library/').glob('**/*.mid')


   process_start_time = datetime.now()


   iteration = 1
   number_of_project_files = 0


   for path in pathlist:
       number_of_project_files += 1
       print(str(number_of_project_files) + " : " + os.path.basename(path))
      
   current_date_time = datetime.now()
   duration_of_task = current_date_time - process_start_time
   seconds = duration_of_task.total_seconds()
   print("Operation completed in " + str(seconds) + " seconds")
  
   process_start_time = datetime.now()


   for path in pathlist1:
       progress = percentage(float(iteration),float(number_of_project_files))
       # because path is PosixPath not string
       midi_to_wav(path)
       # print(path_in_str)
       out_of_total = str(iteration) + "/" + str(number_of_project_files)
       print("Progress : " + out_of_total + " " + str(progress) + "% " + os.path.basename(path))
       iteration += 1






       current_date_time = datetime.now()
       duration_of_task = current_date_time - process_start_time
       seconds = duration_of_task.total_seconds()
       print("Operation duration so-far is " + str(seconds) + " seconds")
       print("Estimated time remaining: " + str(duration_of_task*(number_of_project_files-iteration)))
       # break


   print("Operation completed in " + str(seconds) + " seconds")


if __name__ == "__main__":
   robotlilyDriver()
   # loop_songs()
   # loop_production_voices()
  
  
   # {0: {
   # 0: 'Yamaha C5 Grand',
   # 1: 'Large Concert Grand',
   # 2: 'Mellow C5 Grand',
   # 3: 'Bright C5 Grand',
   # 4: 'Upright Piano',
   # 5: 'Chateau Grand',
   # 6: 'Mellow Chateau Grand',
   # 7: 'Dark Chateau Grand',
   # 8: 'Rhodes EP', 9: 'DX7 EP',
   # 10: 'Rhodes Bell EP',
   # 11: 'Rotary Organ',
   # 12: 'Small Pipe Organ',
   # 13: 'Pipe Organ Full',
   # 14: 'Small Plein-Jeu',
   # 15: 'Flute Sml Plein-Jeu',
   # 16: 'FlutePad Sml Plein-J',
   # 17: 'Plein-jeu Organ Lge',
   # 18: 'Pad Plein-Jeu Large',
   # 19: 'Warm Pad',
   # 20: 'Synth Strings',
   # 21: 'Voyager-8',
   # 22: 'Full Strings Vel',
   # 23: 'Full Orchestra',
   # 24: 'Chamber Strings 1',
   # 25: 'Chamber Str 2 (SSO)',
   # 26: 'Violin (all around)',
   # 27: 'Two Violins',
   # 28: 'Cello 1',
   # 29: 'Cello 2 (SSO)',
   # 30: 'Trumpet',
   # 31: 'Trumpet+8 Vel',
   # 32: 'Tuba', 33: 'Oboe',
   # 34: 'Tenor Sax', 3
   # 35: 'Alto Sax',
   # 36: 'Flute Expr+8 (SSO)',
   # 37: 'Flute 2',
   # 38: 'Timpani',
   # 39: 'Banjo 5 String',
   # 40: 'Steel Guitar',
   # 41: 'Nylon Guitar',
   # 42: 'Spanish Guitar',
   # 43: 'Spanish V Slide',
   # 44: 'Clean Guitar',
   # 45: 'LP Twin Elec Gtr',
   # 46: 'LP Twin Dynamic',
   # 47: 'Muted LP Twin',
   # 48: 'Jazz Guitar',
   # 49: 'Chorus Guitar',
   # 50: 'YamC5 + Pad',
   # 51: 'YamC5+LowStrings',
   # 52: 'YamC5+ChamberStr',
   # 53: 'YamC5+Strings',
   # 54: 'Chateau Grand+Pad',
   # 55: 'Ch Grand+LowStrings',
   # 56: 'Ch Grand+ChamberStr',
   # 57: 'Ch Grand+Strings',
   # 58: 'DX7+Pad',
   # 59: 'DX7+LowStrings'}}