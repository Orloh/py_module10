#!/usr/bin/env python3

# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   scope_mysteries.py                                 :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: orhernan <orhernan@student.42.fr>          +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/05/26 18:10:01 by orhernan          #+#    #+#             #
#   Updated: 2026/05/26 18:10:01 by orhernan         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

from typing import Callable, Any, TypedDict


class VaultAPI(TypedDict):
    store: Callable[[str, Any], None]
    recall: Callable[[str], Any]


def mage_counter() -> Callable[[], int]:
    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    accumulated_power: int = initial_power

    def accumulator(additional_power: int) -> int:
        nonlocal accumulated_power
        accumulated_power += additional_power
        return accumulated_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> VaultAPI:
    vault: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    print("=== Testing mage counter ===")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print()

    print("=== Testing spell accumulator ===")
    accumulator = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")

    print()

    print("=== Testing enchantment factory ===")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print()

    print("=== Testing memory vault===")
    vault = memory_vault()
    print("Store 'secret' = 42")
    vault["store"]("secret", 42)
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
