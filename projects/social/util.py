names = ['Paula', 'Ima', 'Cecile', 'Josue', 'Scotty', 'Lavada', 'Roosevelt', 'Delores',  'Carlos',  'Doyle',  'Keaton',  'Emmitt',  'Fatima',  'Hoyt',  'Stan',  'Davonte',  'Alyson',  'Tanner',  'Ali',  'Eulalia',  'Aurelio',  'Kathleen',  'Dee',  'Santina',  'Fay',  'Lavada',  'Kylee',  'Maximus',  'Ezra',  'Lucius',  'Alice',  'Granville',  'Irwin',  'Jose',  'Anastasia',  'Madalyn',  'Boyd',  'Barney',  'Minerva',  'Liam',  'Donnell',  'Khalil',  'Asia',  'Priscilla',  'Louie',  'Breanne',  'Rhiannon',  'Eliza',  'Mose',  'Elyssa',  'Winnifred',  'Sanford',  'Arturo',  'Barrett',  'Mariana',  'Braulio',  'Angelina',  'Julia',  'Creola',  'Taylor',  'Angelo',  'Rosetta',  'Timmothy',  'George',  'Lesley',  'Jorge',  'Clement',  'Adell',  'Annette',  'Erika',  'Alessandra',  'Adriel',  'Sydni',  'Manuel',  'Terrance',  'Adriana',  'Julie',  'Vivian',  'Unique',  'Rachel',  'Cloyd',  'Rodrigo',  'Cicero',  'Maggie',  'Tyshawn',  'Cassidy',  'Eveline',  'Octavia',  'Jeramy',  'Adrain',  'Sofia',  'Craig',  'Ephraim',  'Zula',  'Carey',  'Lamont',  'Stanton',  'Loraine',  'Lesley',  'Melissa']

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

