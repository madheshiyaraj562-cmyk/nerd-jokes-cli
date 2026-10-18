import random
import shutil
import sys
import time

JOKES = [
    # Python
    ("Why did the Python programmer not like the snake?", "Too many indentation errors."),
    ("Why do Python programmers have low self-esteem?", "They're constantly comparing their self to others."),
    ("How do you spot a Python developer at a party?", "They're the one who insists everything is 'Pythonic'."),
    ("Why was the Python script so calm?", "It had nothing to import."),
    # JavaScript
    ("Why was the JavaScript developer sad?", "Because he didn't Node how to Express himself."),
    ("How do you comfort a JavaScript bug?", "You console it."),
    ("Why did the developer quit JavaScript?", "He couldn't handle the callbacks, he wanted a promise."),
    ("What's the difference between 0.1 + 0.2 and 0.3 in JS?", "About 0.00000000000000005551."),
    ("Why does JavaScript love '=='?", "Because it'll say yes to just about anything."),
    # Java
    ("Why do Java developers wear glasses?", "Because they don't C#."),
    ("What's the object-oriented way to become wealthy?", "Inheritance."),
    ("Why did the Java developer stay home?", "He couldn't find his class."),
    ("How many Java developers does it take to change a light bulb?", "One, but he needs a LightBulbFactoryBuilderManager first."),
    # C & C++
    ("Why did the C programmer get lost?", "He kept following null pointers."),
    ("What did the C programmer say to the segfault?", "I didn't mean to touch your memory!"),
    ("Why is C like a sharp knife?", "Fast and powerful, but it'll cut you if you're careless."),
    ("What's a C programmer's favorite song?", "'Free(me)'."),
    ("Why do C++ programmers never finish a project?", "They keep adding features, then C++ adds one more."),
    ("Why did the C++ programmer break up with her?", "She had too many undefined behaviors."),
    ("What's the best thing about C++ jokes?", "Nobody can tell which standard they're from."),
    # C# & Rust & Go
    ("Why was the C# developer always calm?", "Because he always had a good sense of .NET worth."),
    ("Why did the C# class feel lonely?", "It had no interface to relate to."),
    ("Why did the Rust programmer never feel lonely?", "Because the borrow checker was always there for him."),
    ("What's a Rust developer's favorite exercise?", "Ownership transfers."),
    ("How do you know someone uses Rust?", "Don't worry, they'll tell you."),
    ("Why did the Rust code refuse to compile?", "It had trust issues with lifetimes."),
    ("Why did the Go developer get lost?", "He kept returning errors instead of directions."),
    ("What's a Go programmer's favorite line?", "if err != nil. And then again. And again."),
    ("Why are Go programmers so relaxed?", "Goroutines do all the work."),
    # PHP & SQL & HTML/CSS
    ("What's the difference between PHP and a bag of gym clothes?", "At least the gym bag has a consistent smell."),
    ("Why did the PHP developer get hired?", "He had a lot of $experience."),
    ("A SQL query walks into a bar, goes up to two tables and asks...", "'Can I join you?'"),
    ("Why did the DBA leave his wife?", "She had one-to-many relationships."),
    ("Why was the SQL developer afraid of NULL?", "You can't ever be sure what it equals."),
    ("What did the SELECT statement say to the table?", "'You complete me, but I only want some of you.'"),
    ("Why did the CSS developer get a divorce?", "He couldn't center anything in his life."),
    ("Why is HTML a great programming language?", "Because it's not. Nobody can fight about it."),
    ("Why did the web designer go broke?", "Too many margins and not enough padding."),
    # Git & Linux & Binary & General
    ("Why did the git user get lost?", "He forgot to commit to a branch."),
    ("How does a programmer end a relationship?", "git push --force."),
    ("What's a git user's worst fear?", "Merge conflicts at 5 PM on Friday."),
    ("Why do Linux users love the terminal?", "Because GUI is just a suggestion."),
    ("How do you annoy a Linux user?", "Ask if they've tried turning it off and on again."),
    ("Why did the sysadmin cross the road?", "sudo !!"),
    ("There are 10 types of people in the world.", "Those who understand binary and those who don't."),
    ("Why do programmers always mix up Halloween and Christmas?", "Because Oct 31 == Dec 25."),
    ("!false", "It's funny because it's true."),
    ("Why do programmers prefer dark mode?", "Because light attracts bugs."),
    ("Why did the developer go broke?", "He used up all his cache."),
    ("How many programmers does it take to change a light bulb?", "None. That's a hardware problem."),
    ("What's a computer's favorite snack?", "Microchips."),
    ("Why was the computer cold?", "It left its Windows open."),
    ("What do you call 8 hobbits?", "A hobbyte."),
    ("What did the router say to the doctor?", "It hurts when IP."),
    ("Why did the programmer quit his job?", "He didn't get arrays."),
]


def _ensure_utf8_stdout():
    """Ensure standard output handles Unicode/emojis cleanly across platforms."""
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


_ensure_utf8_stdout()


def emoji_rain(duration_sec: float = 2.5):
    """Outputs a raining emoji animation."""
    _ensure_utf8_stdout()
    emojis = ["😂", "🤣", "😄", "😆", "😹"]
    cols = shutil.get_terminal_size(fallback=(80, 24)).columns

    start_time = time.time()
    while time.time() - start_time < duration_sec:
        line = [" "] * cols
        num_drops = random.randint(2, 4)
        for _ in range(num_drops):
            pos = random.randint(0, max(0, cols - 2))
            line[pos] = random.choice(emojis)

        try:
            sys.stdout.write("".join(line) + "\n")
            sys.stdout.flush()
        except UnicodeEncodeError:
            safe_line = [c if ord(c) < 128 else ":D" for c in line]
            sys.stdout.write("".join(safe_line) + "\n")
            sys.stdout.flush()
        time.sleep(0.08)

    print("\nThanks for laughing! Bye!")
    print("Made by Raj Madheshiya@2026\n")


def main():
    _ensure_utf8_stdout()

    print("\nNerd Jokes CLI")
    print("Made by Raj Madheshiya@2026")
    print("Press Enter for a joke, or type 'q' to quit.\n")

    # Keep a pool to avoid repeating jokes until all have been seen
    pool = list(JOKES)
    random.shuffle(pool)

    try:
        while True:
            choice = input("> ").strip().lower()
            if choice == "q":
                break

            # Reshuffle if we ran through all jokes
            if not pool:
                pool = list(JOKES)
                random.shuffle(pool)

            setup, punchline = pool.pop()
            print(f"\n{setup}")
            input("(Press Enter for punchline...)")
            print(f"{punchline}\n")
            print("-" * 40)
            print("Press Enter for another joke, or type 'q' to quit.")

    except (KeyboardInterrupt, EOFError):
        print()

    emoji_rain()


if __name__ == "__main__":
    main()
