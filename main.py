# Tyler Moore, Ian Riley
# Python implementation of stable matching problem
# Homework 1 Starter Code
# CS 2123 last modified 1/14/19

# Tom Sommers, Dina Binmansour, Eric Schnelker - 1/18/19
# Completion of starter code for Gale Shapley implementation
"""
_____________
PSEUDOCODE:
_____________
INITIALIZE S to empty matching.

WHILE (some man m is unmatched and hasn't proposed to every woman)
  WHILE (c, the index of some woman on m's list to whom m has not yet proposed to [where i is initialized to 0), is less than the length of m's preference list)
      IF (w is unmatched)
        Add pair m–w to matching S.
      ELSE IF (w prefers m to her current partner m')
        Remove pair m'–w from matching S.
        Add pair m–w to matching S.
      ELSE
        w rejects m.
        increment w by one
RETURN stable matching S.
"""


def gs(men, women, pref):
    matchedPairs = {}  # initialize dictionary to keep track of pairs
    s = []  # Tuples to contain pairs
    q = men

    print()
    print("The pairing games have begun... Place your bets on the order in which contestants pairs will survive.")
    print("...")
    print("What's that...?")
    print("This isn't a death match...? ")
    print("... What the hell are you paying me for, then?")
    print("Oh?")
    print("They're placing bets on who will be succesfully paired and married? ")
    print("So it IS a death match! Alright, then.")
    print("Ready. ")
    print("Set.")
    print("BEGIN!!!")

    while q:
        m = q.pop(0)
        for w in pref[m]:
            if w not in matchedPairs:
                matchedPairs[w] = m
                print("Pairing " + m + " with " + w + ". Adding the happy couple to matched pairs. They have won the round. Next round - BEGIN!")
                break
            elif pref[w].index(m) < pref[w].index(matchedPairs.get(w)) and m not in matchedPairs:
                mrDumped = matchedPairs.get(w)
                print(mrDumped + " is hopeless and was dumped by " + w + ". Adding him back to the queue and pairing " + w + " with " + m)
                matchedPairs[w] = m
                q.append(mrDumped)
                break

    for w in women:
        s.append((matchedPairs.get(w), w))

    return (s)


"""
      Gale-Shapley algorithm
      Inputs: men (list of men's names)
              women (list of women's names)
              pref (dictionary of preferences mapping names to
                  list of preferred names in sorted order)
      Output: the stable match S which is a
          list of tuples of the form (man, woman)
  """

def gs_block(men, women, pref, blocked):



  """
  Gale-Shapley algorithm, modified to exclude unacceptable matches
  Inputs: men (list of men's names)
          women (list of women's names)
          pref (dictionary of preferences mapping names to
              list of preferred names in sorted order)
          blocked (list of (man, woman) tuples that are unacceptable matches)
  Output: the modified stable match S which is a
      list of tuples of the form (man, woman)
  """


def gs_tie(men, women, preftie):
  """
  Gale-Shapley algorithm, modified to use preferences with ties
  Inputs: men (list of men's names)
          women (list of women's names)
          preftie (dictionary of preferences mapping names to
              list of sets of preferred names in sorted order)
  Output: the stable match S which is a list of pairs of the form (m, w)
  """
  return "test"


if __name__ == "__main__":
  # input data
  the_men = ['xavier', 'yancey', 'zeus']
  the_women = ['amy', 'bertha', 'clare']

  the_pref = {
      'xavier': ['amy', 'bertha', 'clare'],
      'yancey': ['bertha', 'amy', 'clare'],
      'zeus': ['amy', 'bertha', 'clare'],
      'amy': ['yancey', 'xavier', 'zeus'],
      'bertha': ['xavier', 'yancey', 'zeus'],
      'clare': ['xavier', 'yancey', 'zeus']
  }

  the_preftie = {
      'xavier': [{'bertha'}, {'amy'}, {'clare'}],
      'yancey': [{'amy', 'bertha'}, {'clare'}],
      'zeus': [{'amy'}, {'bertha', 'clare'}],
      'amy': [{'zeus', 'xavier', 'yancey'}],
      'bertha': [{'zeus'}, {'xavier'}, {'yancey'}],
      'clare': [{'xavier', 'yancey'}, {'zeus'}]
  }

  blocked = {
      ('xavier', 'clare'),
      ('zeus', 'clare'),
      ('zeus', 'amy'),
      ('yancey', 'bertha')
  }

  match = gs(the_men, the_women, the_pref)
  print(match)

  match_block = gs_block(the_men, the_women, the_pref, blocked)
  print(match_block)

  match_tie = gs_tie(the_men, the_women, the_preftie)
  print(match_tie)
