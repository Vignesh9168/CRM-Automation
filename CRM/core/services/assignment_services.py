# services/assignment_service.py

from ..models import Agent, Lead


def assign_lead(lead):

    # Step 1 → check lead priority
    if lead.priority == "High":
        agent = priority_assignment()

    else:
        agent = round_robin_assignment()

    # Step 2 → assign lead
    if agent:
        lead.assigned_to = agent
        lead.save()

    return lead


def available_agent_assignment():

    """
    Returns only available agents
    """

    agents = Agent.objects.filter(
        is_available=True
    ).order_by("id")

    return agents   


def round_robin_assignment():

    """
    Assign leads one by one in rotation
    """

    agents = available_agent_assignment()

    if not agents.exists():
        return None

    # Get last assigned lead
    last_lead = Lead.objects.exclude(
        assigned_to=None
    ).order_by("-id").first()

    # First lead assignment
    if not last_lead:
        return agents.first()

    last_agent = last_lead.assigned_to

    # Get current agent index
    agent_ids = list(agents.values_list("id", flat=True))

    # If last agent not available now
    if last_agent.id not in agent_ids:
        return agents.first()

    current_index = agent_ids.index(last_agent.id)

    next_index = (current_index + 1) % len(agent_ids)

    next_agent_id = agent_ids[next_index]

    next_agent = Agent.objects.get(id=next_agent_id)

    return next_agent


def priority_assignment():

    """
    High priority leads go to senior agents
    """

    senior_agents = Agent.objects.filter(
        is_available=True,
        priority_level=3
    ).order_by("id")

    if senior_agents.exists():
        return senior_agents.first()

    return round_robin_assignment()