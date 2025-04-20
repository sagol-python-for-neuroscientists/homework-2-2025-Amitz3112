
from shared import Condition


def only_meeters(agent_list:tuple )-> tuple:
    """
    Takes out the Agents that are not taking part in the meeting. 

    Parameters
    ----------
    agent_listing: Tuple of Agents
    A listing of Agents in which each Agent has a name and a category.

    Returns
    -------
    meeters: Tuple of Agents
    An updated listing of agents where only "SICK", "DYING", and "CURE" are in.  
    """
    meeters=(agent for agent in agent_list if agent.category not in (Condition.DEAD, Condition.HEALTHY))
    return tuple(meeters)
    
    
    



