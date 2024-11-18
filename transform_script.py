import re
import shutil
import sys
import argparse
from pathlib import Path
from typing import List, Tuple

def read_transformations(transform_file: str) -> List[Tuple[str, str]]:
    transformations = []
    with open(transform_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):  # Skip empty lines and comments
                try:
                    before, after = line.split('->', 1)
                    transformations.append((before.strip(), after.strip()))
                except ValueError:
                    print(f"Warning: Skipping invalid line in transform file: {line}")
    return transformations

def transform_file(input_file: str, transformations: List[Tuple[str, str]]) -> str:
    with open(input_file, 'r') as f:
        content = f.read()
    
    # Transform 2: append pxmcore. to functional imports
    content = re.sub(
        r'from functional\.', 
        'from pxmcore.functional.', 
        content
    )
    
    # Transform 3: apply custom transformations from file
    for before, after in transformations:
        content = content.replace(before, after)
    
    return content

def main():
    parser = argparse.ArgumentParser(description='Transform a Python file with optional transformation rules.')
    parser.add_argument('input_file', help='Input file to transform')
    parser.add_argument('-t', '--transform-file', help='File containing transformation rules (before,after)')
    args = parser.parse_args()
    
    # Check if input file exists
    if not Path(args.input_file).is_file():
        print(f"Error: File '{args.input_file}' not found")
        sys.exit(1)
    
    # Create backup of original file
    backup_file = args.input_file + '.bak'
    shutil.copy2(args.input_file, backup_file)

    print(f"Original file backed up to: {backup_file}")
    print(f"Transformations applied to: {args.input_file}")
    
    transformations = []
    
    # If transform file is provided, read transformations from it
    if args.transform_file:
        if not Path(args.transform_file).is_file():
            print(f"Error: Transform file '{args.transform_file}' not found")
            sys.exit(1)
        transformations = read_transformations(args.transform_file)

        # Transform and write back to original file
        transformed = transform_file(args.input_file, transformations)
        with open(args.input_file, 'w') as f:
            f.write(transformed)
    
    while True:
        # If no transform file, ask for single transformation
        before_transform = input("Enter text to replace: ")
        after_transform = input("Enter replacement text: ")
        transformations = [(before_transform, after_transform)]

        if before_transform == "exit" or after_transform == "exit":
            break
    
        # Transform and write back to original file
        transformed = transform_file(args.input_file, transformations)
        with open(args.input_file, 'w') as f:
            f.write(transformed)


if __name__ == "__main__":
    main() 
