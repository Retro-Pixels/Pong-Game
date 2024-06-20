import time
from Buzzer import PassiveBuzzer


# Note definitions
NOTE_B0 = 31
NOTE_C1 = 33
NOTE_CS1 = 35
NOTE_D1 = 37
NOTE_DS1 = 39
NOTE_E1 = 41
NOTE_F1 = 44
NOTE_FS1 = 46
NOTE_G1 = 49
NOTE_GS1 = 52
NOTE_A1 = 55
NOTE_AS1 = 58
NOTE_B1 = 62
NOTE_C2 = 65
NOTE_CS2 = 69
NOTE_D2 = 73
NOTE_DS2 = 78
NOTE_E2 = 82
NOTE_F2 = 87
NOTE_FS2 = 93
NOTE_G2 = 98
NOTE_GS2 = 104
NOTE_A2 = 110
NOTE_AS2 = 117
NOTE_B2 = 123
NOTE_C3 = 131
NOTE_CS3 = 139
NOTE_D3 = 147
NOTE_DS3 = 156
NOTE_E3 = 165
NOTE_F3 = 175
NOTE_FS3 = 185
NOTE_G3 = 196
NOTE_GS3 = 208
NOTE_A3 = 220
NOTE_AS3 = 233
NOTE_B3 = 247
NOTE_C4 = 262
NOTE_CS4 = 277
NOTE_D4 = 294
NOTE_DS4 = 311
NOTE_E4 = 330
NOTE_F4 = 349
NOTE_FS4 = 370
NOTE_G4 = 392
NOTE_GS4 = 415
NOTE_A4 = 440
NOTE_AS4 = 466
NOTE_B4 = 494
NOTE_C5 = 523
NOTE_CS5 = 554
NOTE_D5 = 587
NOTE_DS5 = 622
NOTE_E5 = 659
NOTE_F5 = 698
NOTE_FS5 = 740
NOTE_G5 = 784
NOTE_GS5 = 831
NOTE_A5 = 880
NOTE_AS5 = 932
NOTE_B5 = 988
NOTE_C6 = 1047
NOTE_CS6 = 1109
NOTE_D6 = 1175
NOTE_DS6 = 1245
NOTE_E6 = 1319
NOTE_F6 = 1397
NOTE_FS6 = 1480
NOTE_G6 = 1568
NOTE_GS6 = 1661
NOTE_A6 = 1760
NOTE_AS6 = 1865
NOTE_B6 = 1976
NOTE_C7 = 2093
NOTE_CS7 = 2217
NOTE_D7 = 2349
NOTE_DS7 = 2489
NOTE_E7 = 2637
NOTE_F7 = 2794
NOTE_FS7 = 2960
NOTE_G7 = 3136
NOTE_GS7 = 3322
NOTE_A7 = 3520
NOTE_AS7 = 3729
NOTE_B7 = 3951
NOTE_C8 = 4186
NOTE_CS8 = 4435
NOTE_D8 = 4699
NOTE_DS8 = 4978
REST = 0

"""
    Song Selector number
    1: 'asa_branca', 2: 'at_dooms_gate', 3: 'bach_badinerie', 4: 'baby_elephant_walk', 
    5: 'bloody_tears', 6: 'brahms_lullaby', 7: 'cantina_band', 8: 'fur_elise', 
    9: 'game_of_thrones', 10: 'green_hill_zone', 11: 'greensleeves', 12: 'happy_birthday', 
    13: 'hedwigs_theme', 14: 'imperial_march', 15: 'jigglypuff_song', 16: 'keyboard_cat', 
    17: 'mii_channel_theme', 18: 'minuet_in_g', 19: 'never_gonna_give_you_up', 20: 'nokia_tune', 
    21: 'ode-to-joy', 22: 'pacman_intro_theme', 23: 'pachelbels_canon', 24: 'pink_panther_theme', 
    25: 'professor_laytons_theme', 26: 'pulo_da_gaita', 27: 'silent_night', 28: 'song_of_storms', 
    29: 'star_trek_intro', 30: 'star_wars_theme', 31: 'super_mario_theme', 32: 'take_on_me', 
    33: 'the_godfather', 34: 'the_lion_sleeps_tonight', 35: 'the_lick', 36: 'tetris_theme', 
    37: 'vampire_killer', 38: 'we_wish_you_a_merry_christmas', 39: 'zelda_melody', 40: 'zeldas_lullaby'
"""
melodyNumber = {1: 'asa_branca', 2: 'at_dooms_gate', 3: 'bach_badinerie', 4: 'baby_elephant_walk', 
    5: 'bloody_tears', 6: 'brahms_lullaby', 7: 'cantina_band', 8: 'fur_elise', 
    9: 'game_of_thrones', 10: 'green_hill_zone', 11: 'greensleeves', 12: 'happy_birthday', 
    13: 'hedwigs_theme', 14: 'imperial_march', 15: 'jigglypuff_song', 16: 'keyboard_cat', 
    17: 'mii_channel_theme', 18: 'minuet_in_g', 19: 'never_gonna_give_you_up', 20: 'nokia_tune', 
    21: 'ode-to-joy', 22: 'pacman_intro_theme', 23: 'pachelbels_canon', 24: 'pink_panther_theme', 
    25: 'professor_laytons_theme', 26: 'pulo_da_gaita', 27: 'silent_night', 28: 'song_of_storms', 
    29: 'star_trek_intro', 30: 'star_wars_theme', 31: 'super_mario_theme', 32: 'take_on_me', 
    33: 'the_godfather', 34: 'the_lion_sleeps_tonight', 35: 'the_lick', 36: 'tetris_theme', 
    37: 'vampire_killer', 38: 'we_wish_you_a_merry_christmas', 39: 'zelda_melody', 40: 'zeldas_lullaby'}

class Melody:
    def __init__(self, pin):
        self._buz = PassiveBuzzer(pin)
        self._melody_playing = False

    def play_melody(self, melodynumber):
        melody_name = melodyNumber.get(melodynumber)
        melody, tempo = melodies[melody_name], melody_tempos[melody_name]
        self._play_melody(melody, tempo)

    def stop(self):
        self._melody_playing = False
        self._buz.stop()

    """
        METHODS FOR INTERNAL USE ONLY 
    """
    def _play_melody(self, melody, tempo):
        
        wholenote = (60000 * 4) / tempo
        notes = len(melody) // 2

        self._melody_playing = True
        for thisNote in range(notes):
            if not self._melody_playing:
                break
            note = melody[thisNote * 2]
            duration = melody[thisNote * 2 + 1]
            if duration > 0:
                note_duration = wholenote / duration
            else:
                note_duration = wholenote / abs(duration) * 1.5

            if note >= 31:
                self._buz.play(note)
                time.sleep(note_duration * 0.9 / 1000)
                self._buz.stop()
                time.sleep(note_duration * 0.1 / 1000)
                
        self._melody_playing = False

    
# Define the tempos for each melody
melody_tempos = {
    'zelda_melody': 88,
    'zeldas_lullaby': 100,
    'mii_channel_theme': 114,
    'never_gonna_give_you_up': 114,
    'jigglypuff_song': 85,
    'pink_panther_theme': 120,
    'tetris_theme': 144,
    'super_mario_theme': 200,
    'song_of_storms': 108,
    'asa_branca': 120,
    'baby_elephant_walk': 132,
    'bloody_tears': 144,
    'brahms_lullaby': 76,
    'pachelbels_canon': 100,
    'cantina_band': 140,
    'at_dooms_gate': 225,
    'fur_elise': 80,
    'game_of_thrones': 85,
    'green_hill_zone': 140,
    'greensleeves': 70,
    'happy_birthday': 140,
    'hedwigs_theme': 144,
    'imperial_march': 120,
    'keyboard_cat': 160,
    'we_wish_you_a_merry_christmas': 140,
    'minuet_in_g': 140,
    'nokia_tune': 180,
    'ode-to-joy': 114,
    'pacman_intro_theme': 105,
    'professor_laytons_theme': 140,
    'pulo_da_gaita': 100,
    'silent_night': 140,
    'star_trek_intro': 80,
    'star_wars_theme': 108,
    'take_on_me': 140,
    'bach_badinerie': 120,
    'the_godfather': 80,
    'the_lick': 108,
    'the_lion_sleeps_tonight': 122,
    'vampire_killer': 130
}

# Define the melodies
melodies = {
    'zelda_melody': [
        NOTE_AS4, -2, NOTE_F4, 8, NOTE_F4, 8, NOTE_AS4, 8,
        NOTE_GS4, 16, NOTE_FS4, 16, NOTE_GS4, -2,
        NOTE_AS4, -2, NOTE_FS4, 8, NOTE_FS4, 8, NOTE_AS4, 8,
        NOTE_A4, 16, NOTE_G4, 16, NOTE_A4, -2,
        REST, 1,

        NOTE_AS4, 4, NOTE_F4, -4, NOTE_AS4, 8, NOTE_AS4, 16, NOTE_C5, 16, NOTE_D5, 16, NOTE_DS5, 16,
        NOTE_F5, 2, NOTE_F5, 8, NOTE_F5, 8, NOTE_F5, 8, NOTE_FS5, 16, NOTE_GS5, 16,
        NOTE_AS5, -2, NOTE_AS5, 8, NOTE_AS5, 8, NOTE_GS5, 8, NOTE_FS5, 16,
        NOTE_GS5, -8, NOTE_FS5, 16, NOTE_F5, 2, NOTE_F5, 4,

        NOTE_DS5, -8, NOTE_F5, 16, NOTE_FS5, 2, NOTE_F5, 8, NOTE_DS5, 8,
        NOTE_CS5, -8, NOTE_DS5, 16, NOTE_F5, 2, NOTE_DS5, 8, NOTE_CS5, 8,
        NOTE_C5, -8, NOTE_D5, 16, NOTE_E5, 2, NOTE_G5, 8,
        NOTE_F5, 16, NOTE_F4, 16, NOTE_F4, 16, NOTE_F4, 16, NOTE_F4, 16, NOTE_F4, 16, NOTE_F4, 16, NOTE_F4, 16, NOTE_F4, 8, NOTE_F4, 16, NOTE_F4, 8,

        NOTE_AS4, 4, NOTE_F4, -4, NOTE_AS4, 8, NOTE_AS4, 16, NOTE_C5, 16, NOTE_D5, 16, NOTE_DS5, 16,
        NOTE_F5, 2, NOTE_F5, 8, NOTE_F5, 8, NOTE_F5, 8, NOTE_FS5, 16, NOTE_GS5, 16,
        NOTE_AS5, -2, NOTE_CS6, 4,
        NOTE_C6, 4, NOTE_A5, 2, NOTE_F5, 4,
        NOTE_FS5, -2, NOTE_AS5, 4,
        NOTE_A5, 4, NOTE_F5, 2, NOTE_F5, 4,

        NOTE_FS5, -2, NOTE_AS5, 4,
        NOTE_A5, 4, NOTE_F5, 2, NOTE_D5, 4,
        NOTE_DS5, -2, NOTE_FS5, 4,
        NOTE_F5, 4, NOTE_CS5, 2, NOTE_AS4, 4,
        NOTE_C5, -8, NOTE_D5, 16, NOTE_E5, 2, NOTE_G5, 8,
        NOTE_F5, 16, NOTE_F4, 16, NOTE_F4, 16, NOTE_F4, 16, NOTE_F4, 16, NOTE_F4, 16, NOTE_F4, 16, NOTE_F4, 16, NOTE_F4, 8, NOTE_F4, 16, NOTE_F4, 8
    ],
    'zeldas_lullaby': [
        NOTE_E4, 2, NOTE_G4, 4,
        NOTE_D4, 2, NOTE_C4, 8, NOTE_D4, 8,
        NOTE_E4, 2, NOTE_G4, 4,
        NOTE_D4, -2,
        NOTE_E4, 2, NOTE_G4, 4,
        NOTE_D5, 2, NOTE_C5, 4,
        NOTE_G4, 2, NOTE_F4, 8, NOTE_E4, 8,
        NOTE_D4, -2,
        NOTE_E4, 2, NOTE_G4, 4,
        NOTE_D4, 2, NOTE_C4, 8, NOTE_D4, 8,
        NOTE_E4, 2, NOTE_G4, 4,
        NOTE_D4, -2,
        NOTE_E4, 2, NOTE_G4, 4,

        NOTE_D5, 2, NOTE_C5, 4,
        NOTE_G4, 2, NOTE_F4, 8, NOTE_E4, 8,
        NOTE_F4, 8, NOTE_E4, 8, NOTE_C4, 2,
        NOTE_F4, 2, NOTE_E4, 8, NOTE_D4, 8,
        NOTE_E4, 8, NOTE_D4, 8, NOTE_A3, 2,
        NOTE_G4, 2, NOTE_F4, 8, NOTE_E4, 8,
        NOTE_F4, 8, NOTE_E4, 8, NOTE_C4, 4, NOTE_F4, 4,
        NOTE_C5, -2,
    ],
    'mii_channel_theme': [
        NOTE_FS4, 8, REST, 8, NOTE_A4, 8, NOTE_CS5, 8, REST, 8, NOTE_A4, 8, REST, 8, NOTE_FS4, 8,
        NOTE_D4, 8, NOTE_D4, 8, NOTE_D4, 8, REST, 8, REST, 4, REST, 8, NOTE_CS4, 8,
        NOTE_D4, 8, NOTE_FS4, 8, NOTE_A4, 8, NOTE_CS5, 8, REST, 8, NOTE_A4, 8, REST, 8, NOTE_F4, 8,
        NOTE_E5, -4, NOTE_DS5, 8, NOTE_D5, 8, REST, 8, REST, 4,

        NOTE_GS4, 8, REST, 8, NOTE_CS5, 8, NOTE_FS4, 8, REST, 8, NOTE_CS5, 8, REST, 8, NOTE_GS4, 8,
        REST, 8, NOTE_CS5, 8, NOTE_G4, 8, NOTE_FS4, 8, REST, 8, NOTE_E4, 8, REST, 8,
        NOTE_E4, 8, NOTE_E4, 8, NOTE_E4, 8, REST, 8, REST, 4, NOTE_E4, 8, NOTE_E4, 8,
        NOTE_E4, 8, REST, 8, REST, 4, NOTE_DS4, 8, NOTE_D4, 8,

        NOTE_CS4, 8, REST, 8, NOTE_A4, 8, NOTE_CS5, 8, REST, 8, NOTE_A4, 8, REST, 8, NOTE_FS4, 8,
        NOTE_D4, 8, NOTE_D4, 8, NOTE_D4, 8, REST, 8, NOTE_E5, 8, NOTE_E5, 8, NOTE_E5, 8, REST, 8,
        REST, 8, NOTE_FS4, 8, NOTE_A4, 8, NOTE_CS5, 8, REST, 8, NOTE_A4, 8, REST, 8, NOTE_F4, 8,
        NOTE_E5, 2, NOTE_D5, 8, REST, 8, REST, 4,

        NOTE_B4, 8, NOTE_G4, 8, NOTE_D4, 8, NOTE_CS4, 4, NOTE_B4, 8, NOTE_G4, 8, NOTE_CS4, 8,
        NOTE_A4, 8, NOTE_FS4, 8, NOTE_C4, 8, NOTE_B3, 4, NOTE_F4, 8, NOTE_D4, 8, NOTE_B3, 8,
        NOTE_E4, 8, NOTE_E4, 8, NOTE_E4, 8, REST, 4, REST, 4, NOTE_AS4, 4,
        NOTE_CS5, 8, NOTE_D5, 8, NOTE_FS5, 8, NOTE_A5, 8, REST, 8, REST, 4,

        REST, 2, NOTE_A3, 4, NOTE_AS3, 4,
        NOTE_A3, -4, NOTE_A3, 8, NOTE_A3, 2,
        REST, 4, NOTE_A3, 8, NOTE_AS3, 8, NOTE_A3, 8, NOTE_F4, 4, NOTE_C4, 8,
        NOTE_A3, -4, NOTE_A3, 8, NOTE_A3, 2,

        REST, 2, NOTE_B3, 4, NOTE_C4, 4,
        NOTE_CS4, -4, NOTE_C4, 8, NOTE_CS4, 2,
        REST, 4, NOTE_CS4, 8, NOTE_C4, 8, NOTE_CS4, 8, NOTE_GS4, 4, NOTE_DS4, 8,
        NOTE_CS4, -4, NOTE_DS4, 8, NOTE_B3, 1,

        NOTE_E4, 4, NOTE_E4, 4, NOTE_E4, 4, REST, 8,
        NOTE_FS4, 8, REST, 8, NOTE_A4, 8, NOTE_CS5, 8, REST, 8, NOTE_A4, 8, REST, 8, NOTE_FS4, 8,
        NOTE_D4, 8, NOTE_D4, 8, NOTE_D4, 8, REST, 8, REST, 4, REST, 8, NOTE_CS4, 8,
        NOTE_D4, 8, NOTE_FS4, 8, NOTE_A4, 8, NOTE_CS5, 8, REST, 8, NOTE_A4, 8, REST, 8, NOTE_F4, 8,
        NOTE_E5, -4, NOTE_DS5, 8, NOTE_D5, 8, REST, 8, REST, 4,

        NOTE_GS4, 8, REST, 8, NOTE_CS5, 8, NOTE_FS4, 8, REST, 8, NOTE_CS5, 8, REST, 8, NOTE_GS4, 8,
        REST, 8, NOTE_CS5, 8, NOTE_G4, 8, NOTE_FS4, 8, REST, 8, NOTE_E4, 8, REST, 8,
        NOTE_E4, 8, NOTE_E4, 8, NOTE_E4, 8, REST, 8, REST, 4, NOTE_E4, 8, NOTE_E4, 8,
        NOTE_E4, 8, REST, 8, REST, 4, NOTE_DS4, 8, NOTE_D4, 8,

        NOTE_CS4, 8, REST, 8, NOTE_A4, 8, NOTE_CS5, 8, REST, 8, NOTE_A4, 8, REST, 8, NOTE_FS4, 8,
        NOTE_D4, 8, NOTE_D4, 8, NOTE_D4, 8, REST, 8, NOTE_E5, 8, NOTE_E5, 8, NOTE_E5, 8, REST, 8,
        REST, 8, NOTE_FS4, 8, NOTE_A4, 8, NOTE_CS5, 8, REST, 8, NOTE_A4, 8, REST, 8, NOTE_F4, 8,
        NOTE_E5, 2, NOTE_D5, 8, REST, 8, REST, 4,

        NOTE_B4, 8, NOTE_G4, 8, NOTE_D4, 8, NOTE_CS4, 4, NOTE_B4, 8, NOTE_G4, 8, NOTE_CS4, 8,
        NOTE_A4, 8, NOTE_FS4, 8, NOTE_C4, 8, NOTE_B3, 4, NOTE_F4, 8, NOTE_D4, 8, NOTE_B3, 8,
        NOTE_E4, 8, NOTE_E4, 8, NOTE_E4, 8, REST, 4, REST, 4, NOTE_AS4, 4,
        NOTE_CS5, 8, NOTE_D5, 8, NOTE_FS5, 8, NOTE_A5, 8, REST, 8, REST, 4,

        REST, 2, NOTE_A3, 4, NOTE_AS3, 4,
        NOTE_A3, -4, NOTE_A3, 8, NOTE_A3, 2,
        REST, 4, NOTE_A3, 8, NOTE_AS3, 8, NOTE_A3, 8, NOTE_F4, 4, NOTE_C4, 8,
        NOTE_A3, -4, NOTE_A3, 8, NOTE_A3, 2,

        REST, 2, NOTE_B3, 4, NOTE_C4, 4,
        NOTE_CS4, -4, NOTE_C4, 8, NOTE_CS4, 2,
        REST, 4, NOTE_CS4, 8, NOTE_C4, 8, NOTE_CS4, 8, NOTE_GS4, 4, NOTE_DS4, 8,
        NOTE_CS4, -4, NOTE_DS4, 8, NOTE_B3, 1,

        NOTE_E4, 4, NOTE_E4, 4, NOTE_E4, 4, REST, 8,
    ],
    'never_gonna_give_you_up': [
        NOTE_D5, -4, NOTE_E5, -4, NOTE_A4, 4,
        NOTE_E5, -4, NOTE_FS5, -4, NOTE_A5, 16, NOTE_G5, 16, NOTE_FS5, 8,
        NOTE_D5, -4, NOTE_E5, -4, NOTE_A4, 2,
        NOTE_A4, 16, NOTE_A4, 16, NOTE_B4, 16, NOTE_D5, 8, NOTE_D5, 16,
        NOTE_D5, -4, NOTE_E5, -4, NOTE_A4, 4,
        NOTE_E5, -4, NOTE_FS5, -4, NOTE_A5, 16, NOTE_G5, 16, NOTE_FS5, 8,
        NOTE_D5, -4, NOTE_E5, -4, NOTE_A4, 2,
        NOTE_A4, 16, NOTE_A4, 16, NOTE_B4, 16, NOTE_D5, 8, NOTE_D5, 16,
        REST, 4, NOTE_B4, 8, NOTE_CS5, 8, NOTE_D5, 8, NOTE_D5, 8, NOTE_E5, 8, NOTE_CS5, -8,
        NOTE_B4, 16, NOTE_A4, 2, REST, 4,

        REST, 8, NOTE_B4, 8, NOTE_B4, 8, NOTE_CS5, 8, NOTE_D5, 8, NOTE_B4, 4, NOTE_A4, 8,
        NOTE_A5, 8, REST, 8, NOTE_A5, 8, NOTE_E5, -4, REST, 4,
        NOTE_B4, 8, NOTE_B4, 8, NOTE_CS5, 8, NOTE_D5, 8, NOTE_B4, 8, NOTE_D5, 8, NOTE_E5, 8, REST, 8,
        REST, 8, NOTE_CS5, 8, NOTE_B4, 8, NOTE_A4, -4, REST, 4,
        REST, 8, NOTE_B4, 8, NOTE_B4, 8, NOTE_CS5, 8, NOTE_D5, 8, NOTE_B4, 8, NOTE_A4, 4,
        NOTE_E5, 8, NOTE_E5, 8, NOTE_E5, 8, NOTE_FS5, 8, NOTE_E5, 4, REST, 4,

        NOTE_D5, 2, NOTE_E5, 8, NOTE_FS5, 8, NOTE_D5, 8,
        NOTE_E5, 8, NOTE_E5, 8, NOTE_E5, 8, NOTE_FS5, 8, NOTE_E5, 4, NOTE_A4, 4,
        REST, 2, NOTE_B4, 8, NOTE_CS5, 8, NOTE_D5, 8, NOTE_B4, 8,
        REST, 8, NOTE_E5, 8, NOTE_FS5, 8, NOTE_E5, -4, NOTE_A4, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_B4, 16,
        NOTE_FS5, -8, NOTE_FS5, -8, NOTE_E5, -4, NOTE_A4, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_B4, 16,

        NOTE_E5, -8, NOTE_E5, -8, NOTE_D5, -8, NOTE_CS5, 16, NOTE_B4, -8, NOTE_A4, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_B4, 16,
        NOTE_D5, 4, NOTE_E5, 8, NOTE_CS5, -8, NOTE_B4, 16, NOTE_A4, 8, NOTE_A4, 8, NOTE_A4, 8,
        NOTE_E5, 4, NOTE_D5, 2, NOTE_A4, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_B4, 16,
        NOTE_FS5, -8, NOTE_FS5, -8, NOTE_E5, -4, NOTE_A4, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_B4, 16,
        NOTE_A5, 4, NOTE_CS5, 8, NOTE_D5, -8, NOTE_CS5, 16, NOTE_B4, 8, NOTE_A4, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_B4, 16,

        NOTE_D5, 4, NOTE_E5, 8, NOTE_CS5, -8, NOTE_B4, 16, NOTE_A4, 4, NOTE_A4, 8,
        NOTE_E5, 4, NOTE_D5, 2, REST, 4,
        REST, 8, NOTE_B4, 8, NOTE_D5, 8, NOTE_B4, 8, NOTE_D5, 8, NOTE_E5, 4, REST, 8,
        REST, 8, NOTE_CS5, 8, NOTE_B4, 8, NOTE_A4, -4, REST, 4,
        REST, 8, NOTE_B4, 8, NOTE_B4, 8, NOTE_CS5, 8, NOTE_D5, 8, NOTE_B4, 8, NOTE_A4, 4,
        REST, 8, NOTE_A5, 8, NOTE_A5, 8, NOTE_E5, 8, NOTE_FS5, 8, NOTE_E5, 8, NOTE_D5, 8,

        REST, 8, NOTE_A4, 8, NOTE_B4, 8, NOTE_CS5, 8, NOTE_D5, 8, NOTE_B4, 8,
        REST, 8, NOTE_CS5, 8, NOTE_B4, 8, NOTE_A4, -4, REST, 4,
        NOTE_B4, 8, NOTE_B4, 8, NOTE_CS5, 8, NOTE_D5, 8, NOTE_B4, 8, NOTE_A4, 4, REST, 8,
        REST, 8, NOTE_E5, 8, NOTE_E5, 8, NOTE_FS5, 4, NOTE_E5, -4,
        NOTE_D5, 2, NOTE_D5, 8, NOTE_E5, 8, NOTE_FS5, 8, NOTE_E5, 4,
        NOTE_E5, 8, NOTE_E5, 8, NOTE_FS5, 8, NOTE_E5, 8, NOTE_A4, 8, NOTE_A4, 4,

        REST, -4, NOTE_A4, 8, NOTE_B4, 8, NOTE_CS5, 8, NOTE_D5, 8, NOTE_B4, 8,
        REST, 8, NOTE_E5, 8, NOTE_FS5, 8, NOTE_E5, -4, NOTE_A4, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_B4, 16,
        NOTE_FS5, -8, NOTE_FS5, -8, NOTE_E5, -4, NOTE_A4, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_B4, 16,
        NOTE_E5, -8, NOTE_E5, -8, NOTE_D5, -8, NOTE_CS5, 16, NOTE_B4, 8, NOTE_A4, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_B4, 16,
        NOTE_D5, 4, NOTE_E5, 8, NOTE_CS5, -8, NOTE_B4, 16, NOTE_A4, 4, NOTE_A4, 8,

        NOTE_E5, 4, NOTE_D5, 2, NOTE_A4, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_B4, 16,
        NOTE_FS5, -8, NOTE_FS5, -8, NOTE_E5, -4, NOTE_A4, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_B4, 16,
        NOTE_A5, 4, NOTE_CS5, 8, NOTE_D5, -8, NOTE_CS5, 16, NOTE_B4, 8, NOTE_A4, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_B4, 16,
        NOTE_D5, 4, NOTE_E5, 8, NOTE_CS5, -8, NOTE_B4, 16, NOTE_A4, 4, NOTE_A4, 8,
        NOTE_E5, 4, NOTE_D5, 2, NOTE_A4, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_B4, 16,

        NOTE_FS5, -8, NOTE_FS5, -8, NOTE_E5, -4, NOTE_A4, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_B4, 16,
        NOTE_A5, 4, NOTE_CS5, 8, NOTE_D5, -8, NOTE_CS5, 16, NOTE_B4, 8, NOTE_A4, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_B4, 16,
        NOTE_D5, 4, NOTE_E5, 8, NOTE_CS5, -8, NOTE_B4, 16, NOTE_A4, 4, NOTE_A4, 8,

        NOTE_E5, 4, NOTE_D5, 2, REST, 4
    ],
    'jigglypuff_song': [
        NOTE_D5, -4, NOTE_A5, 8, NOTE_FS5, 8, NOTE_D5, 8,
        NOTE_E5, -4, NOTE_FS5, 8, NOTE_G5, 4,
        NOTE_FS5, -4, NOTE_E5, 8, NOTE_FS5, 4,
        NOTE_D5, -2,
        NOTE_D5, -4, NOTE_A5, 8, NOTE_FS5, 8, NOTE_D5, 8,
        NOTE_E5, -4, NOTE_FS5, 8, NOTE_G5, 4,
        NOTE_FS5, -1,
        NOTE_D5, -4, NOTE_A5, 8, NOTE_FS5, 8, NOTE_D5, 8,
        NOTE_E5, -4, NOTE_FS5, 8, NOTE_G5, 4,
        NOTE_FS5, -4, NOTE_E5, 8, NOTE_FS5, 4,
        NOTE_D5, -2,
        NOTE_D5, -4, NOTE_A5, 8, NOTE_FS5, 8, NOTE_D5, 8,
        NOTE_E5, -4, NOTE_FS5, 8, NOTE_G5, 4,
        NOTE_FS5, -1,
    ],
    'pink_panther_theme': [
        REST, 2, REST, 4, REST, 8, NOTE_DS4, 8,
        NOTE_E4, -4, REST, 8, NOTE_FS4, 8, NOTE_G4, -4, REST, 8, NOTE_DS4, 8,
        NOTE_E4, -8, NOTE_FS4, 8, NOTE_G4, -8, NOTE_C5, 8, NOTE_B4, -8, NOTE_E4, 8, NOTE_G4, -8, NOTE_B4, 8,
        NOTE_AS4, 2, NOTE_A4, -16, NOTE_G4, -16, NOTE_E4, -16, NOTE_D4, -16,
        NOTE_E4, 2, REST, 4, REST, 8, NOTE_DS4, 4,

        NOTE_E4, -4, REST, 8, NOTE_FS4, 8, NOTE_G4, -4, REST, 8, NOTE_DS4, 8,
        NOTE_E4, -8, NOTE_FS4, 8, NOTE_G4, -8, NOTE_C5, 8, NOTE_B4, -8, NOTE_G4, 8, NOTE_B4, -8, NOTE_E5, 8,
        NOTE_DS5, 1,
        NOTE_D5, 2, REST, 4, REST, 8, NOTE_DS4, 8,
        NOTE_E4, -4, REST, 8, NOTE_FS4, 8, NOTE_G4, -4, REST, 8, NOTE_DS4, 8,
        NOTE_E4, -8, NOTE_FS4, 8, NOTE_G4, -8, NOTE_C5, 8, NOTE_B4, -8, NOTE_E4, 8, NOTE_G4, -8, NOTE_B4, 8,

        NOTE_AS4, 2, NOTE_A4, -16, NOTE_G4, -16, NOTE_E4, -16, NOTE_D4, -16,
        NOTE_E4, -4, REST, 4,
        REST, 4, NOTE_E5, -8, NOTE_D5, 8, NOTE_B4, -8, NOTE_A4, 8, NOTE_G4, -8, NOTE_E4, -8,
        NOTE_AS4, 16, NOTE_A4, -8, NOTE_AS4, 16, NOTE_A4, -8, NOTE_AS4, 16, NOTE_A4, -8, NOTE_AS4, 16, NOTE_A4, -8,
        NOTE_G4, -16, NOTE_E4, -16, NOTE_D4, -16, NOTE_E4, 16, NOTE_E4, 16, NOTE_E4, 2,
    ],
    'tetris_theme': [
        NOTE_E5, 4, NOTE_B4, 8, NOTE_C5, 8, NOTE_D5, 4, NOTE_C5, 8, NOTE_B4, 8,
        NOTE_A4, 4, NOTE_A4, 8, NOTE_C5, 8, NOTE_E5, 4, NOTE_D5, 8, NOTE_C5, 8,
        NOTE_B4, -4, NOTE_C5, 8, NOTE_D5, 4, NOTE_E5, 4,
        NOTE_C5, 4, NOTE_A4, 4, NOTE_A4, 8, NOTE_A4, 4, NOTE_B4, 8, NOTE_C5, 8,

        NOTE_D5, -4, NOTE_F5, 8, NOTE_A5, 4, NOTE_G5, 8, NOTE_F5, 8,
        NOTE_E5, -4, NOTE_C5, 8, NOTE_E5, 4, NOTE_D5, 8, NOTE_C5, 8,
        NOTE_B4, 4, NOTE_B4, 8, NOTE_C5, 8, NOTE_D5, 4, NOTE_E5, 4,
        NOTE_C5, 4, NOTE_A4, 4, NOTE_A4, 4, REST, 4,

        NOTE_E5, 4, NOTE_B4, 8, NOTE_C5, 8, NOTE_D5, 4, NOTE_C5, 8, NOTE_B4, 8,
        NOTE_A4, 4, NOTE_A4, 8, NOTE_C5, 8, NOTE_E5, 4, NOTE_D5, 8, NOTE_C5, 8,
        NOTE_B4, -4, NOTE_C5, 8, NOTE_D5, 4, NOTE_E5, 4,
        NOTE_C5, 4, NOTE_A4, 4, NOTE_A4, 8, NOTE_A4, 4, NOTE_B4, 8, NOTE_C5, 8,

        NOTE_D5, -4, NOTE_F5, 8, NOTE_A5, 4, NOTE_G5, 8, NOTE_F5, 8,
        NOTE_E5, -4, NOTE_C5, 8, NOTE_E5, 4, NOTE_D5, 8, NOTE_C5, 8,
        NOTE_B4, 4, NOTE_B4, 8, NOTE_C5, 8, NOTE_D5, 4, NOTE_E5, 4,
        NOTE_C5, 4, NOTE_A4, 4, NOTE_A4, 4, REST, 4,

        NOTE_E5, 2, NOTE_C5, 2,
        NOTE_D5, 2, NOTE_B4, 2,
        NOTE_C5, 2, NOTE_A4, 2,
        NOTE_GS4, 2, NOTE_B4, 4, REST, 8,
        NOTE_E5, 2, NOTE_C5, 2,
        NOTE_D5, 2, NOTE_B4, 2,
        NOTE_C5, 4, NOTE_E5, 4, NOTE_A5, 2,
        NOTE_GS5, 2,
    ],
    'super_mario_theme': [
        NOTE_E5, 8, NOTE_E5, 8, REST, 8, NOTE_E5, 8, REST, 8, NOTE_C5, 8, NOTE_E5, 8,
        NOTE_G5, 4, REST, 4, NOTE_G4, 8, REST, 4,
        NOTE_C5, -4, NOTE_G4, 8, REST, 4, NOTE_E4, -4,
        NOTE_A4, 4, NOTE_B4, 4, NOTE_AS4, 8, NOTE_A4, 4,
        NOTE_G4, -8, NOTE_E5, -8, NOTE_G5, -8, NOTE_A5, 4, NOTE_F5, 8, NOTE_G5, 8,
        REST, 8, NOTE_E5, 4, NOTE_C5, 8, NOTE_D5, 8, NOTE_B4, -4,
        NOTE_C5, -4, NOTE_G4, 8, REST, 4, NOTE_E4, -4,
        NOTE_A4, 4, NOTE_B4, 4, NOTE_AS4, 8, NOTE_A4, 4,
        NOTE_G4, -8, NOTE_E5, -8, NOTE_G5, -8, NOTE_A5, 4, NOTE_F5, 8, NOTE_G5, 8,
        REST, 8, NOTE_E5, 4, NOTE_C5, 8, NOTE_D5, 8, NOTE_B4, -4,

        REST, 4, NOTE_G5, 8, NOTE_FS5, 8, NOTE_F5, 8, NOTE_DS5, 4, NOTE_E5, 8,
        REST, 8, NOTE_GS4, 8, NOTE_A4, 8, NOTE_C4, 8, REST, 8, NOTE_A4, 8, NOTE_C5, 8, NOTE_D5, 8,
        REST, 4, NOTE_DS5, 4, REST, 8, NOTE_D5, -4,
        NOTE_C5, 2, REST, 2,

        REST, 4, NOTE_G5, 8, NOTE_FS5, 8, NOTE_F5, 8, NOTE_DS5, 4, NOTE_E5, 8,
        REST, 8, NOTE_GS4, 8, NOTE_A4, 8, NOTE_C4, 8, REST, 8, NOTE_A4, 8, NOTE_C5, 8, NOTE_D5, 8,
        REST, 4, NOTE_DS5, 4, REST, 8, NOTE_D5, -4,
        NOTE_C5, 2, REST, 2,

        NOTE_C5, 8, NOTE_C5, 4, NOTE_C5, 8, REST, 8, NOTE_C5, 8, NOTE_D5, 4,
        NOTE_E5, 8, NOTE_C5, 4, NOTE_A4, 8, NOTE_G4, 2,

        NOTE_C5, 8, NOTE_C5, 4, NOTE_C5, 8, REST, 8, NOTE_C5, 8, NOTE_D5, 8, NOTE_E5, 8,
        REST, 1,
        NOTE_C5, 8, NOTE_C5, 4, NOTE_C5, 8, REST, 8, NOTE_C5, 8, NOTE_D5, 4,
        NOTE_E5, 8, NOTE_C5, 4, NOTE_A4, 8, NOTE_G4, 2,
        NOTE_E5, 8, NOTE_E5, 8, REST, 8, NOTE_E5, 8, REST, 8, NOTE_C5, 8, NOTE_E5, 4,
        NOTE_G5, 4, REST, 4, NOTE_G4, 4, REST, 4,
        NOTE_C5, -4, NOTE_G4, 8, REST, 4, NOTE_E4, -4,
        
        NOTE_A4, 4, NOTE_B4, 4, NOTE_AS4, 8, NOTE_A4, 4,
        NOTE_G4, -8, NOTE_E5, -8, NOTE_G5, -8, NOTE_A5, 4, NOTE_F5, 8, NOTE_G5, 8,
        REST, 8, NOTE_E5, 4, NOTE_C5, 8, NOTE_D5, 8, NOTE_B4, -4,

        NOTE_C5, -4, NOTE_G4, 8, REST, 4, NOTE_E4, -4,
        NOTE_A4, 4, NOTE_B4, 4, NOTE_AS4, 8, NOTE_A4, 4,
        NOTE_G4, -8, NOTE_E5, -8, NOTE_G5, -8, NOTE_A5, 4, NOTE_F5, 8, NOTE_G5, 8,
        REST, 8, NOTE_E5, 4, NOTE_C5, 8, NOTE_D5, 8, NOTE_B4, -4,

        NOTE_E5, 8, NOTE_C5, 4, NOTE_G4, 8, REST, 4, NOTE_GS4, 4,
        NOTE_A4, 8, NOTE_F5, 4, NOTE_F5, 8, NOTE_A4, 2,
        NOTE_D5, -8, NOTE_A5, -8, NOTE_A5, -8, NOTE_A5, -8, NOTE_G5, -8, NOTE_F5, -8,
        
        NOTE_E5, 8, NOTE_C5, 4, NOTE_A4, 8, NOTE_G4, 2,
        NOTE_E5, 8, NOTE_C5, 4, NOTE_G4, 8, REST, 4, NOTE_GS4, 4,
        NOTE_A4, 8, NOTE_F5, 4, NOTE_F5, 8, NOTE_A4, 2,
        NOTE_B4, 8, NOTE_F5, 4, NOTE_F5, 8, NOTE_F5, -8, NOTE_E5, -8, NOTE_D5, -8,
        NOTE_C5, 8, NOTE_E4, 4, NOTE_E4, 8, NOTE_C4, 2,

        NOTE_E5, 8, NOTE_C5, 4, NOTE_G4, 8, REST, 4, NOTE_GS4, 4,
        NOTE_A4, 8, NOTE_F5, 4, NOTE_F5, 8, NOTE_A4, 2,
        NOTE_D5, -8, NOTE_A5, -8, NOTE_A5, -8, NOTE_A5, -8, NOTE_G5, -8, NOTE_F5, -8,
        
        NOTE_E5, 8, NOTE_C5, 4, NOTE_A4, 8, NOTE_G4, 2,
        NOTE_E5, 8, NOTE_C5, 4, NOTE_G4, 8, REST, 4, NOTE_GS4, 4,
        NOTE_A4, 8, NOTE_F5, 4, NOTE_F5, 8, NOTE_A4, 2,
        NOTE_B4, 8, NOTE_F5, 4, NOTE_F5, 8, NOTE_F5, -8, NOTE_E5, -8, NOTE_D5, -8,
        NOTE_C5, 8, NOTE_E4, 4, NOTE_E4, 8, NOTE_C4, 2,
        NOTE_C5, 8, NOTE_C5, 4, NOTE_C5, 8, REST, 8, NOTE_C5, 8, NOTE_D5, 8, NOTE_E5, 8,
        REST, 1,

        NOTE_C5, 8, NOTE_C5, 4, NOTE_C5, 8, REST, 8, NOTE_C5, 8, NOTE_D5, 4,
        NOTE_E5, 8, NOTE_C5, 4, NOTE_A4, 8, NOTE_G4, 2,
        NOTE_E5, 8, NOTE_E5, 8, REST, 8, NOTE_E5, 8, REST, 8, NOTE_C5, 8, NOTE_E5, 4,
        NOTE_G5, 4, REST, 4, NOTE_G4, 4, REST, 4,
        NOTE_E5, 8, NOTE_C5, 4, NOTE_G4, 8, REST, 4, NOTE_GS4, 4,
        NOTE_A4, 8, NOTE_F5, 4, NOTE_F5, 8, NOTE_A4, 2,
        NOTE_D5, -8, NOTE_A5, -8, NOTE_A5, -8, NOTE_A5, -8, NOTE_G5, -8, NOTE_F5, -8,
        
        NOTE_E5, 8, NOTE_C5, 4, NOTE_A4, 8, NOTE_G4, 2,
        NOTE_E5, 8, NOTE_C5, 4, NOTE_G4, 8, REST, 4, NOTE_GS4, 4,
        NOTE_A4, 8, NOTE_F5, 4, NOTE_F5, 8, NOTE_A4, 2,
        NOTE_B4, 8, NOTE_F5, 4, NOTE_F5, 8, NOTE_F5, -8, NOTE_E5, -8, NOTE_D5, -8,
        NOTE_C5, 8, NOTE_E4, 4, NOTE_E4, 8, NOTE_C4, 2,
        
        # Game over sound
        NOTE_C5, -4, NOTE_G4, -4, NOTE_E4, 4,
        NOTE_A4, -8, NOTE_B4, -8, NOTE_A4, -8, NOTE_GS4, -8, NOTE_AS4, -8, NOTE_GS4, -8,
        NOTE_G4, 8, NOTE_D4, 8, NOTE_E4, -2,
    ],
    'song_of_storms': [
        NOTE_D4, 4, NOTE_A4, 4, NOTE_A4, 4,
        REST, 8, NOTE_E4, 8, NOTE_B4, 2,
        NOTE_F4, 4, NOTE_C5, 4, NOTE_C5, 4,
        REST, 8, NOTE_E4, 8, NOTE_B4, 2,
        NOTE_D4, 4, NOTE_A4, 4, NOTE_A4, 4,
        REST, 8, NOTE_E4, 8, NOTE_B4, 2,
        NOTE_F4, 4, NOTE_C5, 4, NOTE_C5, 4,
        REST, 8, NOTE_E4, 8, NOTE_B4, 2,
        NOTE_D4, 8, NOTE_F4, 8, NOTE_D5, 2,
        
        NOTE_D4, 8, NOTE_F4, 8, NOTE_D5, 2,
        NOTE_E5, -4, NOTE_F5, 8, NOTE_E5, 8, NOTE_E5, 8,
        NOTE_E5, 8, NOTE_C5, 8, NOTE_A4, 2,
        NOTE_A4, 4, NOTE_D4, 4, NOTE_F4, 8, NOTE_G4, 8,
        NOTE_A4, -2,
        NOTE_A4, 4, NOTE_D4, 4, NOTE_F4, 8, NOTE_G4, 8,
        NOTE_E4, -2,
        NOTE_D4, 8, NOTE_F4, 8, NOTE_D5, 2,
        NOTE_D4, 8, NOTE_F4, 8, NOTE_D5, 2,

        NOTE_E5, -4, NOTE_F5, 8, NOTE_E5, 8, NOTE_E5, 8,
        NOTE_E5, 8, NOTE_C5, 8, NOTE_A4, 2,
        NOTE_A4, 4, NOTE_D4, 4, NOTE_F4, 8, NOTE_G4, 8,
        NOTE_A4, 2, NOTE_A4, 4,
        NOTE_D4, 1,
    ],
    'asa_branca': [
      NOTE_G4, 8, NOTE_A4, 8, NOTE_B4, 4, NOTE_D5, 4, NOTE_D5, 4, NOTE_B4, 4, 
      NOTE_C5, 4, NOTE_C5, 2, NOTE_G4, 8, NOTE_A4, 8,
      NOTE_B4, 4, NOTE_D5, 4, NOTE_D5, 4, NOTE_C5, 4,
      NOTE_B4, 2, REST, 8, NOTE_G4, 8, NOTE_G4, 8, NOTE_A4, 8,
      NOTE_B4, 4, NOTE_D5, 4, REST, 8, NOTE_D5, 8, NOTE_C5, 8, NOTE_B4, 8,
      NOTE_G4, 4, NOTE_C5, 4, REST, 8, NOTE_C5, 8, NOTE_B4, 8, NOTE_A4, 8,
      NOTE_A4, 4, NOTE_B4, 4, REST, 8, NOTE_B4, 8, NOTE_A4, 8, NOTE_G4, 8,
      NOTE_G4, 2, REST, 8, NOTE_G4, 8, NOTE_G4, 8, NOTE_A4, 8,
      NOTE_B4, 4, NOTE_D5, 4, REST, 8, NOTE_D5, 8, NOTE_C5, 8, NOTE_B4, 8,
      NOTE_G4, 4, NOTE_C5, 4, REST, 8, NOTE_C5, 8, NOTE_B4, 8, NOTE_A4, 8,
      NOTE_A4, 4, NOTE_B4, 4, REST, 8, NOTE_B4, 8, NOTE_A4, 8, NOTE_G4, 8,
      NOTE_G4, 4, NOTE_F5, 8, NOTE_D5, 8, NOTE_E5, 8, NOTE_C5, 8, NOTE_D5, 8, NOTE_B4, 8,
      NOTE_C5, 8, NOTE_A4, 8, NOTE_B4, 8, NOTE_G4, 8, NOTE_A4, 8, NOTE_G4, 8, NOTE_E4, 8, NOTE_G4, 8,
      NOTE_G4, 4, NOTE_F5, 8, NOTE_D5, 8, NOTE_E5, 8, NOTE_C5, 8, NOTE_D5, 8, NOTE_B4, 8,
      NOTE_C5, 8, NOTE_A4, 8, NOTE_B4, 8, NOTE_G4, 8, NOTE_A4, 8, NOTE_G4, 8, NOTE_E4, 8, NOTE_G4, 8,
      NOTE_G4, -2, REST, 4
    ],
    'baby_elephant_walk': [
      NOTE_C4, -8, NOTE_E4, 16, NOTE_G4, 8, NOTE_C5, 8, NOTE_E5, 8, NOTE_D5, 8, NOTE_C5, 8, NOTE_A4, 8,
      NOTE_FS4, 8, NOTE_G4, 8, REST, 4, REST, 2,
      NOTE_C4, -8, NOTE_E4, 16, NOTE_G4, 8, NOTE_C5, 8, NOTE_E5, 8, NOTE_D5, 8, NOTE_C5, 8, NOTE_A4, 8,
      NOTE_G4, -2, NOTE_A4, 8, NOTE_DS4, 1,
      NOTE_A4, 8,
      NOTE_E4, 8, NOTE_C4, 8, REST, 4, REST, 2,
      NOTE_C4, -8, NOTE_E4, 16, NOTE_G4, 8, NOTE_C5, 8, NOTE_E5, 8, NOTE_D5, 8, NOTE_C5, 8, NOTE_A4, 8,
      NOTE_FS4, 8, NOTE_G4, 8, REST, 4, REST, 4, REST, 8, NOTE_G4, 8,
      NOTE_D5, 4, NOTE_D5, 4, NOTE_B4, 8, NOTE_G4, 8, REST, 8, NOTE_G4, 8,
      NOTE_C5, 4, NOTE_C5, 4, NOTE_AS4, 16, NOTE_C5, 16, NOTE_AS4, 16, NOTE_G4, 16, NOTE_F4, 8, NOTE_DS4, 8,
      NOTE_FS4, 4, NOTE_FS4, 4, NOTE_F4, 16, NOTE_G4, 16, NOTE_F4, 16, NOTE_DS4, 16, NOTE_C4, 8, NOTE_G4, 8,
      NOTE_AS4, 8, NOTE_C5, 8, REST, 4, REST, 2,
    ],
    'bloody_tears': [
        REST, 4, NOTE_G5, 4, NOTE_A5, 4, NOTE_AS5, 4, NOTE_A5, 4, NOTE_F5, 4, NOTE_A5, 4, NOTE_G5, 4,
        REST, 4, NOTE_G5, 4, NOTE_A5, 4, NOTE_AS5, 4, NOTE_C6, 4, NOTE_AS5, 4, NOTE_A5, 4, NOTE_G5, 4,
        REST, 4, NOTE_G5, 4, NOTE_A5, 4, NOTE_AS5, 4, NOTE_A5, 4, NOTE_F5, 4, NOTE_A5, 4, NOTE_G5, 4,
        NOTE_D6, 4, REST, 8, NOTE_C6, 8, REST, 4, NOTE_AS5, 4, NOTE_A5, 4, NOTE_AS5, 8, NOTE_C6, 8,
        NOTE_F6, 8, REST, 8, REST, 4, NOTE_G5, 16, NOTE_D5, 16, NOTE_D6, 16, NOTE_D5, 16, NOTE_C6, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16,
        NOTE_A5, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16, NOTE_A5, 16, NOTE_D5, 16, NOTE_G5, 16, NOTE_D5, 16,
        NOTE_A5, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16, NOTE_C6, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16,
        NOTE_A5, 16, NOTE_D5, 16, NOTE_F5, 16, NOTE_D5, 16, NOTE_A5, 16, NOTE_D5, 16, NOTE_G5, 16, NOTE_D5, 16,
        NOTE_G5, 16, NOTE_D5, 16, NOTE_D6, 16, NOTE_D5, 16, NOTE_C6, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16,
        NOTE_A5, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16, NOTE_A5, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16,
        NOTE_A5, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16, NOTE_C6, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16,
        NOTE_A5, 16, NOTE_D5, 16, NOTE_F5, 16, NOTE_D5, 16, NOTE_A5, 16, NOTE_D5, 16, NOTE_G5, 16, NOTE_D5, 16,
        NOTE_AS5, 16, NOTE_D5, 16, NOTE_D6, 16, NOTE_D5, 16, NOTE_C6, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16,
        NOTE_A5, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16, NOTE_A5, 16, NOTE_D5, 16, NOTE_G5, 16, NOTE_D5, 16,
        NOTE_A5, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16, NOTE_C6, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16,
        NOTE_A5, 16, NOTE_D5, 16, NOTE_F5, 16, NOTE_D5, 16, NOTE_A5, 16, NOTE_D5, 16, NOTE_G5, 16, NOTE_D5, 16,
        NOTE_G5, 16, NOTE_D5, 16, NOTE_D6, 16, NOTE_D5, 16, NOTE_C6, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16,
        NOTE_A5, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16, NOTE_A5, 16, NOTE_D5, 16, NOTE_G5, 16, NOTE_D5, 16,
        NOTE_A5, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16, NOTE_C6, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16,
        NOTE_A5, 16, NOTE_D5, 16, NOTE_F5, 16, NOTE_D5, 16, NOTE_A5, 16, NOTE_D5, 16, NOTE_G5, 16, NOTE_D5, 16,
        NOTE_C6, 16, NOTE_C6, 16, NOTE_F6, 16, NOTE_D6, 8, REST, 16, REST, 8, REST, 4, NOTE_C6, 16, NOTE_AS5, 16,
        NOTE_C6, -8, NOTE_F6, -8, NOTE_D6, -4, NOTE_C6, 8, NOTE_AS5, 8, NOTE_C6, 8, NOTE_F6, 16, NOTE_D6, 8, REST, 16, REST, 8, REST, 4,
        NOTE_C6, 8, NOTE_D6, 8, NOTE_DS6, -8, NOTE_F6, -8, NOTE_D6, -8, REST, 16, NOTE_DS6, 8, REST, 8, NOTE_C6, 8, NOTE_F6, 16, NOTE_D6, 8, REST, 16, REST, 8,
        REST, 4, NOTE_C6, 8, NOTE_AS5, 8, NOTE_C6, -8, NOTE_F6, -8, NOTE_D6, -4, NOTE_C6, 8, NOTE_AS5, 8, NOTE_C6, 8, NOTE_F6, 16, NOTE_D6, 8, REST, 16, REST, 8,
        REST, 4, NOTE_C6, 8, NOTE_D6, 8, NOTE_DS6, -8, NOTE_F6, -8, NOTE_D5, 8, NOTE_FS5, 8, NOTE_F5, 8, NOTE_A5, 8,
        NOTE_A5, -8, NOTE_G5, -4, NOTE_A5, -8, NOTE_G5, -4, NOTE_A5, -8, NOTE_G5, -4, NOTE_AS5, 8, NOTE_A5, 8, NOTE_G5, 8, NOTE_F5, 8, NOTE_A5, -8, NOTE_G5, -8, NOTE_D5, 8,
        NOTE_A5, -8, NOTE_G5, -8, NOTE_D5, 8, NOTE_A5, -8, NOTE_G5, -8, NOTE_D5, 8, NOTE_AS5, 4, NOTE_C6, 4, NOTE_A5, 4, NOTE_AS5, 4,
        NOTE_G5, 16, NOTE_D5, 16, NOTE_D6, 16, NOTE_D5, 16, NOTE_C6, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16, NOTE_A5, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16, NOTE_A5, 16, NOTE_D5, 16, NOTE_G5, 16, NOTE_D5, 16,
        NOTE_A5, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16, NOTE_C6, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16, NOTE_A5, 16, NOTE_D5, 16, NOTE_F5, 16, NOTE_D5, 16, NOTE_A5, 16, NOTE_D5, 16, NOTE_G5, 16, NOTE_D5, 16,
        NOTE_G5, 16, NOTE_D5, 16, NOTE_D6, 16, NOTE_D5, 16, NOTE_C6, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16, NOTE_A5, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16, NOTE_A5, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16,
        NOTE_A5, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16, NOTE_C6, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16, NOTE_A5, 16, NOTE_D5, 16, NOTE_F5, 16, NOTE_D5, 16, NOTE_A5, 16, NOTE_D5, 16, NOTE_G5, 16, NOTE_D5, 16,
        NOTE_G5, 16, NOTE_D5, 16, NOTE_D6, 16, NOTE_D5, 16, NOTE_C6, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16, NOTE_A5, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16, NOTE_A5, 16, NOTE_D5, 16, NOTE_G5, 16, NOTE_D5, 16,
        NOTE_A5, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16, NOTE_C6, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16, NOTE_A5, 16, NOTE_D5, 16, NOTE_F5, 16, NOTE_D5, 16, NOTE_A5, 16, NOTE_D5, 16, NOTE_G5, 16, NOTE_D5, 16,
        NOTE_AS5, 16, NOTE_D5, 16, NOTE_D6, 16, NOTE_D5, 16, NOTE_C6, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16, NOTE_A5, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16, NOTE_A5, 16, NOTE_D5, 16, NOTE_G5, 16, NOTE_D5, 16,
        NOTE_A5, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16, NOTE_A5, 16, NOTE_D5, 16, NOTE_G5, 16, NOTE_D5, 16, NOTE_A5, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16, NOTE_C6, 16, NOTE_D5, 16, NOTE_AS5, 16, NOTE_D5, 16,
        NOTE_A5, 16, NOTE_D5, 16, NOTE_F5, 16, NOTE_D5, 16, NOTE_A5, 8, NOTE_G5, 32, NOTE_A5, 32, NOTE_AS5, 32, NOTE_C6, 32,
        NOTE_D6, 16, NOTE_G5, 16, NOTE_AS5, 16, NOTE_G5, 16, NOTE_C6, 16, NOTE_G5, 16, NOTE_D6, 16, NOTE_G5, 16, NOTE_C6, 16, NOTE_G5, 16, NOTE_A5, 16, NOTE_G5, 16, NOTE_F6, 16, NOTE_G5, 16, NOTE_D6, 16, NOTE_DS5, 16,
        NOTE_D6, 4, REST, 4, NOTE_C5, 8, REST, 8, NOTE_A4, -16, NOTE_AS4, -16, NOTE_C5, 16, NOTE_D6, 16, NOTE_G4, 16, NOTE_AS4, 16, NOTE_G4, 16, NOTE_C5, 16, NOTE_G4, 16, NOTE_D6, 16, NOTE_G4, 16, NOTE_C6, 16, NOTE_F4, 16,
        NOTE_A4, 16, NOTE_F4, 16, NOTE_F5, 16, NOTE_F4, 16, NOTE_D6, 16, NOTE_DS4, 16, NOTE_D6, 16, REST, 8, NOTE_E4, 16, NOTE_F4, 16, NOTE_GS4, 8, REST, 8, NOTE_AS4, 8, REST, 8, NOTE_DS5, 16, NOTE_GS4, 16, NOTE_B4, 16,
        NOTE_GS4, 16, NOTE_CS5, 16, NOTE_GS4, 16, NOTE_DS5, 16, NOTE_GS4, 16, NOTE_CS5, 16, NOTE_FS4, 16, NOTE_AS4, 16, NOTE_FS4, 16, NOTE_FS5, 16, NOTE_FS4, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_D5, 4, REST, 4, NOTE_CS5, 8,
        REST, 8, NOTE_AS4, -16, NOTE_B4, -16, NOTE_CS5, 16, NOTE_DS5, 16, NOTE_GS4, 16, NOTE_B4, 16, NOTE_GS4, 16, NOTE_CS5, 16, NOTE_GS4, 16, NOTE_DS5, 16, NOTE_GS4, 16, NOTE_CS5, 16, NOTE_FS4, 16, NOTE_AS4, 16, NOTE_FS4, 16,
        NOTE_FS5, 16, NOTE_FS4, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_DS5, 4, REST, 8, NOTE_DS5, 16, NOTE_E5, 16, NOTE_FS5, 16, NOTE_CS5, 16, NOTE_E5, 16, NOTE_CS4, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_G5, 16, NOTE_AS5, 16,
        NOTE_GS5, 16, NOTE_DS5, 16, NOTE_DS6, 16, NOTE_DS5, 16, NOTE_CS6, 16, NOTE_DS5, 16, NOTE_B5, 16, NOTE_DS5, 16, NOTE_AS5, 16, NOTE_DS5, 16, NOTE_B5, 16, NOTE_DS5, 16, NOTE_AS5, 16, NOTE_DS5, 16, NOTE_GS5, 16, NOTE_DS5, 16,
        NOTE_AS5, 16, NOTE_DS5, 16, NOTE_B5, 16, NOTE_DS5, 16, NOTE_CS6, 16, NOTE_DS5, 16, NOTE_B5, 16, NOTE_DS5, 16, NOTE_AS5, 16, NOTE_DS5, 16, NOTE_FS5, 16, NOTE_DS5, 16, NOTE_AS5, 16, NOTE_DS5, 16, NOTE_GS5, 16, NOTE_DS5, 16,
        NOTE_GS5, 16, NOTE_DS5, 16, NOTE_DS6, 16, NOTE_DS5, 16, NOTE_CS6, 16, NOTE_DS5, 16, NOTE_B5, 16, NOTE_DS5, 16, NOTE_AS5, 16, NOTE_DS5, 16, NOTE_B5, 16, NOTE_DS5, 16, NOTE_AS5, 16, NOTE_DS5, 16, NOTE_GS5, 16, NOTE_DS5, 16,
        NOTE_AS5, 16, NOTE_DS5, 16, NOTE_B5, 16, NOTE_DS5, 16, NOTE_CS6, 16, NOTE_DS5, 16, NOTE_B5, 16, NOTE_DS5, 16, NOTE_AS5, 16, NOTE_DS5, 16, NOTE_FS5, 16, NOTE_DS5, 16, NOTE_AS5, 16, NOTE_DS5, 16, NOTE_GS5, 16, NOTE_DS5, 16,
        NOTE_GS5, 16, NOTE_DS5, 16, NOTE_DS6, 16, NOTE_DS5, 16, NOTE_CS6, 16, NOTE_DS5, 16, NOTE_B5, 16, NOTE_DS5, 16, NOTE_AS5, 16, NOTE_DS5, 16, NOTE_B5, 16, NOTE_DS5, 16, NOTE_AS5, 16, NOTE_DS5, 16, NOTE_GS5, 16, NOTE_DS5, 16,
        NOTE_AS5, 16, NOTE_DS5, 16, NOTE_B5, 16, NOTE_DS5, 16, NOTE_CS6, 16, NOTE_DS5, 16, NOTE_B5, 16, NOTE_DS5, 16, NOTE_AS5, 16, NOTE_DS5, 16, NOTE_FS5, 16, NOTE_DS5, 16, NOTE_AS5, 16, NOTE_DS5, 16, NOTE_GS5, 16, NOTE_DS5, 16,
        NOTE_GS5, 16, NOTE_DS5, 16, NOTE_DS6, 16, NOTE_DS5, 16, NOTE_CS6, 16, NOTE_DS5, 16, NOTE_B5, 16, NOTE_DS5, 16, NOTE_AS5, 16, NOTE_DS5, 16, NOTE_B5, 16, NOTE_DS5, 16, NOTE_AS5, 16, NOTE_DS5, 16, NOTE_GS5, 16, NOTE_DS5, 16,
        NOTE_CS6, 8, NOTE_FS6, 16, NOTE_DS6, 8, REST, 16, REST, 8, REST, 4, NOTE_CS6, 8, NOTE_B5, 8, NOTE_CS6, -8, NOTE_FS6, -8, NOTE_DS6, -4, NOTE_CS6, 8, NOTE_B5, 8, NOTE_CS6, 8, NOTE_FS6, 16, NOTE_DS6, 8, REST, 16, REST, 8,
        REST, 4, NOTE_CS6, 8, NOTE_B5, 8, NOTE_E6, -8, NOTE_F6, -8, NOTE_DS6, -8, REST, 16, NOTE_E6, 8, REST, 16, REST, 16, NOTE_CS6, 8, NOTE_FS6, 16, NOTE_DS6, 8, REST, 16, REST, 8, REST, 4, NOTE_CS6, 8, NOTE_B5, 8,
        NOTE_CS6, -8, NOTE_FS6, -8, NOTE_DS6, -4, NOTE_CS6, 8, NOTE_B5, 8, NOTE_CS6, 8, NOTE_FS6, 16, NOTE_DS6, 8, REST, 16, REST, 8, REST, 4, NOTE_CS6, 8, NOTE_DS5, 8, NOTE_E5, -8, NOTE_F5, -8, NOTE_DS5, 8, NOTE_G5, 8,
        NOTE_GS5, 8, NOTE_AS5, 8, NOTE_AS5, -8, NOTE_GS5, -8, NOTE_AS5, -8, NOTE_GS5, -8, NOTE_AS5, -8, NOTE_GS5, -8, NOTE_B6, 8, NOTE_AS5, 8, NOTE_GS5, 8, NOTE_FS5, 8, NOTE_AS5, -8, NOTE_GS6, -8, NOTE_DS5, 8, NOTE_AS5, -8,
        NOTE_GS6, -8, NOTE_DS5, 8, NOTE_AS5, -8, NOTE_GS6, -8, NOTE_DS5, 8, NOTE_B5, 8, NOTE_CS6, 8, NOTE_AS5, 8, NOTE_B5, 8, NOTE_GS5, 8, REST, 8, REST, 16
    ],
    'brahms_lullaby': [
        NOTE_G4, 4, NOTE_G4, 4,
        NOTE_AS4, -4, NOTE_G4, 8, NOTE_G4, 4,
        NOTE_AS4, 4, REST, 4, NOTE_G4, 8, NOTE_AS4, 8,
        NOTE_DS5, 4, NOTE_D5, -4, NOTE_C5, 8,
        NOTE_C5, 4, NOTE_AS4, 4, NOTE_F4, 8, NOTE_G4, 8,
        NOTE_GS4, 4, NOTE_F4, 4, NOTE_F4, 8, NOTE_G4, 8,
        NOTE_GS4, 4, REST, 4, NOTE_F4, 8, NOTE_GS4, 8,
        NOTE_D5, 8, NOTE_C5, 8, NOTE_AS4, 4, NOTE_D5, 4,
        NOTE_DS5, 4, REST, 4, NOTE_DS4, 8, NOTE_DS4, 8,
        NOTE_DS5, 2, NOTE_C5, 8, NOTE_GS4, 8,
        NOTE_AS4, 2, NOTE_G4, 8, NOTE_DS4, 8,
        NOTE_GS4, 4, NOTE_AS4, 4, NOTE_C5, 4,
        NOTE_AS4, 2, NOTE_DS4, 8, NOTE_DS4, 8,
        NOTE_DS5, 2, NOTE_C5, 8, NOTE_GS4, 8,
        NOTE_AS4, 2, NOTE_G4, 8, NOTE_DS4, 8,
        NOTE_AS4, 4, NOTE_G4, 4, NOTE_DS4, 4,
        NOTE_DS4, 2
    ],
    'pachelbels_canon': [
        NOTE_FS4, 2, NOTE_E4, 2,
        NOTE_D4, 2, NOTE_CS4, 2,
        NOTE_B3, 2, NOTE_A3, 2,
        NOTE_B3, 2, NOTE_CS4, 2,
        NOTE_FS4, 2, NOTE_E4, 2,
        NOTE_D4, 2, NOTE_CS4, 2,
        NOTE_B3, 2, NOTE_A3, 2,
        NOTE_B3, 2, NOTE_CS4, 2,
        NOTE_D4, 2, NOTE_CS4, 2,
        NOTE_B3, 2, NOTE_A3, 2,
        NOTE_G3, 2, NOTE_FS3, 2,
        NOTE_G3, 2, NOTE_A3, 2,
        NOTE_D4, 4, NOTE_FS4, 8, NOTE_G4, 8, NOTE_A4, 4, NOTE_FS4, 8, NOTE_G4, 8,
        NOTE_A4, 4, NOTE_B3, 8, NOTE_CS4, 8, NOTE_D4, 8, NOTE_E4, 8, NOTE_FS4, 8, NOTE_G4, 8,
        NOTE_FS4, 4, NOTE_D4, 8, NOTE_E4, 8, NOTE_FS4, 4, NOTE_FS3, 8, NOTE_G3, 8,
        NOTE_A3, 8, NOTE_G3, 8, NOTE_FS3, 8, NOTE_G3, 8, NOTE_A3, 2,
        NOTE_G3, 4, NOTE_B3, 8, NOTE_A3, 8, NOTE_G3, 4, NOTE_FS3, 8, NOTE_E3, 8,
        NOTE_FS3, 4, NOTE_D3, 8, NOTE_E3, 8, NOTE_FS3, 8, NOTE_G3, 8, NOTE_A3, 8, NOTE_B3, 8,
        NOTE_G3, 4, NOTE_B3, 8, NOTE_A3, 8, NOTE_B3, 4, NOTE_CS4, 8, NOTE_D4, 8,
        NOTE_A3, 8, NOTE_B3, 8, NOTE_CS4, 8, NOTE_D4, 8, NOTE_E4, 8, NOTE_FS4, 8, NOTE_G4, 8, NOTE_A4, 2,
        NOTE_A4, 4, NOTE_FS4, 8, NOTE_G4, 8, NOTE_A4, 4,
        NOTE_FS4, 8, NOTE_G4, 8, NOTE_A4, 8, NOTE_A3, 8, NOTE_B3, 8, NOTE_CS4, 8,
        NOTE_D4, 8, NOTE_E4, 8, NOTE_FS4, 8, NOTE_G4, 8, NOTE_FS4, 4, NOTE_D4, 8, NOTE_E4, 8,
        NOTE_FS4, 8, NOTE_CS4, 8, NOTE_A3, 8, NOTE_A3, 8,
        NOTE_CS4, 4, NOTE_B3, 4, NOTE_D4, 8, NOTE_CS4, 8, NOTE_B3, 4,
        NOTE_A3, 8, NOTE_G3, 8, NOTE_A3, 4, NOTE_D3, 8, NOTE_E3, 8, NOTE_FS3, 8, NOTE_G3, 8,
        NOTE_A3, 8, NOTE_B3, 4, NOTE_G3, 4, NOTE_B3, 8, NOTE_A3, 8, NOTE_B3, 4,
        NOTE_CS4, 8, NOTE_D4, 8, NOTE_A3, 8, NOTE_B3, 8, NOTE_CS4, 8, NOTE_D4, 8, NOTE_E4, 8,
        NOTE_FS4, 8, NOTE_G4, 8, NOTE_A4, 2,
    ],
    'cantina_band': [
        NOTE_B4, -4, NOTE_E5, -4, NOTE_B4, -4, NOTE_E5, -4,
        NOTE_B4, 8, NOTE_E5, -4, NOTE_B4, 8, REST, 8, NOTE_AS4, 8, NOTE_B4, 8,
        NOTE_B4, 8, NOTE_AS4, 8, NOTE_B4, 8, NOTE_A4, 8, REST, 8, NOTE_GS4, 8, NOTE_A4, 8, NOTE_G4, 8,
        NOTE_G4, 4, NOTE_E4, -2,
        NOTE_B4, -4, NOTE_E5, -4, NOTE_B4, -4, NOTE_E5, -4,
        NOTE_B4, 8, NOTE_E5, -4, NOTE_B4, 8, REST, 8, NOTE_AS4, 8, NOTE_B4, 8,
        NOTE_A4, -4, NOTE_A4, -4, NOTE_GS4, 8, NOTE_A4, -4,
        NOTE_D5, 8, NOTE_C5, -4, NOTE_B4, -4, NOTE_A4, -4,
        NOTE_B4, -4, NOTE_E5, -4, NOTE_B4, -4, NOTE_E5, -4,
        NOTE_B4, 8, NOTE_E5, -4, NOTE_B4, 8, REST, 8, NOTE_AS4, 8, NOTE_B4, 8,
        NOTE_D5, 4, NOTE_D5, -4, NOTE_B4, 8, NOTE_A4, -4,
        NOTE_G4, -4, NOTE_E4, -2,
        NOTE_E4, 2, NOTE_G4, 2,
        NOTE_B4, 2, NOTE_D5, 2,
        NOTE_F5, -4, NOTE_E5, -4, NOTE_AS4, 8, NOTE_AS4, 8, NOTE_B4, 4, NOTE_G4, 4,
    ],
    'at_dooms_gate': [
        NOTE_E2, 8, NOTE_E2, 8, NOTE_E3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_D3, 8, NOTE_E2, 8, NOTE_E2, 8, 
        NOTE_C3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_AS2, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_B2, 8, NOTE_C3, 8,
        NOTE_E2, 8, NOTE_E2, 8, NOTE_E3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_D3, 8, NOTE_E2, 8, NOTE_E2, 8,
        NOTE_C3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_AS2, -2,
        NOTE_E2, 8, NOTE_E2, 8, NOTE_E3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_D3, 8, NOTE_E2, 8, NOTE_E2, 8, 
        NOTE_C3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_AS2, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_B2, 8, NOTE_C3, 8,
        NOTE_E2, 8, NOTE_E2, 8, NOTE_E3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_D3, 8, NOTE_E2, 8, NOTE_E2, 8,
        NOTE_C3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_AS2, -2,
        NOTE_E2, 8, NOTE_E2, 8, NOTE_E3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_D3, 8, NOTE_E2, 8, NOTE_E2, 8, 
        NOTE_C3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_AS2, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_B2, 8, NOTE_C3, 8,
        NOTE_E2, 8, NOTE_E2, 8, NOTE_E3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_D3, 8, NOTE_E2, 8, NOTE_E2, 8,
        NOTE_C3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_AS2, -2,
        NOTE_E2, 8, NOTE_E2, 8, NOTE_E3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_D3, 8, NOTE_E2, 8, NOTE_E2, 8, 
        NOTE_C3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_AS2, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_B2, 8, NOTE_C3, 8,
        NOTE_E2, 8, NOTE_E2, 8, NOTE_E3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_D3, 8, NOTE_E2, 8, NOTE_E2, 8,
        NOTE_FS3, -16, NOTE_D3, -16, NOTE_B2, -16, NOTE_A3, -16, NOTE_FS3, -16, NOTE_B2, -16, NOTE_D3, -16, NOTE_FS3, -16, NOTE_A3, -16, NOTE_FS3, -16, NOTE_D3, -16, NOTE_B2, -16,
        NOTE_E2, 8, NOTE_E2, 8, NOTE_E3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_D3, 8, NOTE_E2, 8, NOTE_E2, 8, 
        NOTE_C3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_AS2, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_B2, 8, NOTE_C3, 8,
        NOTE_E2, 8, NOTE_E2, 8, NOTE_E3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_D3, 8, NOTE_E2, 8, NOTE_E2, 8,
        NOTE_C3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_AS2, -2,
        NOTE_E2, 8, NOTE_E2, 8, NOTE_E3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_D3, 8, NOTE_E2, 8, NOTE_E2, 8, 
        NOTE_C3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_AS2, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_B2, 8, NOTE_C3, 8,
        NOTE_E2, 8, NOTE_E2, 8, NOTE_E3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_D3, 8, NOTE_E2, 8, NOTE_E2, 8,
        NOTE_B3, -16, NOTE_G3, -16, NOTE_E3, -16, NOTE_G3, -16, NOTE_B3, -16, NOTE_E4, -16, NOTE_G3, -16, NOTE_B3, -16, NOTE_E4, -16, NOTE_B3, -16, NOTE_G4, -16, NOTE_B4, -16,
        NOTE_A2, 8, NOTE_A2, 8, NOTE_A3, 8, NOTE_A2, 8, NOTE_A2, 8, NOTE_G3, 8, NOTE_A2, 8, NOTE_A2, 8, 
        NOTE_F3, 8, NOTE_A2, 8, NOTE_A2, 8, NOTE_DS3, 8, NOTE_A2, 8, NOTE_A2, 8, NOTE_E3, 8, NOTE_F3, 8,
        NOTE_A2, 8, NOTE_A2, 8, NOTE_A3, 8, NOTE_A2, 8, NOTE_A2, 8, NOTE_G3, 8, NOTE_A2, 8, NOTE_A2, 8,
        NOTE_F3, 8, NOTE_A2, 8, NOTE_A2, 8, NOTE_DS3, -2,
        NOTE_A2, 8, NOTE_A2, 8, NOTE_A3, 8, NOTE_A2, 8, NOTE_A2, 8, NOTE_G3, 8, NOTE_A2, 8, NOTE_A2, 8, 
        NOTE_F3, 8, NOTE_A2, 8, NOTE_A2, 8, NOTE_DS3, 8, NOTE_A2, 8, NOTE_A2, 8, NOTE_E3, 8, NOTE_F3, 8,
        NOTE_A2, 8, NOTE_A2, 8, NOTE_A3, 8, NOTE_A2, 8, NOTE_A2, 8, NOTE_G3, 8, NOTE_A2, 8, NOTE_A2, 8,
        NOTE_A3, -16, NOTE_F3, -16, NOTE_D3, -16, NOTE_A3, -16, NOTE_F3, -16, NOTE_D3, -16, NOTE_C4, -16, NOTE_A3, -16, NOTE_F3, -16, NOTE_A3, -16, NOTE_F3, -16, NOTE_D3, -16,
        NOTE_E2, 8, NOTE_E2, 8, NOTE_E3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_D3, 8, NOTE_E2, 8, NOTE_E2, 8, 
        NOTE_C3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_AS2, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_B2, 8, NOTE_C3, 8,
        NOTE_E2, 8, NOTE_E2, 8, NOTE_E3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_D3, 8, NOTE_E2, 8, NOTE_E2, 8,
        NOTE_C3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_AS2, -2,
        NOTE_E2, 8, NOTE_E2, 8, NOTE_E3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_D3, 8, NOTE_E2, 8, NOTE_E2, 8, 
        NOTE_C3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_AS2, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_B2, 8, NOTE_C3, 8,
        NOTE_E2, 8, NOTE_E2, 8, NOTE_E3, 8, NOTE_E2, 8, NOTE_E2, 8, NOTE_D3, 8, NOTE_E2, 8, NOTE_E2, 8,
        NOTE_B3, -16, NOTE_G3, -16, NOTE_E3, -16, NOTE_B2, -16, NOTE_E3, -16, NOTE_G3, -16, NOTE_C4, -16, NOTE_B3, -16, NOTE_G3, -16, NOTE_B3, -16, NOTE_G3, -16, NOTE_E3, -16  
    ],
    'fur_elise': [
        NOTE_E5, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_C5, 16,
        NOTE_A4, -8, NOTE_C4, 16, NOTE_E4, 16, NOTE_A4, 16, NOTE_B4, -8, NOTE_E4, 16, NOTE_GS4, 16, NOTE_B4, 16,
        NOTE_C5, 8,  REST, 16, NOTE_E4, 16, NOTE_E5, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_C5, 16,
        NOTE_A4, -8, NOTE_C4, 16, NOTE_E4, 16, NOTE_A4, 16, NOTE_B4, -8, NOTE_E4, 16, NOTE_C5, 16, NOTE_B4, 16, NOTE_A4 , 4, REST, 8,
        NOTE_E5, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_C5, 16,
        NOTE_A4, -8, NOTE_C4, 16, NOTE_E4, 16, NOTE_A4, 16, NOTE_B4, -8, NOTE_E4, 16, NOTE_GS4, 16, NOTE_B4, 16,
        NOTE_C5, 8,  REST, 16, NOTE_E4, 16, NOTE_E5, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_C5, 16,
        NOTE_A4, -8, NOTE_C4, 16, NOTE_E4, 16, NOTE_A4, 16, NOTE_B4, -8, NOTE_E4, 16, NOTE_C5, 16, NOTE_B4, 16, NOTE_A4, 8, REST, 16, NOTE_B4, 16, NOTE_C5, 16, NOTE_D5, 16,
        NOTE_E5, -8, NOTE_G4, 16, NOTE_F5, 16, NOTE_E5, 16, NOTE_D5, -8, NOTE_F4, 16, NOTE_E5, 16, NOTE_D5, 16,
        NOTE_C5, -8, NOTE_E4, 16, NOTE_D5, 16, NOTE_C5, 16, NOTE_B4, 8, REST, 16, NOTE_E4, 16, NOTE_E5, 16, REST, 16, REST, 16, NOTE_E5, 16, NOTE_E6, 16, REST, 16, REST, 16, NOTE_DS5, 16,
        NOTE_E5, 16, REST, 16, REST, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_C5, 16,
        NOTE_A4, 8, REST, 16, NOTE_C4, 16, NOTE_E4, 16, NOTE_A4, 16, NOTE_B4, 8, REST, 16, NOTE_E4, 16, NOTE_GS4, 16, NOTE_B4, 16,
        NOTE_C5, 8, REST, 16, NOTE_E4, 16, NOTE_E5, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_C5, 16,
        NOTE_A4, 8, REST, 16, NOTE_C4, 16, NOTE_E4, 16, NOTE_A4, 16, NOTE_B4, 8, REST, 16, NOTE_E4, 16, NOTE_C5, 16, NOTE_B4, 16, NOTE_A4, 8, REST, 16, NOTE_B4, 16, NOTE_C5, 16, NOTE_D5, 16,
        NOTE_E5, -8, NOTE_G4, 16, NOTE_F5, 16, NOTE_E5, 16, NOTE_D5, -8, NOTE_F4, 16, NOTE_E5, 16, NOTE_D5, 16,
        NOTE_C5, -8, NOTE_E4, 16, NOTE_D5, 16, NOTE_C5, 16, NOTE_B4, 8, REST, 16, NOTE_E4, 16, NOTE_E5, 16, REST, 16, REST, 16, NOTE_E5, 16, NOTE_E6, 16, REST, 16, REST, 16, NOTE_DS5, 16,
        NOTE_E5, 16, REST, 16, REST, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_C5, 16,
        NOTE_A4, 8, REST, 16, NOTE_C4, 16, NOTE_E4, 16, NOTE_A4, 16, NOTE_B4, 8, REST, 16, NOTE_E4, 16, NOTE_GS4, 16, NOTE_B4, 16,
        NOTE_C5, 8, REST, 16, NOTE_E4, 16, NOTE_E5, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_C5, 16,
        NOTE_A4, 8, REST, 16, NOTE_C4, 16, NOTE_E4, 16, NOTE_A4, 16, NOTE_B4, 8, REST, 16, NOTE_E4, 16, NOTE_C5, 16, NOTE_B4, 16, NOTE_A4, 8, REST, 16, NOTE_B4, 16, NOTE_C5, 16, NOTE_D5, 16,
        NOTE_E5, -8, NOTE_G4, 16, NOTE_F5, 16, NOTE_E5, 16, NOTE_D5, -8, NOTE_F4, 16, NOTE_E5, 16, NOTE_D5, 16,
        NOTE_C5, -8, NOTE_E4, 16, NOTE_D5, 16, NOTE_C5, 16, NOTE_B4, 8, REST, 16, NOTE_E4, 16, NOTE_E5, 16, REST, 16, REST, 16, NOTE_E5, 16, NOTE_E6, 16, REST, 16, REST, 16, NOTE_DS5, 16,
        NOTE_E5, 16, REST, 16, REST, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_D5, 16, NOTE_E5, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_C5, 16,
        NOTE_A4, 8, REST, 16, NOTE_C4, 16, NOTE_E4, 16, NOTE_A4, 16, NOTE_B4, 8, REST, 16, NOTE_E4, 16, NOTE_GS4, 16, NOTE_B4, 16,
        NOTE_C5, 8, REST, 16, NOTE_E4, 16, NOTE_E5, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_C5, 16,
        NOTE_A4, 8, REST, 16, NOTE_C4, 16, NOTE_E4, 16, NOTE_A4, 16, NOTE_B4, 8, REST, 16, NOTE_E4, 16, NOTE_C5, 16, NOTE_B4, 16, NOTE_A4, 8, REST, 16, NOTE_C5, 16, NOTE_C5, 16, NOTE_C5, 16,
        NOTE_C5 , 4, NOTE_F5, -16, NOTE_E5, 32, NOTE_E5, 8, NOTE_D5, 8, NOTE_AS5, -16, NOTE_A5, 32,
        NOTE_A5, 16, NOTE_G5, 16, NOTE_F5, 16, NOTE_E5, 16, NOTE_D5, 16, NOTE_C5, 16, NOTE_AS4, 8, NOTE_A4, 8, NOTE_A4, 32, NOTE_G4, 32, NOTE_A4, 32, NOTE_B4, 32,
        NOTE_C5 , 4, NOTE_D5, 16, NOTE_DS5, 16, NOTE_E5, -8, NOTE_E5, 16, NOTE_F5, 16, NOTE_A4, 16, NOTE_C5 , 4,  NOTE_D5, -16, NOTE_B4, 32,
        NOTE_C5, 32, NOTE_G5, 32, NOTE_G4, 32, NOTE_G5, 32, NOTE_A4, 32, NOTE_G5, 32, NOTE_B4, 32, NOTE_G5, 32, NOTE_C5, 32, NOTE_G5, 32, NOTE_D5, 32, NOTE_G5, 32,
        NOTE_E5, 32, NOTE_G5, 32, NOTE_C6, 32, NOTE_B5, 32, NOTE_A5, 32, NOTE_G5, 32, NOTE_F5, 32, NOTE_E5, 32, NOTE_D5, 32, NOTE_G5, 32, NOTE_F5, 32, NOTE_D5, 32,
        NOTE_C5, 32, NOTE_G5, 32, NOTE_G4, 32, NOTE_G5, 32, NOTE_A4, 32, NOTE_G5, 32, NOTE_B4, 32, NOTE_G5, 32, NOTE_C5, 32, NOTE_G5, 32, NOTE_D5, 32, NOTE_G5, 32,
        NOTE_E5, 32, NOTE_G5, 32, NOTE_C6, 32, NOTE_B5, 32, NOTE_A5, 32, NOTE_G5, 32, NOTE_F5, 32, NOTE_E5, 32, NOTE_D5, 32, NOTE_G5, 32, NOTE_F5, 32, NOTE_D5, 32,
        NOTE_E5, 32, NOTE_F5, 32, NOTE_E5, 32, NOTE_DS5, 32, NOTE_E5, 32, NOTE_B4, 32, NOTE_E5, 32, NOTE_DS5, 32, NOTE_E5, 32, NOTE_B4, 32, NOTE_E5, 32, NOTE_DS5, 32,
        NOTE_E5, -8, NOTE_B4, 16, NOTE_E5, 16, NOTE_DS5, 16, NOTE_E5, -8, NOTE_B4, 16, NOTE_E5, 16, REST, 16,
        REST, 16, NOTE_DS5, 16, NOTE_E5, 16, REST, 16, REST, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_C5, 16,
        NOTE_A4, 8, REST, 16, NOTE_C4, 16, NOTE_E4, 16, NOTE_A4, 16, NOTE_B4, 8, REST, 16, NOTE_E4, 16, NOTE_GS4, 16, NOTE_B4, 16, NOTE_C5, 8, REST, 16, NOTE_E4, 16, NOTE_E5, 16, NOTE_DS5, 16,
        NOTE_E5, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_C5, 16, NOTE_A4, 8, REST, 16, NOTE_C4, 16, NOTE_E4, 16, NOTE_A4, 16, NOTE_B4, 8, REST, 16, NOTE_E4, 16, NOTE_C5, 16, NOTE_B4, 16,
        NOTE_A4, 8, REST, 16, REST, 16, REST, 8, NOTE_CS5 , -4, NOTE_D5 , 4, NOTE_E5, 16, NOTE_F5, 16, NOTE_F5 , 4, NOTE_F5, 8, NOTE_E5 , -4,
        NOTE_D5 , 4, NOTE_C5, 16, NOTE_B4, 16, NOTE_A4 , 4, NOTE_A4, 8, NOTE_A4, 8, NOTE_C5, 8, NOTE_B4, 8, NOTE_A4 , -4, NOTE_CS5 , -4,
        NOTE_D5 , 4, NOTE_E5, 16, NOTE_F5, 16, NOTE_F5 , 4, NOTE_F5, 8, NOTE_F5 , -4, NOTE_DS5 , 4, NOTE_D5, 16, NOTE_C5, 16,
        NOTE_AS4 , 4, NOTE_A4, 8, NOTE_GS4 , 4, NOTE_G4, 8, NOTE_A4 , -4, NOTE_B4 , 4, REST, 8, NOTE_A3, -32, NOTE_C4, -32, NOTE_E4, -32, NOTE_A4, -32, NOTE_C5, -32, NOTE_E5, -32, NOTE_D5, -32, NOTE_C5, -32, NOTE_B4, -32,
        NOTE_A4, -32, NOTE_C5, -32, NOTE_E5, -32, NOTE_A5, -32, NOTE_C6, -32, NOTE_E6, -32, NOTE_D6, -32, NOTE_C6, -32, NOTE_B5, -32, NOTE_A4, -32, NOTE_C5, -32, NOTE_E5, -32, NOTE_A5, -32, NOTE_C6, -32, NOTE_E6, -32, NOTE_D6, -32, NOTE_C6, -32, NOTE_B5, -32,
        NOTE_AS5, -32, NOTE_A5, -32, NOTE_GS5, -32, NOTE_G5, -32, NOTE_FS5, -32, NOTE_F5, -32, NOTE_E5, -32, NOTE_DS5, -32, NOTE_D5, -32, NOTE_CS5, -32, NOTE_C5, -32, NOTE_B4, -32, NOTE_AS4, -32, NOTE_A4, -32, NOTE_GS4, -32, NOTE_G4, -32, NOTE_FS4, -32, NOTE_F4, -32,
        NOTE_E4, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_C5, 16, NOTE_A4, -8, NOTE_C4, 16, NOTE_E4, 16, NOTE_A4, 16, NOTE_B4, -8, NOTE_E4, 16, NOTE_GS4, 16, NOTE_B4, 16,
        NOTE_C5, 8, REST, 16, NOTE_E4, 16, NOTE_E5, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_C5, 16, NOTE_A4, -8, NOTE_C4, 16, NOTE_E4, 16, NOTE_A4, 16, NOTE_B4, -8, NOTE_E4, 16, NOTE_C5, 16, NOTE_B4, 16, NOTE_A4, -8, REST, -8,
        REST, -8, NOTE_G4, 16, NOTE_F5, 16, NOTE_E5, 16, NOTE_D5 , 4, REST, 8, REST, -8, NOTE_E4, 16, NOTE_D5, 16, NOTE_C5, 16, NOTE_B4, -8, NOTE_E4, 16, NOTE_E5, 8, NOTE_E5, 8, NOTE_E6, -8, NOTE_DS5, 16,
        NOTE_E5, 16, REST, 16, REST, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_C5, 16, NOTE_A4, -8, NOTE_C4, 16, NOTE_E4, 16, NOTE_A4, 16, NOTE_B4, -8, NOTE_E4, 16, NOTE_GS4, 16, NOTE_B4, 16,
        NOTE_C5, 8, REST, 16, NOTE_E4, 16, NOTE_E5, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_DS5, 16, NOTE_E5, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_C5, 16, NOTE_A4, 8, REST, 16, NOTE_C4, 16, NOTE_E4, 16, NOTE_A4, 16, NOTE_B4, 8, REST, 16, NOTE_E4, 16, NOTE_C5, 16, NOTE_B4, 16,
        NOTE_A4 , -4
    ],
    'game_of_thrones': [
        NOTE_G4,8, NOTE_C4,8, NOTE_DS4,16, NOTE_F4,16, NOTE_G4,8, NOTE_C4,8, NOTE_DS4,16, NOTE_F4,16,
        NOTE_G4,8, NOTE_C4,8, NOTE_DS4,16, NOTE_F4,16, NOTE_G4,8, NOTE_C4,8, NOTE_DS4,16, NOTE_F4,16,
        NOTE_G4,8, NOTE_C4,8, NOTE_E4,16, NOTE_F4,16, NOTE_G4,8, NOTE_C4,8, NOTE_E4,16, NOTE_F4,16,
        NOTE_G4,8, NOTE_C4,8, NOTE_E4,16, NOTE_F4,16, NOTE_G4,8, NOTE_C4,8, NOTE_E4,16, NOTE_F4,16,
        NOTE_G4,-4, NOTE_C4,-4,
        NOTE_DS4,16, NOTE_F4,16, NOTE_G4,4, NOTE_C4,4, NOTE_DS4,16, NOTE_F4,16,
        NOTE_D4,-1,
        NOTE_F4,-4, NOTE_AS3,-4,
        NOTE_DS4,16, NOTE_D4,16, NOTE_F4,4, NOTE_AS3,-4,
        NOTE_DS4,16, NOTE_D4,16, NOTE_C4,-1,
        NOTE_G4,-4, NOTE_C4,-4,
        NOTE_DS4,16, NOTE_F4,16, NOTE_G4,4, NOTE_C4,4, NOTE_DS4,16, NOTE_F4,16,
        NOTE_D4,-2,
        NOTE_F4,-4, NOTE_AS3,-4,
        NOTE_D4,-8, NOTE_DS4,-8, NOTE_D4,-8, NOTE_AS3,-8,
        NOTE_C4,-1,
        NOTE_C5,-2,
        NOTE_AS4,-2,
        NOTE_C4,-2,
        NOTE_G4,-2,
        NOTE_DS4,-2,
        NOTE_DS4,-4, NOTE_F4,-4,
        NOTE_G4,-1,
        NOTE_C5,-2,
        NOTE_AS4,-2,
        NOTE_C4,-2,
        NOTE_G4,-2,
        NOTE_DS4,-2,
        NOTE_DS4,-4, NOTE_D4,-4,
        NOTE_C5,8, NOTE_G4,8, NOTE_GS4,16, NOTE_AS4,16, NOTE_C5,8, NOTE_G4,8, NOTE_GS4,16, NOTE_AS4,16,
        NOTE_C5,8, NOTE_G4,8, NOTE_GS4,16, NOTE_AS4,16, NOTE_C5,8, NOTE_G4,8, NOTE_GS4,16, NOTE_AS4,16,
        REST,4, NOTE_GS5,16, NOTE_AS5,16, NOTE_C6,8, NOTE_G5,8, NOTE_GS5,16, NOTE_AS5,16,
        NOTE_C6,8, NOTE_G5,16, NOTE_GS5,16, NOTE_AS5,16, NOTE_C6,8, NOTE_G5,8, NOTE_GS5,16, NOTE_AS5,16,
    ],
    'green_hill_zone': [
        REST,2, NOTE_D5,8, NOTE_B4,4, NOTE_D5,8,
        NOTE_CS5,4, NOTE_D5,8, NOTE_CS5,4, NOTE_A4,2, 
        REST,8, NOTE_A4,8, NOTE_FS5,8, NOTE_E5,4, NOTE_D5,8,
        NOTE_CS5,4, NOTE_D5,8, NOTE_CS5,4, NOTE_A4,2, 
        REST,4, NOTE_D5,8, NOTE_B4,4, NOTE_D5,8,
        NOTE_CS5,4, NOTE_D5,8, NOTE_CS5,4, NOTE_A4,2, 
        REST,8, NOTE_B4,8, NOTE_B4,8, NOTE_G4,4, NOTE_B4,8,
        NOTE_A4,4, NOTE_B4,8, NOTE_A4,4, NOTE_D4,2,
        REST,4, NOTE_D5,8, NOTE_B4,4, NOTE_D5,8,
        NOTE_CS5,4, NOTE_D5,8, NOTE_CS5,4, NOTE_A4,2, 
        REST,8, NOTE_A4,8, NOTE_FS5,8, NOTE_E5,4, NOTE_D5,8,
        NOTE_CS5,4, NOTE_D5,8, NOTE_CS5,4, NOTE_A4,2, 
        REST,4, NOTE_D5,8, NOTE_B4,4, NOTE_D5,8,
        NOTE_CS5,4, NOTE_D5,8, NOTE_CS5,4, NOTE_A4,2, 
        REST,8, NOTE_B4,8, NOTE_B4,8, NOTE_G4,4, NOTE_B4,8,
        NOTE_A4,4, NOTE_B4,8, NOTE_A4,4, NOTE_D4,8, NOTE_D4,8, NOTE_FS4,8,
        NOTE_E4,-1,
        REST,8, NOTE_D4,8, NOTE_E4,8, NOTE_FS4,-1,
        REST,8, NOTE_D4,8, NOTE_D4,8, NOTE_FS4,8, NOTE_F4,-1,
        REST,8, NOTE_D4,8, NOTE_F4,8, NOTE_E4,8,
        REST,2, NOTE_D5,8, NOTE_B4,4, NOTE_D5,8,
        NOTE_CS5,4, NOTE_D5,8, NOTE_CS5,4, NOTE_A4,2, 
        REST,8, NOTE_A4,8, NOTE_FS5,8, NOTE_E5,4, NOTE_D5,8,
        NOTE_CS5,4, NOTE_D5,8, NOTE_CS5,4, NOTE_A4,2, 
        REST,4, NOTE_D5,8, NOTE_B4,4, NOTE_D5,8,
        NOTE_CS5,4, NOTE_D5,8, NOTE_CS5,4, NOTE_A4,2, 
        REST,8, NOTE_B4,8, NOTE_B4,8, NOTE_G4,4, NOTE_B4,8,
        NOTE_A4,4, NOTE_B4,8, NOTE_A4,4, NOTE_D4,2,
        REST,4, NOTE_D5,8, NOTE_B4,4, NOTE_D5,8,
        NOTE_CS5,4, NOTE_D5,8, NOTE_CS5,4, NOTE_A4,2, 
        REST,8, NOTE_A4,8, NOTE_FS5,8, NOTE_E5,4, NOTE_D5,8,
        NOTE_CS5,4, NOTE_D5,8, NOTE_CS5,4, NOTE_A4,2, 
        REST,4, NOTE_D5,8, NOTE_B4,4, NOTE_D5,8,
        NOTE_CS5,4, NOTE_D5,8, NOTE_CS5,4, NOTE_A4,2, 
        REST,8, NOTE_B4,8, NOTE_B4,8, NOTE_G4,4, NOTE_B4,8,
        NOTE_A4,4, NOTE_B4,8, NOTE_A4,4, NOTE_D4,8, NOTE_D4,8, NOTE_FS4,8,
        NOTE_E4,-1,
        REST,8, NOTE_D4,8, NOTE_E4,8, NOTE_FS4,-1,
        REST,8, NOTE_D4,8, NOTE_D4,8, NOTE_FS4,8, NOTE_F4,-1,
        REST,8, NOTE_D4,8, NOTE_F4,8, NOTE_E4,8,
        NOTE_E4,-2, NOTE_A4,8, NOTE_CS5,8,
        NOTE_FS5,8, NOTE_E5,4, NOTE_D5,8, NOTE_A5,-4,
    ],
    'greensleeves': [
        NOTE_G4,8, NOTE_AS4,4, NOTE_C5,8, NOTE_D5,-8, NOTE_DS5,16, NOTE_D5,8,
        NOTE_C5,4, NOTE_A4,8, NOTE_F4,-8, NOTE_G4,16, NOTE_A4,8,
        NOTE_AS4,4, NOTE_G4,8, NOTE_G4,-8, NOTE_FS4,16, NOTE_G4,8,
        NOTE_A4,4, NOTE_FS4,8, NOTE_D4,4, NOTE_G4,8,
        NOTE_AS4,4, NOTE_C5,8, NOTE_D5,-8, NOTE_DS5,16, NOTE_D5,8,
        NOTE_C5,4, NOTE_A4,8, NOTE_F4,-8, NOTE_G4,16, NOTE_A4,8,
        NOTE_AS4,-8, NOTE_A4,16, NOTE_G4,8, NOTE_FS4,-8, NOTE_E4,16, NOTE_FS4,8, 
        NOTE_G4,-2,
        NOTE_F5,2, NOTE_E5,16, NOTE_D5,8,
        NOTE_C5,4, NOTE_A4,8, NOTE_F4,-8, NOTE_G4,16, NOTE_A4,8,
        NOTE_AS4,4, NOTE_G4,8, NOTE_G4,-8, NOTE_FS4,16, NOTE_G4,8,
        NOTE_A4,4, NOTE_FS4,8, NOTE_D4,04,
        NOTE_F5,2, NOTE_E5,16, NOTE_D5,8,
        NOTE_C5,4, NOTE_A4,8, NOTE_F4,-8, NOTE_G4,16, NOTE_A4,8,
        NOTE_AS4,-8, NOTE_A4,16, NOTE_G4,8, NOTE_FS4,-8, NOTE_E4,16, NOTE_FS4,8,
        NOTE_G4,-2,
        NOTE_G4,8, NOTE_AS4,4, NOTE_C5,8, NOTE_D5,-8, NOTE_DS5,16, NOTE_D5,8,
        NOTE_C5,4, NOTE_A4,8, NOTE_F4,-8, NOTE_G4,16, NOTE_A4,8,
        NOTE_AS4,4, NOTE_G4,8, NOTE_G4,-8, NOTE_FS4,16, NOTE_G4,8,
        NOTE_A4,4, NOTE_FS4,8, NOTE_D4,4, NOTE_G4,8,
        NOTE_AS4,4, NOTE_C5,8, NOTE_D5,-8, NOTE_DS5,16, NOTE_D5,8,
        NOTE_C5,4, NOTE_A4,8, NOTE_F4,-8, NOTE_G4,16, NOTE_A4,8,
        NOTE_AS4,-8, NOTE_A4,16, NOTE_G4,8, NOTE_FS4,-8, NOTE_E4,16, NOTE_FS4,8,
        NOTE_G4,-2,
        NOTE_F5,2, NOTE_E5,16, NOTE_D5,8,
        NOTE_C5,4, NOTE_A4,8, NOTE_F4,-8, NOTE_G4,16, NOTE_A4,8,
        NOTE_AS4,4, NOTE_G4,8, NOTE_G4,-8, NOTE_FS4,16, NOTE_G4,8,
        NOTE_A4,4, NOTE_FS4,8, NOTE_D4,04,
        NOTE_F5,2, NOTE_E5,16, NOTE_D5,8,
        NOTE_C5,4, NOTE_A4,8, NOTE_F4,-8, NOTE_G4,16, NOTE_A4,8,
        NOTE_AS4,-8, NOTE_A4,16, NOTE_G4,8, NOTE_FS4,-8, NOTE_E4,16, NOTE_FS4,8,
        NOTE_G4,-2
    ],
    'happy_birthday': [
        NOTE_C4,4, NOTE_C4,8,
        NOTE_D4,-4, NOTE_C4,-4, NOTE_F4,-4,
        NOTE_E4,-2, NOTE_C4,4, NOTE_C4,8,
        NOTE_D4,-4, NOTE_C4,-4, NOTE_G4,-4,
        NOTE_F4,-2, NOTE_C4,4, NOTE_C4,8,
        NOTE_C5,-4, NOTE_A4,-4, NOTE_F4,-4,
        NOTE_E4,-4, NOTE_D4,-4, NOTE_AS4,4, NOTE_AS4,8,
        NOTE_A4,-4, NOTE_F4,-4, NOTE_G4,-4,
        NOTE_F4,-2
    ],
    'hedwigs_theme': [
        REST, 2, NOTE_D4, 4,
        NOTE_G4, -4, NOTE_AS4, 8, NOTE_A4, 4,
        NOTE_G4, 2, NOTE_D5, 4,
        NOTE_C5, -2,
        NOTE_A4, -2,
        NOTE_G4, -4, NOTE_AS4, 8, NOTE_A4, 4,
        NOTE_F4, 2, NOTE_GS4, 4,
        NOTE_D4, -1,
        NOTE_D4, 4,

        NOTE_G4, -4, NOTE_AS4, 8, NOTE_A4, 4,
        NOTE_G4, 2, NOTE_D5, 4,
        NOTE_F5, 2, NOTE_E5, 4,
        NOTE_DS5, 2, NOTE_B4, 4,
        NOTE_DS5, -4, NOTE_D5, 8, NOTE_CS5, 4,
        NOTE_CS4, 2, NOTE_B4, 4,
        NOTE_G4, -1,
        NOTE_AS4, 4,

        NOTE_D5, 2, NOTE_AS4, 4,
        NOTE_D5, 2, NOTE_AS4, 4,
        NOTE_DS5, 2, NOTE_D5, 4,
        NOTE_CS5, 2, NOTE_A4, 4,
        NOTE_AS4, -4, NOTE_D5, 8, NOTE_CS5, 4,
        NOTE_CS4, 2, NOTE_D4, 4,
        NOTE_D5, -1,
        REST, 4, NOTE_AS4, 4,

        NOTE_D5, 2, NOTE_AS4, 4,
        NOTE_D5, 2, NOTE_AS4, 4,
        NOTE_F5, 2, NOTE_E5, 4,
        NOTE_DS5, 2, NOTE_B4, 4,
        NOTE_DS5, -4, NOTE_D5, 8, NOTE_CS5, 4,
        NOTE_CS4, 2, NOTE_AS4, 4,
        NOTE_G4, -1
    ],
    'imperial_march': [
        NOTE_A4, -4, NOTE_A4, -4, NOTE_A4, 16, NOTE_A4, 16, NOTE_A4, 16, NOTE_A4, 16, NOTE_F4, 8, REST, 8,
        NOTE_A4, -4, NOTE_A4, -4, NOTE_A4, 16, NOTE_A4, 16, NOTE_A4, 16, NOTE_A4, 16, NOTE_F4, 8, REST, 8,
        NOTE_A4, 4, NOTE_A4, 4, NOTE_A4, 4, NOTE_F4, -8, NOTE_C5, 16,
        NOTE_A4, 4, NOTE_F4, -8, NOTE_C5, 16, NOTE_A4, 2,
        NOTE_E5, 4, NOTE_E5, 4, NOTE_E5, 4, NOTE_F5, -8, NOTE_C5, 16,
        NOTE_A4, 4, NOTE_F4, -8, NOTE_C5, 16, NOTE_A4, 2,
        NOTE_A5, 4, NOTE_A4, -8, NOTE_A4, 16, NOTE_A5, 4, NOTE_GS5, -8, NOTE_G5, 16,
        NOTE_DS5, 16, NOTE_D5, 16, NOTE_DS5, 8, REST, 8, NOTE_A4, 8, NOTE_DS5, 4, NOTE_D5, -8, NOTE_CS5, 16,
        NOTE_C5, 16, NOTE_B4, 16, NOTE_C5, 16, REST, 8, NOTE_F4, 8, NOTE_GS4, 4, NOTE_F4, -8, NOTE_A4, -16,
        NOTE_C5, 4, NOTE_A4, -8, NOTE_C5, 16, NOTE_E5, 2,
        NOTE_A5, 4, NOTE_A4, -8, NOTE_A4, 16, NOTE_A5, 4, NOTE_GS5, -8, NOTE_G5, 16,
        NOTE_DS5, 16, NOTE_D5, 16, NOTE_DS5, 8, REST, 8, NOTE_A4, 8, NOTE_DS5, 4, NOTE_D5, -8, NOTE_CS5, 16,
        NOTE_C5, 16, NOTE_B4, 16, NOTE_C5, 16, REST, 8, NOTE_F4, 8, NOTE_GS4, 4, NOTE_F4, -8, NOTE_A4, -16,
        NOTE_A4, 4, NOTE_F4, -8, NOTE_C5, 16, NOTE_A4, 2
    ],
    'keyboard_cat': [
        REST, 1, REST, 1, NOTE_C4, 4, NOTE_E4, 4, NOTE_G4, 4, NOTE_E4, 4,
        NOTE_C4, 4, NOTE_E4, 8, NOTE_G4, -4, NOTE_E4, 4,
        NOTE_A3, 4, NOTE_C4, 4, NOTE_E4, 4, NOTE_C4, 4,
        NOTE_A3, 4, NOTE_C4, 8, NOTE_E4, -4, NOTE_C4, 4,
        NOTE_G3, 4, NOTE_B3, 4, NOTE_D4, 4, NOTE_B3, 4,
        NOTE_G3, 4, NOTE_B3, 8, NOTE_D4, -4, NOTE_B3, 4,

        NOTE_G3, 4, NOTE_G3, 8, NOTE_G3, -4, NOTE_G3, 8, NOTE_G3, 4,
        NOTE_G3, 4, NOTE_G3, 4, NOTE_G3, 8, NOTE_G3, 4,
        NOTE_C4, 4, NOTE_E4, 4, NOTE_G4, 4, NOTE_E4, 4,
        NOTE_C4, 4, NOTE_E4, 8, NOTE_G4, -4, NOTE_E4, 4,
        NOTE_A3, 4, NOTE_C4, 4, NOTE_E4, 4, NOTE_C4, 4,
        NOTE_A3, 4, NOTE_C4, 8, NOTE_E4, -4, NOTE_C4, 4,
        NOTE_G3, 4, NOTE_B3, 4, NOTE_D4, 4, NOTE_B3, 4,
        NOTE_G3, 4, NOTE_B3, 8, NOTE_D4, -4, NOTE_B3, 4,

        NOTE_G3, -1
    ],
    'we_wish_you_a_merry_christmas': [
        NOTE_C5, 4,
        NOTE_F5, 4, NOTE_F5, 8, NOTE_G5, 8, NOTE_F5, 8, NOTE_E5, 8,
        NOTE_D5, 4, NOTE_D5, 4, NOTE_D5, 4,
        NOTE_G5, 4, NOTE_G5, 8, NOTE_A5, 8, NOTE_G5, 8, NOTE_F5, 8,
        NOTE_E5, 4, NOTE_C5, 4, NOTE_C5, 4,
        NOTE_A5, 4, NOTE_A5, 8, NOTE_AS5, 8, NOTE_A5, 8, NOTE_G5, 8,
        NOTE_F5, 4, NOTE_D5, 4, NOTE_C5, 8, NOTE_C5, 8,
        NOTE_D5, 4, NOTE_G5, 4, NOTE_E5, 4,

        NOTE_F5, 2, NOTE_C5, 4,
        NOTE_F5, 4, NOTE_F5, 8, NOTE_G5, 8, NOTE_F5, 8, NOTE_E5, 8,
        NOTE_D5, 4, NOTE_D5, 4, NOTE_D5, 4,
        NOTE_G5, 4, NOTE_G5, 8, NOTE_A5, 8, NOTE_G5, 8, NOTE_F5, 8,
        NOTE_E5, 4, NOTE_C5, 4, NOTE_C5, 4,
        NOTE_A5, 4, NOTE_A5, 8, NOTE_AS5, 8, NOTE_A5, 8, NOTE_G5, 8,
        NOTE_F5, 4, NOTE_D5, 4, NOTE_C5, 8, NOTE_C5, 8,
        NOTE_D5, 4, NOTE_G5, 4, NOTE_E5, 4,
        NOTE_F5, 2, NOTE_C5, 4,

        NOTE_F5, 4, NOTE_F5, 4, NOTE_F5, 4,
        NOTE_E5, 2, NOTE_E5, 4,
        NOTE_F5, 4, NOTE_E5, 4, NOTE_D5, 4,
        NOTE_C5, 2, NOTE_A5, 4,
        NOTE_AS5, 4, NOTE_A5, 4, NOTE_G5, 4,
        NOTE_C6, 4, NOTE_C5, 4, NOTE_C5, 8, NOTE_C5, 8,
        NOTE_D5, 4, NOTE_G5, 4, NOTE_E5, 4,
        NOTE_F5, 2, NOTE_C5, 4,
        NOTE_F5, 4, NOTE_F5, 8, NOTE_G5, 8, NOTE_F5, 8, NOTE_E5, 8,
        NOTE_D5, 4, NOTE_D5, 4, NOTE_D5, 4,

        NOTE_G5, 4, NOTE_G5, 8, NOTE_A5, 8, NOTE_G5, 8, NOTE_F5, 8,
        NOTE_E5, 4, NOTE_C5, 4, NOTE_C5, 4,
        NOTE_A5, 4, NOTE_A5, 8, NOTE_AS5, 8, NOTE_A5, 8, NOTE_G5, 8,
        NOTE_F5, 4, NOTE_D5, 4, NOTE_C5, 8, NOTE_C5, 8,
        NOTE_D5, 4, NOTE_G5, 4, NOTE_E5, 4,
        NOTE_F5, 2, NOTE_C5, 4,
        NOTE_F5, 4, NOTE_F5, 8, NOTE_G5, 8, NOTE_F5, 8, NOTE_E5, 8,
        NOTE_D5, 4, NOTE_D5, 4, NOTE_D5, 4,
        NOTE_G5, 4, NOTE_G5, 8, NOTE_A5, 8, NOTE_G5, 8, NOTE_F5, 8,
        NOTE_E5, 4, NOTE_C5, 4, NOTE_C5, 4,

        NOTE_A5, 4, NOTE_A5, 8, NOTE_AS5, 8, NOTE_A5, 8, NOTE_G5, 8,
        NOTE_F5, 4, NOTE_D5, 4, NOTE_C5, 8, NOTE_C5, 8,
        NOTE_D5, 4, NOTE_G5, 4, NOTE_E5, 4,
        NOTE_F5, 2, REST, 4
    ],
    'minuet_in_g': [
        NOTE_D5, 4, NOTE_G4, 8, NOTE_A4, 8, NOTE_B4, 8, NOTE_C5, 8,
        NOTE_D5, 4, NOTE_G4, 4, NOTE_G4, 4,
        NOTE_E5, 4, NOTE_C5, 8, NOTE_D5, 8, NOTE_E5, 8, NOTE_FS5, 8,
        NOTE_G5, 4, NOTE_G4, 4, NOTE_G4, 4,
        NOTE_C5, 4, NOTE_D5, 8, NOTE_C5, 8, NOTE_B4, 8, NOTE_A4, 8,

        NOTE_B4, 4, NOTE_C5, 8, NOTE_B4, 8, NOTE_A4, 8, NOTE_G4, 8,
        NOTE_FS4, 4, NOTE_G4, 8, NOTE_A4, 8, NOTE_B4, 8, NOTE_G4, 8,
        NOTE_A4, -2,
        NOTE_D5, 4, NOTE_G4, 8, NOTE_A4, 8, NOTE_B4, 8, NOTE_C5, 8,
        NOTE_D5, 4, NOTE_G4, 4, NOTE_G4, 4,
        NOTE_E5, 4, NOTE_C5, 8, NOTE_D5, 8, NOTE_E5, 8, NOTE_FS5, 8,

        NOTE_G5, 4, NOTE_G4, 4, NOTE_G4, 4,
        NOTE_C5, 4, NOTE_D5, 8, NOTE_C5, 8, NOTE_B4, 8, NOTE_A4, 8,
        NOTE_B4, 4, NOTE_C5, 8, NOTE_B4, 8, NOTE_A4, 8, NOTE_G4, 8,
        NOTE_A4, 4, NOTE_B4, 8, NOTE_A4, 8, NOTE_G4, 8, NOTE_FS4, 8,
        NOTE_G4, -2,

        NOTE_B5, 4, NOTE_G5, 8, NOTE_A5, 8, NOTE_B5, 8, NOTE_G5, 8,
        NOTE_A5, 4, NOTE_D5, 8, NOTE_E5, 8, NOTE_FS5, 8, NOTE_D5, 8,
        NOTE_G5, 4, NOTE_E5, 8, NOTE_FS5, 8, NOTE_G5, 8, NOTE_D5, 8,
        NOTE_CS5, 4, NOTE_B4, 8, NOTE_CS5, 8, NOTE_A4, 4,
        NOTE_A4, 8, NOTE_B4, 8, NOTE_CS5, 8, NOTE_D5, 8, NOTE_E5, 8, NOTE_FS5, 8,

        NOTE_G5, 4, NOTE_FS5, 4, NOTE_E5, 4,
        NOTE_FS5, 4, NOTE_A4, 4, NOTE_CS5, 4,
        NOTE_D5, -2,
        NOTE_D5, 4, NOTE_G4, 8, NOTE_FS5, 8, NOTE_G4, 4,
        NOTE_E5, 4, NOTE_G4, 8, NOTE_FS4, 8, NOTE_G4, 4,
        NOTE_D5, 4, NOTE_C5, 4, NOTE_B4, 4,

        NOTE_A4, 8, NOTE_G4, 8, NOTE_FS4, 8, NOTE_G4, 8, NOTE_A4, 4,
        NOTE_D4, 8, NOTE_E4, 8, NOTE_FS4, 8, NOTE_G4, 8, NOTE_A4, 8, NOTE_B4, 8,
        NOTE_C5, 4, NOTE_B4, 4, NOTE_A4, 4,
        NOTE_B4, 8, NOTE_D5, 8, NOTE_G4, 4, NOTE_FS4, 4,
        NOTE_G4, -2
    ],
    'nokia_tune': [
        NOTE_E5, 8, NOTE_D5, 8, NOTE_FS4, 4, NOTE_GS4, 4, 
        NOTE_CS5, 8, NOTE_B4, 8, NOTE_D4, 4, NOTE_E4, 4, 
        NOTE_B4, 8, NOTE_A4, 8, NOTE_CS4, 4, NOTE_E4, 4,
        NOTE_A4, 2
    ],
    'ode_to_joy': [
        NOTE_E4, 4, NOTE_E4, 4, NOTE_F4, 4, NOTE_G4, 4, 
        NOTE_G4, 4, NOTE_F4, 4, NOTE_E4, 4, NOTE_D4, 4,
        NOTE_C4, 4, NOTE_C4, 4, NOTE_D4, 4, NOTE_E4, 4,
        NOTE_E4, -4, NOTE_D4, 8, NOTE_D4, 2,

        NOTE_E4, 4, NOTE_E4, 4, NOTE_F4, 4, NOTE_G4, 4,
        NOTE_G4, 4, NOTE_F4, 4, NOTE_E4, 4, NOTE_D4, 4,
        NOTE_C4, 4, NOTE_C4, 4, NOTE_D4, 4, NOTE_E4, 4,
        NOTE_D4, -4, NOTE_C4, 8, NOTE_C4, 2,

        NOTE_D4, 4, NOTE_D4, 4, NOTE_E4, 4, NOTE_C4, 4,
        NOTE_D4, 4, NOTE_E4, 8, NOTE_F4, 8, NOTE_E4, 4, NOTE_C4, 4,
        NOTE_D4, 4, NOTE_E4, 8, NOTE_F4, 8, NOTE_E4, 4, NOTE_D4, 4,
        NOTE_C4, 4, NOTE_D4, 4, NOTE_G3, 2,

        NOTE_E4, 4, NOTE_E4, 4, NOTE_F4, 4, NOTE_G4, 4,
        NOTE_G4, 4, NOTE_F4, 4, NOTE_E4, 4, NOTE_D4, 4,
        NOTE_C4, 4, NOTE_C4, 4, NOTE_D4, 4, NOTE_E4, 4,
        NOTE_D4, -4, NOTE_C4, 8, NOTE_C4, 2
    ],
    'pacman_intro_theme': [
        NOTE_B4, 16, NOTE_B5, 16, NOTE_FS5, 16, NOTE_DS5, 16,
        NOTE_B5, 32, NOTE_FS5, -16, NOTE_DS5, 8, NOTE_C5, 16,
        NOTE_C6, 16, NOTE_G6, 16, NOTE_E6, 16, NOTE_C6, 32, NOTE_G6, -16, NOTE_E6, 8,

        NOTE_B4, 16, NOTE_B5, 16, NOTE_FS5, 16, NOTE_DS5, 16,
        NOTE_B5, 32, NOTE_FS5, -16, NOTE_DS5, 8, NOTE_DS5, 32, NOTE_E5, 32, NOTE_F5, 32,
        NOTE_F5, 32, NOTE_FS5, 32, NOTE_G5, 32, NOTE_G5, 32, NOTE_GS5, 32, NOTE_A5, 16, NOTE_B5, 8
    ],
    'professor_laytons_theme': [
        NOTE_D5, 1, NOTE_DS5, 1, NOTE_F5, 1, REST, 4, NOTE_F5, -4, NOTE_DS5, 8,
        NOTE_D5, 8, NOTE_F5, 1, NOTE_AS4, 8, NOTE_G4, -2, NOTE_F4, 1, NOTE_F4, 1,
        REST, 4, REST, 8, NOTE_F4, 8, NOTE_G4, 8, NOTE_GS4, 8, NOTE_AS4, 8,
        NOTE_C5, 8, NOTE_D5, 1, NOTE_DS5, 1, NOTE_F5, 1, NOTE_F5, -4, NOTE_DS5, 8,
        NOTE_D5, 8, NOTE_CS5, 8, NOTE_C5, -2, NOTE_AS4, 8, NOTE_G4, 1, NOTE_F4, -1,
        REST, 4, NOTE_D5, -4, REST, 16, NOTE_D5, 16, NOTE_D5, 2, REST, 4, NOTE_D5, 8,
        NOTE_DS5, 8, NOTE_F5, 8, NOTE_G5, 8, NOTE_F5, 8, NOTE_DS5, 8, NOTE_D5, 8,
        NOTE_D5, -4, NOTE_DS5, 16, NOTE_DS5, 2, REST, 4, NOTE_G4, 8, NOTE_C5, 8,
        NOTE_D5, 8, NOTE_DS5, 8, NOTE_F5, 8, NOTE_DS5, 8, NOTE_D5, 8, NOTE_C5, -4,
        REST, 16, NOTE_G4, 2, REST, 4, NOTE_G4, 8, NOTE_GS4, 8, NOTE_AS4, 8,
        NOTE_C5, 8, NOTE_AS4, 8, NOTE_GS4, 8, NOTE_G5, 8, NOTE_F4, -4, NOTE_AS4, -4,
        NOTE_G4, 2, REST, 8, NOTE_C4, 8, NOTE_D4, 8, NOTE_DS4, 8, NOTE_G4, 8,
        NOTE_C5, 8, NOTE_D5, -4, REST, 16, NOTE_D5, -16, NOTE_D5, 2, REST, 4,
        NOTE_D5, 8, NOTE_DS5, 8, NOTE_F5, 8, NOTE_G5, 8, NOTE_F5, 8, NOTE_DS5, 8,
        NOTE_D5, 8, NOTE_D5, -4, NOTE_DS5, -16, NOTE_DS5, 2, REST, 4, NOTE_C5, 8,
        NOTE_D5, 8, NOTE_DS5, 8, NOTE_F5, 8, NOTE_DS5, 8, NOTE_D5, 8, NOTE_AS4, 8,
        NOTE_AS4, -4, NOTE_C5, -4, NOTE_C5, -4, NOTE_F4, -4, REST, 8, NOTE_G4, 4,
        NOTE_D5, 4, NOTE_DS5, 4, NOTE_D5, -4, REST, 16, NOTE_C5, 16, NOTE_C5, 2,
        REST, 4, NOTE_D5, 4, NOTE_DS5, 4, NOTE_F5, 4, NOTE_G5, -4, REST, 16,
        NOTE_F5, 2, NOTE_AS5, -4, NOTE_G5, -4, NOTE_DS5, 4, NOTE_D5, -4, REST, 16,
        NOTE_DS5, 2, REST, 4, NOTE_C5, 8, NOTE_D5, 8, NOTE_DS5, 8, NOTE_E5, 8,
        NOTE_F5, 8, NOTE_FS5, 8, NOTE_G5, -4, NOTE_F5, -4, REST, 4, NOTE_AS5, 2,
        NOTE_G5, 4, NOTE_F5, 8, NOTE_G5, 8, REST, 8, NOTE_E5, 8, REST, 8, NOTE_D5, 8,
        NOTE_C5, -2, REST, 8, NOTE_G4, 8, NOTE_A4, 8, NOTE_AS4, 8, NOTE_C5, 8,
        NOTE_D5, 8, NOTE_DS5, 8, NOTE_DS5, -4, NOTE_D5, -4, NOTE_AS4, 4, REST, 4,
        NOTE_DS5, 8, NOTE_E5, 8, NOTE_F5, 4, NOTE_E5, 8, NOTE_DS5, 8, NOTE_D5, 8,
        NOTE_AS5, 8, NOTE_C5, 4, NOTE_G4, 8, NOTE_D5, 4, NOTE_G4, 8, NOTE_D5, 4,
        REST, 8, NOTE_FS5, 8, NOTE_G5, 8, NOTE_FS5, 8, NOTE_F5, 8, NOTE_DS5, 8,
        NOTE_D5, 8, NOTE_DS5, 8, REST, 8, NOTE_AS5, 8, NOTE_G5, 8, NOTE_DS5, 8,
        NOTE_F5, 8, REST, 8, NOTE_G5, 8, REST, 8, NOTE_FS5, 8, NOTE_F5, 8,
        NOTE_DS5, 8, NOTE_F5, 8, NOTE_DS5, 8, NOTE_D5, 8, NOTE_DS5, 8, NOTE_D5, -4,
        NOTE_C5, -4, REST, 4, REST, 4, NOTE_C5, 8, NOTE_D5, 8, NOTE_DS5, 8, NOTE_D5, 8,
        NOTE_C5, 8, NOTE_AS4, 8, NOTE_D5, 8, NOTE_DS5, 8, NOTE_F5, 8, NOTE_G5, 8,
        NOTE_D5, 8, NOTE_C5, 8, NOTE_D5, 8, NOTE_DS5, 8, NOTE_F5, 8, NOTE_G5, 8,
        NOTE_AS5, 8, NOTE_GS5, 8, NOTE_G5, 8, NOTE_F5, 8, NOTE_DS5, 8, NOTE_F5, 8,
        NOTE_DS5, 8, NOTE_D5, 16, NOTE_DS5, 16, NOTE_D5, 16, NOTE_AS4, 8, NOTE_C5, 8,
        NOTE_D5, 8, NOTE_DS5, 8, NOTE_F5, 8, NOTE_G5, 8, NOTE_AS5, 8, NOTE_GS5, 8,
        NOTE_G5, 8, NOTE_F5, 8, NOTE_DS5, 8, NOTE_D5, 8, NOTE_DS5, 8, NOTE_C5, 8,
        NOTE_D5, 8, NOTE_DS5, 8, NOTE_F5, 8, NOTE_C5, 8, NOTE_G4, 8, NOTE_C5, 8,
        NOTE_D5, 8, NOTE_DS5, 8, NOTE_F5, 8, NOTE_AS5, 8, NOTE_F5, 8, NOTE_DS5, 8,
        NOTE_D5, 8, NOTE_AS4, 8, NOTE_DS5, 8, NOTE_D5, 8, NOTE_D5, 16, NOTE_DS5, 16,
        NOTE_D5, 16, NOTE_G4, 8, NOTE_C5, 8, NOTE_D5, 8, NOTE_DS5, 8, NOTE_F5, 8,
        NOTE_F5, 8, NOTE_AS5, 8, NOTE_F5, 8, NOTE_DS5, 8, NOTE_D5, 8, NOTE_DS5, 8,
        NOTE_D5, 8, NOTE_AS4, 8, NOTE_D5, 8, NOTE_DS5, 8, NOTE_F5, 8, NOTE_G5, 8,
        NOTE_AS4, 8, NOTE_G4, 8, NOTE_AS4, 8, NOTE_DS5, 8, NOTE_AS5, 8, NOTE_DS5, 8,
        NOTE_AS5, 8, NOTE_GS5, 8, NOTE_G5, 8, NOTE_GS5, 8, NOTE_G5, 8, NOTE_F5, 8,
        NOTE_DS5, 8, NOTE_D5, 16, NOTE_DS5, 16, NOTE_D5, 16, NOTE_AS4, 8, NOTE_C5, 8,
        NOTE_D5, 8, NOTE_DS5, 8, NOTE_F5, 8, NOTE_C6, 8, NOTE_D5, 8, NOTE_AS5, 8,
        NOTE_D5, 8, NOTE_C5, 8, NOTE_D5, 8, NOTE_B5, 8, NOTE_G4, 8, NOTE_C4, 8,
        NOTE_DS4, 8, NOTE_G4, 8, NOTE_C5, 8, NOTE_DS5, 8, NOTE_G5, 8, REST, 8,
        NOTE_C5, 8, NOTE_D5, 8, NOTE_DS5, 8, NOTE_D5, 16, NOTE_DS5, 16, NOTE_D5, 16,
        NOTE_C5, 8, NOTE_G4, 8, NOTE_C5, 8, NOTE_G5, 8, NOTE_D5, -4, NOTE_C5, 8,
        NOTE_C5, 1, REST, 4, NOTE_DS4, 8, NOTE_C4, -4, NOTE_DS4, 2, NOTE_D6, 2,
        NOTE_B3, 2, NOTE_DS4, 8, NOTE_C4, -4, NOTE_G3, 2, NOTE_D6, 2, NOTE_B3, 2,
        NOTE_DS4, 8, NOTE_C4, -4, NOTE_G4, 2, NOTE_FS4, 2, NOTE_D4, 2, NOTE_F4, 2,
        NOTE_D4, 2, NOTE_G4, 2, NOTE_G4, 1, NOTE_G4, 1, NOTE_G4, 1, NOTE_G4, 1,
        REST, 1, REST, 1, NOTE_G4, 1, NOTE_G4, 1, NOTE_DS4, 2, NOTE_G4, 2, NOTE_G4, 2,
        NOTE_C4, 4, NOTE_D4, 8, NOTE_DS4, 8, NOTE_F4, 2, NOTE_AS4, 2, NOTE_AS4, 2,
        NOTE_C4, 4, NOTE_D4, 8, NOTE_DS4, 8, NOTE_DS4, 2, NOTE_G4, -2, NOTE_F4, 2,
        NOTE_G4, 8, NOTE_F4, 8, NOTE_G4, -2, NOTE_D4, -1, NOTE_C4, 2, NOTE_G4, -2,
        NOTE_F4, 2, NOTE_D4, 8, NOTE_DS4, 8, NOTE_F4, 2, NOTE_AS3, 2, NOTE_AS4, 2,
        NOTE_C4, 4, NOTE_D4, 8, NOTE_DS4, 8, NOTE_DS4, 2, NOTE_AS4, -2, NOTE_GS4, 2,
        NOTE_G4, 8, NOTE_F4, 8, NOTE_F4, 8, NOTE_G4, -1, NOTE_DS4, 2, NOTE_G4, 2,
        NOTE_G4, 2, NOTE_C4, 4, NOTE_D4, 8, NOTE_DS4, 8, NOTE_F4, 2, NOTE_AS4, 2,
        NOTE_AS4, 2, NOTE_C4, 4, NOTE_D4, 8, NOTE_DS4, 8, NOTE_DS4, 2, NOTE_G4, -2,
        NOTE_F4, 2, NOTE_G4, 8, NOTE_F4, 8, NOTE_G4, -2, NOTE_D4, -1, NOTE_C4, 2,
        NOTE_G4, -2, NOTE_F4, 2, NOTE_D4, 8, NOTE_DS4, 8, NOTE_F4, 2, NOTE_AS3, 2,
        NOTE_AS4, 2, NOTE_C4, 4, NOTE_D4, 8, NOTE_DS4, 8, NOTE_DS4, 2, NOTE_AS4, -2,
        NOTE_GS4, 2, NOTE_G4, 8, NOTE_F4, 8, NOTE_F4, 8, NOTE_G4, -1,
    ],
    'pulo_da_gaita': [
        NOTE_C5, 4, NOTE_G4, 8, NOTE_AS4, 4, NOTE_A4, 8,
        NOTE_G4, 16, NOTE_C4, 8, NOTE_C4, 16, NOTE_G4, 16, NOTE_G4, 8, NOTE_G4, 16,
        NOTE_C5, 4, NOTE_G4, 8, NOTE_AS4, 4, NOTE_A4, 8,
        NOTE_G4, 2,
        
        NOTE_C5, 4, NOTE_G4, 8, NOTE_AS4, 4, NOTE_A4, 8,
        NOTE_G4, 16, NOTE_C4, 8, NOTE_C4, 16, NOTE_G4, 16, NOTE_G4, 8, NOTE_G4, 16,
        NOTE_F4, 8, NOTE_E4, 8, NOTE_D4, 8, NOTE_C4, 8,
        NOTE_C4, 2,
    
        NOTE_C5, 4, NOTE_G4, 8, NOTE_AS4, 4, NOTE_A4, 8,
        NOTE_G4, 16, NOTE_C4, 8, NOTE_C4, 16, NOTE_G4, 16, NOTE_G4, 8, NOTE_G4, 16,
        NOTE_C5, 4, NOTE_G4, 8, NOTE_AS4, 4, NOTE_A4, 8,
        NOTE_G4, 2,
    
        NOTE_C5, 4, NOTE_G4, 8, NOTE_AS4, 4, NOTE_A4, 8,
        NOTE_G4, 16, NOTE_C4, 8, NOTE_C4, 16, NOTE_G4, 16, NOTE_G4, 8, NOTE_G4, 16,
        NOTE_F4, 8, NOTE_E4, 8, NOTE_D4, 8, NOTE_C4, 8,
        NOTE_C4, 16, NOTE_D5, 8, NOTE_D5, 16, NOTE_D5, 16, NOTE_D5, 8, NOTE_D5, 16,
    
        NOTE_D5, 16, NOTE_D5, 8, NOTE_D5, 16, NOTE_C5, 8, NOTE_E5, -8,
        NOTE_C5, 8, NOTE_C5, 16, NOTE_E5, 16, NOTE_E5, 8, NOTE_C5, 16,
        NOTE_F5, 8, NOTE_D5, 8, NOTE_D5, 8, NOTE_E5, -8,
        NOTE_C5, 8, NOTE_D5, 16, NOTE_E5, 16, NOTE_D5, 8, NOTE_C5, 16,
    
        NOTE_F5, 8, NOTE_F5, 8, NOTE_A5, 8, NOTE_G5, -8,
        NOTE_G5, 8, NOTE_C5, 16, NOTE_C5, 16, NOTE_C5, 8, NOTE_C5, 16,
        NOTE_F5, -8, NOTE_E5, 16, NOTE_D5, 8, NOTE_C5, 4,
        NOTE_C5, 16, NOTE_C5, 16, NOTE_C5, 16, NOTE_C5, 16,
    
        NOTE_F5, 8, NOTE_F5, 16, NOTE_A5, 8, NOTE_G5, -8,
        NOTE_G5, 8, NOTE_C5, 16, NOTE_C5, 16, NOTE_C5, 8, NOTE_C5, 16,
        NOTE_F5, 16, NOTE_E5, 8, NOTE_D5, 16, NOTE_C5, 8, NOTE_E5, -8,
        NOTE_C5, 8, NOTE_D5, 16, NOTE_E5, 16, NOTE_D5, 8, NOTE_C5, 16,
    
        NOTE_F5, 8, NOTE_F5, 16, NOTE_A5, 8, NOTE_G5, -8,
        NOTE_G5, 8, NOTE_C5, 16, NOTE_C5, 16, NOTE_C5, 8, NOTE_C5, 16,
        NOTE_F5, 8, NOTE_E5, 16, NOTE_D5, 8, NOTE_C5, 8,
        NOTE_C5, 4, NOTE_G4, 8, NOTE_AS4, 4, NOTE_A4, 8,
    
        NOTE_G4, 16, NOTE_C4, 8, NOTE_C4, 16, NOTE_G4, 16, NOTE_G4, 8, NOTE_G4, 16,
        NOTE_C5, 4, NOTE_G4, 8, NOTE_AS4, 4, NOTE_A4, 8,
        NOTE_G4, 2,
        NOTE_C5, 4, NOTE_G4, 8, NOTE_AS4, 4, NOTE_A4, 8,
    
        NOTE_G4, 16, NOTE_C4, 8, NOTE_C4, 16, NOTE_G4, 16, NOTE_G4, 8, NOTE_G4, 16,
        NOTE_F4, 8, NOTE_E4, 8, NOTE_D4, 8, NOTE_C4, -2,
        NOTE_C5, 4, NOTE_G4, 8, NOTE_AS4, 4, NOTE_A4, 8,
    
        NOTE_G4, 16, NOTE_C4, 8, NOTE_C4, 16, NOTE_G4, 16, NOTE_G4, 8, NOTE_G4, 16,
        NOTE_C5, 4, NOTE_G4, 8, NOTE_AS4, 4, NOTE_A4, 8,
        NOTE_G4, 2,
        NOTE_C5, 4, NOTE_G4, 8, NOTE_AS4, 4, NOTE_A4, 8,
    
        NOTE_G4, 16, NOTE_C4, 8, NOTE_C4, 16, NOTE_G4, 16, NOTE_G4, 8, NOTE_G4, 16,
        NOTE_F4, 8, NOTE_E4, 8, NOTE_D4, 8, NOTE_C4, -2,
        NOTE_C4, 16, NOTE_C4, 8, NOTE_C4, 16, NOTE_E4, 16, NOTE_E4, 8, NOTE_E4, 16,
        NOTE_F4, 16, NOTE_F4, 8, NOTE_F4, 16, NOTE_FS4, 16, NOTE_FS4, 8, NOTE_FS4, 16,
    
        NOTE_G4, 8, REST, 8, NOTE_AS4, 8, NOTE_C5, 1,
    ],
    'silent_night': [
        NOTE_G4, -4, NOTE_A4, 8, NOTE_G4, 4,
        NOTE_E4, -2, 
        NOTE_G4, -4, NOTE_A4, 8, NOTE_G4, 4,
        NOTE_E4, -2, 
        NOTE_D5, 2, NOTE_D5, 4,
        NOTE_B4, -2,
        NOTE_C5, 2, NOTE_C5, 4,
        NOTE_G4, -2,

        NOTE_A4, 2, NOTE_A4, 4,
        NOTE_C5, -4, NOTE_B4, 8, NOTE_A4, 4,
        NOTE_G4, -4, NOTE_A4, 8, NOTE_G4, 4,
        NOTE_E4, -2, 
        NOTE_A4, 2, NOTE_A4, 4,
        NOTE_C5, -4, NOTE_B4, 8, NOTE_A4, 4,
        NOTE_G4, -4, NOTE_A4, 8, NOTE_G4, 4,
        NOTE_E4, -2, 

        NOTE_D5, 2, NOTE_D5, 4,
        NOTE_F5, -4, NOTE_D5, 8, NOTE_B4, 4,
        NOTE_C5, -2,
        NOTE_E5, -2,
        NOTE_C5, 4, NOTE_G4, 4, NOTE_E4, 4,
        NOTE_G4, -4, NOTE_F4, 8, NOTE_D4, 4,
        NOTE_C4, -2,
        NOTE_C4, -1,
    ],
    'star_trek_intro': [
        NOTE_D4, -8, NOTE_G4, 16, NOTE_C5, -4, 
        NOTE_B4, 8, NOTE_G4, -16, NOTE_E4, -16, NOTE_A4, -16,
        NOTE_D5, 2,
    ],
    'star_wars_theme': [
        NOTE_AS4, 8, NOTE_AS4, 8, NOTE_AS4, 8,
        NOTE_F5, 2, NOTE_C6, 2,
        NOTE_AS5, 8, NOTE_A5, 8, NOTE_G5, 8, NOTE_F6, 2, NOTE_C6, 4,
        NOTE_AS5, 8, NOTE_A5, 8, NOTE_G5, 8, NOTE_F6, 2, NOTE_C6, 4,
        NOTE_AS5, 8, NOTE_A5, 8, NOTE_AS5, 8, NOTE_G5, 2, NOTE_C5, 8, NOTE_C5, 8, NOTE_C5, 8,
        NOTE_F5, 2, NOTE_C6, 2,
        NOTE_AS5, 8, NOTE_A5, 8, NOTE_G5, 8, NOTE_F6, 2, NOTE_C6, 4,

        NOTE_AS5, 8, NOTE_A5, 8, NOTE_G5, 8, NOTE_F6, 2, NOTE_C6, 4,
        NOTE_AS5, 8, NOTE_A5, 8, NOTE_AS5, 8, NOTE_G5, 2, NOTE_C5, -8, NOTE_C5, 16,
        NOTE_D5, -4, NOTE_D5, 8, NOTE_AS5, 8, NOTE_A5, 8, NOTE_G5, 8, NOTE_F5, 8,
        NOTE_F5, 8, NOTE_G5, 8, NOTE_A5, 8, NOTE_G5, 4, NOTE_D5, 8, NOTE_E5, 4, NOTE_C5, -8, NOTE_C5, 16,
        NOTE_D5, -4, NOTE_D5, 8, NOTE_AS5, 8, NOTE_A5, 8, NOTE_G5, 8, NOTE_F5, 8,

        NOTE_C6, -8, NOTE_G5, 16, NOTE_G5, 2, REST, 8, NOTE_C5, 8,
        NOTE_D5, -4, NOTE_D5, 8, NOTE_AS5, 8, NOTE_A5, 8, NOTE_G5, 8, NOTE_F5, 8,
        NOTE_F5, 8, NOTE_G5, 8, NOTE_A5, 8, NOTE_G5, 4, NOTE_D5, 8, NOTE_E5, 4, NOTE_C6, -8, NOTE_C6, 16,
        NOTE_F6, 4, NOTE_DS6, 8, NOTE_CS6, 4, NOTE_C6, 8, NOTE_AS5, 4, NOTE_GS5, 8, NOTE_G5, 4, NOTE_F5, 8,
        NOTE_C6, 1
    ],
    'take_on_me': [
        NOTE_FS5, 8, NOTE_FS5, 8, NOTE_D5, 8, NOTE_B4, 8, REST, 8, NOTE_B4, 8, REST, 8, NOTE_E5, 8,
        REST, 8, NOTE_E5, 8, REST, 8, NOTE_E5, 8, NOTE_GS5, 8, NOTE_GS5, 8, NOTE_A5, 8, NOTE_B5, 8,
        NOTE_A5, 8, NOTE_A5, 8, NOTE_A5, 8, NOTE_E5, 8, REST, 8, NOTE_D5, 8, REST, 8, NOTE_FS5, 8,
        REST, 8, NOTE_FS5, 8, REST, 8, NOTE_FS5, 8, NOTE_E5, 8, NOTE_E5, 8, NOTE_FS5, 8, NOTE_E5, 8,
        NOTE_FS5, 8, NOTE_FS5, 8, NOTE_D5, 8, NOTE_B4, 8, REST, 8, NOTE_B4, 8, REST, 8, NOTE_E5, 8,

        REST, 8, NOTE_E5, 8, REST, 8, NOTE_E5, 8, NOTE_GS5, 8, NOTE_GS5, 8, NOTE_A5, 8, NOTE_B5, 8,
        NOTE_A5, 8, NOTE_A5, 8, NOTE_A5, 8, NOTE_E5, 8, REST, 8, NOTE_D5, 8, REST, 8, NOTE_FS5, 8,
        REST, 8, NOTE_FS5, 8, REST, 8, NOTE_FS5, 8, NOTE_E5, 8, NOTE_E5, 8, NOTE_FS5, 8, NOTE_E5, 8,
        NOTE_FS5, 8, NOTE_FS5, 8, NOTE_D5, 8, NOTE_B4, 8, REST, 8, NOTE_B4, 8, REST, 8, NOTE_E5, 8,
        REST, 8, NOTE_E5, 8, REST, 8, NOTE_E5, 8, NOTE_GS5, 8, NOTE_GS5, 8, NOTE_A5, 8, NOTE_B5, 8,

        NOTE_A5, 8, NOTE_A5, 8, NOTE_A5, 8, NOTE_E5, 8, REST, 8, NOTE_D5, 8, REST, 8, NOTE_FS5, 8,
        REST, 8, NOTE_FS5, 8, REST, 8, NOTE_FS5, 8, NOTE_E5, 8, NOTE_E5, 8, NOTE_FS5, 8, NOTE_E5, 8,
    ],
    'bach_badinerie': [
        NOTE_B5, -8, NOTE_D6, 16, NOTE_B5, 16,
        NOTE_FS5, -8, NOTE_B5, 16, NOTE_FS5, 16, NOTE_D5, -8, NOTE_FS5, 16, NOTE_D5, 16,
        NOTE_B4, 4, NOTE_F4, 16, NOTE_B4, 16, NOTE_D5, 16, NOTE_B4, 16,
        NOTE_CS5, 16, NOTE_B4, 16, NOTE_CS5, 16, NOTE_B4, 16, NOTE_AS4, 16, NOTE_CS5, 16, NOTE_E5, 16, NOTE_CS5, 16,
        NOTE_D5, 8, NOTE_B4, 8, NOTE_B5, -8, NOTE_D6, 16, NOTE_B5, 16,
        NOTE_FS5, -8, NOTE_B5, 16, NOTE_FS5, 16, NOTE_D5, -8, NOTE_FS5, 16, NOTE_D5, 16,

        NOTE_B4, 4, NOTE_D5, 16, NOTE_CS5, -16, NOTE_D5, -8,
        NOTE_D5, 16, NOTE_CS5, -16, NOTE_D5, -8, NOTE_B5, -8, NOTE_D5, -8,
        NOTE_D5, 8, NOTE_CS5, -8, NOTE_FS5, -16, NOTE_F5, 16, NOTE_FS5, -8,
        NOTE_FS5, -16, NOTE_F5, 16, NOTE_FS5, -8, NOTE_D6, -8, NOTE_FS5, -8,
        NOTE_FS5, 8, NOTE_F5, 8, NOTE_CS5, 16, NOTE_FS5, 16, NOTE_A5, 16, NOTE_FS5, 16,
        NOTE_GS5, 16, NOTE_FS5, 16, NOTE_GS5, 16, NOTE_FS5, 16, NOTE_F5, 16, NOTE_G5, 16, NOTE_B5, 16, NOTE_G5, 16,

        NOTE_A5, 16, NOTE_GS5, 16, NOTE_A5, 16, NOTE_G5, 16, NOTE_F5, 16, NOTE_A5, 16, NOTE_FS5, 16, NOTE_F5, 16,
        NOTE_FS5, 16, NOTE_B5, 16, NOTE_FS5, 16, NOTE_F5, 16, NOTE_FS5, 16, NOTE_C6, 16, NOTE_FS5, 16, NOTE_E5, 16,
        NOTE_FS5, 16, NOTE_D6, 16, NOTE_FS5, 16, NOTE_F5, 16, NOTE_FS5, 16, NOTE_D6, 16, NOTE_C6, 16, NOTE_B5, 16,
        NOTE_C6, 16, NOTE_A5, 16, NOTE_GS5, 16, NOTE_FS5, 16, NOTE_A5, 8, NOTE_G5, 8,
        NOTE_FS5, 4, REST, 4, NOTE_FS5, -8, NOTE_A5, 16, NOTE_FS5, 16,

        NOTE_CS5, -4, NOTE_FS5, 16, NOTE_CS5, 16, NOTE_A4, -8, NOTE_CS5, 16, NOTE_A4, 16,
        NOTE_F4, 4, NOTE_C5, 8, NOTE_B4, 8,
        NOTE_E5, 8, NOTE_DS5, 16, NOTE_FS5, 16, NOTE_A5, 8, NOTE_GS5, 16, NOTE_FS5, 16,
        NOTE_GS5, 8, NOTE_D5, 8, NOTE_GS5, -8, NOTE_B5, 16, NOTE_GS5, 8,
        NOTE_E5, -8, NOTE_GS5, 16, NOTE_E5, 16, NOTE_CS5, -8, NOTE_E5, 16, NOTE_CS5, 16,
        NOTE_A4, 4, NOTE_A4, 16, NOTE_D5, 16, NOTE_FS5, 16, NOTE_D5, 16,

        NOTE_E5, 16, NOTE_D5, 16, NOTE_E5, 16, NOTE_D5, 16, NOTE_CS5, 16, NOTE_E5, 16, NOTE_G5, 16, NOTE_E5, 16,
        NOTE_FS5, 16, NOTE_E5, 16, NOTE_FS5, 16, NOTE_E5, 16, NOTE_D5, 16, NOTE_FS5, 16, NOTE_D5, 16, NOTE_CS5, 16,
        NOTE_D5, 16, NOTE_G5, 16, NOTE_D5, 16, NOTE_CS5, 16, NOTE_D5, 16, NOTE_A5, 16, NOTE_D5, 16, NOTE_CS5, 16,
        NOTE_D5, 16, NOTE_B5, 16, NOTE_D5, 16, NOTE_CS5, 16, NOTE_D5, 16, NOTE_B5, 16, NOTE_A5, 16, NOTE_G5, 16,
        NOTE_A5, 16, NOTE_FS5, 16, NOTE_E5, 16, NOTE_D5, 16, NOTE_FS5, 8, NOTE_E5, 16,

        NOTE_D5, 4, NOTE_FS5, 16, NOTE_E5, 16, NOTE_FS5, -8,
        NOTE_FS5, 16, NOTE_E5, 16, NOTE_FS5, -8, NOTE_D6, -8, NOTE_FS5, -8,
        NOTE_FS5, 8, NOTE_E5, 8, NOTE_E5, 16, NOTE_D5, 16, NOTE_E5, -8,
        NOTE_E5, 16, NOTE_D5, 16, NOTE_E5, -8, NOTE_D6, -8, NOTE_E5, -8,
        NOTE_E5, 8, NOTE_D5, 8, NOTE_B5, -8, NOTE_D6, 16, NOTE_B5, 16,
        NOTE_B5, 8, NOTE_G5, 4, NOTE_G5, 4, NOTE_B5, 32, NOTE_A5, 32, NOTE_G5, 32, NOTE_FS5, 32,

        NOTE_E5, 4, NOTE_E5, 8, NOTE_G5, 32, NOTE_FS5, 32, NOTE_E5, 32, NOTE_D5, 32,
        NOTE_C5, 16, NOTE_E5, 16, NOTE_G5, 16, NOTE_E5, 16, NOTE_CS5, 16, NOTE_B4, 16, NOTE_CS5, 16, NOTE_A4, 16,
        NOTE_AS4, -8, NOTE_A4, -8, NOTE_G4, 8, NOTE_F4, 8,
        NOTE_A4, 8, NOTE_AS4, 16, NOTE_CS5, 16, NOTE_E5, 8, NOTE_D5, 16, NOTE_CS5, 16,

        NOTE_D5, 8, NOTE_B4, 32, NOTE_CS5, 32, NOTE_D5, 32, NOTE_E5, 32, NOTE_FS5, 8, NOTE_D5, 16, NOTE_FS5, 16,
        NOTE_B5, 8, NOTE_FS5, 8, NOTE_E5, 16, NOTE_D5, 16, NOTE_CS5, 16, NOTE_D5, 16,
        NOTE_CS5, 8, NOTE_B4, 4
    ],
    'the_godfather': [
        REST, 4, REST, 8, REST, 8, REST, 8, NOTE_E4, 8, NOTE_A4, 8, NOTE_C5, 8,
        NOTE_B4, 8, NOTE_A4, 8, NOTE_C5, 8, NOTE_A4, 8, NOTE_B4, 8, NOTE_A4, 8, NOTE_F4, 8, NOTE_G4, 8,
        NOTE_E4, 2, NOTE_E4, 8, NOTE_A4, 8, NOTE_C5, 8,
        NOTE_B4, 8, NOTE_A4, 8, NOTE_C5, 8, NOTE_A4, 8, NOTE_C5, 8, NOTE_A4, 8, NOTE_E4, 8, NOTE_DS4, 8,

        NOTE_D4, 2, NOTE_D4, 8, NOTE_F4, 8, NOTE_GS4, 8,
        NOTE_B4, 2, NOTE_D4, 8, NOTE_F4, 8, NOTE_GS4, 8,
        NOTE_A4, 2, NOTE_C4, 8, NOTE_C4, 8, NOTE_G4, 8,
        NOTE_F4, 8, NOTE_E4, 8, NOTE_G4, 8, NOTE_F4, 8, NOTE_F4, 8, NOTE_E4, 8, NOTE_E4, 8, NOTE_GS4, 8,

        NOTE_A4, 2, REST, 8, NOTE_A4, 8, NOTE_A4, 8, NOTE_GS4, 8,
        NOTE_G4, 2, NOTE_B4, 8, NOTE_A4, 8, NOTE_F4, 8,
        NOTE_E4, 2, NOTE_E4, 8, NOTE_G4, 8, NOTE_E4, 8,
        NOTE_D4, 2, NOTE_D4, 8, NOTE_D4, 8, NOTE_F4, 8, NOTE_DS4, 8,

        NOTE_E4, 2, REST, 8, NOTE_E4, 8, NOTE_A4, 8, NOTE_C5, 8,

        NOTE_B4, 8, NOTE_A4, 8, NOTE_C5, 8, NOTE_A4, 8, NOTE_B4, 8, NOTE_A4, 8, NOTE_F4, 8, NOTE_G4, 8,
        NOTE_E4, 2, NOTE_E4, 8, NOTE_A4, 8, NOTE_C5, 8,
        NOTE_B4, 8, NOTE_A4, 8, NOTE_C5, 8, NOTE_A4, 8, NOTE_C5, 8, NOTE_A4, 8, NOTE_E4, 8, NOTE_DS4, 8,

        NOTE_D4, 2, NOTE_D4, 8, NOTE_F4, 8, NOTE_GS4, 8,
        NOTE_B4, 2, NOTE_D4, 8, NOTE_F4, 8, NOTE_GS4, 8,
        NOTE_A4, 2, NOTE_C4, 8, NOTE_C4, 8, NOTE_G4, 8,
        NOTE_F4, 8, NOTE_E4, 8, NOTE_G4, 8, NOTE_F4, 8, NOTE_F4, 8, NOTE_E4, 8, NOTE_E4, 8, NOTE_GS4, 8,

        NOTE_A4, 2, REST, 8, NOTE_A4, 8, NOTE_A4, 8, NOTE_GS4, 8,
        NOTE_G4, 2, NOTE_B4, 8, NOTE_A4, 8, NOTE_F4, 8,
        NOTE_E4, 2, NOTE_E4, 8, NOTE_G4, 8, NOTE_E4, 8,
        NOTE_D4, 2, NOTE_D4, 8, NOTE_D4, 8, NOTE_F4, 8, NOTE_DS4, 8,

        NOTE_E4, 2
    ],
    'the_lick': [
        NOTE_D4, 8, NOTE_E4, 8, NOTE_F4, 8, NOTE_G4, 8, NOTE_E4, 4, NOTE_C4, 8, NOTE_D4, 1,
    ]
} 

sorted_melody_tempos = {
    1: 'asa_branca',
    2: 'at_dooms_gate',
    3: 'bach_badinerie',
    4: 'baby_elephant_walk',
    5: 'bloody_tears',
    6: 'brahms_lullaby',
    7: 'cantina_band',
    8: 'fur_elise',
    9: 'game_of_thrones',
    10: 'green_hill_zone',
    11: 'greensleeves',
    12: 'happy_birthday',
    13: 'hedwigs_theme',
    14: 'imperial_march',
    15: 'jigglypuff_song',
    16: 'keyboard_cat',
    17: 'mii_channel_theme',
    18: 'minuet_in_g',
    19: 'never_gonna_give_you_up',
    20: 'nokia_tune',
    21: 'ode-to-joy',
    22: 'pacman_intro_theme',
    23: 'pachelbels_canon',
    24: 'pink_panther_theme',
    25: 'professor_laytons_theme',
    26: 'pulo_da_gaita',
    27: 'silent_night',
    28: 'song_of_storms',
    29: 'star_trek_intro',
    30: 'star_wars_theme',
    31: 'super_mario_theme',
    32: 'take_on_me',
    33: 'the_godfather',
    34: 'the_lion_sleeps_tonight',
    35: 'the_lick',
    36: 'tetris_theme',
    37: 'vampire_killer',
    38: 'we_wish_you_a_merry_christmas',
    39: 'zelda_melody',
    40: 'zeldas_lullaby'
}