import numpy as np

class QLearningAgent:
    def __init__(self, nb_X, num_actions = 4, alpha=0.1, gamma=0.99, epsilon=0.1):
        self.nb_X = nb_X
        self.nb_Y = nb_X
        self.num_states = nb_X * nb_X
        self.num_actions = num_actions
        self.possible_actions = np.arange(0, self.num_actions)
        self.alpha = alpha  # Taux d'apprentissage
        self.gamma = gamma  # Facteur d'actualisation
        self.epsilon = epsilon  # Taux d'exploration
        self.q_table = np.zeros((self.num_states, self.num_actions))       
        self.state = np.random.randint(0, self.num_states)
        self.previous_state = self.state
        self.x = self.state % self.nb_X
        self.y = self.state // self.nb_Y
        self.index_state = 0
        self.x_target = 0
        self.y_target = 0
        self.nb_episodes = 1000

    def choose_random_state(self):
        self.state = np.random.randint(0, self.num_states)
        self.previous_state = self.state
        self.x = self.state % self.nb_X
        self.y = self.state // self.nb_Y

    def choose_action(self):
        if np.random.uniform(0, 1) < self.epsilon:
            # Exploration : Choix d'une action aléatoire
            return np.random.choice(self.possible_actions)
        else:
            # Exploitation : Choix de l'action avec la plus grande valeur Q
            return np.argmax(self.q_table[self.state, :])

    def move(self):
        action = self.choose_action()
        self.change_state(action)   
        self.index_state += 1
        print("state n° " + str(self.index_state) + " state = " + str(self.state) + " x = " + str(self.x) + " y = " + str(self.y))
            
    def change_state(self, action):
        self.previous_state = self.state
        if action == 0: #up
            self.y = max(0, (self.y - 1))
        elif action == 1: #right
            self.x = min(self.nb_X - 1, (self.x + 1))
        elif action == 2: #down
            self.y = min(self.nb_Y - 1, (self.y + 1))
        elif action == 3: #left
            self.x = max(0, (self.x - 1))
        self.state = self.nb_Y*self.y + self.x

        
    def update_q_table(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table[next_state, :])
        td_target = reward + self.gamma * self.q_table[next_state, best_next_action]
        td_error = td_target - self.q_table[state, action]
        self.q_table[state, action] += self.alpha * td_error
        

    def learn(self):
        print("learning...")
        n0_episode = 0
        for _ in range(self.nb_episodes):
            print("n0_episode = " + str(n0_episode))
            n0_episode += 1
            self.choose_random_state()
            while True:
                action = self.choose_action()
                self.change_state(action)
                reward = 0
                if self.x == self.x_target and self.y == self.y_target:
                    reward = 1                    
                self.update_q_table(self.previous_state, action, reward, self.state)
                if self.x == self.x_target and self.y == self.y_target:
                    break          
        print("learning finished")     
        self.choose_random_state()
