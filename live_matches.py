def liveMatch(matches):
    liveMatches = get_live_matches(matches)
    if not liveMatches:
        return "No matches are currently live."
    game = (matches["homeTeam"]["name"],  matches["score"]["fullTime"]["home"], matches["score"]["fullTime"]["away"], matches["awayTeam"]["name"])
    return game
