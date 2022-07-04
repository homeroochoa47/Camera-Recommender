#camera-recommender
#the previous version of this program incorporated a series of functions which called eachother and made suggestions based on the returned value of the functions.
#while effective, the structure was a but confusing to read and a bit messy, so this time the plan is to make something neater and easier to read. 
#the plan is to use a tree which starts with a first question and branches out, with the children being the result of certain choices the user makes as they answer questions on what their camera preferences are
#down the road, it may be interesting to consider some sort of machine learning into the program to better decide what the user might be interested; for now, the program will remain the same in terms of deciding which camera to suggest to the user as the previous version of this program
    #for now I dont think the amount of choices and cameras for me to recommend is vast enought to need some sort of machine learning-based recommendation, but the idea could be interesting should I choose to try some kind of project based on that down the road


#choices are nodes which contain the the input function which get called and asks the user to select their camera preferences. Depending on what the input is we need to be able to connect that with the correct child node
import re


class Choice:

    #the suggestion is the assigned topic for this node. e.g. if a user inputs portraits in the last choice, the topic for this choice would be portraits, and we would be able propertly route toward this node based on that input. 
    def __init__(self, topic = None, input = None):
        self.topic = topic
        self.input = input
        self.children = []
        self.next_node = None

    def __repr__(self):
        return ""
        
    
    def add_child(self, child):
        self.children.append(child)
    
    #we might be able to have this function be where we assign an input function to the node instead of instantiating it when the node is created.
    def request_user_input(self):
        prompt_input = input(self.input)
        return prompt_input

    #this function will be called in the traverse method to 
    def select_child(self):
        for child in children:
            if self.input == self.topic:
                self.next_node = child
        return self.next_node


def traverse(start_point):
    current_children = start_point.children
    while len(current_children) > 0:
        start_point.request_user_input()
        start_point.select_child()
         #implement the key:value pair selection w a dictionary

         
        
def show_tree_structure(start_node):
    current_children = start_node.children
    if len(current_children) == 0:
        return
    while len(current_children) > 0:
        print(start_node.topic)
        for child in current_children:
            print (f"----->{child.topic}")
        return show_tree_structure(child)

            
first_choice = Choice(
    [
        "first_choice"
    ],
    "What types of photos do you want to take? (Portraits, landscapes, pics of your friends, quick snapshots or maybe a little bit of everything: \n"
)

first_choice_child1 = Choice(
        [
            "portrait", "landscape"
        ],
            "Nice. Do you wand a camera with a fixed lens or do you want to be able to switch lenses? \n"
)

first_choice_child2 = Choice(
        [
            "friend", "snap"
        ],
             "You're probably best off with a point and shoot camera. What's your budget? \n"
)

second_choice1 = Choice()

first_choice.add_child(first_choice_child1)
first_choice.add_child(first_choice_child2)





print (show_tree_structure(first_choice))


        

#maybe add a traverse method in order to initiate the sequence and traverse through all of the nodes based on the input/script
#also need to figure out how to more effectively move back up to the past node if we get an input we cant work with as opposed to restarting the while script as with the last program. The nodes may make that a possibility. 
#this might be a recursive function in which the base case is when we determine a selection (or run out of child nodes)

#we might be able to use a dictionry to assign values of certain topics/inputs to their corrensponsing follow up question ,or the camera recommendation in a key: value pair
    #in that case we might be able to combine that with a linked list?
    
#at some point we have to figure out what to do when the user submits an invalid input