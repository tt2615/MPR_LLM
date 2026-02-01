INIT_PROMPT = f"Your task is to recommend a user’s next point-of-interest (POI) from the candidate POIs %s by analyzing the users’ preferences on category, region, and distance."

CAT_EXT_PROMPT = f"Given the user’s Category sequence: %s, what is the user’s categorical transition preference? Considering: what are the ‘category pairs’ the user usually visits consecutively? (format:category-category,...) What is the user’s categorical temporal preference? Considering: what are the ‘categories’ the user visits at a certain time (day/hour)? (format:time: [categories]). Omit reasoning"

CAT_PRE_PROMPT = f"The user has visited categories %s. Based on the user’s categorical transition preference and categorical temporal preference, predict users’ next most likely visiting ‘category’. (format:category). Omit reasoning"

REG_EXT_PROMPT = f"Given the user’s Region sequence: %s, what is the user’s regional transition preference? Considering: what are the region pairs’ the user usually visits consecutively? (format:region-region,...) What is the user’s regional temporal preference? Considering: what are the regions the user visits at a certain time (day/hour)? (format:time: [region]). Omit reasoning"

REG_PRE_PROMPT = f"The user has visited categories %s. Based on the user’s regional transition preference and regional temporal preference, predict users’ next most likely visiting region. (format:category). Omit reasoning"

DIS_EXT_PROMPT = f"Given the user’s Category sequence: %s, what is the user’s distance temporal preference? Considering: what are the distances the user visits at a certain time (day/hour)? (format:time: [ditance]). Omit reasoning"

DIS_PRE_PROMPT = f"The user has visited categories %s. Based on the user’s distance temporal preference, predict users’ next most likely visiting distance. (format:ditance). Omit reasoning"

REC_PROMPT = f"Given users’ current check-in sequence %s, recommend 10 POIs from %s considering his next likely visiting category, region, and distance. State the reason for each recommendation and rank the importance of category, region, and distance preferences. (format: POI: reason; [importance ranking])"
