import random

SIZE = 800
NUM_BIN = 4

select = ""
select_index = 0

member_list = [
    "member1",
    "member2",
    "member3",
    "member4",
    "member5",
    "member6"
]

class Bin:

    def __init__(self, id, x):
        self.id = id
        self.x = x
        self.name = "unknown"
        self.bin_height = -SIZE
        self.change_height = -random.randint(35, 70)*10
        self.speed = 10

    def move(self):
        if self.bin_height == self.change_height:
            self.change_height = -random.randint(35, 70)*10
        elif self.bin_height < self.change_height:
            self.bin_height += self.speed
        else:
            self.bin_height -= self.speed
        
        rect(self.x, 650, 100, self.bin_height)
        text(self.name, self.x + 50, 700)
        
    def stay(self):
        rect(self.x, 650, 100, self.bin_height)
        text(self.name, self.x + 50, 700)

    def selected(self, select_id):
        if self.id == select_id:
            self.bin_height = -SIZE
        else:
            self.bin_height = -SIZE/2
        rect(self.x, 650, 100, self.bin_height)

    def rename(self, name):
        self.name = name

def select_member(mem_list, num):
    select_index = random.randrange(num)
    return mem_list.pop(select_index), select_index

def setup():
    #frame.setTitle("Python Test")
    size(SIZE, SIZE)
    bin_x = [50, 250, 450, 650]
    global bin_list
    bin_list = [Bin(i, bin_x[i])for i in range(NUM_BIN)]
    noStroke()
    fill(255, 255, 255)

def draw():
    background(0)
    fill(255)
    textSize(25)
    textAlign(CENTER)
    
    for i in range(NUM_BIN):
        bin_list[i].stay()

    if (mousePressed):
        for i in range(NUM_BIN):
            bin_list[i].move()
        
def mousePressed():
    global select, select_index
    num = 0
    if len(member_list) < NUM_BIN:
        num = len(member_list)
        for i in range(len(member_list), NUM_BIN):
            bin_list[i].rename("unknown")
    else:
        num = NUM_BIN
    random.shuffle(member_list)
    print(member_list)
    suggest = member_list[:num]
    for index, value in enumerate(suggest):
        bin_list[index].rename(value)
    if len(suggest) > 0:
        select, select_index = select_member(member_list, num)

def mouseReleased():
    for i in range(NUM_BIN):
        bin_list[i].selected(select_index)
