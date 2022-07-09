#camera-recommender
#the previous version of this program incorporated a series of functions which called eachother and made suggestions based on the returned value of the functions.
#while effective, the structure was a but confusing to read and a bit messy, so this time the plan is to make something neater and easier to read. 
#the plan is to use a tree which starts with a first question and branches out, with the children being the result of certain choices the user makes as they answer questions on what their camera preferences are
#down the road, it may be interesting to consider some sort of machine learning into the program to better decide what the user might be interested; for now, the program will remain the same in terms of deciding which camera to suggest to the user as the previous version of this program
    #for now I dont think the amount of choices and cameras for me to recommend is vast enought to need some sort of machine learning-based recommendation, but the idea could be interesting should I eventually choose to try some kind of project based on that 



#choices are nodes which contain the the input function which get called and asks the user to select their camera preferences. Depending on what the input is we need to be able to connect that with the correct child node
class Choice:

    #the actions dictionary is what we use to traverse the nodes and decide which one is the correct next node based on user input. The structure for the actions dictionary is {'topic: [listof topics], 'inputstring': "string", 'recommendation': "camera recommendation"}
    #Using this structure will make it to where we can ask for an input if an input string exists, and suggest a recommendation if there is no longer a need for user input, meaning we have determined what their recommendation is
    def __init__(self, actions = None):
        self.actions = actions #this is a dictionary
        self.children = []
        
    def __repr__(self):
        if type(self.actions['topic']) == list:
            return "/".join(self.actions['topic'])
        else:
            return self.actions['topic']
        
    def get_children(self):
        return self.children
    
    #might be able to clean this up
    def add_child(self, child):
        child_list = self.children
        child_list.append(child)
        self.children = child_list
        return self.children

#need to figure out why nothing happens after the first input. The function should move on to the next node and ask for a new input or return a recommendation
def traverse(start_point):
    current_node = start_point
    current_children = start_point.children
    print (start_point.children)
    while len(current_children) > 0:
        if 'inputstring' in current_node.actions.keys():
            userinput = input(current_node.actions['inputstring'])
        else:
            return current_node['recommendation']
        for child in current_children:
            if userinput.lower() in child.actions['topic']:
                current_node = child
                current_children = current_node.children
            else:
                pass
         
        
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
        {
            'topic': ["first_choice"],
            'inputstring': "What types of photos do you want to take? (Portraits, landscapes, pics of your friends, quick snapshots or maybe a little bit of everything: \n"
        }
            
)

first_choice_child1 = Choice(
        {
            'topic': ["portraits", "landscapes"],
            'inputstring': "Nice. Do you wand a camera with a fixed lens or do you want to be able to switch lenses? \n"
        }
)

first_choice_child2 = Choice(
        {
            'topic': ["friend", "snap"],
            'inputstring' :"You're probably best off with a point and shoot camera. What's your budget? \n"
        }
)

first_choice_child3 = Choice(
        {
            'topic': ["everything"],
            'inputstring': None,
            'recommendation':"Your best bet would be the Minolta Hi-Matic 7S."
            
        }
)


first_choice.add_child(first_choice_child1)
first_choice.add_child(first_choice_child2)
first_choice.add_child(first_choice_child3)


traverse(first_choice)


        

#also need to figure out how to more effectively move back up to the past node if we get an input we cant work with as opposed to restarting the while script as with the last program. The nodes may make that a possibility. 
    #perhaps a recursive call

#at some point we have to figure out what to do when the user submits an invalid input