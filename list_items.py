import argparse
import sys


def parse_args():
    p = argparse.ArgumentParser(description="List items from a file, one per line.")
    p.add_argument("file", nargs="?", default="README.md", help="Path to input file (default: README.md)")
    p.add_argument("--step", "-s", action="store_true", help="Pause between items (press Enter to continue)")
    return p.parse_args()


def main():
    args = parse_args()
    try:
        with open(args.file, encoding="utf-8") as f:
            lines = [line.strip() for line in f.readlines()]
    except Exception as e:
        print(f"Erro ao abrir {args.file}: {e}")
        sys.exit(1)

    # Filter out empty lines and header lines starting with '#'
    items = [l for l in lines if l and not l.startswith('#')]

    if not items:
        print("Nenhum item encontrado no arquivo.")
        return

    for i, item in enumerate(items, start=1):
        print(f"{i}. {item}")
        if args.step and i != len(items):
            try:
                input("Pressione Enter para o próximo item...")
            except EOFError:
                pass


if __name__ == '__main__':
    main()
