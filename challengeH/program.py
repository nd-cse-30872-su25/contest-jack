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
        try:
            children_to_parents[parent2] = children_to_parents[parent1]
        except KeyError:
            continue

    # return tuple of dicts and gifters list
    return parents_to_children, children_to_parents, gifters

# determine nieces and nephews that a certain gifter needs to buy gifts for
def find_niece_neph(gifter: str, parents_to_children, children_to_parents) -> list[str] | None:
    # determine if gifter is at the root (does not need to buy gifts)
    if not gifter in children_to_parents:
        return None

    # find parents of gifter
    parents  = children_to_parents[gifter]

    # locate marreid pair of gifter if it exists
    married_pair = None
    for parent_pair in parents_to_children.keys():
        if gifter in parent_pair:
            married_pair = tuple(parent_pair)

    # find siblings/siblings-in-law of married pair for gifter (disclude gifter and spouse)
    if married_pair:
        siblings = [sibling for sibling in parents_to_children[parents] if not sibling in married_pair]
    else:
        siblings = [sibling for sibling in parents_to_children[parents] if sibling != gifter]

    # add all of siblings' children to recipient set (set so there are no duplicates)
    recipients = set()
    for sibling in siblings:
        for pair in parents_to_children.keys():
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