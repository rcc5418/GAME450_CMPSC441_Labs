'''
Lab 4: Rock-Paper-Scissor AI Agent

In this lab you will build one AI agent for the game of Rock-Paper-Scissors, that can defeat a few different kinds of 
computer players.

You will update the AI agent class to create your first AI agent for this course.
Use the precept sequence to find out which opponent agent you are facing, 
so that it can beat these three opponent agents:

    Agent Single:  this agent picks a weapon at random at the start, 
                   and always plays that weapon.  
                   For example: 2,2,2,2,2,2,2,.....

    Agent Switch:  this agent picks a weapon at random at the start,
                   and randomly picks a weapon once every 10 rounds.  
                   For example:  2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,...

    Agent Mimic:  this agent picks a weapon at random in the first round, 
                  and then always does what you did the previous round.  
                  For example:  if you played 1,2,0,1,2,0,1,2,0,...  
                   then this agent would play 0,1,2,0,1,2,0,1,2,...

Discussions in lab:  You don't know ahead of time which opponent you will be facing, 
so the first few rounds will be used to figure this out.   How?

Once you've figured out the opponent, apply rules against that opponent. 
A model-based reflex agent uses rules (determined by its human creator) to decide which action to take.

If your AI is totally random, you should be expected to win about 33% of the time, so here is the requirement:  
In 100 rounds, you should consistently win at least 85 rounds to be considered a winner.

You get a 0 point for beating the single agent, 1 points for beating the switch agent, 
and 4 points for beating the mimic agent.

'''

from rock_paper_scissor import Player
from rock_paper_scissor import run_game
from rock_paper_scissor import random_weapon_select

class AiPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.initial_weapon = random_weapon_select()
    
    def weapon_selecting_strategy(self):
        default_move= random_weapon_select()
        if (len(self.opponent_choices) == 0):
            return default_move
        #Check if single
        is_single = True
        for past_moves in range(len(self.opponent_choices)):
            for current_move in range(past_moves):
                if(self.opponent_choices[past_moves] != self.opponent_choices[current_move]):
                    is_single = False
                    break
        #Check if switch
        if (not is_single): #(not is_single)
            is_switch=False
            first_10_same = True
            if len(self.opponent_choices) >= 10:
                for move1 in range(10):
                    if(self.opponent_choices[move1] != self.opponent_choices[0]):
                        first_10_same = False
                        break
                if(first_10_same):
                    is_switch = True
        #Check if mimic
        is_mimic = False
        if ((not is_single) and (not is_switch)):
            is_mimic = True

        #counter single
        if(is_single):
            if(self.opponent_choices[0] == 0):
                return 1
            if(self.opponent_choices[0] == 1):
                return 2
            if(self.opponent_choices[0] == 2):
                return 0
        #counter switch
        if(is_switch):
            num_rounds=len(self.my_choices)
            if(num_rounds % 10 == 0):
                return default_move #He's going to switch things up every 10th round
            else:                   #If we know he's not switching things up, we can just counter his last move.
                if(self.opponent_choices[-1] == 0):
                    return 1
                if(self.opponent_choices[-1] == 1):
                    return 2
                if(self.opponent_choices[-1] == 2):
                    return 0
        #counter mimic
        if(is_mimic):
            opponent_next_choice = self.my_choices[-1] #He's copying me, so we can tell what move he'll use/
            if( opponent_next_choice == 0):
                return 1
            if( opponent_next_choice == 1):
                return 2
            if( opponent_next_choice == 2):
                return 0
        return default_move


if __name__ == '__main__':
    final_tally = [0]*3
    for agent in range(3):
        for i in range(100):
            tally = [score for _, score in run_game(AiPlayer("AI"), 100, agent)]
            if sum(tally) == 0:
                final_tally[agent] = 0
            else:
                final_tally[agent] += tally[0]/sum(tally)

    print("Final tally: ", final_tally)  