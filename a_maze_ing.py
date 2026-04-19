import sys

from src.maze_logic import parser
from src.maze_logic.generator import MazeGenerator


def main():
    """Main entry point for maze generation."""
    # Determine config file
    config_file = sys.argv[1] if len(sys.argv) > 1 else "config.txt"

    # Load configuration
    try:
        config = parser.load_config(config_file)
    except parser.InputFileError as e:
        print(f"Error loading configuration: {e}")
        sys.exit(1)

    print("=" * 60)
    print("A-MAZE-ING - Maze Generator")
    print("=" * 60)
    print(f"Configuration loaded from: {config_file}")
    print(f"  Dimensions: {config['WIDTH']}x{config['HEIGHT']}")
    print(f"  Entry: {config['ENTRY']}")
    print(f"  Exit: {config['EXIT']}")
    print(f"  Perfect maze: {config['PERFECT']}")
    if "SEED" in config:
        print(f"  Seed: {config['SEED']}")
    print()

    # Generate maze
    try:
        print("Generating maze...")
        generator = MazeGenerator(
            width=config['WIDTH'],
            height=config['HEIGHT'],
            entry=config['ENTRY'],
            exit=config['EXIT'],
            perfect=config['PERFECT'],
            seed=config.get('SEED')
        )
        maze = generator.generate()
        print("✓ Maze generated successfully!")
        print(f"  Total cells: {maze.width * maze.height}")
        print()

        # Display sample grid info
        print("Maze structure created with:")
        print(f"  Width:  {maze.width} cells")
        print(f"  Height: {maze.height} cells")
        print(f"  Entry:  {maze.entry}")
        print(f"  Exit:   {maze.exit}")
        print()

        # Write maze to output file
        output_file = config['OUTPUT_FILE']
        print(f"Writing maze to {output_file}...")
        with open(output_file, 'w', encoding='utf-8') as f:
            for y in range(maze.height):
                for x in range(maze.width):
                    cell = maze.get_cell(x, y)
                    f.write(cell.to_hex())
                f.write('\n')
        print(f"✓ Maze saved to {output_file}")
        print()
        print("=" * 60)

    except Exception as e:
        print(f"✗ Error generating maze: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
