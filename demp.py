
"""Sample module for bitdemo/demp.py

Provides a simple demonstration function and a CLI entry.
"""

from __future__ import annotations

def greet(name: str) -> str:
	"""Return a greeting for the given name.

	Args:
		name: Person's name.

	Returns:
		A greeting string.
	"""
	return f"Hello, {name}!"


def main() -> None:
	"""Simple command-line demo: prints a greeting for 'World'."""
	print(greet("World"))


if __name__ == "__main__":
	main()
