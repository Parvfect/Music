
notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

def create_sequence(linear , start):
    """Creates a sequence of musical notes"""
    return (notes[start::]+ notes[0:start])

class Strings:
    """Class representation of a string with its notes"""
    name = ""
    notes_chart = []
    def __init__(self, name):
        self.name = name

    def create_notes(self, start):
        self.notes_chart = create_sequence(True, start)

    def get_note(self, note):
        for c,i in enumerate(self.notes_chart):
            if i == note:
                return c
        return 0



class Guitar:
    """A class representation of a Guitar with six strings"""
    E = Strings("E")
    E.create_notes(7)

    A = Strings("A")
    A.create_notes(0)

    D = Strings("D")
    D.create_notes(5)

    G = Strings("G")
    G.create_notes(10)

    B = Strings("B")
    B.create_notes(2)

    e = Strings("e")
    e.create_notes(7)

    StringChart = {1:e, 2:B, 3:G, 4:D, 5:A, 6:E}
    
    def get_fret(self, string, note):
        """Gets the fret of a specific note on a specific string"""
        return StringChart[string].get_fret(note)


