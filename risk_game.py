from ui import GameBoard
import argparse


def main():


	parser = argparse.ArgumentParser(description = "Risk Game")

	parser.add_argument("player1", type = str, help = "player1 Agent")
	parser.add_argument("player2", type = str, help = "player2 Agent")


	args = parser.parse_args()

	risk_game = GameBoard((args.player1, args.player2))


if __name__ == '__main__':
	main()