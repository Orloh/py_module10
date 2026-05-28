#!/usr/bin/env python3

# ************************************************************************ #
#                                                                          #
#                                                       :::      ::::::::  #
#  decorator_mastery.py                               :+:      :+:    :+:  #
#                                                   +:+ +:+         +:+    #
#  By: orhernan <orhernan@student.42.fr>          +#+  +:+       +#+       #
#                                               +#+#+#+#+#+   +#+          #
#  Created: 2026/05/28 18:24:39 by orhernan          #+#    #+#            #
#  Updated: 2026/05/28 18:24:39 by orhernan         ###   ########.fr      #
#                                                                          #
# ************************************************************************ #

from functools import wraps
import time
from typing import Callable, Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time

        print(f"Spell completed in {execution_time:.3f} seconds")

        return result

    return wrapper


def power_validator(
        min_power: int
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power_level = None

            if "power" in kwargs:
                power_level = kwargs["power"]

            else:
                var_names = func.__code__.co_varnames

                if "power" in var_names:
                    power_index = var_names.index("power")

                    if power_index < len(args):
                        power_level = args[power_index]

            if power_level is not None and power_level < min_power:
                return "Insufficient power for this spell"

            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(
        max_attempts: int
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):

                try:
                    return func(*args, **kwargs)

                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )

                    else:
                        return f"Spell failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (
            len(name) >= 3 and
            all(char.isalpha() or char.isspace() for char in name)
        )

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("=== Testing spell timer ===")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.3)
        return "Fireball cast!"

    print(f"Result: {fireball()}")

    print("\n=== Testing power validator ===")

    @power_validator(20)
    def cast_ultimate_nova(power: int | None) -> str:
        return f"Ultimate Nova cast with {power} power!"

    print(cast_ultimate_nova(50))
    print(cast_ultimate_nova(power=10))

    print("\n=== Testing retrying spell ===")

    @retry_spell(3)
    def cast_unstable_portal() -> str:
        raise RuntimeError("Portal collapsed!")

    print(cast_unstable_portal())

    success_tracker = 0

    @retry_spell(3)
    def waaaaaaagh_spell() -> str:
        nonlocal success_tracker
        success_tracker += 1
        if success_tracker < 2:
            raise ValueError("Not enough Waaaaaaagh!")
        return "Waaaaaaagh spelled !"

    print(waaaaaaagh_spell())

    print("\n=== Testing MageGuild ===")

    print(MageGuild.validate_mage_name("Gandalf the White"))
    print(MageGuild.validate_mage_name("Oz"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
