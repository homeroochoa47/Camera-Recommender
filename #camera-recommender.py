#camera-recommender
#the previous version of this program incorporated a series of functions which called eachother and made suggestions based on the returned value of the functions.
#while effective, the structure was a but confusing to read and a bit messy, so this time the plan is to make something neater and easier to read. 
#this program is structured as a tree, where we collect inputs starting at the root and move down along the child nodes depending on what the user inputs are. Once we reach a leaf node we return a camera recommendation for the user based on the path their inputs took us down.


#choices are nodes which contain the the input function which get called and asks the user to select their camera preferences. Depending on what the input is we move to the corresponding child node. We search through the topics in the child nodes and match that with the user input to select which node to move to.
class Choice:

    #the actions dictionary is what we use to traverse the nodes and decide which one is the correct next node based on user input. The structure for the actions dictionary is {'topic: [listof topics], 'inputstring': "string", 'recommendation': "camera recommendation"}
    #Using this structure will make it to where we can ask for an input if an input string exists, and suggest a recommendation if there is no longer a need for user input, meaning we have determined what to recommend them
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

def request_input(node):
    userinput = input(node.actions['inputstring'])
    return userinput

def restart():
    restart = input('Would you like to start over? ')
    if "y" in restart.lower():
        return traverse(root)
    elif "n" in restart.lower():
        print ("See ya!")
        return
    else:
        print ("Enter yes or no")
        return restart()

def give_recommendation(node):
    print(node.actions['recommendation'])
    return restart()


#function was made to call recursively. Works for now, but will require further refining once all of the tree nodes are added.
def traverse(start_point):
    current_node = start_point
    current_children = start_point.children
    #base case
    if 'recommendation' in current_node.actions.keys():
        return give_recommendation(current_node)
        #call function to get more info or start over
    
    #recursive call
    if 'inputstring' in current_node.actions.keys():
        userinput = request_input(current_node)
        
    for child in current_children:
        for topic in child.actions['topic']:       
            if topic in userinput.lower():
                return traverse(child)
            
    print ("Sorry, I didn't get that. Please try again.")
    traverse(current_node)

#maybe add a fourth child in each node that returns to the beginning if the user entered an invalid input
#need to update node names to clarify the structure of the trees
root = Choice(
        {
            'topic': ["first_choice"],
            'inputstring': "What types of photos do you want to take? (Portraits, landscapes, pics of your friends, quick snapshots or maybe a little bit of everything: \n"
        }
            
)

#second level
#---------------------
#portraits or landscapes
root_child1 = Choice(
        {
            'topic': ["portraits", "landscapes"],
            'inputstring': "Nice. Do you wand a camera with a fixed lens or do you want to be able to switch lenses? \n"
        }
)
#snapshots or friends
root_child2 = Choice(
        {
            'topic': ["friends", "snapshots"],
            'inputstring' :"You're probably best off with a point and shoot camera. What's your budget? Enter 'a' for under $50, 'b' for $51-$150, or 'c' for $150+ \n"
        }
)
#everything
root_child3 = Choice(
        {
            'topic': ["everything"],
            'recommendation':"Your best bet would be the Minolta Hi-Matic 7S." 
        }
)
#---------------------
#under root child 1
portraits_landscapes_fixed = Choice(
        {
        'topic': ['fixed'], 
        'inputstring': "Fixed lens it is. Now, are you interested in a fully mechanical camera, or one that relies on batteries? \n"
        }
)
#under root child 1
portraits_landscapes_interchangeable = Choice(
    {
        'topic': ['switch', 'lenses'],
        'inputstring': "So you'd prefer something with interchangeable lenses. Do you want battery powered or fully mechanical? \n"
    }
)
#---------------------
#under portraits and landscapes -- fixed
fixed_mechanical = Choice(
    {
        'topic': ['mechanical', 'mech'],
        'recommendation': "You might like the Olympus 35 RC"
    }
)
#under portraits and labdscapes -- fixed
fixed_battery = Choice(
    {
        'topic': ['battery', 'batt'],
        'recommencation': "You might like the Olympus XA"
    }
)
#---------------------
#under portraits and landscapes -- interchangeable
interchangeable_mechanical = Choice(
    {
        'topic': ['mechanical', 'mech'],
        'recommendation': "How about the Nikon FM?"
    }
)

interchangeable_battery = Choice(
    {
        'topic': ['battery', 'batt'],
        'recommendation': "How about the Nikon FE?"
    }
)
#---------------------
#under root child 2
snapshots_under50 = Choice(
    {
        'topic': ['a'],
        'recommendation': "Check out the Pentax IQZoom"
    }
)

snapshots_51_150 = Choice(
    {
        'topic': ['b'],
        'recommendation':  "Check out the Olympus Stylus Zoom"
    }
)

snapshots_any_price = Choice(
    {
        'topic': ['c'],
        'recommendation': "Check out the Konica Big Mini"
    }
)
#---------------------

#second level
root.add_child(root_child1)
root.add_child(root_child2)
root.add_child(root_child3)

#third level
root_child1.add_child(portraits_landscapes_fixed)
root_child1.add_child(portraits_landscapes_interchangeable)

root_child2.add_child(snapshots_under50)
root_child2.add_child(snapshots_51_150)
root_child2.add_child(snapshots_any_price)

#fourth level
portraits_landscapes_fixed.add_child(fixed_mechanical)
portraits_landscapes_fixed.add_child(fixed_battery)

portraits_landscapes_interchangeable.add_child(interchangeable_mechanical)
portraits_landscapes_interchangeable.add_child(interchangeable_battery)



print ("\nWelcome to the best friend of the modern youth: a tool that helps you figure out what film camera you should buy! What an exciting way to kick off your new hobby.\n")
print ("Lets start with a few questions to figure out the right choice for you.\n")
traverse(root)

