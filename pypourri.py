def human2machine(human_input,exact_matches,prefixes=(None,),icase=True):
    """Coerce an ambiguous or imprecise input string into an exact match or None.

    exact_matches is a tuple or list of tuples of strings, e.g.:
    [ ('infinite','permanent','always'), ('never','impossible') ]
    The human_input is matched against every string and if there is an exact
    match, the [0] element of the tuple where the match occurred is returned.
    prefixes is an optional tuple or list of tuples of strings, e.g.:
    [ ('prema','inif','inf'), ('no','forget','surely n')] which is a set of prefixes
    that must correspond to the exact matches and will be tested against the human
    input as well. If one of the prefixes is found as a prefix of the human_input,
    again the [0] element of the corresponding *exact* matches will be returned.
    The optional prefixes are mainly there to catch typos. An list of exact matches
    must always exist, the corresponding prefix list may be given as None.
    If icase==True (default), then the input is converted to lowercase which
    requires all matches and prefixes to be lowercase also."""
    if icase:
        human_input = human_input.lower()
    prefixes = prefixes + (None,)*(len(exact_matches)-len(prefixes))
    for exacts,prefixes in zip(exact_matches,prefixes):
        if (human_input in exacts) or prefixes and any(map(human_input.startswith,prefixes)):
            return exacts[0]
    return None
    
