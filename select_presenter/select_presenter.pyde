import random

SIZE = 800
NUM_BIN = 4

select = ""
select_index = 0

bin_x = [50, 250, 450, 650]
bin_height = [- SIZE / 2 for _ in range(NUM_BIN)]
bin_name = ["unknown" for _ in range(NUM_BIN)]
change_height = bin_height

member_list = [
    "member1",
    "member2",
    "member3",
    "member4",
    "member5",
    "member6"
]

def select_member(mem_list, num):
    select_index = random.randrange(num)
    return mem_list.pop(select_index), select_index

def setup():
    #frame.setTitle("Python Test")
    size(SIZE, SIZE)
    noStroke()
    fill(255, 255, 255)

def draw():
    global change_height
    background(0)
    fill(255)
    textSize(25);
    textAlign(CENTER);
    bin_height = change_height
    for i in range(NUM_BIN):
        rect(bin_x[i], 650, 100, bin_height[i])
        text(bin_name[i], bin_x[i]+50 , 700)
    if (mousePressed):
        if change_height == bin_height:
            change_height = [-random.randint(350, 700) for _ in range(NUM_BIN)]

def mousePressed():
    global change_height, select, select_index, bin_name
    num = 0
    if len(member_list) < NUM_BIN : 
        num = len(member_list) 
        for i in range(len(member_list), NUM_BIN):
            bin_name[i] = "unknown"
    else: 
        num = NUM_BIN
    random.shuffle(member_list)
    print(member_list)
    suggest = member_list[:num]
    for index, value in enumerate(suggest):
        bin_name[index] = value
    if len(suggest) > 0:
        select, select_index = select_member(member_list, num)
    
def mouseReleased():
    global change_height
    change_height = [-SIZE/2 if i != select_index else -SIZE for i in range(NUM_BIN)]
