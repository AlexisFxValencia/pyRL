import tkinter as tk
import agent


nb_X = 12
nb_Y = nb_X
# Fonction pour déplacer la case
def move(event):
    global x_case, y_case
    key = event.keysym
    if key == 'Up':
        y_case = max(y_case - 1, 0)
    elif key == 'Down':
        y_case = min(y_case + 1, nb_Y - 1)
    elif key == 'Left':
        x_case = max(x_case - 1, 0)
    elif key == 'Right':
        x_case = min(x_case + 1, nb_X - 1)
    update_grid()

# Fonction pour mettre à jour le quadrillage
def update_grid():
    for i in range(nb_Y):
        for j in range(nb_X):
            if (i, j) == (myagent.y, myagent.x):
                    color = 'red'            
            elif (i, j) == (y_case, x_case):
                color = 'blue' 
            else :
                color = 'white'
            grid[i][j].configure(bg=color)

def change_agent_state(event):
    myagent.move()
    update_grid()

def reset_agent_position():
    myagent.choose_random_state()
    update_grid()

def start_learning():
    myagent.x_target = x_case 
    myagent.y_target = y_case
    myagent.nb_episodes = int(entry.get())
    myagent.learn()
    update_grid()

# Initialiser les coordonnées de la case
x_case = 2
y_case = 3



# Créer la fenêtre principale
root = tk.Tk()
root.title("Grid")

# Créer une grille de cases
grid = []
for i in range(nb_Y):
    row = []
    for j in range(nb_X):
        cell = tk.Frame(root, width=50, height=50, bg='white', highlightbackground="black", highlightthickness=1)
        cell.grid(row=i, column=j)
        row.append(cell)
    grid.append(row)

# Lier la fonction de déplacement aux touches directionnelles
root.bind('<KeyPress>', move)

myagent = agent.QLearningAgent(nb_X)
reset_agent_position()
root.bind('<space>', change_agent_state)

# Focus sur la fenêtre principale pour capturer les événements du clavier
root.focus_set()

# Mettre à jour le quadrillage initial
update_grid()

reset_button = tk.Button(root, text="Reset Agent Position", command=reset_agent_position)
reset_button.grid(row=0, column=nb_X, rowspan=1, padx=10)
learning_button = tk.Button(root, text="Start agent learning", command=start_learning)
learning_button.grid(row=1, column=nb_X, rowspan=1, padx=10)
entry = tk.Entry(root)
entry.grid(row=2, column=nb_X, rowspan=1, padx=10)
entry.insert(0, "1000")
# Démarrer la boucle principale
root.mainloop()
