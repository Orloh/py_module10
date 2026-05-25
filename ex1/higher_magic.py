#!/usr/bin/env python3

# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    higher_magic.py                                   :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/05/24 22:40:59 by orhernan         #+#    #+#              #
#    Updated: 2026/05/24 22:40:59 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from typing import Callable, TypeAlias


Spell: TypeAlias = Callable[[str, int], str]
SpellCombo: TypeAlias = Callable[[str, int], tuple[str, str]]
Condition: TypeAlias = Callable[[str, int], bool]


def spell_combiner(spell1: Spell, spell2: Spell) -> SpellCombo:
    def inner_spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    return inner_spell


def power_amplifier(base_spell: Spell, multiplier: int) -> Spell:
    def inner_spell(target: str, power: int) -> str:
        amplified_power = power * multiplier
        return base_spell(target, amplified_power)

    return inner_spell


def conditional_caster(condition: Condition, spell: Spell) -> Spell:
    def inner_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"

    return inner_spell


def spell_sequence(spells: list[Spell]) -> Callable[[str, int], list[str]]:
    def inner_spell(target: str, power: int) -> list[str]:
        return list(map(lambda spell: spell(target, power), spells))

    return inner_spell


def main() -> None:
    # --- Spells and Conditions ---
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage!"

    def heal(target: str, power: int) -> str:
        return f"Healing {target} for {power} HP!"

    def shield(target: str, power: int) -> str:
        return f"Shielding {target} with {power} defense!"

    def is_powerful_enough(target: str, power: int) -> bool:
        return power >= 50

    # --- Tests ---
    print("=== Testing spell_combiner ===")
    combo_spell = spell_combiner(fireball, heal)
    print(combo_spell("The Paladin", 100))

    print("\n=== Testing power_amplifier ===")
    amplified_fireball = power_amplifier(fireball, 3)
    print(amplified_fireball("The Dragon", 50))

    print("\n=== Testing conditional_caster ===")
    safe_spell = conditional_caster(is_powerful_enough, heal)
    print(f"Cast with 75 power: {safe_spell('The Rogue', 75)}")
    print(f"Cast with 20 power: {safe_spell('The Rogue', 20)}")

    print("\n=== Testing spell_sequence ===")
    barrage = spell_sequence([fireball, heal, shield])
    results = barrage("The Golem", 80)
    for res in results:
        print(f"- {res}")


if __name__ == "__main__":
    main()
