from tickets import create_ticket

def main():
    try:
        create_ticket()
    except (KeyboardInterrupt, EOFError):
        print("\nCancelled.")
    except OSError as e:
        print(f"File error: {e}")

if __name__ == "__main__":
    main()