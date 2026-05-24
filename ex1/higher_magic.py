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

from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def inner_spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    return inner_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def inner_spell(target: str, power: int) -> str:
        amplified_power = power * multiplier
        return base_spell(target, amplified_power)

    return inner_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def inner_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"

    return inner_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def inner_spell(target: str, power: int) -> list[str]:
        return list(map(lambda spell: spell(target, power), spells))

    return inner_spell
