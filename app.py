from config import RAW_DATA
from src.extract.csv_loader import load_data

df = load_data(RAW_DATA)


def main() -> None:
	"""Application entry point."""
	pass


if __name__ == "__main__":
	main()
