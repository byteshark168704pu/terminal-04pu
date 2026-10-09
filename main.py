"""Simple terminal task manager."""
import sys, os, json

TASK_FILE = os.path.expanduser("~/.tasks.json")

def load():
    if not os.path.exists(TASK_FILE): return []
    with open(TASK_FILE) as f: return json.load(f)

def save(tasks):
    with open(TASK_FILE, "w") as f: json.dump(tasks, f, indent=2)

def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h","help"):
        print("usage: task.py [add TASK | list | del INDEX]")
        return
    cmd = args[0]
    tasks = load()
    if cmd == "add" and len(args) > 1:
        tasks.append(" ".join(args[1:]))
        save(tasks)
        print("Added task.")
    elif cmd == "list":
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
    elif cmd in ("del","delete","remove") and len(args)>=2 and args[1].isdigit():
        idx = int(args[1]) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            save(tasks)
            print(f"Removed: {removed}")
        else:
            print("Invalid index.")
    else:
        print("Unknown command.")

if __name__ == "__main__":
    main()