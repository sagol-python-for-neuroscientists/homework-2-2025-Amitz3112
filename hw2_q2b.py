
from itertools import batched
from shared import Condition

def now_we_meet(meeters:tuple)->list:
    """
    Sets the meetings between each agent and the consecutive one. 
    if the meeters n is uneven, the last agent remains unchanges.

    Parametes
    ---------
    meeters: Tuple of Agents
    list of Agents of the conditions "SICK", "DYING", and "CURE".  
    """
    updated_agents=[]
    for pair in batched(meeters, 2):
        if len(pair) == 2 and pair[0].category == Condition.SICK and pair[1].category == Condition.SICK:
            updated_agents.append(pair[0]._replace(category=Condition.DYING))
            updated_agents.append(pair[1]._replace(category=Condition.DYING))
        elif len(pair) == 2 and pair[0].category == Condition.SICK and pair[1].category == Condition.DYING:
            updated_agents.append(pair[0]._replace(category=Condition.DYING))
            updated_agents.append(pair[1]._replace(category=Condition.DEAD))
        elif len(pair) == 2 and pair[0].category == Condition.SICK and pair[1].category == Condition.CURE:
            updated_agents.append(pair[0]._replace(category=Condition.HEALTHY))
            updated_agents.append(pair[1]._replace(category=Condition.CURE))
        elif len(pair) == 2 and pair[0].category == Condition.CURE and pair[1].category == Condition.SICK:
            updated_agents.append(pair[0]._replace(category=Condition.CURE))
            updated_agents.append(pair[1]._replace(category=Condition.HEALTHY))
        elif len(pair) == 2 and pair[0].category == Condition.DYING and pair[1].category == Condition.DYING:
            updated_agents.append(pair[0]._replace(category=Condition.DEAD))
            updated_agents.append(pair[1]._replace(category=Condition.DEAD))
        elif len(pair) == 2 and pair[0].category == Condition.DYING and pair[1].category == Condition.SICK:
            updated_agents.append(pair[0]._replace(category=Condition.DEAD))
            updated_agents.append(pair[1]._replace(category=Condition.DYING))
        elif len(pair) == 2 and pair[0].category == Condition.DYING and pair[1].category == Condition.CURE:
            updated_agents.append(pair[0]._replace(category=Condition.SICK))
            updated_agents.append(pair[1]._replace(category=Condition.CURE))
        elif len(pair) == 2 and pair[0].category == Condition.CURE and pair[1].category == Condition.DYING:
            updated_agents.append(pair[0]._replace(category=Condition.CURE))
            updated_agents.append(pair[1]._replace(category=Condition.SICK))
        else:
            updated_agents.extend(pair)
    
    return(updated_agents)
    
    