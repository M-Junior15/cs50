import sys

if len(sys.argv) != 2:
    print("Missed command-line argument")
    sys.exit(1)
    
print(f"Hello, {sys.argv[1]}")
print(sys.exit(0))
