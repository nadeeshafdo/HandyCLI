import sys

def add_alias(alias, command):
    with open('.aliases', 'a') as f:
        f.write(f"{alias}={command}\n")
    print(f"Alias '{alias}' added for command '{command}'")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python alias.py <alias_name> <command>")
    else:
        add_alias(sys.argv[1], sys.argv[2])
