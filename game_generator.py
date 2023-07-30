import random
import csv

def simulate_game_rounds(players, num_rounds):
    results = []
    for player in players:
        player_score = [player, random.randint(0, 1000)]
        results.append(player_score * num_rounds)
    return results

def save_scores(scores):
    with open('game_scores.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Player name', 'Score'])
        csv_writer.writerows(scores)

if __name__ == "__main__":
    players = ['Josh', 'Luke', 'Kate', 'Mark', 'Mary']
    num_rounds = 100

    simulated_scores = simulate_game_rounds(players, num_rounds)
    save_scores(simulated_scores)