from tkinter import Tk, simpledialog, messagebox

def read_from_file():
    with open("manager_data.txt") as file:
        for line in file:
            line = line.rstrip('\n')
            club,manager = line.split('/')
            the_sports[club] = manager
def write_to_file(club_name,manager_name):
    with open('manager_data.txt','a') as file:
        file.write(club_name + '/' + manager_name + '\n')

print('Ask the Sports Club manager program')
root = Tk()
root.withdraw()
the_sports = {}

read_from_file()
while True:
    query_club = simpledialog.askstring('Club','ENTER THE NAME OF THE CLUB:')
    query_club = query_club.capitalize()
    if query_club in the_sports:
        result = the_sports[query_club]
        messagebox.showinfo('REPLY','The current manager of ' + str (query_club) + ' is ' + result + '!')
    else:
        new_manager = simpledialog.askstring('TELL ME','I don\'t know '+'Who is the current manager of ' + str(query_club) + ' ?')
        the_sports[query_club] = new_manager
        #print (the_sports)
        write_to_file(query_club,new_manager)
