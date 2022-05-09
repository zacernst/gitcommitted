#!/usr/bin/env python

import sys
import pathlib

message_file = pathlib.Path(sys.argv[-1])
jira_ticket_file = pathlib.Path(*list(message_file.parts[:-1] + ("JIRA_TICKET",)))


icon_dict = {
    "0": ":boom:",
    "1": ":bug:",
    "2": ":art:",
    "3": ":books:",
    "4": ":star:",
    "5": ":horse_racing:",
    "6": ":hammer:",
    "7": ":microscope:",
    "8": ":poop:",
    "9": ":truck:",
    "10": ":question:",
}


type_msg = (
    """What type of changes are in this commit?\n"""
    """0)  Initial commit\n"""
    """1)  Bugfix\n"""
    """2)  Formatting or cosmetic change\n"""
    """3)  Documentation\n"""
    """4)  Feature\n"""
    """5)  Performance\n"""
    """6)  Refactoring\n"""
    """7)  Tests\n"""
    """8)  Lots of stuff\n"""
    """9)  Deployment\n"""
    """10) Something else\n"""
)

commit_type = input(type_msg)

if commit_type not in icon_dict:
    print("Unrecognized change type. Exiting.")
    sys.exit(1)

commit_emoji = icon_dict[commit_type]

if jira_ticket_file.exists():
    with open(jira_ticket_file, "r") as f:
        jira_ticket = f.read().strip()
else:
    jira_ticket = ""

jira_msg = f"""Enter JIRA ticket, "none", or <Return> for {jira_ticket}\n"""
input_jira_ticket = input(jira_msg)
if input_jira_ticket.lower() == "none":
    jira_ticket = "none"
elif input_jira_ticket == "":
    pass
else:
    jira_ticket = input_jira_ticket.replace(" ", "-").replace(":", "-").upper()

# jira_ticket = jira_ticket.replace(" ", "-").replace(":", "-").upper()

with open(jira_ticket_file, "w") as f:
    f.write(jira_ticket + "\n")


commit_msg = input("Enter a commit message:\n")

total_msg = (
    f"{commit_emoji} [{jira_ticket}] {commit_msg}"
    if jira_ticket != "none"
    else f"{commit_emoji} {commit_msg}"
)
print(total_msg)

with open(message_file, "w") as f:
    f.write(total_msg + "\n")
