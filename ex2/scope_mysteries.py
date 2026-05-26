#!/usr/bin/dev python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scope_mysteries.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: orhernan <orhernan@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/26 18:10:01 by orhernan          #+#    #+#              #
#    Updated: 2026/05/26 18:10:01 by orhernan         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import Callable


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
    def enchant(item_name: str):
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, Callable[[], ]]:
    pass