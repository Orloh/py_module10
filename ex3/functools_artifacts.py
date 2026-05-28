#!/usr/bin/env python3

# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   functools_artifacts.py                             :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: orhernan <orhernan@student.42.fr>          +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/05/28 16:26:45 by orhernan          #+#    #+#             #
#   Updated: 2026/05/28 16:26:45 by orhernan         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #


import functools
import operator
from typing import Callable, Any, cast, Literal


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str]
) -> dict[str, Callable[[str], str]]:
    return {
        "fire": functools.partial(base_enchantment, 50, "Fire"),
        "ice": functools.partial(base_enchantment, 50, "Ice"),
        "lightning": functools.partial(base_enchantment, 50, "Lightning")
    }


def spell_reducer(
        spells: list[int],
        operation: Literal["add", "multiply", "max", "min"]
) -> int:

    if not spells:
        return 0

    operations: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")

    return functools.reduce(operations[operation], spells)


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("The sequence is not defined for negative numbers")
    if n in (0, 1):
        return n

    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @functools.singledispatch
    def dispatcher(spell: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatcher.register
    def _(spell: str) -> str:
        return f"Enchantment spell: {spell}"

    @dispatcher.register
    def _(spell: list[Any]) -> str:
        results = [dispatcher(item) for item in spell]
        formatted_results = "\n -> ".join(results)
        return (
            f"Multi-cast: executed {len(spell)} spells:\n "
            f"-> {formatted_results}"
        )

    return dispatcher


def main() -> None:
    print("=== Testing partial enchanter ===")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"{element} {target} (power level: {power})"

    enchantments = partial_enchanter(base_enchantment)

    def cast_enchantment(element: str, target: str) -> str:

        return enchantments.get(
            element,
            cast(
                Callable[[str], str],
                lambda t: f"Spell fizzled: Unknown element applied to {t}!"
            )
        )(target)

    print(cast_enchantment("fire", "sword"))
    print(cast_enchantment("ice", "shield"))
    print(cast_enchantment("lightning", "staff"))
    print(cast_enchantment("Water", "Armor"))
    print()

    print("=== Testing spell reducer ===")

    spells = [20, 30, 40, 10]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    print()

    print("=== Testing memoized fibonacci ===")
    try:
        print(f"Fib(0): {memoized_fibonacci(0)}")
        print(f"Fib(1): {memoized_fibonacci(1)}")
        print(f"Fib(10): {memoized_fibonacci(10)}")
        print(f"Fib(15): {memoized_fibonacci(15)}")
        print(f"Fib(-3): {memoized_fibonacci(-3)}")
    except ValueError as e:
        print(e)
    print()

    print("=== \nTesting spell dispatcher ===")

    cast_spell = spell_dispatcher()
    print(cast_spell(42))
    print(cast_spell("fireball"))
    print(cast_spell(["heal", {"rage": 200}, "shield", "buff", 3]))
    print(cast_spell({"power": 100}))


if __name__ == "__main__":
    main()
