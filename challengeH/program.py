#!/usr/bin/env python3

import sys
from collections import defaultdict

# parse families from input
def parse_input() -> tuple[dict[tuple[str, str], list[str]], dict[str, tuple[str, str]], list[str]] | None:
    # parse number of families, signal if end of input (num_families == 0)
    num_families = int(sys.stdin.readline().strip())
    if num_families == 0:
        return None
    
    # initialize dictionaries in both directions for traversal later on
    parents_to_children = defaultdict(list)
    children_to_parents = {}

    for _ in range(num_families):
        # parse each family
        line = sys.stdin.readline().strip()
        parents, children = line.split(':')

        # make parents and children lists
        parents  = tuple(parents.strip().split())
        children = children.strip().split()

        # add family to parents -> children dict
        parents_to_children[parents] = children

        # add family to children -> parents dict
        for child in children:
            children_to_parents[child] = parents

    # collect list of gifters
    num_gifters = int(sys.stdin.readline().strip())
    gifters = []
    for _ in range(num_gifters):
        name = sys.stdin.readline().strip()
        gifters.append(name)

    # post-parsing to add in-law relationships
    for parent1, parent2 in parents_to_children.keys():
        if parent2 not in children_to_parents and parent1 not in children_to_parents:
            continue
        elif parent2 not in children_to_parents:
            children_to_parents[parent2] = children_to_parents[parent1]
        elif parent1 not in children_to_parents:
            children_to_parents[parent1] = children_to_parents[parent2]
        else:
            continue

    # return tuple of dicts and gifters list
    return parents_to_children, children_to_parents, gifters

# determine nieces and nephews that a certain gifter needs to buy gifts for
def find_niece_neph(gifter: str, parents_to_children, children_to_parents) -> list[str] | None:
    # determine if gifter is at the root (does not need to buy gifts)
    if not gifter in children_to_parents:
        return None

    # find married pair of the gifter
    married_pair = None
    for pair in parents_to_children:
        if gifter in pair:
            married_pair = pair
            break

    # find biological siblings of gifter
    bio_siblings = []
    bio_parents = children_to_parents.get(gifter)
    if bio_parents:
        bio_siblings = [s for s in parents_to_children[bio_parents] if s != gifter and (s not in married_pair if married_pair else True)]

    # find in-law siblings of gifter
    spouse = None

    # find the spouse of gifter
    if married_pair:
        spouse = married_pair[1] if married_pair[0] == gifter else married_pair[0]

    # find the in-law siblings of the spouse
    inlaw_siblings = []
    spouse_parents = children_to_parents.get(spouse)
    if spouse_parents:
        inlaw_siblings = [s for s in parents_to_children[spouse_parents] if s != spouse and (s not in married_pair if married_pair else True)]

    # collect children of all siblings and in-law siblings
    recipients = set()
    for sibling in bio_siblings + inlaw_siblings:
        for pair in parents_to_children:
            if sibling in pair:
                for child in parents_to_children[pair]:
                    recipients.add(child)

    # return the list of recipients for gifter
    return sorted(recipients) if recipients else None

# main driver
def main():
    while True:
        # parse the families and break if end of input
        result = parse_input()
        if not result:
            break

        # split up results of parsing
        parents_to_children, children_to_parents, gifters = result

        # loop through gifters and call algorithm on each gifter
        for gifter in gifters:
            niece_neph = find_niece_neph(gifter, parents_to_children, children_to_parents)

            # print statements
            if not niece_neph:
                print(f"{gifter} does not need to buy gifts")
            else:
                print(f"{gifter} needs to buy gifts for: {', '.join(niece_neph)}")

if __name__ == "__main__":
    main()