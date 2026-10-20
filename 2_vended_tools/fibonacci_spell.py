"""
✨🧙 The Ancient Scroll of Fibonacci — Inscribed by Kiro the Grey Hat 🧙✨
A spell to summon the first 10 numbers of the sacred Fibonacci sequence.
"""

def cast_fibonacci_spell(n=10):
    print("=" * 45)
    print("  ✨ Kiro's Fibonacci Summoning Spell ✨")
    print("=" * 45)

    sequence = []
    a, b = 0, 1

    for i in range(n):
        sequence.append(a)
        a, b = b, a + b

    print(f"\n🔮 Summoning the first {n} Fibonacci numbers...\n")
    for idx, num in enumerate(sequence, start=1):
        print(f"   Position {idx:>2}: ✦ {num}")

    print(f"\n📜 Full Sequence: {sequence}")
    print("\n💫 The spell is complete! The ancient sequence lives!\n")
    print("=" * 45)

    return sequence

if __name__ == "__main__":
    cast_fibonacci_spell(10)
