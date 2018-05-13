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
        self.bin_height = -SIZE/2
        self.change_height = -random.randint(20, 60)*10
        self.speed = 10

    def move(self):
        if self.bin_height == self.change_height:
            self.change_height = -random.randint(20, 60)*10
        elif self.bin_height < self.change_height:
            self.bin_height += self.speed
        else:
            self.bin_height -= self.speed

        fill(0)
        text(self.name, self.x + 50, 700)
        fill(0, 64, -float(self.bin_height)/SIZE*255)
        rect(self.x, 650, 100, self.bin_height)
        
    def stay(self):
        fill(0, 64, -float(self.bin_height)/SIZE*255)
        rect(self.x, 650, 100, self.bin_height)
        fill(0)
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

def draw():
    background(255)
    textSize(25)
    textAlign(CENTER)
    
    if (mousePressed):
        for i in range(NUM_BIN):
            bin_list[i].move()
    else:
        for i in range(NUM_BIN):
            bin_list[i].stay()

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
