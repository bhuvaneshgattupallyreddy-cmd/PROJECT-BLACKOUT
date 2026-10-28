
import time


# ==================== SLOW TYPING EFFECT ====================

def slow_type(text, delay=0.04):
    for character in text:
        print(character, end="", flush=True)
        time.sleep(delay)
    print()


# ==================== GAME INTRO ====================

slow_type("=" * 45)
slow_type("       OPERATION: BLACKOUT")
slow_type("       DIGITAL INVESTIGATION UNIT")
slow_type("=" * 45)

slow_type("")
slow_type("SYSTEM STATUS: ONLINE")
slow_type("SECURITY LEVEL: CLASSIFIED")
slow_type("")
slow_type("Incoming encrypted transmission...")
slow_type("A mysterious file has been detected.")
slow_type("")
slow_type("Your mission begins now, Investigator.")
slow_type("=" * 45)


# ==================== AGENT IDENTIFICATION ====================

slow_type("")
slow_type("IDENTIFICATION REQUIRED")
slow_type("Enter your investigator codename:")

codename = input("> ").strip()

if codename == "":
    codename = "UNKNOWN"

slow_type("")
slow_type(f"ACCESS GRANTED. Welcome, Agent {codename}.")
slow_type("Preparing your mission briefing...")


# ==================== MISSION 1: PASSWORD LOCK ====================

slow_type("")
slow_type("=" * 45)
slow_type("      CLASSIFIED FILE: ACCESS LOCKED")
slow_type("=" * 45)

slow_type("A password is required to open the file.")
slow_type("HINT: The secret code is BLACKOUT")

attempts = 3

while attempts > 0:

    password = input("ENTER PASSWORD > ").strip().upper()

    if password == "BLACKOUT":

        slow_type("")
        slow_type("PASSWORD ACCEPTED...")
        slow_type("Decrypting classified file...")
        slow_type("ACCESS GRANTED!")
        slow_type(f"MISSION 1 COMPLETE, AGENT {codename}!")


        # ==================== MISSION 2: INTELLIGENCE REPORT ====================

        slow_type("")
        slow_type("=" * 45)
        slow_type("       CLASSIFIED INTELLIGENCE")
        slow_type("=" * 45)

        slow_type("FILE ID: BX-104")
        slow_type("SUBJECT: Project Nightfall")
        slow_type("")
        slow_type("CLUE 1:")
        slow_type("A security officer accessed the")
        slow_type("server room at 23:40.")
        slow_type("")
        slow_type("CLUE 2:")
        slow_type("The server was shut down at 23:45.")
        slow_type("")
        slow_type("CLUE 3:")
        slow_type("Three employees had access that night:")
        slow_type("1. Alex - Security Officer")
        slow_type("2. Morgan - System Administrator")
        slow_type("3. Jordan - Research Analyst")
        slow_type("")
        slow_type("END OF REPORT")
        slow_type("=" * 45)


        slow_type("")
        slow_type("MISSION 3: SUSPECT INVESTIGATION")
        slow_type("")
        slow_type("Three employees were present that night.")
        slow_type("Your job is to investigate them.")
        slow_type("")

        suspects = {
            "1": "Alex - Security Officer",
            "2": "Morgan - System Administrator",
            "3": "Jordan - Research Analyst",
        }

        while True:

            slow_type("")
            slow_type("========== SUSPECT DATABASE ==========")

            for number, suspect in suspects.items():
                slow_type(f"{number}. {suspect}")

            slow_type("4. Review intelligence report")
            slow_type("5. End investigation")

            choice = input("Select an option > ").strip()


            if choice == "1":

                slow_type("")
                slow_type("========== ALEX ==========")
                slow_type("Position: Security Officer")
                slow_type("Access: Server room")
                slow_type("Statement:")
                slow_type("I entered the server room at 23:40.")
                slow_type("I was checking the security equipment.")


          

            elif choice == "2":

                slow_type("")
                slow_type("========== MORGAN ==========")
                slow_type("Position: System Administrator")
                slow_type("Access: Computer systems")
                slow_type("Statement:")
                slow_type("I was monitoring the computer systems.")
                slow_type("I noticed the server shut down at 23:45.")


           

            elif choice == "3":

                slow_type("")
                slow_type("========== JORDAN ==========")
                slow_type("Position: Research Analyst")
                slow_type("Access: Research files")
                slow_type("Statement:")
                slow_type("I was reviewing research documents.")
                slow_type("I heard an alarm around 23:45.")


           

            elif choice == "4":

                slow_type("")
                slow_type("========== INTELLIGENCE REPORT ==========")
                slow_type("Server room accessed: 23:40")
                slow_type("Server shut down: 23:45")
                slow_type("Three employees had access.")
                slow_type("Compare their statements.")

            elif choice == "5":

                slow_type("")
                slow_type("Investigation suspended.")
                slow_type("Returning to mission control...")
                break


            

            else:

                slow_type("Invalid selection. Choose 1-5.")


        break



    else:

        attempts -= 1

        slow_type("ACCESS DENIED.")
        slow_type(f"Attempts remaining: {attempts}")


if attempts == 0:

    slow_type("")
    slow_type("SECURITY ALERT!")
    slow_type("FILE LOCKED. MISSION FAILED.")
