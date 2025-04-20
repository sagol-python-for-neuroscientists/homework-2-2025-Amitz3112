from shared import Condition
from shared import Agent
from hw2_q2a import only_meeters
from hw2_q2b import now_we_meet

def meetup(agent_listing: tuple) -> list:
    """Model the outcome of the meetings of pairs of agents.

    The pairs of agents are ((a[0], a[1]), (a[2], a[3]), ...). If there's an uneven
    number of agents, the last agent will remain the same.

    Notes
    -----
    The rules governing the meetings were described in the question. The outgoing
    listing may change its internal ordering relative to the incoming one.

    Parameters
    ----------
    agent_listing : tuple of Agent
        A listing (tuple in this case) in which each element is of the Agent
        type, containing a 'name' field and a 'category' field, with 'category' being
        of the type Condition.

    Returns
    -------
    updated_listing : list
        A list of Agents with their 'category' field changed according to the result
        of the meeting.
    """
    
    #Taking out healthy and dead agents
    meeters=only_meeters(agent_listing)

    #non-dead and non-healthy agents meet and change status
    updated_agents=now_we_meet(meeters)
    
    #Concatenate updated agents list and excluded non-meeters list
    for Agent in agent_listing:
        if Agent.category == Condition.HEALTHY or Agent.category == Condition.DEAD:
            updated_agents.append(Agent)
    return(updated_agents)