import hashlib


# Name:      Ankit Joshi
# ULID:      C00541037
# Course:    CMPS 315
# Assignment: pa1 - Password racking
# Certification of Authenticity:
# I certify that this assignment is entirely my own work.


def add_candidate(candidates, candidate):
    """Add a candidate only once."""
    if candidate not in candidates:
        candidates.append(candidate)


def make_candidates(word, username):
    """Create the required password variations for one dictionary word."""
    candidates = []

    add_candidate(candidates, word)
    add_candidate(candidates, word.lower())
    add_candidate(candidates, word.upper())

    if len(word) > 0:
        add_candidate(candidates, word[0].upper() + word[1:].lower())
        add_candidate(candidates, word[:-1].lower() + word[-1].upper())
        add_candidate(candidates, word[-1] + word[:-1])

    add_candidate(candidates, word + word[::-1])
    add_candidate(candidates, word.replace("o", "0").replace("O", "0"))

    original_count = len(candidates)
    for index in range(original_count):
        add_candidate(candidates, candidates[index] + username)

    return candidates


def read_shadow_file(filename):
    """Read usernames, salts, and hashes from the shadow file."""
    usernames = []
    salts = []
    hashes = []
    passwords = []

    shadow_file = open(filename, "r")
    for line in shadow_file:
        fields = line.rstrip("\r\n").split(":")
        password_fields = fields[1].split("$")

        usernames.append(fields[0])
        salts.append(password_fields[2])
        hashes.append(password_fields[3])
        passwords.append("")
    shadow_file.close()

    return usernames, salts, hashes, passwords


def main():
    usernames, salts, hashes, passwords = read_shadow_file("shadow.txt")
    cracked_count = 0

    for account_index in range(len(usernames)):
        dictionary_file = open("rockyou.txt", "r")
        for line in dictionary_file:
            word = line.rstrip("\r\n")
            candidates = make_candidates(word, usernames[account_index])

            for candidate in candidates:
                value = salts[account_index] + candidate
                digest = hashlib.md5(value.encode("utf-8")).hexdigest()

                if digest == hashes[account_index]:
                    passwords[account_index] = candidate
                    cracked_count += 1
                    break

            if passwords[account_index] != "":
                break
        dictionary_file.close()

    print("Name         Salt       Hash                            Password")
    print()
    for index in range(len(usernames)):
        print(
            "{:<12} {:<10} {:<32} {}".format(
                usernames[index], salts[index], hashes[index], passwords[index]
            )
        )

    print()
    print("Cracked Hashes:     {}".format(cracked_count))
    print("Uncracked Hashes:   {}".format(len(usernames) - cracked_count))


if __name__ == "__main__":
    main()
