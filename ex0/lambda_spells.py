#!/usr/bin/env python3

# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    lambda_spells.py                                  :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/05/23 22:52:55 by orhernan         #+#    #+#              #
#    Updated: 2026/05/24 00:09:12 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from typing import TypedDict, TypeAlias


class Artifact(TypedDict):
    name: str
    power: int
    type: str


ArtifactList: TypeAlias = list[Artifact]


class Mage(TypedDict):
    name: str
    power: int
    element: str


MageList: TypeAlias = list[Mage]

SpellList: TypeAlias = list[str]


class MageStats(TypedDict):
    max_power: int
    min_power: int
    avg_power: float


def artifact_sorter(artifacts: ArtifactList) -> ArtifactList:
    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True
    )


def power_filter(mages: MageList, min_power: int) -> MageList:
    return list(filter(
        lambda mage: mage["power"] >= min_power,
        mages
    ))


def spell_transformer(spells: SpellList) -> SpellList:
    return list(map(
        lambda spell: f"* {spell} *",
        spells
    ))


def mage_stats(mages: MageList) -> MageStats:
    max_power = max(mages, key=lambda mage: mage["power"])["power"]

    min_power = min(mages, key=lambda mage: mage["power"])["power"]

    avg_power = round(
        sum(map(lambda mage: mage["power"], mages)) / len(mages), 2
    )

    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
    }


def main() -> None:

    artifacts: ArtifactList = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Rusty Dagger', 'power': 15, 'type': 'weapon'}
    ]

    mages: MageList = [
        {'name': 'Alex', 'power': 150, 'element': 'Fire'},
        {'name': 'Jordan', 'power': 80, 'element': 'Water'},
        {'name': 'Riley', 'power': 220, 'element': 'Arcane'},
        {'name': 'Sam', 'power': 45, 'element': 'Earth'}
    ]

    spells: SpellList = ["fireball", "heal", "shield"]

    single_artifact: ArtifactList = artifacts[:1]

    empty_list: ArtifactList = []

    # --- Tests ---
    print("=== Testing artifact sorter ===")
    for test_name, data in [
        ("Normal List", artifacts),
        ("Single Item", single_artifact),
        ("Empty List", empty_list)
    ]:
        print(f"\n--- {test_name} ---")
        sorted_artifacts = artifact_sorter(data)

        if len(sorted_artifacts) >= 2:
            print(
                f"{sorted_artifacts[0]['name']} "
                f"({sorted_artifacts[0]['power']} power) "
                f"comes before {sorted_artifacts[1]['name']} "
                f"({sorted_artifacts[1]['power']} power)"
            )
        elif len(sorted_artifacts) == 1:
            print(
                "Only one artifact sorted: "
                f"{sorted_artifacts[0]['name']} "
                f"({sorted_artifacts[0]['power']} power)"
            )
        else:
            print("The artifact list is empty.")

    print("\nTesting power filter (min_power = 100)...")

    powerful_mages = power_filter(mages, 100)

    if powerful_mages:
        for mage in powerful_mages:
            print(f"{mage['name']} has {mage['power']} power.")
    else:
        print("There are no powerful mages in this realm.")

    print("\nTesting spell transformer...")
    transformed = spell_transformer(spells)
    if transformed:
        print(f"{' '.join(transformed)}")
    else:
        print("Can't transform spells if none are provied")

    print("\nTesting mage stats...")
    try:
        stats = mage_stats(mages)
        print(f"Max Power: {stats['max_power']}")
        print(f"Min Power: {stats['min_power']}")
        print(f"Average Power: {stats['avg_power']}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Could not calculate stats: {e}")


if __name__ == "__main__":
    main()
