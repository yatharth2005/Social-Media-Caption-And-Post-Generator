def enhance_caption(caption):
    hashtags=[]
    emojis=[]

    words=caption.lower().split()
    for word in words:
        if word in ["fitness","health","gym"]:
            hashtags+=["#FitnessGoals","#StayHealthy"]
            emojis+=["💪","🏋️"]
        elif word in ["travel","adventure","trip"]:
            hashtags+=["#Wanderlust","#TravelDiaries"]
            emojis+=["✈️", "🌍"]
        elif word in ["ai","tech","coding"]:
            hashtags+=["#AI","#TechLife"]
            emojis+=["🤖","💻"]
        elif word in ["motivation","inspiration"]:
            hashtags+=["#MondayMotivation","#DailyInspo"]
            emojis+=["🔥","🚀"]

    if not hashtags:
        hashtags=["#Awesome","#SocialPost"]
    if not emojis:
        emojis=["✨","🌟"]

    return f"{caption}\n\n{' '.join(emojis)}{' '.join(hashtags)}"
